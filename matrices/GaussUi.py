import flet as ft
from ui import SuccessButton
from gauss import GaussJordan

class MatrizInputs():
    def __init__(self, num):
        self.GenInputs(num)
        self.InputsColumn = ft.Column(
            self.GetRows(), alignment=ft.MainAxisAlignment.START, expand=True, scroll=ft.ScrollMode.ALWAYS,
        )

    def GenInputs(self, num):
        self.rows = []
        for n in range(0, num):
            elements = []
            for n in range(0, num):
                element = ft.TextField(
                    input_filter=ft.InputFilter('^[0-9]*$'),
                    border=ft.InputBorder.NONE,
                    filled=True,
                    col={"md": 1, 'sm': 1, 'lg': 1}
                )
                elements.append(element)
            self.rows.append(ft.ResponsiveRow(elements, alignment=ft.MainAxisAlignment.SPACE_EVENLY))

    def GetRows(self):
        return self.rows
    
    def GetInputs(self):
        return self.InputsColumn
    
    def ChangeInputs(matriz, num):
        matriz.GenInputs(int(num))
        matriz.InputsColumn.controls = matriz.GetRows()
        matriz.InputsColumn.update()

class VectorInput():
    def __init__(self, num):
        self.GenInputs(num)
        self.InputsColumn = ft.Column(
            [self.GetRow()], alignment=ft.MainAxisAlignment.START, expand=True, scroll=ft.ScrollMode.ALWAYS,
        )

    def GenInputs(self, num):
        elements = []
        for n in range(0, num):
            element = ft.TextField(
                input_filter=ft.InputFilter('^[0-9]*$'),
                border=ft.InputBorder.NONE,
                filled=True,
                col={"md": 1, 'sm': 1, 'lg': 1}
            )
            elements.append(element)
        self.row = ft.ResponsiveRow(elements, alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    def GetRow(self):
        return self.row
    
    def GetInputs(self):
        return self.InputsColumn
    
    def ChangeInputs(vector, num):
        vector.GenInputs(int(num))
        vector.InputsColumn.controls = [vector.GetRow()]
        vector.InputsColumn.update()

class GaussUi:
    matriz = MatrizInputs(3)
    vector = VectorInput(3)
    DimensionInput = ft.Slider(
        value=3, min=2, max=10, divisions=8, label="{value}",
        on_change = lambda e, matriz=matriz, vector=vector: ChangeInputs(matriz, vector, e.control.value)
    )

    def __init__(self, output):
        self.output = output
        self.ObtenerButton = SuccessButton(lambda e: self.ShowResult(), "Obtener")
    
    def GetUi(self):   
        return (
            ft.Text("Dimensiòn de la matriz:"), self.DimensionInput,
            ft.Text("Matriz:"), self.matriz.GetInputs(),
            ft.Text("Vector de tèrminos independientes:"), self.vector.GetInputs(),
            self.ObtenerButton,
            self.output)
    
    def ShowResult(self):
        matriz = []
        for row in self.matriz.GetRows():
            elements = []
            for element in row.controls:
                elements.append(float(element.value))
            matriz.append(elements)
        vector = []
        for element in self.vector.GetRow().controls:
            vector.append(float(element.value))
        result = GaussJordan(matriz, vector)
        self.output.value = str(result)
        self.output.update()

def ChangeInputs(matriz, vector, value):
    MatrizInputs.ChangeInputs(matriz, value)
    VectorInput.ChangeInputs(vector, value)