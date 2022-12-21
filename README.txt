Gerador de Sonetos

Aqui eu pretendo construir uma máquina de produzir sonetos  petrarquianos (2 quartetos e 2 tercetos) com rimas seguindo o esquema "abba abba cdc dcd". A contagem das sílabas é feita com a biblioteca pyhyphen https://pypi.org/project/pyphen/
então não realiza a contagem de sílabas poéticas, que levam em conta a sonoridade, mas faz a contagem de sílabas gramaticais. Além disso alguns versos tem mais de dez sílabas, o que contraria a norma clássica para se fazer um soneto.

Os sonetos foram construídos aleatoriamente com base na lista de palavras da língua portuguesa elaborada por Renzo Nuccitelli e disponível em https://github.com/pythonprobr/palavras

Os sonetos produzidos estão salvos na pasta Sonetos.

O programa está escrito em Python e foram usadas as seguintes bibliotecas: random, os, hyphen e time. Você pode precisar instalá-las.
