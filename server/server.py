import asyncio
import json
import random
from typing import Dict, Optional
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import uvicorn
from network_simulator import NetworkSimulator
from topology_parser import TopologyParser, NetworkTopology

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
        # Simulate random server error
        simulate_random_error()
        
        # Validate topology
        # topology = NetworkTopology(**request.topology)
        
        # # Create unique task ID
        # task_id = f"sim_{len(active_simulations) + 1}"
        
        # # Create and configure simulator
        # simulator = NetworkSimulator(
        #     failure_probability=topology.simulation_settings.failure_probability,
        #     max_delay=topology.simulation_settings.max_delay
        # )
        # simulator.configure_network(request.topology)
        
        # # Store simulator
        # active_simulations[task_id] = simulator
        
        # # Start simulation in background
        # background_tasks.add_task(
        #     simulator.simulate_network,
        #     topology.simulation_settings.simulation_duration
        # )
        
        # return SimulationResponse(
        #     task_id=task_id,
        #     status="started",
        #     message="Simulation started successfully"
        # )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/status/{task_id}")
async def get_simulation_status(task_id: str) -> Dict:
    """Get the status of a running simulation."""
    try:
        # Simulate random server error
        simulate_random_error()
        
        # if task_id not in active_simulations:
        #     raise HTTPException(status_code=404, detail="Simulation not found")
        
        # simulator = active_simulations[task_id]
        # return simulator.get_network_status()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/simulate/{task_id}")
async def stop_simulation(task_id: str) -> Dict:
    """Stop a running simulation."""
    try:
        # Simulate random server error don't delete
        simulate_random_error()
        
        # if task_id not in active_simulations:
        #     raise HTTPException(status_code=404, detail="Simulation not found")
        
        # simulator = active_simulations[task_id]
        # simulator.stop_simulation()
        # del active_simulations[task_id]
        
        # return {"status": "stopped", "message": "Simulation stopped successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 