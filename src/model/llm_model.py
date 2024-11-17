from langchain_openai import ChatOpenAI
from dataclasses import dataclass
from typing import Any

@dataclass
class LLMConfig:
    api_key: str
    temperature: float = 0.7
    model_name: str = "gpt-4o-mini"

class LLMManager:
    def __init__(self, config: LLMConfig):
        self.config = config
        self.model = self._initialize_model()

    def _initialize_model(self) -> ChatOpenAI:
        return ChatOpenAI(
            temperature=self.config.temperature,
            openai_api_key=self.config.api_key,
            model_name=self.config.model_name
        )

    def generate_response(self, prompt: str) -> str:
        response = self.model.invoke(prompt)
        return response.content