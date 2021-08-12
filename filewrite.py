from datetime import date
import os
import os.path

class FolderWrite:
    def FolderWrite():
        username = os.getlogin()
        try:
            os.mkdir(f'C:\\Users\\{username}\\Desktop\\CovidApiScript')
            return 0
            
        except:
            print("Pasta já existente na área de trabalho")
            return 1


class FileWrite:
    def FileWriteTxt(cdata, Pais):
        dia = date.today()
        data_hoje = (f'{dia.day}.{dia.month}.{dia.year}')
        username = os.getlogin()
        folder = FolderWrite.FolderWrite()
        if folder == 0:
            path = (f'C:\\Users\\{username}\\Desktop\\CovidApiScript')
        if folder == 1:
            try:
                path = (f'C:\\Users\\{username}\\Desktop\\CovidApiScript')
            except:
                path = (f'C:\\Users\\{username}\\Desktop\\CovidApiScript')
                
        try:
            file = open(f'{path}\\{Pais}_{data_hoje}_Estatística-Covid.txt', 'x')
            file.write(cdata)
            file.close()
        except:
            print("*O arquivo já existe, o programa escreverá os novos conteúdos no final do arquivo original*")
            file = open(f'{path}\\{Pais}_{data_hoje}_Estatística-Covid.txt', "a")
            file.write(cdata)
            file.close()

    def OpenFileWriteTxt(cdata, Pais):
        try:
            file = open(f"{Pais}_Estatística-Covid.txt", "x")
            file.write(cdata)
            file.close()
        except:
            print("*O arquivo já existe, o programa escreverá os novos conteúdos no final do arquivo original*")
            file = open(f"{Pais}_Estatística-Covid.txt", "a")
            file.write(cdata)
            file.close()

    def FileWriteJson(data):
    
        dia = date.today()
        data_hoje = (f'{dia.day}.{dia.month}.{dia.year}')
        username = os.getlogin()
        folder = FolderWrite.FolderWrite()
        if folder == 0:
            path = (f'C:\\Users\\{username}\\Desktop\\CovidApiScript')
        if folder == 1:
            try:
                path = (f'C:\\Users\\{username}\\Desktop\\CovidApiScript')
            except:
                path = (f'C:\\Users\\{username}\\Desktop\\CovidApiScript')

        try:
            file = open(f'{path}\\Estatística-Covid_{data_hoje}.json', 'a')
            file.write(data)
            file.close()
        except:
            print("*O arquivo já existe, o programa escreverá os novos conteúdos no final do arquivo original*")
            file = open(f'{path}\\Estatística-Covid_{data_hoje}.json', 'a')
            file.write(data)
            file.close()
    def OpenFileWriteJson(data):
        dia = date.today()
        data_hoje = (f'{dia.day}.{dia.month}.{dia.year}')
        try:
            file = open(f'Estatística-Covid_{data_hoje}.json', 'a')
            file.write(data)
            file.close()
        except:
            print("*O arquivo já existe, o programa escreverá os novos conteúdos no final do arquivo original*")
            file = open(f'Estatística-Covid_{data_hoje}.json', 'a')
            file.write(data)
            file.close()