# FastAPI Project

This project is a FastAPI application that provides an endpoint to perform addition on input lists of integers using Python's multiprocessing pool. The project is organized following the MVC (Model-View-Controller) pattern.

## Project Structure
```
fastapi_assignment/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── addition_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── addition_model.py
│   ├── views/
│   │   ├── __init__.py
│   │   └── addition_view.py
│   └── utils/
│       ├── __init__.py
│       ├── logger.py
│       └── monitoring.py
│
├── logs/                # Directory for log files
│   └── app.log          # Log file
│
├── tests/
│   ├── __init__.py
│   ├── test_addition.py
│
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic
- Gunicorn
- Prometheus Client

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SumanKanrar-IEM/fastapi-assignment.git
cd fastapi_assignment
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application Locally
To start the FastAPI application, run the following command:

```bash
uvicorn app.main:app --reload
```
The application will be available at `http://127.0.0.1:8000`

## Running the Application with Docker
1. Build the Docker Image
```bash
docker build -t fastapi_assignment .
```
2. Run the Docker Container
```bash
docker run -d -p 8000:8000 -p 8001:8001 fastapi_assignment
```

The application will be available at `http://127.0.0.1:8000`

## API Endpoint

### POST /api/add
This endpoint performs addition on input lists of integers.

### Request format:
```json
{
  "batchid": "id0101",
  "payload": [[1, 2], [3, 4]]
}
```

### Response Format
```json
{
  "batchid": "id0101",
  "response": [3, 7],
  "status": "complete",
  "started_at": "<timestamp>",
  "completed_at": "<timestamp>"
}
```

## Monitoring and Logging
- **Prometheus**: The Prometheus metrics are exposed at http://127.0.0.1:8001. These metrics include request processing time.

## Running Tests
To run the tests, use the following command:
```bash
pytest tests
```

## Deployment to Production
### Step 1: Build and Push Docker Image to a Container Registry

#### 1. Build the Docker Image:
```bash
docker build -t fastapi_assignment .
```

#### 2. Tag the Docker Image:
```bash
docker tag fastapi_assignment:latest your-aws-account-id.dkr.ecr.your-region.amazonaws.com/fastapi_assignment:latest
```

#### 3. Push the Docker Image:
```bash
docker push your-aws-account-id.dkr.ecr.your-region.amazonaws.com/fastapi_assignment:latest
```

### Step 2: Deploy the Application Using AWS ECS
####1. Create ECS Cluster:
Follow the AWS ECS documentation to create a cluster.

####2. Create Task Definition:
Define a task that references your Docker image.

####3. Deploy the Service:
Deploy your service using the created task definition.

### Step 3: Set Up Monitoring and Logging
- **AWS CloudWatch**: Configure CloudWatch for logging and monitoring.
- **Prometheus**: Integrate Prometheus with a monitoring solution that supports it.