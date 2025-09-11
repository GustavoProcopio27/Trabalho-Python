def get_estado(abreviatura:str)->str:
    estados:dict[str,str]={
                "AC":'Acre' ,
                "AL":'Alagoas' ,
                "AP":'Amapá' ,
                "AM":'Amazonas' ,
                "BA":'Bahia' ,
                "CE":'Ceará' ,
                "DF":'Distrito Federal',
                "ES":'Espírito Santo',
                "GO":'Goiás' ,
                "MA":'Maranhão' ,
                "MT":'Mato Grosso' ,
                "MS":'Mato Grosso do Sul' ,
                "MG":'Minas Gerais' ,
                "PA":'Pará' ,
                "PB":'Paraíba' ,
                "PR":'Paraná' ,
                "PE":'Pernambuco' ,
                "PI":'Piauí ',
                "RJ":'Rio de Janeiro' ,
                "RN":'Rio Grande do Norte' ,
                "RS":'Rio Grande do Sul' ,
                "RO":'Rondônia' ,
                "RR":'Roraima' ,
                "SC":'Santa Catarina' ,
                "SP":'São Paulo ',
                "SE":'Sergipe' ,
                "TO":'Tocantins' ,
            }
    return estados.get(abreviatura)

def get_region(abreviatura:str)->str:
    regioes:dict[str,str]={
        "S":"Sul",
        "CO":"Centro Oeste",
        "NE":"Nordeste",
        "SE":"Sudeste",
        "N":"Norte"
    }
    return regioes.get(abreviatura)