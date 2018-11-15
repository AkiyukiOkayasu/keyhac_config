import sys
import os
#import datetime

import pyauto
from keyhac import *


def configure(keymap):
    keymap_global = keymap.defineWindowKeymap()

    # L/R AltをL/R Ctrlにリマップ
    keymap.replaceKey("LAlt", "LCtrl")
    keymap.replaceKey("RAlt", "RCtrl")
    keymap.replaceKey("LWin", "LAlt")

    # CapsLockをEmacsキーバインド専用モディファイア"User0"に変更
    keymap.defineModifier("CapsLock", "User0")

    # Emacsキーバインド
    keymap_global[ "U0-P"] = "Up"
    keymap_global[ "U0-B"] = "Left"
    keymap_global[ "U0-N"] = "Down"
    keymap_global[ "U0-F"] = "Right"
    keymap_global[ "U0-A"] = "Home"# 行頭に移動
    keymap_global[ "U0-E"] = "End"# 行末に移動
    keymap_global[ "U0-K"] = "S-End","C-X"# 行末まで削除
    keymap_global[ "U0-D"] = "Delete"
    keymap_global[ "U0-H"] = "Back"

    # Alfred
    keymap_global[ "Ctrl-Space"] = "Win-S"

    # IME切り替え関数定義
    def ime_on():
	    keymap.wnd.setImeStatus( 1 )

    def ime_off():
	    keymap.wnd.setImeStatus( 0 )

    keymap_global[ "O-RCtrl" ] = ime_on# 英
    keymap_global[ "O-LCtrl" ] = ime_off# かな