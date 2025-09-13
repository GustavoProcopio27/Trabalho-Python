from app.models.registro import RegistroMetereologico
from app.utils.matchers import get_estado,get_region

class EstacaoMeteorologica:
    def __init__(self, nome,codigo,regiao,uf,latitude,longitude,altitude,registros):
        self._nome:str=nome
        self._codigo:str=codigo
        self._regiao:str=regiao
        self._uf:str=uf
        self._latitude:float=latitude
        self._longitude:float=longitude
        self._altitude:float=altitude
        self._registros:list[RegistroMetereologico]=registros
        
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self,v):
        if not isinstance(v,str):
            raise TypeError("Codigo deve ser uma string")
        self._codigo=v
        
    @property
    def uf(self):
        return self._uf

    @uf.setter
    def uf(self, v):
        if not isinstance(v, str):
            raise TypeError("UF deve ser uma string.")
        self._uf = v

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, v):
        if not isinstance(v, float):
            raise TypeError("Latitude deve ser float.")
        self._latitude = v

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, v):
        if not isinstance(v, float):
            raise TypeError("Longitude deve ser float.")
        self._longitude = v

    @property
    def altitude(self):
        return self._altitude

    @altitude.setter
    def altitude(self, v):
        if not isinstance(v, float):
            raise TypeError("Altitude deve ser float.")
        self._altitude = v

    @property
    def registros(self):
        return self._registros

    @registros.setter
    def registros(self, v):
        if not isinstance(v, list):
            raise TypeError("Registros deve ser uma lista.")
        self._registros = v

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, v):
        if not isinstance(v, str):
            raise TypeError("Nome deve ser uma string.")
        self._nome = v
        
    @property
    def regiao(self):
        return self._regiao
    
    @regiao.setter
    def regiao(self,v):
        if not isinstance(v,str):
            raise TypeError("Região deve ser uma string")
        self._regiao=v
        
    def __str__(self):
        return f"Estação :\n\n Nome:{self.nome}; Codigo:{self.codigo}; Estado:{get_estado(self.uf)}; Regiao:{get_region(self.regiao)}; Altitude:{self.altitude}; Latitude:{self.latitude}; Longitude:{self.longitude}"    
         
    def __repr__(self):
        return  f"EstacaoMeteorologica({self.nome},{self.codigo},{self.regiao},{self.uf},{self.latitude},{self.longitude},{self.altitude},{self.registros})"
    
