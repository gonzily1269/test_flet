# main
import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


# メイン処理
def main(page: ft.Page):
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

    for i in range(5):
        r = ft.Row(wrap=5, expand=False)
        page.add(r)
        for j in range(5):
            r.controls.append(
                ft.DragTarget(
                    group="number",
                    content=ft.Draggable(
                        group="number",
                        content=ft.Container(
                            width=50,
                            height=50,
                            bgcolor=ft.colors.CYAN_200,
                            border_radius=5,
                            content=ft.Text(f"{i}-{j}", size=20),
                            alignment=ft.alignment.center,
                        ),
                    ),
                    on_accept=drag_accept,
                ),
            )
            # TODO:座標に応じてテキストを変更するようにしたい。
            page.update()


ft.app(target=main)
