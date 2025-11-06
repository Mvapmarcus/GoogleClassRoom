import flet as ft

def principal(pagina: ft.Page):
    pagina.bgcolor = "green"

    teto1 = ft.Text("Olá mundo!",
                    size=50,
                    height=50,
                    color="blue"
                    )
                    
    image1 = ft.Image("https://motobrasil.wordpress.com/wp-content/uploads/2010/06/img_7105.jpg")

    
    pagina.add(teto1,image1)
   

ft.app(target=principal)