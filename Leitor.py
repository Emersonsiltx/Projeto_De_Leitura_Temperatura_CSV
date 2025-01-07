import csv
import os

aq = str(input('Digite o nome do arquivo: '))

if os.path.isfile("./"+aq):
    with open(aq, 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=',')
        for linhas in leitor:
            print(linhas)
else:
    print('O arquivo não existe')