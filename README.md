# AI Virtual Career Counsellor

An intelligent career counselling chatbot that helps users discover suitable career paths based on their interests and skills.

## Features

- Natural Language Processing for understanding user interests
- Personalized career recommendations
- Interactive chat interface
- Comprehensive career path information
- Skills assessment
- Educational requirements guidance

## Project Structure

```
ai_career_counsellor/
├── rasa_chatbot/       # Rasa chatbot files
├── frontend/           # Streamlit frontend
└── data/              # Career data and training data
```

## Setup

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Initialize Rasa (from rasa_chatbot directory):
```bash
rasa init
```

3. Train the model:
```bash
rasa train
```

4. Run the Streamlit app:
```bash
streamlit run frontend/app.py
```

## Development

- The chatbot is built using Rasa for natural language understanding
- Frontend is developed using Streamlit
- NLTK is used for text preprocessing
- Career data is stored in structured JSON format

## Usage

1. Start the Rasa server
2. Launch the Streamlit interface
3. Start chatting and explore career options

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT License
