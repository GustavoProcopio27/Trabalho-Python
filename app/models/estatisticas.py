from typing import TYPE_CHECKING
from statistics import mean
from app.models.registro import RegistroMetereologico
    
class Estatisticas:
    def __init__(self,registros):
        self._registros:list[RegistroMetereologico]=registros
        self._lista_temperatura:list[float]=list()
        self._lista_umidade:list[float]=list()
        self._lista_precipitacao:list[float]=list()
        self.calculate_estatistics()
        
    @property
    def registros(self)->list[RegistroMetereologico]:
        return self._registros
    
    @property
    def lista_temperatura(self)->list[float]:
        return self._lista_temperatura
    @property
    def lista_umidade(self)->list[float]:
        return self._lista_umidade
    
    @property
    def lista_precipitacao(self)->list[float]: 
        return self._lista_precipitacao
    
    @registros.setter
    def registros(self,v)->None:
        if not isinstance(v,list):
            raise TypeError("registros deve ser uma lista")
        
        if not all(isinstance(item, RegistroMetereologico) for item in v):
            raise TypeError("Todo item na lista deve ser um registro meteorologico deve ser um float ou int")
        self._registros=v
        
        
    @lista_temperatura.setter
    def lista_temperatura(self,v)->None:
        if not isinstance(v,list):
            raise TypeError("Lista de temperaturas deve ser uma lista")
        
        if not all(isinstance(item, (int,float)) for item in v):
            raise TypeError("Todo item na lista de temperaturas deve ser um float ou int")
        
        self._lista_temperatura=v
        
        
    @lista_umidade.setter
    def lista_umidade(self,v)->None:
        if not isinstance(v,list):
            raise TypeError("Lista de umidade deve ser uma lista")
        
        if not all(isinstance(item, (int,float)) for item in v):
            raise TypeError("Todo item na lista de umidade deve ser um float ou int")
        self._lista_umidade=v
        
        
        
    @lista_precipitacao.setter
    def lista_precipitacao(self,v)->None:
        if not isinstance(v,list):
            raise TypeError("Lista de precipitacao deve ser uma lista")
        
        if not all(isinstance(item, (int,float)) for item in v):
            raise TypeError("Todo item na lista de precipitacao deve ser um float ou int")
        self._lista_precipitacao=v
    
    
    def calculate_estatistics(self)->None:
        for registro in self.registros:
            self._lista_temperatura.append(registro.temperatura)
            self._lista_umidade.append(registro.umidade)
            self._lista_precipitacao.append(registro.precipitacao)
                    
    def media_temperatura(self)->float:
        return mean(self.lista_temperatura)
    
    def max_umidade(self)->float:
        return max(self.lista_umidade)
    
    def total_precipitacao(self)->float:
        return sum(self.lista_precipitacao)
        
        
        
        
        
        
        
        
    def __str__(self)->str:
        return (
                '=============================\n'
                f'Temperatura media:{self.media_temperatura()} °C \n'
                f'Umidade máxima:{self.max_umidade()}% \n'
                f'Precipitação total:{self.total_precipitacao()}mm \n'
                '=============================\n\n\n\n'
                )
    