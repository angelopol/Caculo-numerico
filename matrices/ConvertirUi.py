import flet as ft
from ui import SuccessButton
from convertions import AllToAll

class ConvertirUi:
    NumInput = ft.TextField(label="Nùmero")
    ToBaseDrop = ft.Dropdown(
        label="Base objetivo",
        options=[
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("10"),
            ft.dropdown.Option("16"),
        ]
    )
    BaseDrop = ft.Dropdown(
        label="Base del nùmero",
        options=[
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("10"),
            ft.dropdown.Option("16"),
        ]
    )

    def __init__(self, output):
        self.output = output
        self.ConvertirButton = SuccessButton(lambda e: self.ShowResult(), "Convertir")

    def GetUi(self):   
        return self.NumInput, self.BaseDrop, self.ToBaseDrop, self.ConvertirButton, self.output
    
    def ShowResult(self):
        result = AllToAll(self.NumInput.value, self.BaseDrop.value, self.ToBaseDrop.value)
        self.output.value = str(result)
        self.output.update()