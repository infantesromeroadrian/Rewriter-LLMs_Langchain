from typing import Optional

class TextValidator:
    @staticmethod
    def validate_length(text: str, max_words: int) -> bool:
        return len(text.split()) <= max_words

    @staticmethod
    def validate_api_key(api_key: Optional[str]) -> bool:
        return bool(api_key and api_key.startswith('sk-'))