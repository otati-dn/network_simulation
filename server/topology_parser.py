from typing import Dict, List
from pydantic import BaseModel, Field, validator
import json

class Connection(BaseModel):
    target_router: str
    bandwidth: int = Field(gt=0)
    latency: int = Field(ge=0)

class Router(BaseModel):
    id: str
    ip: str
    connections: List[Connection]

    @validator('ip')
    def validate_ip(cls, v):
        parts = v.split('.')
        if len(parts) != 4:
            raise ValueError('Invalid IP address format')
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                raise ValueError('Invalid IP address values')
        return v

class SimulationSettings(BaseModel):
    failure_probability: float = Field(ge=0, le=1)
    max_delay: int = Field(ge=0)
    simulation_duration: int = Field(gt=0)

class NetworkTopology(BaseModel):
    network_name: str
    routers: List[Router]
    simulation_settings: SimulationSettings

    @validator('routers')
    def validate_router_connections(cls, routers):
        router_ids = {router.id for router in routers}
        
        # Check if all target routers exist
        for router in routers:
            for conn in router.connections:
                if conn.target_router not in router_ids:
                    raise ValueError(f'Target router {conn.target_router} does not exist')
        
        return routers

class TopologyParser:
    @staticmethod
    def parse_topology_file(file_path: str) -> NetworkTopology:
        """Parse and validate a network topology file."""
        try:
            with open(file_path, 'r') as f:
                topology_data = json.load(f)
            
            return NetworkTopology(**topology_data)
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON format in topology file')
        except Exception as e:
            raise ValueError(f'Error parsing topology file: {str(e)}')

    @staticmethod
    def validate_topology(topology: Dict) -> bool:
        """Validate a topology dictionary."""
        try:
            NetworkTopology(**topology)
            return True
        except Exception:
            return False 