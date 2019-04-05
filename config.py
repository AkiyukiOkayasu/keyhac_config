import sys
import os
import pyauto
from keyhac import *

def configure(keymap):
    keymap_global = keymap.defineWindowKeymap()

    keymap.replaceKey("LAlt", "LCtrl") #L AltをL Ctrlにリマップ
    keymap.replaceKey("LWin", "LAlt") #L WinをL Altにリマップ

    keymap.replaceKey("LCtrl", 235)#LCtrl（HHKBの左手小指側）を仮想キーコード235に割り当て
    keymap.defineModifier(235, "User0")#仮想キーコード235をモディファイア"User0"に変更（HHKBの左手小指側）
    keymap.defineModifier("CapsLock", "User0") #CapsLockをモディファイア"User0"に変更
	
    keymap.replaceKey("RAlt", "RCtrl")# R AltをR Ctrlにリマップ

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

    # ウインドウ整列
    keymap_global["U0-Left"] = "Win-Left"
    keymap_global["U0-Right"] = "Win-Right"
    keymap_global["U0-Up"] = "Win-Up"
    keymap_global["U0-Down"] = "Win-Down"

    # IME切り替え関数
    def ime_on():
	    keymap.wnd.setImeStatus( 1 )

    def ime_off():
	    keymap.wnd.setImeStatus( 0 )

    keymap_global[ "O-LCtrl" ] = ime_off # 英
    keymap_global[ "O-RCtrl" ] = ime_on # かな
