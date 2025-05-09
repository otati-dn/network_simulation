import asyncio
import json
import aiohttp
from typing import Dict, Optional

class NetworkSimulationClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def start_simulation(self, topology_file: str) -> Dict:
        """Start a new network simulation."""
        if not self.session:
            raise RuntimeError("Client session not initialized")

        with open(topology_file, 'r') as f:
            topology = json.load(f)

        async with self.session.post(
            f"{self.base_url}/simulate",
            json={"topology": topology}
        ) as response:
            if response.status != 200:
                error = await response.text()
                raise RuntimeError(f"Failed to start simulation: {error}")
            return await response.json()

    async def get_simulation_status(self, task_id: str) -> Dict:
        """Get the status of a running simulation."""
        if not self.session:
            raise RuntimeError("Client session not initialized")

        async with self.session.get(
            f"{self.base_url}/status/{task_id}"
        ) as response:
            if response.status != 200:
                error = await response.text()
                raise RuntimeError(f"Failed to get simulation status: {error}")
            return await response.json()

    async def stop_simulation(self, task_id: str) -> Dict:
        """Stop a running simulation."""
        if not self.session:
            raise RuntimeError("Client session not initialized")

        async with self.session.delete(
            f"{self.base_url}/simulate/{task_id}"
        ) as response:
            if response.status != 200:
                error = await response.text()
                raise RuntimeError(f"Failed to stop simulation: {error}")
            return await response.json()

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