import asyncio
import json
import aiohttp
from typing import Dict, Optional

# TODO
# 1. Implement context manager for the client
# 2. Implement the start_simulation method
# 3. Implement the get_simulation_status method
# 4. Implement the stop_simulation method

class NetworkSimulationClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session: Optional[aiohttp.ClientSession] = None

    # TODO fill here
    async def __aenter__(self):
        pass

    # TODO fill here
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
 
    # TODO fill here
    async def start_simulation(self, topology_file: str) -> Dict:
        """Start a new network simulation."""
        pass

    # TODO fill here
    async def get_simulation_status(self, task_id: str) -> Dict:
        """Get the status of a running simulation."""
        pass
    # TODO fill here
    async def stop_simulation(self, task_id: str) -> Dict:
        """Stop a running simulation."""
        pass

async def main():
    # Example usage
    async with NetworkSimulationClient() as client:
        try:
            # Start simulation
            response = await client.start_simulation("topology_example.json")
            task_id = response["task_id"]
            print(f"Simulation started with task ID: {task_id}")

            # Monitor simulation for 10 seconds
            for _ in range(10):
                status = await client.get_simulation_status(task_id)
                print("\nCurrent simulation status:")
                print(json.dumps(status, indent=2))
                await asyncio.sleep(1)

            # Stop simulation
            await client.stop_simulation(task_id)
            print("\nSimulation stopped")

        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main()) 