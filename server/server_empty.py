import asyncio
import json
import random
from typing import Dict, Optional
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import uvicorn
from network_simulator import NetworkSimulator
from topology_parser import TopologyParser, NetworkTopology

# TODO
# 1. Implement the server
# 2. Implement the start_simulation method
# 3. Implement the get_simulation_status method
# 4. Implement the stop_simulation method

app = FastAPI(title="Network Simulation Server")

# Store active simulations
active_simulations: Dict[str, NetworkSimulator] = {}

class SimulationResponse(BaseModel):
    task_id: str
    status: str
    message: str

class TopologyRequest(BaseModel):
    topology: Dict

# List of possible error messages
ERROR_MESSAGES = [
    "Internal server error",
    "Service temporarily unavailable",
    "Connection timeout"
]

def simulate_random_error():
    """Simulate a random error with 20% probability."""
    if random.random() < 0.2:  # 20% chance of error
        error_message = random.choice(ERROR_MESSAGES)
        raise HTTPException(status_code=500, detail=error_message)

@app.post("/simulate", response_model=SimulationResponse)
async def start_simulation(
    request: TopologyRequest,
    background_tasks: BackgroundTasks
) -> SimulationResponse:
    """Start a new network simulation."""
    try:

        # DON'T DELETE THIS LINE: Simulate random server error
        simulate_random_error()
        # TODO fill here
        return {}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/status/{task_id}")
async def get_simulation_status(task_id: str) -> Dict:
    """Get the status of a running simulation."""
    try:

        # DON'T DELETE THIS LINE: Simulate random server error
        simulate_random_error()
        # TODO fill here
        return {}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/simulate/{task_id}")
async def stop_simulation(task_id: str) -> Dict:
    """Stop a running simulation."""
    try:
        # DON'T DELETE THIS LINE
        simulate_random_error()
        # TODO fill here
        return {}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 