from beanie import Document, PydanticObjectId
from typing import Optional, List
from datetime import date

class EventoModel(Document):
    id: Optional[PydanticObjectId] = None
    nombre: str
    fecha_nacimiento: date

    class Settings:
        name = "eventos"