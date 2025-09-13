from datetime import date,datetime

class RegistroMetereologico:

    def __init__ (self, data, hora, temperatura, umidade, precipitacao):
        self._data:date=datetime.strptime(data, "%Y/%m/%d").date()
        self._hora:str=hora
        self._temperatura:float=temperatura
        self._umidade:float=umidade
        self._precipitacao:float=precipitacao

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value,str):
            raise TypeError("data deve ser passado como string")
        try:
            self._data:date = datetime.strptime(value, "%Y/%m/%d").date() 
        except Exception as ex:
            print(f"Formatacao incorreta {ex}")
            raise TypeError("formato incorreto")
        
    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, value):
        if not isinstance(value,str):
            raise TypeError("hora deve ser passado como string")
        self._hora = value

    @property
    def temperatura(self):
        return self._temperatura

    @temperatura.setter
    def temperatura(self, value):
        if not isinstance(value,(float,int)):
            raise TypeError("temperatura deve ser passado como float ou int")
        self._temperatura = value

    @property
    def umidade(self):
        return self._umidade

    @umidade.setter
    def umidade(self, value):
        if not isinstance(value,(float,int)):
            raise TypeError("temperatura deve ser passado como float ou int")
        self._umidade = value

    @property
    def precipitacao(self):
        return self._precipitacao

    @precipitacao.setter
    def precipitacao(self, value):
        if not isinstance(value,(float,int)):
            raise TypeError("temperatura deve ser passado como float ou int") 
        self._precipitacao = value
 
    def __str__(self):
        return f"data:{self.data},hora:{self.hora},temperatura:{self.temperatura},umidade:{self.umidade},precipitação:{self.precipitacao}"
    
    def __repr__(self):
        return f"RegistroMetereologico({self.data},{self.hora},{self.temperatura},{self.umidade},{self.precipitacao})"
    
    def tolist(self)->list[str | float]:
        return [self.data,self.hora,self.temperatura,self.umidade,self.precipitacao]