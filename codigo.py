#botão de iniciar chat

import flet as ft 

def main(pagina):
    texto = ft.Text("Chat do Timão")
    pagina.add(texto)

    chat =ft.Column()

    nome_usuario= ft.TextField(label="Escreva o nome do Torcedor")

    def enviar_mensagem_tunel(mensagem):
       texto_mensagem = mensagem["texto"]
       usuario_mensagem=mensagem["usuario"]

       chat.controls.append(ft.Text(f"{usuario_mensagem}:{texto_mensagem}"))
       pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
  

    def enviar_mensagem(evento):
       pagina.pubsub.send_all({"texto":campo_mensagem.value,"Usuario":nome_usuario.value})
       campo_mensagem.value =""
       pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem")

    botao_enviar_mensagem= ft.ElevatedButton("Enviar", on_click= enviar_mensagem)

    def entrar_popup(evento):
       pagina.add(chat)
       popup.open=False
       pagina.remove(botao)
       pagina.add(ft.Row(
          [campo_mensagem,botao_enviar_mensagem]
          ))
    
       pagina.update()


    popup = ft.AlertDialog(
       open=False,
       modal=True,
       title=ft.Text("Bem vindo ao Chat do Timão"),
       content=nome_usuario,
       actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
       )
        

    def entrar_chat(evento):
      pagina.dialog = popup
      popup.open = True
      pagina.update()



    botao= ft.ElevatedButton("Iniciar o Chat", on_click=entrar_chat)
    pagina.add(botao)

ft.app(target=main)
