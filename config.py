import sys
import os
import pyauto
from keyhac import *

def configure(keymap):
    keymap_global = keymap.defineWindowKeymap()

    # L AltをR Ctrlにリマップ
    keymap.replaceKey("LAlt", "RCtrl")

    # L WinをL Altにリマップ
    keymap.replaceKey("LWin", "LAlt")

    # LCtrl（HHKBの左手小指側）を仮想キーコード235に割り当て
    keymap.replaceKey("LCtrl", 235)
    # 仮想キーコード235をモディファイア"User0"に変更（HHKBの左手小指側）
    keymap.defineModifier(235, "User0")

    # CapsLockをモディファイア"User0"に変更
    keymap.defineModifier("CapsLock", "User0")

    # R Altを仮想キーコード255に割り当て（かな変換専用）
    keymap.replaceKey("RAlt", 255)

    # カーソル
    keymap_global[ "U0-U"] = "Up"
    keymap_global[ "U0-H"] = "Left"
    keymap_global[ "U0-N"] = "Down"
    keymap_global[ "U0-J"] = "Right"
    keymap_global[ "U0-A"] = "Home"# 行頭に移動
    keymap_global[ "U0-E"] = "End"# 行末に移動
    keymap_global[ "U0-K"] = "S-End","C-X"# 行末まで削除
    keymap_global[ "U0-D"] = "Delete"
    keymap_global[ "U0-B"] = "Back"

    # ラウンチャ
    keymap_global[ "Ctrl-Space"] = "Win-S"

    # ウインドウ整列
    keymap_global["Ctrl-Shift-H"] = "Win-Left"
    keymap_global["Ctrl-Shift-J"] = "Win-Right"
    keymap_global["Ctrl-Shift-U"] = "Win-Up"
    keymap_global["Ctrl-Shift-N"] = "Win-Down"

    # IME切り替え関数定義
    def ime_on():
	    keymap.wnd.setImeStatus( 1 )

    def ime_off():
	    keymap.wnd.setImeStatus( 0 )

    keymap_global[ "O-RCtrl" ] = ime_off # 英
    keymap_global[ "O-(255)" ] = ime_on # かな
