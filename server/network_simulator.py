import asyncio
import random
import time
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class RouterStatus(Enum):
    ACTIVE = "active"
    FAILED = "failed"
    DEGRADED = "degraded"

@dataclass
class Connection:
    target_router: str
    bandwidth: int
    latency: int
    status: RouterStatus = RouterStatus.ACTIVE

@dataclass
class Router:
    id: str
    ip: str
    connections: List[Connection]
    status: RouterStatus = RouterStatus.ACTIVE

class NetworkSimulator:
    def __init__(self, failure_probability: float = 0.1, max_delay: int = 1000):
        self.routers: Dict[str, Router] = {}
        self.failure_probability = failure_probability
        self.max_delay = max_delay
        self.simulation_start_time: Optional[float] = None
        self.simulation_end_time: Optional[float] = None
        self.is_running = False

    def configure_network(self, topology: dict) -> None:
        """Configure the network based on the provided topology."""
        self.routers.clear()
        
        for router_data in topology["routers"]:
            connections = [
                Connection(
                    target_router=conn["target_router"],
                    bandwidth=conn["bandwidth"],
                    latency=conn["latency"]
                )
                for conn in router_data["connections"]
            ]
            
            self.routers[router_data["id"]] = Router(
                id=router_data["id"],
                ip=router_data["ip"],
                connections=connections
            )

    async def simulate_network(self, duration: int) -> None:
        """Run the network simulation for the specified duration."""
        self.is_running = True
        self.simulation_start_time = time.time()
        self.simulation_end_time = self.simulation_start_time + duration

        while time.time() < self.simulation_end_time and self.is_running:
            await self._simulate_network_cycle()
            await asyncio.sleep(1)  # Simulate one cycle per second

        self.is_running = False

    async def _simulate_network_cycle(self) -> None:
        """Simulate one cycle of network activity."""
        for router in self.routers.values():
            if random.random() < self.failure_probability:
                router.status = RouterStatus.FAILED
                continue

            for connection in router.connections:
                if random.random() < self.failure_probability:
                    connection.status = RouterStatus.FAILED
                else:
                    # Simulate random delays
                    delay = random.randint(0, self.max_delay)
                    await asyncio.sleep(delay / 1000)  # Convert to seconds

    def get_network_status(self) -> dict:
        """Get the current status of the network."""
        return {
            "status": "running" if self.is_running else "completed",
            "elapsed_time": time.time() - self.simulation_start_time if self.simulation_start_time else 0,
            "routers": {
                router_id: {
                    "status": router.status.value,
                    "connections": [
                        {
                            "target": conn.target_router,
                            "status": conn.status.value,
                            "bandwidth": conn.bandwidth,
                            "latency": conn.latency
                        }
                        for conn in router.connections
                    ]
                }
                for router_id, router in self.routers.items()
            }
        }

    def stop_simulation(self) -> None:
        """Stop the network simulation."""
        self.is_running = False 