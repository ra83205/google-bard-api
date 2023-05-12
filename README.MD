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
uvicorn main:app --reload
```

The application should now be running at `http://localhost:8000`.

### Usage

You can send POST requests to the `/ask` endpoint with a JSON payload containing a `session_id` (your `__Secure-1PSID` cookie) and a `message`.

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

1. Run the Docker container:

```
docker run -p 4000:80 your-image-name
```

The application should now be running at `http://localhost:4000`.

## Collaboration

I'm open to collaborating with other developers who want to help expand the functionality of this project. Feel free to fork the repository and submit a pull request with your proposed changes. I'd be happy to review them and merge them in if they're a good fit.

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request or open an issue.

## License

The code provided in this project is available for anyone to use for any purpose without any restrictions or warranties.

## Acknowledgments

- Google for creating Google Bard
- FastAPI for providing a simple and efficient web framework
