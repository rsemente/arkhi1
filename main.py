import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, colors
import random
import arkhi
#import pdfarkhi

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

#referencias: https://www.youtube.com/watch?v=pRa52ihSq_A&t=3725s





def main(page):
    page.title = "ARKHI 1"

    nome = 'teste'        
    dados = ''
    forca = ''
    
    def btn_click(e):
        #if not txt_name.value:
        #    txt_name.error_text = "Por favor, insira seu nome"
        #    page.update()
        #else:
            #print(type(txt_name.value))
            saidaarkhi = arkhi.arkhi('1',0)
            nome = saidaarkhi #txt_name.value
            txt_saida.value = nome
            page.update()
            #meu_app(nome,'')

    def btn_click2(e):
        #if not txt_name.value:
        #    txt_name.error_text = "Por favor, insira seu nome"
        #    page.update()
        #else:
            #print(type(txt_name.value))
            #saidaarkhi = arkhi.arkhi('2',0)
            personagem =  [None] * 69
            saidaarkhi,personagem = arkhi.atributos2()
            txt_forca.value = str(personagem[3])
            txt_int.value = str(personagem[4])
            txt_sab.value = str(personagem[5])
            txt_des.value = str(personagem[6])
            txt_con.value = str(personagem[7])
            txt_car.value = str(personagem[8])

            txt_cobre.value = str(personagem[63])

            txt_classe.options.clear()
            if personagem[7] >= 9: 
                txt_classe.options.append(  ft.dropdown.Option("Anão"))

            txt_classe.options.append( ft.dropdown.Option("Clérigo"))
            if personagem[4] >= 9:
                txt_classe.options.append( ft.dropdown.Option("Elfo"))

            txt_classe.options.append( ft.dropdown.Option("Guerreiro"))
            if personagem[7] >= 9 and personagem[6] >= 9: 
                txt_classe.options.append(ft.dropdown.Option("Halfling"))

             
            txt_classe.options.append( ft.dropdown.Option("Ladrão"))
            txt_classe.options.append( ft.dropdown.Option("Mago"))
                
            #txt_classe.options.append( classes_jogaveis)
            if saidaarkhi[19] == 0:
                nome = "Não é Fracote" #str(saidaarkhi) #txt_name.value
            else:
                nome = "Fracote!!\nPode rolar novamente" #str(saidaarkhi) #txt_name.value
            
            txt_saida2.value = nome
            page.update()
            #meu_app(nome,'')

    def btn_save(e:ft.FilePickerResultEvent):   #https://www.youtube.com/watch?v=KDZOoxTNqaU
            save_location = e.path
            if save_location:
                try:
                    personagem =  [None] * 69

                    personagem[0] = txt_nome_personagem.value
                    personagem[1] = txt_classe.value
                    
                    personagem[3] = int(txt_forca.value)
                    personagem[4] = int(txt_int.value)
                    personagem[5] = int(txt_sab.value)
                    personagem[6] = int(txt_des.value)
                    personagem[7] = int(txt_con.value)
                    personagem[8] = int(txt_car.value)
            
                    #pdfarkhi.preencher_ficha(personagem, save_location)
                except Exception as e:
                    print("Erro ao salvar",e)
                    
     
    def btn_click3(e):
        if not txt_name.value:
            txt_name.error_text = "Por favor, digite a quantidade de encontros que deseja criar"
            page.update()
        else:
            #print(type(txt_name.value))
            saidaarkhi = arkhi.arkhi('3',txt_name.value)
            nome = saidaarkhi #txt_name.value
            txt_saida.value = nome
            page.update()
            #meu_app(nome,'')

    def btn_click_4(e):
        #if not txt_name.value:
        #    txt_name.error_text = "Por favor, digite a quantidade de encontros que deseja criar"
        #    page.update()
        #else:
            #print(type(txt_name.value))
            saidaarkhi = arkhi.mostrar_calendario_arkhi()
            nome = saidaarkhi #txt_name.value
            txt_saida.value = nome
            page.update()
            
            #meu_app(nome,'')
 
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
            txt_dado.value = dados
            page.update()
            #meu_app(nome,dados)


    def escolha_de_classe(e):
        print("classe escolhida")


    txt_dado = ft.TextField(f"{dados}")
    txt_saida = ft.TextField(f"{nome}",multiline=True,)
    txt_saida2 = ft.TextField(f"{nome}",multiline=True, width=300)
    txt_name = ft.TextField(label="Digite a quantidade de encontros")
    txt_qdado = ft.TextField(label="Quantidade de Dados", width=100)
    txt_tipo_dado = ft.TextField(label="Tipo de Dado", width=100)

    txt_nome_personagem = ft.TextField(label="Digite o nome do personagem")
    classes_jogaveis = []
             #   ft.dropdown.Option("Anão"),
             #   ft.dropdown.Option("Clérigo"),
             #   ft.dropdown.Option("Elfo"),
             #   ft.dropdown.Option("Guerreiro"),
             #   ft.dropdown.Option("Halfling"),
             #   ft.dropdown.Option("Ladrão"),
             #   ft.dropdown.Option("Mago"),
 
            #]
    txt_classe = ft.Dropdown(
                label="Classe de personagem",
                hint_text = "role os dados",
                #hint_text="Choose your favourite color?",
                options=classes_jogaveis,
                width=250,
                on_change=escolha_de_classe)
            #ft.TextField(label="Escolha a classe de personagem")

    txt_forca = ft.TextField(f"{forca}", width=50)
    txt_int = ft.TextField(f"{forca}", width=50)
    txt_sab = ft.TextField(f"{forca}", width=50)
    txt_des = ft.TextField(f"{forca}", width=50)
    txt_con = ft.TextField(f"{forca}", width=50)
    txt_car = ft.TextField(f"{forca}", width=50)
    txt_cobre = ft.TextField(f"{forca}", width=50)

    saveme = ft.FilePicker(on_result=btn_save)
    page.overlay.append(saveme)
    
    
    def meu_app(e):
        page.views.clear()
        page.views.append(  #pagina principal
            View(
                "/",
                [
                    
                    AppBar(leading = ft.Icon(ft.Icons.DARK_MODE),
                                     title=Text("Arkhi 1"),
                                     bgcolor=ft.Colors.GREY_500),
                    #ElevatedButton("Criar Personagens", on_click=lambda _: page.go("/store")),
                    ElevatedButton("Que dia é hoje em Arkhi?", on_click=btn_click_4),
                    ElevatedButton("Gerar condições iniciais de jogo", on_click=btn_click),
                    ft.Row(spacing=10, controls=[ft.ElevatedButton("Gerar encontros aleatóreos",
                                                                on_click=btn_click3),
                                              txt_name,]),
                    ft.Row(spacing=10,
                          controls=[ft.ElevatedButton("rolar dados", on_click=rolar_dados),
                                                                txt_qdado,
                                              txt_tipo_dado,txt_dado,]),
                    ft.Container( ft.Column(spacing=10,
                                             height=300,
                                             #width=600,
                                             scroll=ft.ScrollMode.ALWAYS,
                                             controls=[ 
                                                     ft.Container(
                                                               txt_saida,
                                                     ),
                                                     ft.Container(ft.Text("                              ")),                                                     
                                             ]),
                                   #border=ft.border.all(1),
                                   ),
                    ft.Row(  controls=[ft.Text("\n\n\nARKHI 1 v0.4 \nCriado por Rodrigo Soares Semente\nDúvidas, reportar bugs e sugestões enviar e-mail para: rodrigo.semente@ufersa.edu.br ")])

                ],
            )
        )
        if page.route == "/store":    #pagina de criação de personagens
            page.views.append(      
                View(
                    "/store",
                    [
                        AppBar(ft.Icon(ft.Icons.DARK_MODE),
                               title=Text("Arkhi 1 - Criador de personagem"),
                               bgcolor=ft.Colors.GREY_500),
                        ft.Row(spacing=10, controls=[txt_nome_personagem,
                                              txt_classe,]),
                        ElevatedButton("Rolar atributos de personagens", on_click=btn_click2),
                        ft.Container( ft.Column(spacing=10,
                                             height=300,
                                             #width=600,
                                             scroll=ft.ScrollMode.ALWAYS,
                                             controls=[ 
                                                     ft.Container(ft.Row(spacing=10,
                                                              controls=[ ft.Text("Força:           "),
                                                                         txt_forca,
                                                                         ft.Text("Inteligencia:   "),
                                                                         txt_int,
                                                                       ]),
                                                     ),
                                                    # ft.Container(ft.Row(spacing=10,
                                                    #          controls=[ ft.Text("Inteligencia: "),
                                                   #                      txt_int,
                                                    #                   ]),
                                                    # ),
                                                     ft.Container(ft.Row(spacing=10,
                                                              controls=[ ft.Text("Sabedoria:    "),
                                                                         txt_sab,
                                                                         ft.Text("Destreza:        "),
                                                                         txt_des,
                                                                       ]),
                                                     ),
                                                   #  ft.Container(ft.Row(spacing=10,
                                                  #            controls=[ ft.Text("Destreza:      "),
                                                  #                       txt_des,
                                                   #                    ]),
                                                   #  ),
                                                     ft.Container(ft.Row(spacing=10,
                                                              controls=[ ft.Text("Constituição: "),
                                                                         txt_con,
                                                                         ft.Text("carisma:         "),
                                                                         txt_car,
                                                                       ]),
                                                     ),
                                                  #   ft.Container(ft.Row(spacing=10,
                                                 #             controls=[ ft.Text("carisma:         "),
                                                #                         txt_car,
                                                 #                      ]),
                                                  #   ),
                                                     ft.Container(txt_saida2,
                                                     ),
                                                     ft.Container(ft.Row(spacing=10,
                                                              controls=[ ft.Text("Peças de Cobre: "),
                                                                         txt_cobre,
                                                                         ]),
                                                     ),
                                                     ElevatedButton("Salvar personagem", on_click=lambda _: saveme.save_file()
                                                     ),
                        
                                                     ft.Container(ft.Text("                              ")),                                                     
                                             ]),
                                   #border=ft.border.all(1),
                                   ),
                        
                    ft.Row(  controls=[ft.Text("\n\n\nARKHI 1 v0.4 \nCriado por Rodrigo Soares Semente\nDúvidas, reportar bugs e sugestões enviar e-mail para: rodrigo.semente@ufersa.edu.br ")])

                        




                        
                    ],
                )
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


  


    page.on_route_change = meu_app
    page.on_view_pop = view_pop

    page.go(page.route)

ft.app(main, view=ft.AppView.WEB_BROWSER)
