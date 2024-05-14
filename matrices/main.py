import flet as ft
from ConvertirUi import ConvertirUi
from GaussUi import GaussUi
from ui import OutputBox, AtentionDialogs, HistorialModal

def main(page: ft.Page):
    page.title = "Calculadora"
    page.theme = ft.Theme(font_family="Nunito")

    output = OutputBox()
    historial = HistorialModal(page, output)
    dialog = AtentionDialogs(page)
    convertir = ConvertirUi(output, dialog, historial).GetUi()   
    gauss = GaussUi(output, dialog, historial).GetUi()

    ContentColumn = ft.Column(
        convertir, alignment=ft.MainAxisAlignment.START, expand=True
    )
    
    def ChangeContent(e):
        if e.control.selected_index == 0:
            ContentColumn.controls = convertir
        else:
            ContentColumn.controls = gauss
        ContentColumn.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        destinations=[
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.NUMBERS_ROUNDED, scale=1.5),
                label_content=ft.Text("Convertir", style=ft.TextStyle(size=20))
            ),
            ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.VIEW_LIST_ROUNDED, scale=1.5),
                label_content=ft.Text("Gauss Jordan", style=ft.TextStyle(size=20))
            )
        ],
        on_change=lambda e: ChangeContent(e),
    )

    RailRow = ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            ContentColumn
        ],
        expand=True,
    )
    page.add(RailRow)

ft.app(main)