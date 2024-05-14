import flet as ft
from ConvertirUi import ConvertirUi
from GaussUi import GaussUi
from ui import OutputBox

def main(page: ft.Page):
    page.title = "Matrices y conversiones"
    page.theme = ft.Theme(font_family="Nunito")

    output = OutputBox()
    convertir = ConvertirUi(output).GetUi()   
    gauss = GaussUi(output).GetUi()

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
                icon=ft.icons.NUMBERS_ROUNDED,
                label="Convertir"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.VIEW_LIST_ROUNDED,
                label="Gauss",
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