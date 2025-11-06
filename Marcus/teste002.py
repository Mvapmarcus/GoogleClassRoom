import flet as ft

def main(pagina: ft.Page):
    pagina.bgcolor = "black"
    var_1 = 0
    var_2 = 0
    def teclado(evento:ft.KeyboardEvent):
        nonlocal var_1, var_2
        if evento.key.lower() == "q": 
            var_1 += 1
            if var_1 == 20:
                win_1 = ft.Text("Jogador 1 venceu!")
                pagina.add(win_1)

        if evento.key.lower() == "p":
            var_2 +=1
            if var_2 == 20:
                win_2 = ft.Text("Jogador 2 venceu!",)
                pagina.add(win_2)      
          
    text = ft.Text("Bem vindos ao app!",color="red",size=60)
    pagina.on_keyboard_event = teclado
    pagina.add(text)
   
ft.app(main)