from dataclasses import dataclass
from src.model.llm_model import LLMManager, LLMConfig
from src.utils.prompt_templates import PromptManager
from typing import Optional

@dataclass
class AdvancedTextProcessingRequest:
    text: str
    language: str
    style: str
    tone: str
    api_key: str

class AdvancedTextProcessor:
    def __init__(self):
        self.prompt_template = PromptManager.get_advanced_rewrite_template()

    def process_text(self, request: AdvancedTextProcessingRequest) -> str:
        llm_config = LLMConfig(api_key=request.api_key)
        llm_manager = LLMManager(llm_config)

        messages = self.prompt_template.format_messages(
            language=request.language,
            style=request.style,
            tone=request.tone,
            draft=request.text
        )

        return llm_manager.generate_response(messages)