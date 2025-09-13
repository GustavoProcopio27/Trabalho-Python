from typing import TYPE_CHECKING
from statistics import mean
if TYPE_CHECKING:
    from app.models.registro import RegistroMetereologico
    
class Estatisticas:
    def __init__(self,registros):
        self._registros:list["RegistroMetereologico"]=registros
        self._lista_temperatura=list()
        self._lista_umidade=list()
        self._lista_precipitacao=list()
        self.calculate_estatistics()
        
    @property
    def registros(self):
        return self._registros
    
    @property
    def lista_temperatura(self):
        return self._lista_temperatura
    @property
    def lista_umidade(self):
        return self._lista_umidade
    
    @property
    def lista_precipitacao(self): 
        return self._lista_precipitacao
    
    @registros.setter
    def registros(self,v):
        self._registros=v
        
    @lista_temperatura.setter
    def lista_temperatura(self,v):
        self._lista_temperatura=v
        
    @lista_umidade.setter
    def lista_umidade(self,v):
        self._lista_umidade=v
        
    @lista_precipitacao.setter
    def lista_precipitacao(self,v):
        self._lista_precipitacao=v
    
    
    def calculate_estatistics(self):
        for registro in self.registros:
            self._lista_temperatura.append(registro.temperatura)
            self._lista_umidade.append(registro.umidade)
            self._lista_precipitacao.append(registro.precipitacao)
                    
    def media_temperatura(self):
        return mean(self.lista_temperatura)
    
    def max_umidade(self):
        return max(self.lista_umidade)
    
    def total_precipitacao(self):
        return sum(self.lista_precipitacao)
        
    def __str__(self):
        return (
                '=============================\n'
                f'Temperatura media:{self.media_temperatura()} °C \n'
                f'Umidade máxima:{self.max_umidade()}% \n'
                f'Precipitação total:{self.total_precipitacao()}mm \n'
                '=============================\n\n\n\n'
                )
    