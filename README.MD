# Google Bard API 

Welcome to the **Google Bard API** project! This repository contains a **FastAPI** wrapper designed to seamlessly interact with 🤖 **Google Bard**, a remarkable conversational AI developed by Google. The project encompasses a comprehensive library for effortlessly dispatching requests to Google Bard, along with a streamlined API server that empowers you to interact with Bard through a REST API. This exceptional fusion of resources facilitates the integration of Bard's capabilities into your applications or services via a single, straightforward API endpoint.

## Getting Started 🚀

Let's embark on a journey to set up and launch the project on your local machine for developmental and testing purposes.

### Prerequisites 📋

Before we dive in, ensure you have the following prerequisites:

- Python 3.9 or newer 🐍
- Docker 🐳

### Installation 🛠️

1. Begin by cloning the repository:

    ```sh
    git clone https://github.com/ra83205/google-bard-api.git
    cd google-bard-api
    ```

2. Create a virtual environment and install the necessary packages:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Launch the application using Uvicorn:

    ```sh
    uvicorn main:app --reload --port 8000
    ```

    Your application should now be live at `http://localhost:8000`.

### Usage 📦

To utilize the power of the Google Bard API, follow these steps:

1. Obtain the cookies as mentioned on **bard.google.com** from an authorized session. These cookies will be used to send POST requests to the `/ask` endpoint, accompanied by a message in a JSON payload. Make sure to include the `session_id`, which corresponds to the `__Secure-1PSID` cookie, in your request.

2. Example request using cURL:

    ```sh
    curl -X POST "http://localhost:8000/ask" -H "accept: application/json" -H "Content-Type: application/json" -d '{"session_id":"your-session-id","message":"What is the meaning of life?"}'
    ```

3. Example request using Postman:

    - Open Postman and choose the "POST" method
    - Enter the URL: `http://localhost:8000/ask`
    - In the "Headers" tab, add a new key-value pair: `Content-Type: application/json`
    - In the "Body" tab, select the "raw" option and input the following JSON payload:

        ```json
        {
          "session_id": "your-session-id",
          "message": "What is the meaning of life?"
        }
        ```

    - Click "Send" to submit the request. You'll receive a JSON response from Google Bard containing the response message.

    > **Note**: To secure the `/ask` endpoint with an authentication key, set the `USER_AUTH_KEY` environment variable to a string value of your choice. The authentication key will be cross-referenced against the `Authorization` header of incoming requests.

## Deployment 🚢

To deploy this application using Docker, embark on the following steps:

1. Construct the Docker image:

    ```sh
    docker build -t your-image-name .
    ```

2. Initiate the Docker container:

    ```sh
    docker run -p 8000:80 your-image-name
    ```

    The application will be accessible at `http://localhost:8000`.

## Collaboration 👥

Are you excited to contribute and expand the horizons of this project? Collaboration is key! Feel free to fork the repository and propose your changes through pull requests. Your contributions will be meticulously reviewed and seamlessly merged if they align with the project's objectives.

## License 📜

The code presented in this repository is generously licensed for unrestricted use, devoid of limitations or warranties.

## Acknowledgments 🙌

A special thanks to:

- Google for creating the visionary Google Bard
- FastAPI for providing an elegant and efficient web framework

Your participation and contributions are truly appreciated! Happy coding! 🎉
