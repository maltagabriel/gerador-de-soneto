import random
import os
from hyphen import Hyphenator
from hyphen.dictools import *
from time import process_time

for lang in ['pt_BR']:
    if not is_installed(lang): install(lang)

pt_br = Hyphenator('pt_BR')

dic = open('palavras.txt')
palavras = list(dic)

# Vetor contendo as duas últimas sílabas das palavras
fins =[]
for palavra in palavras:
    fins.append(pt_br.syllables(palavra[:-1])[-2:])

# Concatenando as duas sílabas finais pra definir o dicionário de terminações
dic_rimas = {}
for fim in fins:
    fim = ''.join(fim)
    dic_rimas[fim] = []

# Adicionando palavras ao dicionário de fins
for palavra in palavras:
    fim_palavra = pt_br.syllables(palavra[:-1])[-2:]
    fim_palavra = ''.join(fim_palavra)
    if fim_palavra in dic_rimas.keys():
        dic_rimas[fim_palavra].append(palavra[:-1])
    else:
        dic_rimas[fim_palavra] = [palavra[:-1]]

def sort_palavra():
    r = random.randint(0, len(palavras))
    ran_palavra = palavras[r][:-1]
    sil_palavra = pt_br.syllables(ran_palavra)
    return ([ran_palavra, sil_palavra])

def cria_verso():
    verso = []
    tam = 0
    while tam < 10:
        palavra = sort_palavra()
        verso.append(palavra[0])
        tam = tam + len(palavra[1])
    palavra_final = verso[len(verso)-1]
    verso_fim = pt_br.syllables(palavra_final)[-2:]
    verso_fim = ''.join(verso_fim)
    return ([verso, verso_fim])

def cria_verso_rimado(verso, verso_fim):
    r = random.randint(0, len(dic_rimas[verso_fim])-1)
    palavra_rimada = dic_rimas[verso_fim][r]
    verso_rimado = [palavra_rimada]
    tam = len(palavra_rimada[1])
    while tam <10:
        palavra_nova = sort_palavra()
        verso_rimado.insert(-1,palavra_nova[0])
        tam = tam + len(palavra_nova[1])
    return(verso_rimado)
        
def cria_soneto():
    proximo_soneto = len(os.listdir("Sonetos"))+1
    titulo = 'Soneto {}'.format(proximo_soneto)
    #pasta = os.listdir("Sonetos")
    #i = len(pasta)
    #cont = str(i+1)
    #titulo = ['Soneto', cont]
    #titulo = ' '.join(titulo)
    
    versoA1 = cria_verso()
    versoB1 = cria_verso()
    versoC1 = cria_verso()
    versoD1 = cria_verso()
    versoA2 = cria_verso_rimado(versoA1[0],versoA1[1])
    versoA3 = cria_verso_rimado(versoA1[0],versoA1[1])
    versoA4 = cria_verso_rimado(versoA1[0],versoA1[1])
    versoB2 = cria_verso_rimado(versoB1[0],versoB1[1])
    versoB3 = cria_verso_rimado(versoB1[0],versoB1[1])
    versoB4 = cria_verso_rimado(versoB1[0],versoB1[1])
    versoC2 = cria_verso_rimado(versoC1[0],versoC1[1])
    versoC3 = cria_verso_rimado(versoC1[0],versoC1[1])
    versoD2 = cria_verso_rimado(versoD1[0],versoD1[1])
    versoD3 = cria_verso_rimado(versoD1[0],versoD1[1])

    verso1 = ' '.join(versoA1[0])
    verso2 = ' '.join(versoB1[0])
    verso3 = ' '.join(versoB2)
    verso4 = ' '.join(versoA2)
    
    estrofe1 = [verso1, verso2, verso3, verso4]
    estrofe1 = '\n'.join(estrofe1)

    verso5 = ' '.join(versoB3)
    verso6 = ' '.join(versoA3)
    verso7 = ' '.join(versoA4)
    verso8 = ' '.join(versoB4)
    
    estrofe2 = [verso5, verso6, verso7, verso8]
    estrofe2 = '\n'.join(estrofe2)

    verso9 = ' '.join(versoC1[0])
    verso10 = ' '.join(versoD1[0])
    verso11 = ' '.join(versoC2)
    
    estrofe3 = [verso9, verso10, verso11]
    estrofe3 = '\n'.join(estrofe3)

    verso12 = ' '.join(versoD2)
    verso13 = ' '.join(versoC3)
    verso14 = ' '.join(versoD3)
    
    estrofe4 = [verso12, verso13, verso14]
    estrofe4 = '\n'.join(estrofe4)

    soneto = [titulo, estrofe1, estrofe2, estrofe3, estrofe4]
    soneto = '\n\n'.join(soneto)
    
    novo_soneto = open('Sonetos/soneto_'+str(proximo_soneto)+'.txt', 'w')
    novo_soneto.write(soneto)
    novo_soneto.close()
    #os.rename('titulo.txt',titulo)
    
    return soneto

if __name__ == "__main__":
    soneto = cria_soneto()
    print(soneto)
