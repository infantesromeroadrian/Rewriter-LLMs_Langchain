📝 Description
An advanced text rewriting application that leverages LangChain and OpenAI's GPT models to transform text in multiple ways:

Translate to different languages
Apply various writing styles
Adjust tone and formality
Maintain consistency and quality

🌟 Features

Multiple Languages: Support for 10+ languages including English, Spanish, French, German, etc.
Writing Styles: Choose from various styles:

Formal
Informal
Business
Academic
Creative
Technical
Journalistic
Persuasive
Narrative
Poetic


Tone Adjustments: Various tone options:

Professional
Friendly
Enthusiastic
Serious
Humorous
Empathetic
Neutral
Confident
Simple
Sophisticated



🛠️ Installation
Prerequisites

Python 3.9+
Poetry (Python dependency management)
OpenAI API key

Setup

Clone the repository

bashCopygit clone https://github.com/yourusername/text-rewriter.git
cd text-rewriter

Install dependencies with Poetry

bashCopypoetry install

Create a .env file

envCopyOPENAI_API_KEY=your_openai_api_key_here
📂 Project Structure
Copytext-rewriter/
├── src/
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── features/
│   │   ├── __init__.py
│   │   ├── text_processor.py
│   │   └── ui_components.py
│   ├── model/
│   │   ├── __init__.py
│   │   └── llm_model.py
│   └── utils/
│       ├── __init__.py
│       ├── prompt_templates.py
│       └── validators.py
├── tests/
├── .env
├── .gitignore
├── README.md
├── poetry.lock
└── pyproject.toml
🚀 Usage

Activate the Poetry environment

bashCopypoetry shell

Run the application

bashCopystreamlit run src/app.py

Access the application in your browser at http://localhost:8501

💻 Application Interface
Main Interface

Text input area for your content
Language selection dropdown
Writing style options
Tone adjustment controls

Advanced Settings

Temperature control for creativity
Maximum length settings
Output format options

🔧 Configuration
Available Writing Styles
pythonCopyWRITING_STYLES = {
    "Formal": "Professional and academic style",
    "Informal": "Casual and conversational style",
    "Business": "Corporate and professional communication",
    # ... more styles
}
Supported Languages
pythonCopyLANGUAGES = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    # ... more languages
}
🤖 Technical Details
LangChain Integration

Uses ChatOpenAI for text generation
Custom prompt templates
Memory management for context

OpenAI Model

Default model: gpt-3.5-turbo
Configurable temperature
Error handling and retry logic

📈 Performance

Average processing time: 2-3 seconds
Maximum text length: 700 words
API rate limiting handled automatically

🔒 Security

API keys stored securely in .env
Input validation and sanitization
No data persistence
Rate limiting implemented

🧪 Testing
Run the test suite:
bashCopypoetry run pytest
🤝 Contributing

Fork the repository
Create a feature branch

bashCopygit checkout -b feature/amazing-feature

Commit your changes

bashCopygit commit -m 'Add amazing feature'

Push to the branch

bashCopygit push origin feature/amazing-feature

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

OpenAI for their GPT models
LangChain team for their framework
Streamlit for the wonderful UI framework

📫 Contact
Your Name - @yourusername
Project Link: https://github.com/yourusername/text-rewriter
🚀 Future Improvements

 Add more language support
 Implement custom style templates
 Add batch processing
 Improve error handling
 Add user authentication
 Implement caching
 Add export options
 Improve processing speed


⭐️ If you find this project useful, please consider giving it a star!