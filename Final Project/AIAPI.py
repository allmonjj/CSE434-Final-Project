from openai import OpenAI
from openai._exceptions import OpenAIError
from pydantic import BaseModel, Field, ValidationError
from typing import Optional
import os
import json

class Item(BaseModel):
    name: str
    description: str
    effect: str

class NPC(BaseModel):
    name: str
    description: str
    hp: int
    xp: int


class Location(BaseModel):
    name: str
    description: str
    hasItem: bool = Field(..., alias='hasItem')
    hasEnemy: bool = Field(..., alias='hasEnemy')
    item: Optional[Item] = None
    npc: Optional[NPC] = None

class Response(BaseModel):
    location: Location

class AIAPI:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    def getAPIResponse(self, player_state):
        system_message = """
            You are a Game Master for a Dungeons & Dragons style game. Your responsibilities include:
            1. Tracking and persisting game states (locations, and whether they have an item and/or an NPC enemy).
            2. Generating location descriptions and managing item and NPC placement dynamically.
            3. Ensuring a coherent narrative and logical progression in the game. As in if a player enters a room previously visited, you must recognize and recall it. Therefore the starting room is (0,0). Moving North/South modifies x accordingly, and moving East/West modifies y accordingly.
            Respond with structured JSON data that aligns with the game's model, including:
            - Location state and descriptions.
            - NPC/item interactions and statuses.
            - Possible item effect format : {"(+-) HP/ATKPOWER"} Keep negative effects to a minimum. Only hp and atkPower modifications.
            Follow the provided schema when responding.
            """

        user_message = f"""
            Player State: {json.dumps(player_state)}
            Request: Provide the new location's details and NPC/item interactions (if any).
            """

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]

        try:
            completion = self.client.beta.chat.completions.parse(
                model="gpt-4o",
                messages=messages,
                response_format=Response
            )

            responseMessage = completion.choices[0].message
            if responseMessage.parsed:
                return completion.choices[0].message.content
            else:
                print(f"Refused Response : \n{responseMessage.refusal}")
                return None

        except OpenAIError as e:
            # Handle specific OpenAI errors
            print(f"OpenAI API error: {e}")
            return None
        except Exception as e:
            # Handle other potential errors
            print(f"An unexpected error occurred: {e}")
            return None

    def parse_api_response(self, json_str: str) -> Response:
        try:
            # Load JSON string into a Python dictionary
            data = json.loads(json_str)

            # Parse the dictionary into the ApiResponse model
            api_response = Response.model_validate(data)
            return api_response
        except ValidationError as e:
            print("Validation Error:", e)
            raise
