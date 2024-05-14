import flet as ft

def MakeBottomButton(label, col, ColorHex, color, icon, function):
    return ft.Container(
        content=ft.ElevatedButton(
            height=80, on_click=function, color=color,
            content=ft.Row(
                [
                    ft.Icon(name=icon, color=ColorHex),
                    ft.Text(label, style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color=ColorHex))
                ],
                width=150,
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ),
        alignment=ft.alignment.bottom_right,
        col=col
    )

def SuccessButton(function, label, col = {}):
    return MakeBottomButton(label, col, "green", ft.colors.GREEN, ft.icons.ARROW_FORWARD_ROUNDED, function)

def HistorialButton(HistorialModal, col = {}):
    return MakeBottomButton("Historial", col, "blue", ft.colors.BLUE,
        ft.icons.FILTER_LIST_ROUNDED, lambda _: HistorialModal.open())

def BottomButtons(function, label, historial, col = {}):
    return ft.Row(
        [HistorialButton(historial, col), SuccessButton(function, label)],
        alignment=ft.MainAxisAlignment.END
    )

def MakeLabel(label = None, content = None, visible = True, bg = True, alignment=ft.alignment.center, size = 20):
    if content == None:
        content = ft.Text(label, style=ft.TextStyle(size=size))
    if bg:
        return ft.Container(
            content=content,
            padding=10,
            alignment=alignment,
            bgcolor=ft.colors.WHITE10,
            border_radius=40,
            visible=visible
        )
    else:
        return ft.Container(
            content=content,
            padding=10,
            alignment=alignment,
            border_radius=40,
            visible=visible
        )

def ModalButton(label, function):
    return ft.ElevatedButton(
        content=ft.Text(label, style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20, color="#D4E1FF")),
        on_click=function, height= 50, width=200
    )

class HistorialModal:
    def __init__(self, page, output):
        self.output = output
        self.page = page
        self.modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Historial."),
            actions=[
                ModalButton("Cerrar", lambda _: self.close())
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER
        )

    def MakeResults(self):
        elements = []
        results = self.output.GetResults()
        if len(results) == 0:
            return ft.Text("Aùn no ha generado ningùn resultado.", style=ft.TextStyle(size=18))
        for result in reversed(results):
            elements.append(MakeLabel(result, size=15))
        return ft.Column(elements, alignment=ft.MainAxisAlignment.START, expand=True)

    def open(self):
        self.modal.content = self.MakeResults()
        self.page.dialog = self.modal
        self.modal.open = True
        self.page.update()
    
    def close(self):
        self.modal.open = False
        self.page.update()

class AtentionDialogs:
    def __init__(self, page):
        self.page = page
        self.modal = ft.AlertDialog(
            modal=True,
            title= ft.Text(),
            content= ft.Text(style=ft.TextStyle(size=18)),
            actions=[
                ModalButton("Continuar", lambda _: self.close())
            ],
            actions_alignment=ft.MainAxisAlignment.END
        )

    def SetContent(self, title, message):
        self.modal.title.value = title
        self.modal.content.value = message
        self.open()

    def open(self):
        self.page.dialog = self.modal
        self.modal.open = True
        self.page.update()
    
    def close(self):
        self.modal.open = False
        self.page.update()

class OutputBox:
    value = ""
    label = None
    results = []
    def __init__(self) -> None:
        self.label = ft.Text(value="", style=ft.TextStyle(size=20))
        self.text = MakeLabel(content=self.label, visible=False)
    
    def update(self):
        self.results.append(self.value)
        self.label.value = self.value
        self.text.visible = True
        self.label.update()
        self.text.update()

    def GetResults(self):
        return self.results