from datetime import date, timedelta
import random
#import pdfarkhi

# Mapeamento dos meses
meses_alternativos = {
    1: "Absolon",
    2: "Braanum",
    3: "Tradesio",
    4: "Mildre",
    5: "Alarin",
    6: "Gaenio",
    7: "Rasmazi",
    8: "Celidet",
    9: "Almadin",
    10: "Flaman",
    11: "Nilantra",
    12: "Izirium"
}

# Mapeamento dos dias da semana
dias_da_semana_alternativos = {
    0: "Trafar  ",   # Segunda-feira
    1: "Bramin",   # Terça-feira
    2: "Tulpa  ",    # Quarta-feira
    3: "Zan     ",      # Quinta-feira
    4: "Adria   ",    # Sexta-feira
    5: "Calend",   # Sábado
    6: "Mudril"    # Domingo
}

        
def dado(n,l):
  #n = numero de dados
  #l = igual a numero de lados do dado

  dados = []
  for i in range(n):
    dados.append(random.randrange(l)+1)

  return dados

def teste():
  print("1d2 = ",dado(10,2))
  print("1d4 = ",dado(10,4))
  print("1d6 = ",dado(10,6))
  print("1d8 = ",dado(10,8))
  print("1d10 = ",dado(10,10))
  print("1d12 = ",dado(10,12))
  print("1d20 = ",dado(10,20))
  print("1d100 = ",dado(10,100))

#teste()

#Hora do dia
def hora_do_dia():
  saida =  dado(1,24)
  return saida[0]

def direcao_ventos():
  saida = ''
  direcao = dado(1,8)
  if direcao[0] == 1:
    saida += "Direção Norte -> Sul"
  elif direcao[0] == 2:
    saida += "Direção Nordeste -> Sudoeste"
  elif direcao[0] == 3:
    saida += "Direção Leste -> Oeste"
  elif direcao[0] == 4:
    saida += "Direção Sudeste -> Noroeste"
  elif direcao[0] == 5:
    saida += "Direção Sul -> Norte"
  elif direcao[0] == 6:
    saida += "Direção Sudoeste -> Nordeste"
  elif direcao[0] == 7:
    saida += "Direção Oeste -> Leste"
  else:
    saida += "Direção Noroeste -> Sudeste"

  saida += ' ('+str(direcao[0])+')'
  return saida

def velocidade_ventos():
  saida = ''
  velocidade = dado(1,10)
  if velocidade[0] < 6:
    saida += "Sem risco de pedrada"
  elif velocidade[0] < 8:
    saida += "Risco de pedrada de 1 em 1d8"
  elif velocidade[0] < 9:
    saida += "Risco de pedrada de 1 em 1d6"
  else:
    saida += "Risco de pedrada de 1 em 1d6"

  saida += ' ('+str(velocidade[0])+')'
  return saida


def temperatura(estacao,dia):
    if estacao == 0:
          temp = dado(1,20)
          temp += dado(1,10)
          temperatura = temp[0] + temp[1]  + 40

    elif estacao == 1:
          temp = dado(1,20)
          #temp += dado(1,10)
          if dia == 0:
              temperatura = temp[0]  + 30
          else:
              temperatura = temp[0]  + 25
              

    elif estacao == 2:
          temp = dado(1,20)
          #temp += dado(1,10)
          if dia == 0:
              temperatura = temp[0]  + 20
          else:
              temperatura = temp[0] +  10

    elif estacao == 3:
          temp = dado(1,20)
          temp += dado(1,10)
          if dia == 0:
              temperatura = temp[0] + temp[1]  + 30
          else:
              temperatura = temp[0] + temp[1]  + 25

    return str(temperatura)

def ajuste_padrao(total):
      ajuste = 0

      if  total < 4:
        ajuste = -3
      elif total < 6:
        ajuste = -2
      elif total < 9:
        ajuste = -1
      elif total < 13:
        ajuste = 0
      elif total < 16:
        ajuste = +1
      elif total < 18:
        ajuste = +2
      else:
        ajuste = +3

      return ajuste

def atributos():
    saida = ''
    while True:
      aux = dado(3,6)
      total = sum(aux)
      ajuste = ajuste_padrao(total)
      ajuste_total = 0
      ajuste_total += ajuste
      saida += "\n\nForça:        "+str(sum(aux))+"("+ str(ajuste)+")"+str(aux )
      aux = dado(3,6)
      total = sum(aux)
      ajuste = ajuste_padrao(total)
      ajuste_total += ajuste
      saida += '\n'+"Inteligência: "+str(sum(aux))+"("+ str(ajuste)+")"+ str(aux)
      aux = dado(3,6)
      total = sum(aux)
      ajuste = ajuste_padrao(total)
      ajuste_total += ajuste
      saida += '\n'+"Sabedoria: "+str(sum(aux))+"("+ str(ajuste)+")"+ str(aux)
      
      aux = dado(3,6)
      total = sum(aux)
      ajuste = ajuste_padrao(total)
      ajuste_total += ajuste
      saida += '\n'+"Destreza: "+str(sum(aux))+"("+ str(ajuste)+")"+ str(aux)
      aux = dado(3,6)
      total = sum(aux)
      ajuste = ajuste_padrao(total)
      ajuste_total += ajuste
      saida += '\n'+"Constituição: "+str(sum(aux))+"("+ str(ajuste)+")"+ str(aux)
      aux = dado(3,6)
      total = sum(aux)
      if  total < 4:
        ajuste = -2
      elif total < 9:
        ajuste = -1
      elif total < 13:
        ajuste = 0
      elif total < 18:
        ajuste = +1
      else:
        ajuste = +2
      ajuste_total += ajuste
      saida += '\n'+"Carisma: "+str(sum(aux))+"("+ str(ajuste)+")"+ str(aux)
      pecas_de_cobre = dado(3,6)
      pecas_de_cobre = sum(pecas_de_cobre)
      saida += '\n'+"Cobre Inicial: "+str(pecas_de_cobre)
      
      if ajuste_total >= 0:
        break
      else:
          saida += "\nFRACOTE!"

    return saida


def atributos2():
    saida = []
    personagem =  [None] * 69
    
    while True:
      aux = dado(3,6)
      total = sum(aux)
      ajuste = ajuste_padrao(total)
      ajuste_total = 0
      ajuste_total += ajuste
      saida += [total,ajuste,aux] #"\n\nForça:        "+str(sum(aux))+"("+ str(ajuste)+")"+str(aux )
      personagem[3] =  total

      aux = dado(3,6)
      total = sum(aux)
      ajuste = ajuste_padrao(total)
      ajuste_total += ajuste
      saida += [total,ajuste,aux] #'\n'+"Inteligência: "+str(sum(aux))+"("+ str(ajuste)+")"+ str(aux)
      personagem[4] =  total

      aux = dado(3,6)
      total = sum(aux)
      ajuste = ajuste_padrao(total)
      ajuste_total += ajuste
      saida += [total,ajuste,aux] # '\n'+"Sabedoria: "+str(sum(aux))+"("+ str(ajuste)+")"+ str(aux)
      personagem[5] =  total

      aux = dado(3,6)
      total = sum(aux)
      ajuste = ajuste_padrao(total)
      ajuste_total += ajuste
      saida += [total,ajuste,aux] # '\n'+"Destreza: "+str(sum(aux))+"("+ str(ajuste)+")"+ str(aux)
      personagem[6] =  total

      aux = dado(3,6)
      total = sum(aux)
      ajuste = ajuste_padrao(total)
      ajuste_total += ajuste
      saida += [total,ajuste,aux] # '\n'+"Constituição: "+str(sum(aux))+"("+ str(ajuste)+")"+ str(aux)
      personagem[7] =  total

      aux = dado(3,6)
      total = sum(aux)
      if  total < 4:
        ajuste = -2
      elif total < 9:
        ajuste = -1
      elif total < 13:
        ajuste = 0
      elif total < 18:
        ajuste = +1
      else:
        ajuste = +2
      ajuste_total += ajuste
      saida += [total,ajuste,aux] # '\n'+"Carisma: "+str(sum(aux))+"("+ str(ajuste)+")"+ str(aux)
      personagem[8] =  total

      pecas_de_cobre = dado(3,6)
      pecas_de_cobre = sum(pecas_de_cobre)*10
      saida += [pecas_de_cobre] # '\n'+"Cobre Inicial: "+str(pecas_de_cobre)
      personagem[63] =  pecas_de_cobre
  
      if ajuste_total >= 0:
        saida += [0]
        break
      else:
        saida += [1]
        break

    #pdfarkhi.preencher_ficha(personagem)
    
    return saida,personagem

tabela1 = [['Humanoide Morto (1)',[1,1],[0,0]] ,
           ['Yeldra (1d2)',[1,2],[2,0]],
           ['Lagarto Gigante do Deserto (1d2)',[1,2],[3,1]],
           ['Escorpião Gigante do Deserto (1d2)',[1,2],[4,0]],
           ['Coiote do Deserto (2d6)',[2,6],[2,0]],
           ['Besouro Gigante (1d6)',[1,6],[3,1]],
           ['Verme Argénteo (1d2)',[1,2],[15,0]],
           ['Esqueleto (2d6)',[2,6],[1,0]],
           ['Zumbi Desidratado (2d6)',[2,6],[2,0]],
           ['Homem Abutre (1d4)',[1,4],[3,0]],
           ['Demônio Abutre (1d2)',[1,2],[8,0]]]

def quantidade(qtd):
  return sum(dado(qtd[0],qtd[1]))

def pv(dadovida):
  return sum(dado(dadovida[0],8))+dadovida[1]

def Tabela1():
  saida = ''
  aux = dado(1,12)
  if aux[0] == 12:
    return Tabela2()
  else:
    saida = '\n'+tabela1[aux[0]-1][0]  +' Quantidade: '+  str(quantidade(tabela1[aux[0]-1][1]))  +' PVs: '+  str(pv(tabela1[aux[0]-1][2]))

    return saida

tabela2 = [['Ghoul (1d3)',[1,3],[3,0]],
           ['Escaravelho (1d6)',[1,6],[8,0]],
           ['Gigante Ígneo (1)',[1,1],[11,2]],
           ['Gigante do Deserto (1)',[1,1],[8,0]],
           ['Cavalo Selvagem (1d6)',[1,6],[2,0]],
           ['Jinn (1)',[1,1],[7,1]],
           ['Aranha Gigante do Deserto (1d4)',[1,4], [4,0] ],
           ['Cactoide Gigante (1d2)',[1,2],[8,0]],
           ['Ninfa do Oásis (1d4)',[1,4],[1,0]],
           ['Abutre Gigante (1d4)',[1,4],[3,3]],
           ['Gênio Areísco (1)',[1,1],[10,0]]]

def Tabela2():
  saida = ''  
  aux = dado(1,12)
  if aux[0] == 12:
    return  Tabela3()
  else:
      saida = '\n'+tabela2[aux[0]-1][0]  +' Quantidade: '+  str(quantidade(tabela2[aux[0]-1][1]))  +' PVs: '+  str(pv(tabela2[aux[0]-1][2]))


      return saida

tabela3 = [['Dríade das Dunas (1d2)',[1,2],[2,0]],
           ['Homem Chacal (1d4)',[1,4],[4,0]],
           ['Demônio do Deserto (1d4)',[1,4],[2,2]],
           ['Ankheg (1d6)',[1,6],[10,0]],
           ['Escorpião Coruja (1d4)',[1,4],[4,0]],
           ['Povo do Verde (Guerreiros) (2d6)',[2,6],[2,0]],
           ['Aventureiro (como Elfos, Anões e Halflings de 2º nível) (1d6)',[1,6],[2,0]],
           ['Assassino (como um Ladrão de 2º nível) (1d4)',[1,4],[2,0]],
           ['Caçador de Recompensas (1d4)',[1,4],[2,0]],
           ['Viajante Misterioso (como um Mago de 2º nível) (1d4)',[1,4],[2,0]],
           ['Clérigo Caótico (como um Mago de 2º nível) (1d4)',[1,4],[2,0]]]

def Tabela3():
  saida = ''
  aux = dado(1,12)
  if aux[0] == 12:
    return  Tabela4()
  elif aux[0] == 6:
  #Aventureiro (como Elfos, Anões e Halflings de 2º nível) (1d6)',[1,6],[2,0]],
      classe = dado(1,3)
      if classe[0] == 0:
         pontodevida = dado(1,6)
         saida = '\n'+tabela3[aux[0]-1][0]  +' Quantidade: '+  str(quantidade(tabela3[aux[0]-1][1]))  +' PVs: '+  str(pontodevida[0]+4) + ' (Elfos)'

      elif classe[0] == 1:
         pontodevida = dado(1,6)
         saida = '\n'+tabela3[aux[0]-1][0]  +' Quantidade: '+  str(quantidade(tabela3[aux[0]-1][1]))  +' PVs: '+  str(pontodevida[0]+4) + ' (Anoes)'

      else:
         pontodevida = dado(1,6)
         saida ='\n'+ tabela3[aux[0]-1][0]  +' Quantidade: '+  str(quantidade(tabela3[aux[0]-1][1]))  +' PVs: '+  str(pontodevida[0]+4) + ' (Halfling)'

  elif aux[0] == 7:
  #Assassino (como um Ladrão de 2º nível) (1d4)',[1,4],[2,0]],
      pontodevida = dado(1,6)
      saida = '\n'+tabela3[aux[0]-1][0]  +' Quantidade: '+  str(quantidade(tabela3[aux[0]-1][1]))  +' PVs: '+  str(pontodevida[0]+6)

  elif aux[0] == 9:
  #Viajante Misterioso (como um Mago de 2º nível) (1d4)',[1,4],[2,0]],
      pontodevida = dado(1,4)
      saida = '\n'+tabela3[aux[0]-1][0]  +' Quantidade: '+  str(quantidade(tabela3[aux[0]-1][1]))  +' PVs: '+  str(pontodevida[0]+4)

  elif aux[0] == 10:
  #Clérigo Caótico (como um Mago de 2º nível) (1d4)',[1,4],[2,0]]]
      pontodevida = dado(1,4)
      saida = '\n'+tabela3[aux[0]-1][0]  +' Quantidade: '+  str(quantidade(tabela3[aux[0]-1][1]))  +' PVs: '+  str(pontodevida[0]+4)

  else:
      saida = '\n'+tabela3[aux[0]-1][0]  +' Quantidade: '+  str(quantidade(tabela3[aux[0]-1][1]))  +' PVs: '+  str(pv(tabela3[aux[0]-1][2]))


  return saida

tabela4 = [['Yeldra (1d4)',[1,4],[2,0]],
           ['Yeldra da Noite (1d3)',[1,3],[2,0]],
           ['Glamério (1d2)',[1,2],[5,0]],
           ['Povo do Verde (Guerreiros) (3d6)',[3,6],[2,0]],
           ['Pterodáctilo (1d2)',[1,2],[4,0]],
           ['Leão Branco (1d6)',[1,6],[5,0]],
           ['Anhandêra (1d6)',[1,6],[3,3]],
           ['Maldição Pedra-Cabelo (4d6)',[4,6],[1,3]],
           ['Castanho (Guerreiro) (1d10)',[1,10],[2,0]],
           ['Morte-Sombra (1d6)',[1,6],[1,0]],
           ['Mãe-Plumada (1d2)',[1,2],[2,0]]]

def Tabela4():
  saida = ''
  aux = dado(1,12)
  if aux[0] == 12:
      return Tabela5()
  elif aux[0] == 9:
      saida ='\n'+ tabela4[aux[0]-1][0]  +' Quantidade: '+  str(quantidade(tabela4[aux[0]-1][1]))  +' PVs: '+  str(dado(1,4))
  else:
      saida = '\n'+tabela4[aux[0]-1][0]  +' Quantidade: '+  str(quantidade(tabela4[aux[0]-1][1]))  +' PVs: '+  str(pv(tabela4[aux[0]-1][2]))

  return saida


tabela5 = [['Javali-Toupeira (1d6)',[1,6],[3,0]],
           ['Ciclope Alienígena (1)',[1,1],[13,0]],
           ['Caveira-Gigante (1d4)',[1,4],[8,0]],
           ['Castanho Xamã (1)',[1,1],[3,0]],
           ['Sombra Agmista (1d8)',[1,8],[2,2]],
           ['Camaleão Jaonída (1)',[1,1],[6,1]],
           ['Rei Bruxo (Líder dos Diabos Brancos Menores) (1)',[1,1],[3,0]],
           ['Rei Branco (Líder dos Diabos Brancos Maiores) (1)',[1,1],[6,0]],
           ['Necromante Místico das Covas Castanhas (1 em 1d100)',[1,2],[10,0]]]

def Tabela5():
  saida = ''
  aux = dado(1,10)
  if aux[0] == 10:
      return Tabela6()
  elif aux[0] == 9:
      if dado(1,100)  == 1:
        saida = tabela5[aux[0]-1][0] +' Quantidade: '+  str(quantidade(tabela5[aux[0]-1][1]))  +' PVs: '+  str(pv(tabela5[aux[0]-1][2]))
      else:
        saida = '\n'+'O Necromante Místico das Covas Castanhas não aparece (Ufa)'
  else:
      saida = '\n'+ tabela5[aux[0]-1][0] +' Quantidade: '+  str(quantidade(tabela5[aux[0]-1][1]))  +' PVs: '+  str(pv(tabela5[aux[0]-1][2]))

  return saida

tabela6 = [['Mestre de ARKHI (ARKHImancista) (1d4)',[1,4],[2,0]],
           ['Caranguejo-Cabeça (1d10)',[1,10],[1,1]],
           ['Normósia (Centopeia Humana) (1)',[1,1],[6,0]],
           ['Escorpião Lunar (1d6)',[1,6],[4,0]],
           ['Morte-Alva (3d4)',[3,4],[2,0]],
           ['Antigo (de maneira discreta ou onírica – jamais o antigo se apresenta de corpo presente) (1)',[1,1],[57,0]]]

def Tabela6():
  saida = ''
  aux = dado(1,6)
  saida = '\n'+ tabela6[aux[0]-1][0] +' Quantidade: '+  str(quantidade(tabela6[aux[0]-1][1]))  +' PVs: '+  str(pv(tabela6[aux[0]-1][2]))
  return saida

def arkhi(opcao, quantidade):
    txtsaida = ''
    #print(type(opcao))
    if opcao == "1":
      txtsaida += "\nHora do dia: " + str(hora_do_dia()) + "h"
      txtsaida += "\nDirecao ventos: " + direcao_ventos()
      txtsaida += "\nVelocidade dos Ventos: " + velocidade_ventos()
      txtsaida += "\nTemperatura: "+ temperatura(0,0)+"°C"
      pass

  # Rolagem de Atributos
    elif opcao == "2":
      txtsaida += "\nRolagem 1"
      txtsaida = atributos()
      txtsaida += "\nRolagem 2"
      txtsaida = atributos()
      txtsaida += "\nRolagem 3"
      txtsaida = atributos()

    #print("\nFunção ainda não implementada")
    #pass

# Encontros Aleatóreos
    elif opcao == "3":
        #aux = input('Digite quantos encontros deseja sortear: ')
        aux = quantidade
        for i in range(int(aux)):
          aux = dado(1,6)
          if aux[0] == 1:
            #tabela 1
            txtsaida +=  Tabela1() 

          elif aux[0] == 2:
            #tabela 2
            txtsaida += Tabela2() 

          elif aux[0] == 3:
            #tabela 3
            txtsaida += Tabela3() 

          elif aux[0] == 4:
            #tabela 4
            txtsaida += Tabela4() 

          elif aux[0] == 5:
            #tabela 5
            txtsaida += Tabela5() 

          else:
            #tabela 6
            txtsaida += Tabela6() 

 #     elif opcao == "s":
  #      break

    else:
         txtsaida = "\nOpção Inválida"

    return txtsaida

def estacao(data_base=None):
    if data_base is None:
        data_base = date.today()

    dia = data_base.day
    nome_mes = meses_alternativos[data_base.month]

    hora1 = dado(1,24)
    dianoite = 0
    if hora1[0] >= 6 and hora1[0] <= 18:
        dianoite = 0
    else: dianoite = 1
    
    if (nome_mes == "Tradesio" and dia >= 20) or nome_mes == "Mildre" or nome_mes == "Alarin" or (nome_mes == "Gaenio" and dia < 21):
            return "  Estação do dia: Lardésia (outono)" + "  Temperatura: "+ temperatura(1,dianoite)+"°C" + " às "+str(hora1[0])+"h"
    elif (nome_mes == "Gaenio" and dia >= 21) or nome_mes == "Rasmazi" or nome_mes == "Celidet" or (nome_mes == "Almadin" and dia < 22):
            return "  Estação do dia: Albayok (inverno)" + "T  emperatura: "+ temperatura(2,dianoite)+"°C" + " às "+str(hora1[0])+"h"
            #print("\nLuzir (verão)")
    elif (nome_mes == "Almadin" and dia >= 22) or nome_mes == "Flaman" or nome_mes == "Nilantra" or (nome_mes == "Izirium" and dia < 22):
            #print("\nLardésia (outono)")
            return "  Estação do dia: Almínea (primavera)" + "  Temperatura: "+ temperatura(3,dianoite)+"°C" + " às "+str(hora1[0])+"h"
    else:
            return "  Estação do dia: Luzir (verão)" + "  Temperatura: "+ temperatura(0,dianoite)+"°C" + " às "+str(hora1[0])+"h"
       
        
           
def mostrar_calendario_arkhi(data_base=None):
    if data_base is None:
        # Data de hoje
        data_base = date.today()

    # Dia 1º de janeiro do mesmo ano
    inicio_do_ano = date(data_base.year, 1, 1)

    # Diferença de dias (incluindo o dia de hoje)
    dias_passados = (data_base - inicio_do_ano).days + 1

    saida = ''
    ano = "Ano: "+str(data_base.year - 1922)+"\n"
    saida +=  ano 

    for i in range(8):  # Hoje + 7 dias
        dia = data_base + timedelta(days=i)
        nome_dia_semana = dias_da_semana_alternativos[dia.weekday()]
        nome_mes = meses_alternativos[dia.month]
        if i == 0:
            saida += "Hoje: "+str(dias_passados)+", "+nome_dia_semana + ", " +str(dia.day)+" de "+nome_mes+estacao()+"\n"  
        else:
            saida += "        "+nome_dia_semana + ", " +str(dia.day)+" de "+nome_mes+estacao()+"\n"  

    return saida
          
            
    
# Executa
#mostrar_calendario_arkhi()
#estacao()
