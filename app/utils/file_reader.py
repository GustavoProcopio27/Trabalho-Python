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
        
        estacoes:list[EstacaoMeteorologica]=list()
        diretorio:list[str]=listdir(path)
        if len(diretorio)==0:
            print("Nenhum dado encontrado, retornando...\n ")
            return None

        for file in diretorio:

            full_path:str=join(path,file)
            if not isfile(full_path):
                print('arquivo inexistente')
                continue
            
            else:    
                linhas:list[str]
                with open(file=full_path,mode="r",encoding="latin-1") as f:
                    linhas:list[str]=f.readlines()
                
                
                organized_records:dict[str,list[str]] = {
                                        'cabecalho':linhas[8].split(';'),
                                        'dados':[row.split(';') for row in linhas[9:len(linhas)]]
                                    }              

                registros_meteorologicos:list[RegistroMetereologico]=list()
                for linha in organized_records['dados']:
                    registros_meteorologicos.append(RegistroMetereologico(
                        data=linha[0],
                        hora=linha[1],
                        temperatura=float(linha[7].replace(',','.') or 0),
                        umidade=float(linha[14].replace(',','.') or 0),
                        precipitacao=float(linha[2].replace(',','.') or 0)
                    ))
                    
                
                estacoes.append(EstacaoMeteorologica(
                                    nome=linhas[2].split(':;')[1].strip(),
                                    codigo=linhas[3].split(':;')[1].strip(),
                                    regiao=linhas[0].split(':;')[1].strip(),
                                    uf=linhas[1].split(':;')[1].strip(),
                                    latitude=float(linhas[4].split(':;')[1].strip().replace(',','.')),
                                    longitude=float(linhas[5].split(':;')[1].strip().replace(',','.')),
                                    altitude=float(linhas[6].split(':;')[1].replace(";","").strip().replace(',','.')),
                                    registros=registros_meteorologicos
                                ))
        
        return estacoes
            