import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


# ①盤・コマ詳細設定
class BoardPieceConfig:
    def __init__(self):
        # 盤の詳細
        self.board_config = {
            "key": "",
            "width": 100,
            "height": 100,
            "bgcolor": ft.colors.CYAN_200,
            "border_radius": 5,
            "on_hover": on_hover,
        }

        # ピンクコマの詳細
        self.pink_piece_config = {
            "key": "player-pink",
            "width": 50,
            "height": 50,
            "bgcolor": ft.colors.PINK_200,
            "border_radius": 5,
            "on_hover": on_hover,
        }

        # 緑のコマの詳細
        self.green_piece_config = {
            "key": "player-green",
            "width": 50,
            "height": 50,
            "bgcolor": ft.colors.GREEN_200,
            "border_radius": 5,
            "on_hover": on_hover,
        }


# ②メイン処理
def main(page: ft.Page):
    config = BoardPieceConfig()
    create_board_and_pieces(page, config)

    def on_hover(e):
        on_hover(e)

    # TODO:④と⑤の動きをどうやって実装する？？


# ③盤・コマの生成
def create_board_and_pieces(page: ft.Page, config: BoardPieceConfig):
    for i in range(5):
        r = ft.Row(wrap=5, expand=False)
        page.add(r)

        # ピンクの駒
        for k in range(5):
            if i == 0:
                r.controls.append(
                    ft.Draggable(
                        group="number",
                        content=ft.Container(
                            **config.pink_piece_config,
                            content=ft.Text(f"歩{k}", key="", size=20),
                        ),
                    )
                )
            else:
                r.controls.append(
                    ft.Container(
                        width=config.pink_piece_config["width"],
                        height=config.pink_piece_config["height"],
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
                            **config.board_config,
                            content=ft.Text("", key=f"{i}-{j}", size=20),
                            alignment=ft.alignment.center,
                        ),
                    ),
                    on_accept=drag_accept,
                ),
            )

        # 緑の駒
        for m in range(5):
            if i == 4:
                r.controls.append(
                    ft.Draggable(
                        group="number",
                        content=ft.Container(
                            **config.green_piece_config,
                            content=ft.Text(f"歩{m}", key="", size=20),
                        ),
                    )
                )
            else:
                r.controls.append(
                    ft.Container(
                        width=config.green_piece_config["width"],
                        height=config.green_piece_config["height"],
                    )
                )
        page.update()


# ④交換の動き
def drag_accept(e):
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


# ⑤カーソルがあった駒の色をつける
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


# 実行？
if __name__ == "__main__":
    page = ft.Page
    ft.app(target=main)
