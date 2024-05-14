import flet as ft
from ConvertirUi import ConvertirUi
from GaussUi import GaussUi
from ui import OutputBox, AtentionDialogs, HistorialModal
from rail import GetRailRow

def main(page: ft.Page):
    page.title = "Calculadora"
    page.theme = ft.Theme(font_family="Nunito")

    output = OutputBox()
    historial = HistorialModal(page, output)
    dialog = AtentionDialogs(page)
    convertir = ConvertirUi(output, dialog, historial).GetUi()   
    gauss = GaussUi(output, dialog, historial).GetUi()

    page.add(GetRailRow(convertir, gauss))

ft.app(main)