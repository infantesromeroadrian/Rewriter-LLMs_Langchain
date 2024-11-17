import streamlit as st
from src.features.ui_components import AdvancedUIElements
from src.features.text_processor import AdvancedTextProcessor, AdvancedTextProcessingRequest
from src.utils.validators import TextValidator
from src.config.settings import AppConfig

class AdvancedTextRewriterApp:
    def __init__(self):
        self.ui = AdvancedUIElements()
        self.processor = AdvancedTextProcessor()
        self.validator = TextValidator()

    def run(self):
        self.ui.create_header()
        self.ui.create_main_content()

        # Sidebar options
        language, style, tone = self.ui.create_sidebar_options()

        # Main content
        api_key = self.ui.get_api_key()
        input_text = self.ui.get_input_text()

        if st.button("Transform Text"):
            if not input_text:
                self.ui.show_error("Please enter some text to transform.")
                return

            if not self.validator.validate_api_key(api_key):
                self.ui.show_error("Please enter a valid OpenAI API key.")
                return

            with st.spinner("Transforming your text..."):
                request = AdvancedTextProcessingRequest(
                    text=input_text,
                    language=language,
                    style=style,
                    tone=tone,
                    api_key=api_key
                )

                result = self.processor.process_text(request)
                self.ui.show_output(result, language)

if __name__ == "__main__":
    app = AdvancedTextRewriterApp()
    app.run()