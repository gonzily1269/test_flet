# sandbox

import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

# TODO:on_hoverで、次行ける場所を表示したい

# TODO:駒があるとき交換しない　ー自分のコマ　ー交換なし
# TODO:　　　　　　　　　　　　ー相手のコマ　ーとる処理


"""
0=スタート
スタート=ゴール
ゴール=0
"""


# メイン処理
def main(page: ft.Page):
    # カーソルがあった駒の色をつける
    def on_hover(e):
        if e.data == "true" and (
            e.control.key == "player-green" or e.control.key == "player-pink"
        ):
            e.control.bgcolor = "blue"
        else:
            if e.control.key == "player-green":
                e.control.bgcolor = "green200"
            elif e.control.key == "player-pink":
                e.control.bgcolor = "pink200"
            else:
                e.control.bgcolor = "cyan200"

        e.control.update()

    def drag_accept(e):
        # IDからドラッグのsourceを持ってくる
        # ドラックのID取得
        src = page.get_control(e.src_id)

        if src.content.key in ("player-green", "player-pink"):
            # 値の交換
            tmp_src_value = src.content.content.value
            src.content.content.value = e.control.content.content.content.value
            e.control.content.content.content.value = tmp_src_value

            # 色の交換
            tmp_src_color = src.content.bgcolor
            src.content.bgcolor = e.control.content.content.bgcolor
            e.control.content.content.bgcolor = tmp_src_color

            # 座標を駒に持たせる
            src.content.content.key = e.control.content.content.content.key

            # 盤にplayer情報を持たせる
            tmp_src_player_info = src.content.key
            src.content.key = e.control.content.content.key
            e.control.content.content.key = tmp_src_player_info

            print(f"src.content.key:{src.content.key}")
            print(f"src.content.content.key:{src.content.content.key}")
            print(f"e.control.content.content.key:{e.control.content.content.key}")
            print(
                f"e.control.content.content.content.key:{e.control.content.content.content.key}"
            )
            print(
                f"e.control.content.content.content.value:{e.control.content.content.content.value}"
            )
        else:
            pass

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
                            key=f"player-pink",
                            width=50,
                            height=50,
                            bgcolor=ft.colors.PINK_200,
                            border_radius=5,
                            content=ft.Text(f"歩{k}", key="", size=20),
                            on_hover=on_hover,
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

        # 盤
        for j in range(5):
            r.controls.append(
                ft.DragTarget(
                    group="number",
                    content=ft.Draggable(
                        group="number",
                        content=ft.Container(
                            key="",
                            width=100,
                            height=100,
                            bgcolor=ft.colors.CYAN_200,
                            border_radius=5,
                            content=ft.Text("", key=f"{i}-{j}", size=20),
                            alignment=ft.alignment.center,
                            on_hover=on_hover,
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
                            key=f"player-green",
                            width=50,
                            height=50,
                            bgcolor=ft.colors.GREEN_200,
                            border_radius=5,
                            content=ft.Text(f"歩{m}", key="", size=20),
                            on_hover=on_hover,
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
