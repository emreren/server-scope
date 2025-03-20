
# Server Scope

**Server Scope** is a lightweight FastAPI-based application designed to monitor server performance metrics in a Docker environment.

## Features
- Monitors total CPU usage
- Tracks total memory usage (free vs used, including percentage)
- Displays total disk usage (free vs used, including percentage)
- Lists the top 5 processes consuming the most CPU
- Lists the top 5 processes consuming the most memory

## Getting Started

### Prerequisites
Ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)

### Installation
Clone the repository:
```bash
git clone https://github.com/your-username/server-scope.git
cd server-scope
```

### Build the Docker Image
```bash
docker build -t server-scope .
```

### Run the Container
```bash
docker run -d -p 8000:8000 server-scope
```

### Access the API
Once the container is running, you can access the FastAPI documentation and test the endpoints via:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Usage
To query server metrics via terminal:
```bash
curl -X GET http://localhost:8000/api/metrics | jq
```

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---



