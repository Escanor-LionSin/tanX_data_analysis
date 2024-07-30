# Online Store Revenue Analysis

Submission for tanX task

## Prerequisites

- Docker
- Docker Compose

## Project Structure

- `main.py`: Contains the main logic for reading the CSV file and computing revenue metrics.
- `test_main.py`: Contains unit tests for the revenue calculation functions.
- `Dockerfile`: Defines the Docker image for the application.
- `docker-compose.yml`: Defines the services for running the task and tests.
- `requirements.txt`: Lists the Python dependencies (empty in this case as we're using only built-in modules).

```
Repo/
│
├── code/
│   ├── script.py
│   ├── test.py
├── data
│   ├── orders.csv
├── requirements.txt
├── dockerfile
├── docker-compose.yml
├── .dockerignore

```
## Running the Application

1. Make sure you have your own copy of (if any) `orders.csv` file in the same directory as the `docker-compose.yml` file, which is the outermost directory.

2. Clone the repo into a local directory

3. To run the main task:

```
docker-compose run task
```

4. To run the tests:

```
docker-compose run test
```
If you want to run the task on a different dataset, then replace the orders.csv file with a dataset file of your choice.

🗿
