import flet as ft


def main(page: ft.Page):
    page.title = "Drag and Drop example"

    def drag_accept(e):
        # IDからドラッグ対象のsourceを持ってくる
        src = page.get_control(e.src_id)

        # ドラッグ側の値と色を取得→ターゲットの値と色と交換
        tmp_src_value = src.content.content.value
        src.content.content.value = e.control.content.content.content.value
        tmp_src_color = src.content.bgcolor
        src.content.bgcolor = e.control.content.content.bgcolor
        e.control.content.content.content.value = tmp_src_value
        e.control.content.content.bgcolor = tmp_src_color
        page.update()

    page.add(
        ft.Row(
            [
                ft.DragTarget(
                    group="number",
                    content=ft.Draggable(
                        group="number",
                        content=ft.Container(
                            width=50,
                            height=50,
                            bgcolor=ft.colors.CYAN_200,
                            border_radius=5,
                            content=ft.Text("1", size=20),
                            alignment=ft.alignment.center,
                        ),
                    ),
                    on_accept=drag_accept,
                ),
                ft.DragTarget(
                    group="number",
                    content=ft.Draggable(
                        group="number",
                        content=ft.Container(
                            width=50,
                            height=50,
                            bgcolor=ft.colors.PINK_200,
                            border_radius=5,
                            content=ft.Text("0", size=20),
                            alignment=ft.alignment.center,
                        ),
                    ),
                    on_accept=drag_accept,
                ),
            ]
        )
    )


ft.app(target=main)
