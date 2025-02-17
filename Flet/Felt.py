import flet as ft

def main(page):

    def add_clicked(e):
        if (usuari.value.strip == "" and password.value.strip == ""):
            usuari.value = ""
            password.value = ""
        else:
            page.add(ft.Checkbox(label=usuari.value.strip()))
            page.add(ft.Checkbox(label=password.value.strip()))
            page.add(ft.Checkbox(label=select_Rol.value.strip()))

            usuari.value = ""
            password.value = ""
            botonsito.disabled = True

            usuari.focus()


            page.update()

    def change(e):
        if (usuari.value.strip != "" and password.value.strip != ""):
            botonsito.disabled = False
        else:
            botonsito.disabled =True

        botonsito.update()

    select_Rol = ft.Dropdown(
        label="Rol",
        width=100,
        options=[
            ft.dropdown.Option("Admin"),
            ft.dropdown.Option("Usuari"),
            ft.dropdown.Option("Convidat"),
        ],
        autofocus=True,
        on_change=change
    )
    usuari = ft.TextField(label="Usuari", width=300, on_change=change)
    password = ft.Row([ ft.TextField(label="Contrasenya",password=True, can_reveal_password=True, on_change=change),])    
    botonsito = ft.ElevatedButton("Afegir",on_click=add_clicked,disabled=True)

 

    page.add(
        ft.Column([
        ft.Text("Formulari de Registre",size=40),
        ft.Divider(), 
        usuari,
        password,
        select_Rol,
        botonsito,
        ft.Divider(), 
        ft.Text("Llista d'usuaris",size=40),
        ]),
        )

ft.app(target=main)