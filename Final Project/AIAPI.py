from openai import OpenAI
import os

class AIAPI:
    def __init__(self):
        self.client = OpenAI(
            # api_key=userdata.get('OPENAI_API_KEY')
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def getAPIResponse(
            self,
            model: str,
            user_message: str,
            temperature: float = 1.0,
            max_tokens: int = 2048,
            top_p: float = 1.0,
            frequency_penalty: float = 0.0,
            presence_penalty: float = 0.0,
            response_format: str = "text",
            system_message: str = ""
    ):

        if system_message == "":
            messages = [{"role": "user", "content": user_message}]
        else:
            messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ]

        completion = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )

        response = completion.choices[0].message.content
        return response