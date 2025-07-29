from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
 
app = FastAPI()
 
# Modelo para los detalles dentro de ReferenceItem
class ReferenceDetail(BaseModel):
    idLineaSistemaExterno: str
    codigoProducto: str
    cantidadReferencia: float
    importeUnitario: float
    anexo1: str
 
# Modelo de cada referencia
class ReferenceItem(BaseModel):
    referencia: str
    codigoAgente: Optional[str] = Field(default="PRO27")
    tipoAgente: Optional[str] = Field(default="PRO")
    tipoRecepcion: Optional[str] = Field(default="MMOC")
    tipoReferencia: Optional[str] = Field(default="OC")
    moneda: Optional[str] = Field(default="USD")
    anexo1: str
    anexo2: str
    anexo3: str
    memo: str
    predio: Optional[str] = Field(default="1")
    fechaEmitida: Optional[str] = Field(default_factory=lambda: datetime.now().strftime("%Y/%m/%d"))
    detalles: List[ReferenceDetail]
 
# Modelo del payload de referencias
class ReferenceReception(BaseModel):
    empresa: Optional[int] = Field(default=1)
    dsReferencia: Optional[str]
    referencias: List[ReferenceItem]
 
@app.post("/create/references_receptions", response_model=ReferenceReception)
def create_references_receptions(payload: ReferenceReception):
    return payload
 
# Modelo para agenda
class AgendaItem(BaseModel):
    codigoAgente: Optional[str] = Field(default="PRO27")
    tipoAgente: Optional[str] = Field(default="PRO")
    tipoRecepcion: Optional[str] = Field(default="MMOC")
    referencia: Optional[str] = Field(default="(VARIOS)")
    tipoReferencia: Optional[str] = Field(default="OC")
    predio: Optional[str] = Field(default="1")
    anexo1: str
    anexo2: str
    anexo3: str
    anexo4: Optional[str] = Field(default=None)
    placaVehiculo: str
    fechaEntrega: Optional[str] = Field(default=None)
 
# Lista de agendas como payload
class AgendaPayload(BaseModel):
    empresa: Optional[int] = Field(default=1)
    dsAgenda: Optional[str]
    agenda: List[AgendaItem]
 
@app.post("/create/agenda", response_model=AgendaPayload)
def create_agenda(payload: AgendaPayload):
    return payload