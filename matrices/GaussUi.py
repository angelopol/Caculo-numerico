import flet as ft
from ui import BottomButtons, MakeLabel
from gauss import GaussJordan

def MakeElements(num):
    elements = []
    if num == 2:
        col = {"md": 6, 'sm': 6, 'lg': 6}
    elif num == 3:
        col = {"md": 4, 'sm': 4, 'lg': 4}
    elif num == 4:
        col = {"md": 3, 'sm': 3, 'lg': 3}
    elif num == 6  or num == 5:
        col = {"md": 2, 'sm': 2, 'lg': 2}
    else:
        col = {"md": 1, 'sm': 1, 'lg': 1}
    for n in range(0, num):
        element = ft.TextField(
            input_filter=ft.InputFilter('^-?[0-9]*$'),
            filled=True,
            col=col,
            border_radius=40,
            border_width=0
        )
        elements.append(element)
    return elements

class MatrizInputs():
    def __init__(self, num):
        self.GenInputs(num)
        self.InputsColumn = ft.Column(
            self.GetRows(), alignment=ft.MainAxisAlignment.START, expand=True, scroll=ft.ScrollMode.ALWAYS,
        )

    def GenInputs(self, num):
        self.rows = []
        for n in range(0, num):
            self.rows.append(ft.ResponsiveRow(MakeElements(num), alignment=ft.MainAxisAlignment.SPACE_EVENLY))

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
        self.row = ft.ResponsiveRow(MakeElements(num), alignment=ft.MainAxisAlignment.SPACE_EVENLY)

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
    DimensionInput = ft.Container(
        content=ft.Slider(
            value=3, min=2, max=10, divisions=8, label="{value}", inactive_color=ft.colors.WHITE10,
            on_change = lambda e, matriz=matriz, vector=vector: ChangeInputs(matriz, vector, e.control.value)
        ),
        padding=10,
        alignment=ft.alignment.center,
        bgcolor="#43474e",
        border_radius=40
    )

    def __init__(self, output, dialog, historial):
        self.dialog = dialog
        self.output = output
        self.ObtenerButton = BottomButtons(lambda e: self.ShowResult(), "Obtener", historial)
    
    def GetUi(self):   
        return (
            MakeLabel(label="Dimensiòn:", bg = False, alignment=ft.alignment.top_left), self.DimensionInput,
            MakeLabel(label="Matriz:", bg = False, alignment=ft.alignment.top_left), self.matriz.GetInputs(),
            MakeLabel(label="Vector de tèrminos independientes:", bg = False,alignment=ft.alignment.top_left), self.vector.GetInputs(),
            self.output.text,
            self.ObtenerButton)
    
    def ShowResult(self):
        matriz = []
        for row in self.matriz.GetRows():
            elements = []
            for element in row.controls:
                if element.value == "":
                    self.dialog.SetContent('Error al resolver con el mètodo de Gauss Jordan.', "Existe un campo de la matriz vacìo.")
                    return
                if not element.value.isnumeric():
                    self.dialog.SetContent('Error al resolver con el mètodo de Gauss Jordan.', element.value + " no es un nùmero vàlido para la matriz.")
                    return
                elements.append(float(element.value))
            matriz.append(elements)
        vector = []
        for element in self.vector.GetRow().controls:
            if element.value == "":
                self.dialog.SetContent('Error al resolver con el mètodo de Gauss Jordan.', "Existe un campo del vector vacìo.")
                return
            if not element.value.isnumeric():
                self.dialog.SetContent('Error al resolver con el mètodo de Gauss Jordan.', element.value + " no es un nùmero vàlido para el vector.")
                return
            vector.append(float(element.value))
        try:
            result = GaussJordan(matriz, vector)
        except Exception as e:
            self.dialog.SetContent('Error al resolver con el mètodo de Gauss Jordan.', str(e))
            return
        self.output.value = str(result)
        self.output.update()

def ChangeInputs(matriz, vector, value):
    MatrizInputs.ChangeInputs(matriz, value)
    VectorInput.ChangeInputs(vector, value)