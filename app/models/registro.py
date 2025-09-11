class RegistroMetereologico:

    def __init__ (self, data, hora, temperatura, umidade, precipitacao):
        self._data:str=data
        self._hora:str=hora
        self._temperatura:float=temperatura
        self._umidade:float=umidade
        self._precipitacao:float=precipitacao

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, value):
        self._hora = value

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, value):
        self._temperatura = value

    @property
    def umidade(self):
        return self._umidade

    @umidade.setter
    def umidade(self, value):
        self._umidade = value

    @property
    def precipitacao(self):
        return self._precipitacao

    @precipitacao.setter
    def precipitacao(self, value):
        self._precipitacao = value
 
    def __str__(self):
        return f"data:{self.data},hora:{self.hora},temperatura:{self.temperatura},umidade:{self.umidade},precipitação:{self.precipitacao}"
    
    def __repr__(self):
        return f"RegistroMetereologico({self.data},{self.hora},{self.temperatura},{self.umidade},{self.precipitacao})"
    
    def tolist(self)->list[str | float]:
        return [self.data,self.hora,self.temperatura,self.umidade,self.precipitacao]