import flet as ft

def main(page: ft.Page):
    page.title = "Matrices y conversiones"

    InputBox = ft.TextField(label="Input", col={"md": 4})
    OutputBox = ft.Text(value="", col={"md": 4})
    BoxesRow = ft.ResponsiveRow([InputBox, OutputBox])

    # Define button click event
    def button_click(e):
        # Update output based on which button was clicked
        if e.control.text == "PRIMARY":
            OutputBox.value = "Primary button clicked"
        elif e.control.text == "DANGER":
            OutputBox.value = "Danger button clicked"
        elif e.control.text == "SUCCESS":
            OutputBox.value = "Success button clicked"
        page.update()

    # Create buttons
    PrimaryButton = ft.ElevatedButton(text="PRIMARY", on_click=button_click, col={"md": 4})
    DangerButton = ft.ElevatedButton(text="DANGER", on_click=button_click, color=ft.colors.RED, col={"md": 4})
    SuccessButton = ft.ElevatedButton(text="SUCCESS", on_click=button_click, color=ft.colors.GREEN, col={"md": 4})
    ButtonsRow = ft.ResponsiveRow([PrimaryButton, DangerButton, SuccessButton])

    # Add controls to the page
    page.add(BoxesRow, ButtonsRow)

ft.app(main)