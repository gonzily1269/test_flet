import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: ft.Page):
    for i in range(5):
        r = ft.Row(wrap=5, expand=False)
        page.add(r)
        for j in range(5):
            r.controls.append(
                ft.Container(
                    content=ft.Text(f"Item {i}-{j}"),
                    width=100,
                    height=100,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER_100,
                    border=ft.border.all(1, ft.colors.AMBER_400),
                    border_radius=ft.border_radius.all(5),
                    ink=True,
                    on_click=lambda e: print(f"Item clicked!"),
                )
            )
            page.update()


ft.app(target=main)
