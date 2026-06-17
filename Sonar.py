from datetime import time
from dataclasses import dataclass, field
import uuid


@dataclass
class Sensor_IoT_Alfanumerico:
    # Identificación
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    
    # Datos del sensor
    temperatura: float
    humedad: float
    distancia_cm: float
    nivel_sonido_db: float
    
    # Timestamps (automáticos)
    timestamp_emision_señal: float = field(default_factory=time.time)
    timestamp_recepcion_señal: float = field(default_factory=time.time)
    timestamp_envio_informe: float = field(default_factory=time.time)
    
    # Estado del lugar
    lugar_ocupado: bool = False
    lugar_id: str # Se lee como A4, A siendo la fila, 4 siendo la columna; una especie de coordenada en una matriz
    
    # Seguridad
    clave_efimera: str = field(default_factory=lambda: uuid.uuid4().hex[:16])
    
    # Formato preliminar de los informes
    # {
    # "id": "a1b2c3d4",
    # "temperatura": 22.5,
    # "humedad": 45.0,
    # "distancia_cm": 150.0,
    # "nivel_sonido_db": 60.0,
    # "timestamp_emision_señal": 1700000000.0,
    # "timestamp_recepcion_señal": 1700000001.0,
    # "timestamp_envio_informe": 1700000002.0,
    # "lugar_ocupado": false,
    # "lugar_id": "A4",
    # "clave_efimera": "1a2b3c4d5e6f7g8h"
    # }