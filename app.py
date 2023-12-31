# main
import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

# TODO:スタートをゴールに
# TODO:ゴールを定位置に
# TODO:定位置をスタート


# メイン処理
def main(page: ft.Page):
    def drag_accept(e):
        # IDからドラッグ対象のsourceを持ってくる
        # スタートのID取得
        src = page.get_control(e.src_id)
        # 値の交換
        tmp_src_value = src.content.content.value
        src.content.content.value = e.control.content.content.content.value
        e.control.content.content.content.value = tmp_src_value
        # 色の交換
        tmp_src_color = src.content.bgcolor
        src.content.bgcolor = e.control.content.content.bgcolor
        e.control.content.content.bgcolor = tmp_src_color
        # アップデート
        page.update()

        """
        0=スタート
        スタート=ゴール
        ゴール=0

        スタート=ゴール
        ゴール=ゴール
        """

    for i in range(5):
        r = ft.Row(wrap=5, expand=False)
        page.add(r)
        for k in range(5):
            if i == 0:
                r.controls.append(
                    ft.Draggable(
                        group="number",
                        content=ft.Container(
                            width=50,
                            height=50,
                            bgcolor=ft.colors.PINK_200,
                            border_radius=5,
                            content=ft.Text(f"歩{k}", size=20),
                        ),
                    )
                )
            else:
                r.controls.append(
                    ft.Container(
                        width=50,
                        height=50,
                    )
                )

        for j in range(5):
            r.controls.append(
                ft.DragTarget(
                    group="number",
                    content=ft.Draggable(
                        group="number",
                        content=ft.Container(
                            key=f"{i}-{j}",
                            width=100,
                            height=100,
                            bgcolor=ft.colors.CYAN_200,
                            border_radius=5,
                            content=ft.Text(f"{i}-{j}", size=20),
                            alignment=ft.alignment.center,
                        ),
                    ),
                    on_accept=drag_accept,
                ),
            )
        for m in range(5):
            if i == 4:
                r.controls.append(
                    ft.Draggable(
                        group="number",
                        content=ft.Container(
                            width=50,
                            height=50,
                            bgcolor=ft.colors.GREEN_200,
                            border_radius=5,
                            content=ft.Text(f"歩{m}", size=20),
                        ),
                    )
                )
            else:
                r.controls.append(
                    ft.Container(
                        width=50,
                        height=50,
                    )
                )
        page.update()


ft.app(target=main)
