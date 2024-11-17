from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate


class PromptManager:
    @staticmethod
    def get_advanced_rewrite_template() -> ChatPromptTemplate:
        system_message = """You are an expert writer and translator. Your task is to rewrite and potentially translate text according to the specified parameters."""

        human_template = """Please rewrite and/or translate the following text:

        Parameters:
        - Target Language: {language}
        - Writing Style: {style}
        - Tone: {tone}

        Original Text:
        {draft}

        Please maintain:
        - The core message and meaning
        - Proper grammar and punctuation
        - Cultural appropriateness for the target language
        - Consistency in style and tone"""

        return ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(system_message),
            HumanMessagePromptTemplate.from_template(human_template)
        ])