import time
import sys
import os
import pyauto
import re
import fnmatch

import keyhac_keymap
from keyhac import *

def configure(keymap):
    # IME切り替え関数
    def ime_on():
	    keymap.wnd.setImeStatus(True)
    def ime_off():
	    keymap.wnd.setImeStatus(False)

    keymap.defineModifier("CapsLock", "User0") # Emacs C
    keymap.replaceKey("LWin", 235) # Emacs M    
    keymap.defineModifier(235, "User1")
    keymap.replaceKey("LCtrl", "LAlt")
    keymap.replaceKey("LAlt", "LCtrl")
    keymap.replaceKey("RAlt", "RCtrl")    
    keymap.replaceKey("PrintScreen", "RWin")

    keymap_global = keymap.defineWindowKeymap()

    # ウインドウ整列
    keymap_global["U0-Left"] = "Win-Left"
    keymap_global["U0-Right"] = "Win-Right"
    keymap_global["u0-Up"] = "Win-Up"
    keymap_global["U0-Down"] = "Win-Down"

    # スクショ
    keymap_global["Ctrl-Shift-3"] = "Alt-PrintScreen"
    keymap_global["Ctrl-Shift-4"] = "Win-Shift-S"

    # 英かな
    keymap_global["O-LCtrl"] = ime_off
    keymap_global["O-RCtrl"] = ime_on

    # カーソル移動
    keymap_global["U0-P"] = "Up"
    keymap_global["U0-B"] = "Left"
    keymap_global["U0-N"] = "Down"
    keymap_global["U0-F"] = "Right"
    keymap_global["U0-A"] = "Home"# 行頭に移動
    keymap_global["U0-E"] = "End"# 行末に移動
    keymap_global["U0-K"] = "S-End","C-X"# 行末まで削除
    keymap_global["U0-D"] = "Delete"
    keymap_global["U0-H"] = "Back"#Backspace

    # カーソル移動（単語）    
    keymap_global["U1-B"] = "C-Left"    
    keymap_global["U1-F"] = "C-Right"
    keymap_global["U1-D"] = "C-Delete"
    keymap_global["U1-H"] = "C-Back"    
    
    # ランチャ
    keymap_global["C-Space"] = "Win-S"
