from pydantic import BaseModel, Field, validator
from typing import Optional, Tuple


class IpInfo(BaseModel):
    city: Optional[str] = Field(None, description="Nome da cidade associada ao IP")
    region: Optional[str] = Field(None, description="Região/estado correspondente")
    country: Optional[str] = Field(None, description="Código do país")
    loc: Optional[str] = Field(None, description="Coordenadas latitude,longitude")
    org: Optional[str] = Field(None, description="Organização ou ASN")
    postal: Optional[str] = Field(None, description="Código postal")

    @validator("loc")
    def validate_loc(cls, value):
        if value and "," not in value:
            raise ValueError("Campo 'loc' inválido: deve conter 'latitude,longitude'")
        return value

    def get_coordinates(self) -> Optional[Tuple[float, float]]:
        if not self.loc:
            return None
        try:
            lat, lon = map(float, self.loc.split(","))
            return lat, lon
        except ValueError:
            return None
