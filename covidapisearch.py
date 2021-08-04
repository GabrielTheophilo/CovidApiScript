import json
from filewrite import FileWrite
from content import Content
from url import *
from request import *
from printmenu import *


if __name__=="__main__":
    PrintMenu.__init__()
    ChoiceMenu.__init__()
    escolha_dados = str(input("---->").lower())
    if escolha_dados == "dados históricos" or escolha_dados == "históricos":
        query = str(input("Insira o país que deseja buscar dados(na grafia inglesa): ").lower())
        ano = int(input("Insira o ano(2020-2021): "))
        mes = str(input("Insira o mês da pesquisa(com dois dígitos): "))
        dia = str(input("Insira o dia da pesquisa(com dois dígitos): "))
        querystring = {"country":f"{query}","day":f"{ano}-{mes}-{dia}"}
        data = RequestHistorical.__init__(UrlHistorical.url, UrlHistorical.headers, querystring)
        wdata = json.loads(data)
        if wdata["response"] != None:
            print("Dados carregados com sucesso")
            escolha = str(input("Deseja escrever seu arquivo no desktop ou na pasta do script?").lower())
            if escolha == "desktop":
                FileWrite.FileWriteJson(data)
            else:
                FileWrite.OpenFileWriteJson(data)
            
    else:    
        data = Request.__init__(UrlGeneral.url, UrlGeneral.headers)
        wdata = json.loads(data)
        if wdata["response"] != None:
            print("Dados carregados com sucesso, gostaria de gravá-los ou refinar sua pesquisa?")
            busca = str(input("Escreva qualquer coisa para gravar OU escreva \"CONTINUAR\" para continuar executando o programa: ").lower())
            if busca == "continuar":
                Content.Content(wdata)
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

