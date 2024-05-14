import flet as ft

def SuccessButton(function, label, col = {}):
    return ft.Container(
        content=ft.ElevatedButton(text=label, on_click=function, color=ft.colors.GREEN),
        alignment=ft.alignment.bottom_right,
        col=col
    )

class OutputBox:
    value = ""
    label = None
    def __init__(self) -> None:
        self.label = ft.Text(value="")
        self.text = ft.Container(
            content=self.label,
            padding=10,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.WHITE10,
            border_radius=10,
            visible=False
        )
    
    def update(self):
        self.label.value = self.value
        self.text.visible = True
        self.label.update()
        self.text.update()