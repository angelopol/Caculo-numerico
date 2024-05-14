import flet as ft

def GetContentColumn(convertir):
    return ft.Column(convertir, alignment=ft.MainAxisAlignment.START, expand=True)
    
def ChangeContent(e, ContentColumn, convertir, gauss):
    if e.control.selected_index == 0:
        ContentColumn.controls = convertir
    else:
        ContentColumn.controls = gauss
    ContentColumn.update()

def MakeDestination(icon, label):
    return ft.NavigationRailDestination(
        icon_content=ft.Icon(icon, scale=1.5),
        label_content=ft.Text(label, style=ft.TextStyle(size=20))
    )

def GetRail(ContentColumn, convertir, gauss):
    return ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        destinations=[
            MakeDestination(ft.icons.NUMBERS_ROUNDED, "Convertir"),
            MakeDestination(ft.icons.VIEW_LIST_ROUNDED, "Gauss Jordan")
        ],
        on_change=(
            lambda e, ContentColumn = ContentColumn, convertir=convertir, gauss=gauss:
            ChangeContent(e, ContentColumn, convertir, gauss)
        )
    )

def GetRailRow(convertir, gauss):
    column = GetContentColumn(convertir)
    return ft.Row(
        [
            GetRail(column, convertir, gauss),
            ft.VerticalDivider(width=1),
            column
        ],
        expand=True,
    )