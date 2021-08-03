import requests
import json
from filewrite import FileWrite
from parse import Parse
from url import Url

def PrintMenu(): 
    print('Covid Api Serch - Este programa busca dados atualizados sobre o avanço do coronavírus')
    print('VERSÃO ALPHA')

def Content(wdata):
    i = 0
    Pais = str(input("Insira o nome do país que precisa procurar. Obs:. Na grafia inglesa e primeira letra maíuscula: "))
    if wdata["results"] != 0:
        for x in wdata["response"]:
            if wdata["response"][i]["country"] == f"{Pais}":
                cdata = Parse.ParseCountryData(wdata, i)
                cdata += Parse.ParseFirstData(wdata, i)
                cdata += Parse.ParseSecondData(wdata, i)
                print(cdata)
                print("A saída do seu arquivo será em texto --> txt(.txt) ")
                escolha = str(input("Deseja escrever seu arquivo no desktop ou na pasta do script?").lower())
                if escolha == "desktop":
                    FileWrite.FileWriteTxt(cdata, Pais)
                else:
                    FileWrite.OpenFileWriteTxt(cdata,Pais)
                break
            else:
                i += 1

if __name__=="__main__":
    PrintMenu()
    response = requests.request("GET", Url.url, headers=Url.headers)
    json_data = response.json()
    data = json.dumps(json_data, indent=4)
    wdata = json.loads(data)
    if wdata["response"] != None:
        print("Dados carregados com sucesso, gostaria de gravá-los ou refinar sua pesquisa?")
        busca = str(input("Escreva qualquer coisa para gravar OU escreva \"CONTINUAR\" para continuar executando o programa: ").lower())
        if busca == "continuar":
            Content(wdata)
        else:
            escolha = str(input("Deseja escrever seu arquivo no desktop ou na pasta do script?").lower())
            if escolha == "desktop":
                FileWrite.FileWriteJson(data)
            else:
                FileWrite.OpenFileWriteJson(data)
    else:
        print('Arquivos não carregados. Você carregou a chave da Api?')
    print("Programa finalizado, pressione Enter para terminar  ")
    str(input(""))

