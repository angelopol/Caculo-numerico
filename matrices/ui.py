import flet as ft

def SuccessButton(function, label, col = {}):
    return ft.Container(
        content=ft.ElevatedButton(
            height=80, on_click=function, color=ft.colors.GREEN,
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.ARROW_FORWARD_ROUNDED, color="green"),
                    ft.Text(label, style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color="green"))
                ],
                width=150,
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ),
        alignment=ft.alignment.bottom_right,
        col=col
    )

class AtentionDialogs:
    def __init__(self, page):
        self.page = page
        self.modal = ft.AlertDialog(
            modal=True,
            actions=[
                ft.TextButton("Continuar", on_click=lambda _, e: self.close()),
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

    def SetContent(self, title, message):
        self.modal.title = ft.Text(title)
        self.modal.content = ft.Text(message)
        self.modal.update()

    def open(self):
        self.page.dialog = self.modal
        self.modal.g.open = True
        self.page.update()
    
    def close(self):
        self.modal.open = False
        self.page.update()

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