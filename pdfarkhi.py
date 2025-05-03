
from fillpdf import fillpdfs

def preencher_ficha(personagem, local):

    form_fields = list(fillpdfs.get_form_fields("ficha_arkhi_editavel_v1.0 (2).pdf").keys())

    name = 'Joãosão'
    classe = 'ladrão'
    titulo = 'mendigo'
    alinhamento = 'neutro'
    nivel = '1'

    data_dict = {
        form_fields[0]: str(personagem [0]),
        form_fields[1]: str(personagem [1]),
        form_fields[2]: titulo,
        form_fields[3]: str(personagem [3]),#'9', #forca
        form_fields[4]: str(personagem [4]),#'10',  # int
        form_fields[5]: str(personagem [5]),#'11',  # sab
        form_fields[6]: str(personagem [6]),#'12',  # dex
        form_fields[7]: str(personagem [7]),#'13',  # con
        form_fields[8]: str(personagem [8]),#'14',  # car
        form_fields[9]: '',  #save morte 
        form_fields[10]: '',  #save varinha
        form_fields[11]: '',  #save paralisia
        form_fields[12]: '',  #save sopro
        form_fields[13]: '',  #save magia
        form_fields[14]: '',  #modificador de sabedoria para clerigos
        form_fields[15]: alinhamento, 
        form_fields[16]: nivel, 
        form_fields[17]: '', #sede
        form_fields[18]: '', #vit ??
        form_fields[19]: '', #fome
        form_fields[20]: '', #pv
        form_fields[21]: '', #CA
        form_fields[22]: '', #atq
        form_fields[23]: '', #pv maximo
        form_fields[24]: '', #modificador de constituição
        form_fields[25]: '', #CA sem armadura
        form_fields[26]: '', #modificador de destreza na CA
        form_fields[27]: '', #modificador de destreza para ataques a distancia
        form_fields[28]: '', #iniciatica modificador
        form_fields[29]: '', #modificador de carisma para reações
        form_fields[30]: '', #teste de ouvir ruidos
        form_fields[31]: '', #abrir portas
        form_fields[32]: '', #encontrar passagem secreta
        form_fields[33]: '', #encontrar armadilhas
        form_fields[34]: '', #movimento base de jornada
        form_fields[35]: '', #movimento exporação
        form_fields[36]: '', #movimento de encontro
        form_fields[37]: '', #hablidades, etnia, divindade
        form_fields[38]: '', #ataque 5
        form_fields[39]: '', #ataque 0
        form_fields[40]: '', #ataque 9
        form_fields[41]: '', #ataque 4
        form_fields[42]: '', #imagem do personagem
        form_fields[43]: '', #idiomas
        form_fields[44]: '', #ataque 8
        form_fields[45]: '', #ataque 3
        form_fields[46]: '', #ataque 7
        form_fields[47]: '', #ataque 2
        form_fields[48]: '', #ataque 6
        form_fields[49]: '', #ataque 1
        form_fields[50]: 'x', #1 exaustão
        form_fields[51]: 'x', #3 exaustao
        form_fields[52]: 'x', #2 exaustao
        form_fields[53]: 'Yes', # letrado
        form_fields[54]: '', #equipamentos
        form_fields[55]: '', #Armas e armaduras
        form_fields[56]: '', #tesouros
        form_fields[57]: '', #itens mágicos
        form_fields[58]: '', #anotações
        form_fields[59]: '', #PL
        form_fields[60]: '', #PO
        form_fields[61]: '', #PE
        form_fields[62]: '', #PP
        form_fields[63]: str(personagem [63]),#'47', #PC
        form_fields[64]: '', #carga de tesouro em moedas
        form_fields[65]: '', #carga de equipamentos em moedas
        form_fields[66]: '', #carga total
        form_fields[67]: '', # XP
        form_fields[68]: '', # xp para o proximo nivel
        form_fields[69]: '', # modificador de atributo primário
    }

    fillpdfs.write_fillable_pdf( 'ficha_arkhi_editavel_v1.0 (2).pdf', local+'.pdf', data_dict)
