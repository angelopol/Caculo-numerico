import flet as ft
from ui import BottomButtons, MakeLabel
from convertions import AllToAll

def VerifyNumero(num, base):
    for n in num:
        if n.isnumeric():
            if int(base) == 16:
                if int(n) >= 10:
                    return False
            else:
                if int(n) >= int(base):
                    return False
        else:
            if int(base) == 16:
                if n not in ('a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'):
                    return False
            else:
                return False
    return True

def MakeBaseDropdown(label):
    return ft.Dropdown(
        label=label,
        label_style=ft.TextStyle(size=20),
        options=[
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("10"),
            ft.dropdown.Option("16"),
        ],
        filled=True,
        border_radius=40,
        border_width=0
    )

class ConvertirUi:
    note = MakeLabel(label="Conversiòn unicamente para nùmeros enteros.")
    NumInput = ft.TextField(
        label="Nùmero",
        label_style=ft.TextStyle(size=20),
        input_filter=ft.InputFilter('^[0-9-a-f-A-F]*$'),
        filled=True,
        border_radius=40,
        border_width=0
    )
    ToBaseDrop = MakeBaseDropdown("Base objetivo")
    BaseDrop = MakeBaseDropdown("Base del nùmero")
    column = ft.Column([note, NumInput, BaseDrop, ToBaseDrop],
        alignment=ft.MainAxisAlignment.START, expand=True)

    def __init__(self, output, dialog, historial):
        self.dialog = dialog
        self.output = output
        self.ConvertirButton = BottomButtons(lambda _: self.ShowResult(), "Convertir", historial)

    def GetUi(self):   
        return self.column, self.output.text, self.ConvertirButton
    
    def ShowResult(self):
        if self.NumInput.value == "":
            self.dialog.SetContent('Error al convertir el nùmero.', "Por favor rellene el campo del nùmero.")
            return
        if self.BaseDrop.value == None:
            self.dialog.SetContent('Error al convertir el nùmero.', "Por favor seleccione la base del nùmero.")
            return
        if self.ToBaseDrop.value == None:
            self.dialog.SetContent('Error al convertir el nùmero.', "Por favor seleccione la base objetivo.")
            return
        if not VerifyNumero(self.NumInput.value, self.BaseDrop.value):
            self.dialog.SetContent(
                'Error al convertir el nùmero.', self.NumInput.value + " no pertenece a la base " + self.BaseDrop.value + "."
            )
            return
        result = AllToAll(self.NumInput.value, self.BaseDrop.value, self.ToBaseDrop.value)
        self.output.value = str(result)
        self.output.update()