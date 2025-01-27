# AI Haiku Poet

A FastAPI-based web service that generates beautiful haikus about any theme using OpenAI's GPT-3.5 model.

## Features

- Generate unique haikus based on user-provided themes
- RESTful API endpoints
- Powered by OpenAI's GPT-3.5 model
- Health check endpoint

## Prerequisites

- Python 3.8+
- OpenAI API key

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd AI-Haiku-Poet
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Copy `.env_example` to `.env`
   - Add your OpenAI API key to the `.env` file:
```bash
OPENAI_API_KEY=your_api_key_here
```

4. Run the application:
```bash
uvicorn main:app --reload
```

## API Endpoints

### Generate a Haiku
```
GET /haiku?theme={theme}
```
- `theme` (optional): The theme for the haiku

Example response:
```json
{
    "Haiku": "Inkling in the woods\nWhispers of the ancient trees\nNature's secrets told"
}
```

### Health Check
```
GET /health
```
Example response:
```json
{
    "Health": "Ok"
}
```

## Deployment

The application uses Gunicorn as the WSGI server for production deployment:

1. Install Gunicorn if not already installed:
```bash
pip install gunicorn
```

2. Start the application with Gunicorn:
```bash
gunicorn main:app -c gunicorn.conf.py
```

Key considerations for production:
- Ensure your `.env` file is properly configured with production settings
- Use appropriate security headers and CORS settings
- Set up proper monitoring and logging
- Consider using a reverse proxy like Nginx in front of Gunicorn

## License

MIT License 