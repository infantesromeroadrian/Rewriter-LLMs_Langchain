import streamlit as st
from dataclasses import dataclass
from src.config.settings import AppConfig, StyleConfig


class AdvancedUIElements:
    def create_header(self):
        st.set_page_config(page_title=AppConfig.PAGE_TITLE)
        st.header(AppConfig.PAGE_TITLE)

    def create_sidebar_options(self):
        st.sidebar.header("Advanced Options")
        language = st.sidebar.selectbox(
            "Target Language",
            options=list(StyleConfig.LANGUAGES.keys()),
            help="Select the target language for your text"
        )

        style = st.sidebar.selectbox(
            "Writing Style",
            options=list(StyleConfig.WRITING_STYLES.keys()),
            help="Choose the writing style for your text"
        )

        tone = st.sidebar.selectbox(
            "Tone",
            options=list(StyleConfig.TONES.keys()),
            help="Select the tone for your text"
        )

        return language, style, tone

    def create_main_content(self):
        st.markdown("## Transform your text")
        st.markdown("""
        This advanced text rewriter can:
        - Translate to multiple languages
        - Apply different writing styles
        - Adjust the tone of your text
        - Maintain consistency and quality
        """)

    def get_api_key(self) -> str:
        return st.text_input(
            "OpenAI API Key",
            type="password",
            key="api_key",
            help="Enter your OpenAI API key"
        )

    def get_input_text(self) -> str:
        return st.text_area(
            "Enter your text",
            height=200,
            max_chars=3000,
            help="Paste or type your text here"
        )

    def show_output(self, text: str, language: str):
        st.markdown(f"### Output ({language})")
        st.markdown(text)

    def show_error(self, message: str):
        st.error(message)

    def show_processing_status(self):
        return st.empty()