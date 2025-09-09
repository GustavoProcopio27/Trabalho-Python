from models.registro import RegistroMetereologico
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
        
    def __str__(self):
        pass