import flet as ft

def SuccessButton(function, label, col = {}):
    return ft.ElevatedButton(text=label, on_click=function, color=ft.colors.GREEN, col=col)

def OutputBox():
    return ft.Text(value="Hola")