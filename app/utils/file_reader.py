from os import listdir
from os.path import join, isfile
from app.models.estacao import EstacaoMeteorologica
from app.models.registro import RegistroMetereologico

class Reader:
    @staticmethod
    def read_csv(option:int)->list[EstacaoMeteorologica]:
        option_year:dict[int,int]={
            1:2020,      
            2:2021,
            3:2022,
            4:2023,
            5:2024
        }
        try:
            path:str=f"data/{option_year[option]}"
        except Exception: 
            raise IndexError() 
        
        estacoes=list()
        if len(listdir(path))==0:
            print("Nenhum dado encontrado, retornando...\n ")
            return None

        for file in listdir(path):

            full_path:str=join(path,file)
            if not isfile(full_path):
                print('arquivo inexistente')
            else:    
                linhas:list[str]
                with open(file=full_path,mode="r",encoding="latin-1") as f:
                    linhas:list[str]=f.readlines()
                
    
                # print('regiao:', get_region(linhas[0].split(':;')[1].rstrip('\n')) )
                # print('unidade federativa:',get_estado(linhas[1].split(':;')[1].rstrip('\n')))
                # print('estacao:',linhas[2].split(':;')[1])
                # print('codigo estacao:',linhas[3].split(':;')[1])
                # print('latitude:',linhas[4].split(':;')[1])
                # print('longitude:',linhas[5].split(':;')[1])
                # print('altitude:',linhas[6].split(':;')[1])
                # print('data fundacao:',linhas[7].split(':;')[1])
                
                headers:str=linhas[8]
                total_records:list[str]=linhas[9:len(linhas)]
                
                organized_records:dict[str,list[str]] = {
                                        'cabecalho':headers.split(';'),
                                        'dados':[row.split(';') for row in total_records]
                                    }              

                registros_meteorologicos=list()
                for linha in organized_records['dados']:
                    registro=RegistroMetereologico(
                        data=linha[0],
                        hora=linha[1],
                        temperatura=float(linha[8].replace(',','.') or 0),
                        umidade=float(linha[16].replace(',','.') or 0),
                        precipitacao=float(linha[3].replace(',','.') or 0)
                    )
                    registros_meteorologicos.append(registro)
                    
                    
                estacao:list[EstacaoMeteorologica]=EstacaoMeteorologica(
                                    nome=linhas[2].split(':;')[1].rstrip('\n'),
                                    codigo=linhas[3].split(':;')[1].rstrip('\n'),
                                    regiao=linhas[0].split(':;')[1].rstrip('\n'),
                                    uf=linhas[1].split(':;')[1].rstrip('\n'),
                                    latitude=float(linhas[4].split(':;')[1].rstrip('\n').replace(',','.')),
                                    longitude=float(linhas[5].split(':;')[1].rstrip('\n').replace(',','.')),
                                    altitude=float(linhas[6].split(':;')[1].rstrip('\n').replace(',','.')),
                                    registros=registros_meteorologicos
                                )
                estacoes.append(estacao)
        
        return estacoes
            