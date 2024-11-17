from dataclasses import dataclass
from typing import List, Dict

@dataclass
class AppConfig:
    PAGE_TITLE = "Advanced Text Rewriter"
    MAX_WORDS = 700
    DEFAULT_TEMPERATURE = 0.7
    CONTACT_URL = "https://aiaccelera.com"

@dataclass
class StyleConfig:
    WRITING_STYLES = {
        "Formal": "Professional and academic style",
        "Informal": "Casual and conversational style",
        "Business": "Corporate and professional communication",
        "Academic": "Scholarly and research-oriented",
        "Creative": "Artistic and imaginative expression",
        "Technical": "Precise and technical documentation",
        "Journalistic": "News reporting style",
        "Persuasive": "Convincing and argumentative",
        "Narrative": "Storytelling format",
        "Poetic": "Lyrical and poetic expression"
    }

    LANGUAGES = {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Italian": "it",
        "Portuguese": "pt",
        "Chinese": "zh",
        "Japanese": "ja",
        "Korean": "ko",
        "Russian": "ru"
    }

    TONES = {
        "Professional": "Formal and business-like",
        "Friendly": "Warm and approachable",
        "Enthusiastic": "Energetic and positive",
        "Serious": "Grave and formal",
        "Humorous": "Light and funny",
        "Empathetic": "Understanding and caring",
        "Neutral": "Balanced and objective",
        "Confident": "Strong and assured",
        "Simple": "Clear and straightforward",
        "Sophisticated": "Complex and refined"
    }