from datetime import date
import os

class FileWrite:
    def FileWriteTxt(cdata, Pais):
        dia = date.today()
        data_hoje = (f'{dia.day}.{dia.month}.{dia.year}')
        username = os.getlogin()
        try:
            file = open(f'C:\\Users\\{username}\\Desktop\\{Pais}_{data_hoje}_Estatística-Covid.txt', 'x')
            file.write(cdata)
            file.close()
        except:
            print("*O arquivo já existe, o programa escreverá os novos conteúdos no final do arquivo original*")
            file = open(f'C:\\Users\\{username}\\Desktop\\{Pais}_{data_hoje}_Estatística-Covid.txt', "a")
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
        try:
            file = open(f'C:\\Users\\{username}\\Desktop\\Estatística-Covid_{data_hoje}.json', 'a')
            file.write(data)
            file.close()
        except:
            print("*O arquivo já existe, o programa escreverá os novos conteúdos no final do arquivo original*")
            file = open(f'C:\\Users\\{username}\\Desktop\\Estatística-Covid_{data_hoje}.json', 'a')
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