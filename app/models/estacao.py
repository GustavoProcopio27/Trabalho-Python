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
    def codigo(self)->str:
        return self._codigo
    
    @codigo.setter
    def codigo(self,v:str)->None:
        if not isinstance(v,str):
            raise TypeError("Codigo deve ser uma string")
        self._codigo:str=v
        
    @property
    def uf(self)->str:
        return self._uf

    @uf.setter
    def uf(self, v:str)->None:
        if not isinstance(v, str):
            raise TypeError("UF deve ser uma string.")
        self._uf:str = v

    @property
    def latitude(self)->float:
        return self._latitude

    @latitude.setter
    def latitude(self, v:float)->None:
        if not isinstance(v, float):
            raise TypeError("Latitude deve ser float.")
        self._latitude:float = v

    @property
    def longitude(self)->float:
        return self._longitude

    @longitude.setter
    def longitude(self, v:float)->None:
        if not isinstance(v, float):
            raise TypeError("Longitude deve ser float.")
        self._longitude:float = v

    @property
    def altitude(self)->float:
        return self._altitude

    @altitude.setter
    def altitude(self, v:float)->None:
        if not isinstance(v, float):
            raise TypeError("Altitude deve ser float.")
        self._altitude :float= v

    @property
    def registros(self)->list[RegistroMetereologico]:
        return self._registros

    @registros.setter
    def registros(self, v:list[RegistroMetereologico])->None:
        if not isinstance(v, list):
            raise TypeError("Registros deve ser uma lista.")
        
        if not all(isinstance(item,RegistroMetereologico) for item in v):
            raise TypeError("Os elementos da lista devem ser Registros meteorologicos")
        
        self._registros :list[RegistroMetereologico]= v

    @property
    def nome(self)->str:
        return self._nome
    
    @nome.setter
    def nome(self, v)->None:
        if not isinstance(v, str):
            raise TypeError("Nome deve ser uma string.")
        self._nome :str= v
        
    @property
    def regiao(self)->str:
        return self._regiao
    
    @regiao.setter
    def regiao(self,v):
        if not isinstance(v,str):
            raise TypeError("Região deve ser uma string")
        self._regiao:str=v
        
    def __str__(self)->str:
        return f"Estação :\n\n Nome:{self.nome}; Codigo:{self.codigo}; Estado:{get_estado(self.uf)}; Regiao:{get_region(self.regiao)}; Altitude:{self.altitude}; Latitude:{self.latitude}; Longitude:{self.longitude}"    
         
    def __repr__(self)->str:
        return  f"EstacaoMeteorologica({self.nome},{self.codigo},{self.regiao},{self.uf},{self.latitude},{self.longitude},{self.altitude},{self.registros})"
    
