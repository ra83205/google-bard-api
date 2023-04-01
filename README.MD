# Google Bard API

This project provides a FastAPI wrapper for interacting with Google Bard, a conversational AI by Google. It allows users to send messages to Google Bard and receive responses through a simple API.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or higher
- Docker

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/google-bard-api.git
cd google-bard-api
```

1. Create a virtual environment and install the required packages:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

1. Run the application using Uvicorn:

```bash
uvicorn main:app --reload
```

The application should now be running at `http://localhost:8000`.

### Usage

You can send POST requests to the `/ask` endpoint with a JSON payload containing a `session_id` (your `__Secure-1PSID` cookie) and a `message`.

Example request:

```bash
curl -X POST "http://localhost:8000/ask" -H "accept: application/json" -H "Content-Type: application/json" -d '{"session_id":"your-session-id","message":"What is the meaning of life?"}'
```

You should receive a JSON response from Google Bard containing the response message.

## Deployment

To deploy this application using Docker, follow these steps:

1. Build the Docker image:

```bash
docker build -t your-image-name .
```

1. Run the Docker container:

```bash
docker run -p 4000:80 your-image-name
```

The application should now be running at `http://localhost:4000`.

## Contributing
  pp21§1
If you would like to contribute to this project, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/LICENSE) file for details.

## Acknowledgments

- Google for creating Google Bard
- FastAPI for providing a simple and efficient web framework