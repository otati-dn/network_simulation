# Network Simulation Assignment

## Overview
This assignment tests your ability to work with network programming, asynchronous operations, and error handling in Python. You will be implementing a network simulation server that can configure and monitor a network of routers.

## Requirements

### Part 1: Network Topology Parser
Create a Python server that can:
1. Accept a network topology file in JSON format
2. Parse and validate the topology configuration
3. Configure the network simulation based on the topology

### Part 2: Network Simulation Server
Implement a server that:
1. Runs the network simulation asynchronously
2. Provides immediate response with a task ID
3. Allows status checking of the simulation
4. Simulates network delays and failures
5. Handles error cases gracefully

You will need to implement the following core server functions in `server.py`:

1. `start_simulation`:
   - Accepts a network topology configuration
   - Validates the topology using the provided parser
   - Creates a new network simulator instance
   - Starts the simulation asynchronously
   - Returns a task ID for status tracking
   - Handles errors appropriately

2. `get_simulation_status`:
   - Accepts a task ID
   - Returns the current status of the simulation
   - Includes router states and connection information
   - Handles invalid task IDs

3. `stop_simulation`:
   - Accepts a task ID
   - Gracefully stops the running simulation
   - Cleans up resources
   - Handles invalid task IDs

The server should handle random failures (20% probability) and return appropriate error responses.

### Part 3: Client Implementation
Create a client that can:
1. Submit network topology configurations
2. Check simulation status
3. Handle errors and retries appropriately

The client should be implemented as a separate Python package that can be used to interact with your server. You should provide:
- A clean API for interacting with the server
- Proper error handling and retries
- Async support for non-blocking operations
- Documentation and usage examples

## Project Structure
```
network_simulation/
├── README.md
├── requirements.txt
├── topology_example.json
└── server/
    ├── __init__.py
    ├── network_simulator.py
    ├── topology_parser.py
    └── server.py
```

## Getting Started
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python -m server.server
   ```

3. Implement your client to interact with the server

## API Endpoints
The server exposes the following endpoints:

- `POST /simulate`: Start a new network simulation
  - Request body: JSON containing network topology
  - Response: `{"task_id": str, "status": str, "message": str}`

- `GET /status/{task_id}`: Get simulation status
  - Response: Current network status including router states

- `DELETE /simulate/{task_id}`: Stop a running simulation
  - Response: Confirmation of simulation stop

## Evaluation Criteria
- Code organization and structure
- Error handling and edge cases
- Asynchronous implementation
- Documentation and comments
- Testing coverage
- Performance considerations
- Client implementation quality
- API design and usability

## Bonus Challenges

### 1. Multiple Topology Support
Enhance your client to support working with multiple topology files:
- Implement a topology manager that can handle a directory of topology files
- Support different topology formats (e.g., YAML, JSON)
- Provide a way to compare different network configurations
- Implement topology validation and conflict detection
- Add support for topology versioning

Example directory structure:
```
topologies/
├── production/
│   ├── network_v1.json
│   └── network_v2.json
├── staging/
│   └── test_network.json
└── development/
    └── local_network.json
```

### 2. Docker Deployment
Containerize the entire solution:
- Create a Dockerfile for both server and client
- Implement Docker Compose for local development
- Add health checks and monitoring
- Configure proper networking between containers
- Implement volume mounting for topology files
- Add environment variable support

Example docker-compose.yml structure:
```yaml
version: '3.8'
services:
  server:
    build: ./server
    ports:
      - "8000:8000"
    volumes:
      - ./topologies:/app/topologies
    environment:
      - FAILURE_PROBABILITY=0.2
      - MAX_DELAY=1000

  client:
    build: ./client
    volumes:
      - ./topologies:/app/topologies
    depends_on:
      - server
```

## Time Limit
This assignment should take approximately 4-6 hours to complete. Bonus challenges can be implemented after the core requirements are met.

## Submission
Submit your solution as a GitHub repository with:
1. All source code
2. Requirements file
3. README with setup and usage instructions
4. Tests
5. Documentation
6. Client implementation with usage examples
7. (Bonus) Docker configuration files
8. (Bonus) Multiple topology support implementation 