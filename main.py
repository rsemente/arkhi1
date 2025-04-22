import flet as ft

import random
import arkhi

#progama pra auxiliar na criação de Arkhi


#funções:
#1 - Rolar as condições iniciais da sessão
      #1 - Hora do dia: Sortear 1d24
      #2 - Sortear direção dos ventos - 1d8
      #3 - Sortear força do vento - 1d10
      #4 - Sortear Temperatura - 1d20 + 1d10 + 40
#2 - Rolagem de atributos
#3 - rolador de dados
#4 - rolagem de encontros aleatóreos
#5 - apresentação de dias de Lumn, com rolagem de temperatura e ventos apropriadas

#Proximas alterações funcionais
# Encontro rolar com tesouro
# Rolador de dados - ok
# Criador de nomes aleatoreos
# Criar login
# savar rolages para a pessoa
# criar lista de equipamentos e inventário


#Proximas alterações estéticas
# imprimir em uma caixa de texto - ok
# ativar funções com botões - ok







def main(page):
 
    app_bar = ft.AppBar(
        leading = ft.Icon(ft.Icons.DARK_MODE),
        title = ft.Text('Arkhi 1'),
        bgcolor=ft.Colors.GREY_500 ,
                          

        )    

    def meu_app(nome,dados):
            page.clean()
            page.add(app_bar)
            #page.add(ft.Text("\nO que deseja fazer? \n1 - Condições do tempo \n2 - Rolar atributos \n3 - Encontro Aleatorio \n"))
            page.add(ft.ElevatedButton("Que dia é hoje em Arkhi?", on_click=btn_click_4))
            page.add(ft.ElevatedButton("Gerar condições iniciais de jogo", on_click=btn_click))
            page.add(ft.ElevatedButton("Rolar atributos de personagens", on_click=btn_click2))

            row = ft.Row(spacing=10, controls=[ft.ElevatedButton("Gerar encontros aleatóreos", on_click=btn_click3),
                                              txt_name,])
                     
            page.add(row)
            
            row = ft.Row(spacing=10,
                          controls=[ft.ElevatedButton("rolar dados", on_click=rolar_dados),
                                                                txt_qdado,
                                              txt_tipo_dado,ft.Text(f"{dados}",
                                                                    selectable=True,),])
            page.add(row)
            page.add(ft.Container( ft.Column(spacing=10,
                                             height=300,
                                             #width=600,
                                             scroll=ft.ScrollMode.ALWAYS,
                                             controls=[ 
                                                     ft.Container(
                                                               ft.Text(f"{nome}",
                                                                       selectable=True,),
                                                     ),
                                                     ft.Container(ft.Text("                              ")),                                                     
                                             ]),
                                   #border=ft.border.all(1),
                                   )
                     )
            
            page.add(ft.Row(  controls=[ft.Text("\n\n\nARKHI 1 v0.3 \nCriado por Rodrigo Soares Semente\nDúvidas, reportar bugs e sugestões enviar e-mail para: rodrigo.semente@ufersa.edu.br ")]))


    def btn_click(e):
        #if not txt_name.value:
        #    txt_name.error_text = "Por favor, insira seu nome"
        #    page.update()
        #else:
            #print(type(txt_name.value))
            saidaarkhi = arkhi.arkhi('1',0)
            name = saidaarkhi #txt_name.value
            meu_app(name,'')

    def btn_click2(e):
        #if not txt_name.value:
        #    txt_name.error_text = "Por favor, insira seu nome"
        #    page.update()
        #else:
            #print(type(txt_name.value))
            saidaarkhi = arkhi.arkhi('2',0)
            name = saidaarkhi #txt_name.value
            meu_app(name,'')


    def btn_click3(e):
        if not txt_name.value:
            txt_name.error_text = "Por favor, digite a quantidade de encontros que deseja criar"
            page.update()
        else:
            #print(type(txt_name.value))
            saidaarkhi = arkhi.arkhi('3',txt_name.value)
            name = saidaarkhi #txt_name.value
            meu_app(name,'')

    def btn_click_4(e):
        #if not txt_name.value:
        #    txt_name.error_text = "Por favor, digite a quantidade de encontros que deseja criar"
        #    page.update()
        #else:
            #print(type(txt_name.value))
            saidaarkhi = arkhi.mostrar_calendario_arkhi()
            name = saidaarkhi #txt_name.value
            meu_app(name,'')
 
    def rolar_dados(e):
        if not txt_qdado.value:
            txt_qdado.error_text = "Quantidade de dados errada"
            page.update()
        elif not txt_tipo_dado.value:
            txt_tipo_dado.error_text = "Tipo de dados errado"
            page.update()
        else:
            #print(type(txt_name.value))
            aux = arkhi.dado(int(txt_qdado.value),int(txt_tipo_dado.value))
            dados = str(sum(aux))+ '  '+ str(aux)
            #page.clean(name)

            meu_app(name,dados)

    page.title = "ARKHI 1"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #Icons: CASSINO, CASTLE COLORIZE DARK_MODE EMOJI_OBJECTS   EMOJI_FLAGS  FILTER_HDR  FLARE  SHIELD  WHATSHOT

    name = ''        
    dados = ''
    
    txt_qdado = ft.TextField(label="Quantidade", width=100)
    txt_tipo_dado = ft.TextField(label="Tipo", width=100)
    txt_name = ft.TextField(label="Digite a quantidade de encontros")

    meu_app(name,dados)            
    
ft.app(main, view=ft.AppView.WEB_BROWSER)
