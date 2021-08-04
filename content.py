from parse import Parse
from filewrite import FileWrite
class Content:
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
