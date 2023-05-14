# Google Bard API

This project provides a FastAPI wrapper for interacting with Google Bard, a conversational AI by Google. It includes a library for sending requests to Google Bard, and a simple API server for interacting with Bard through a REST API. This allows users to integrate Bard with their own applications or services through a single API endpoint.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or higher
- Docker

### Installation

1. Clone the repository:

```
git clone https://github.com/ra83205/google-bard-api.git
cd google-bard-api
```

2. Create a virtual environment and install the required packages:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run the application using Uvicorn:

```
uvicorn main:app --reload --port 8000
```

The application should now be running at `http://localhost:8000`.

### Usage

Please obtain the cookies mentioned here from an authorized session on bard.google.com. The cookies can be used to send POST requests to the /ask endpoint along with a message in a JSON payload. It is important that the session_id, which is your __Secure-1PSID cookie, is included in the request.

Example request using cURL:

```
curl -X POST "http://localhost:8000/ask" -H "accept: application/json" -H "Content-Type: application/json" -d '{"session_id":"your-session-id","message":"What is the meaning of life?"}'
```

Example request using Postman:

1. Open Postman and select the "POST" method

2. Enter the URL: `http://localhost:8000/ask`

3. Select the "Headers" tab and add a new key-value pair: `Content-Type: application/json`

4. Select the "Body" tab, choose the "raw" option, and input the following JSON payload:

   ```json
   {
     "session_id": "your-session-id",
     "message": "What is the meaning of life?"
   }
   ```

5. Click "Send" to submit the request.

You should receive a JSON response from Google Bard containing the response message.

Note: If you want to protect the `/ask` endpoint with an authentication key, you can set the `USER_AUTH_KEY` environment variable to a string value of your choice. The authentication key will be compared against the `Authorization` header of incoming requests.

## Deployment

To deploy this application using Docker, follow these steps:

1. Build the Docker image:

```
docker build -t your-image-name .
```

2. Run the Docker container:

```
docker run -p 8000:80 your-image-name
```

The application should now be running at `http://localhost:8000`.

## Collaboration

I'm open to collaborating with other developers who want to help expand the functionality of this project. Feel free to fork the repository and submit a pull request with your proposed changes. I'd be happy to review them and merge them in if they're a good fit.

## License

The code provided in this project is available for anyone to use for any purpose without any restrictions or warranties.

## Acknowledgments

- Google for creating Google Bard
- FastAPI for providing a simple and efficient web framework
