# Simple Image Server

This repository contains a robust image server built using FastAPI and MongoDB, allowing you to store JPEG images, extract metadata, and manage everything within Docker containers. The Docker Compose configuration provided here simplifies the deployment and management of the entire application stack. This repository is meant to be extend and apply to a machine learning inference platform, but I am still working on it.

## Features

- Store JPEG images: Upload and store your JPEG images using the FastAPI framework.
- Metadata Extraction: Automatically decode and extract metadata from uploaded images. Since it is going to connect with machine learning model, relavent data such as image size is extracted.
- MongoDB Integration: Integrate with MongoDB to store both images and their associated metadata.
- Dockerized Deployment: Utilize Docker Compose to manage multiple containers and streamline the deployment process.
- API Endpoints: Access images and metadata through a well-defined API, allowing for easy retrieval and posting of images.


## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/image-server.git
   ```

2. Navigate to the project directory:

   ```bash
   cd image-server
   ```


3. Build and start the Docker containers using Docker Compose:

   ```bash
   docker-compose up 
   ```

   This command will create and run the FastAPI, MongoDB and client containers.

4. Execute the fastapi server container:

   ```bash
   docker exec -it fastapi-server-1 bash
   python server/main.py
   ```
5. Execute the client container:

   ```bash
   docker exec -it fastapi-client-1 bash
   python client/client.py
   ```

   This command will create and run the FastAPI, MongoDB and client containers.

5. Access the API documentation by navigating to `http://localhost:8000` in your web browser.

