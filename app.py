# sandbox
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
            page.update()
    # TODO:ここに空白を入れたい。
    for k in range(1):
        r = ft.Row(wrap=5, expand=False)
        page.add(r)
        for t in range(5):
            if k == 0 and t == 4:
                r.controls.append(
                    ft.DragTarget(
                        group="number",
                        content=ft.Draggable(
                            group="number",
                            content=ft.Container(
                                width=50,
                                height=50,
                                bgcolor=ft.colors.PINK_200,
                                border_radius=5,
                                content=ft.Text("歩", size=20),
                                alignment=ft.alignment.center,
                            ),
                        ),
                        on_accept=drag_accept,
                    ),
                )
            else:
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
                                content=ft.Text(f"{k}-{t}", size=20),
                                alignment=ft.alignment.center,
                            ),
                        ),
                        on_accept=drag_accept,
                    ),
                )
            page.update()


ft.app(target=main)
