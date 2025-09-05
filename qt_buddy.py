#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dark Souls Buddy - Versão Final
- Usa o método "baralho de cartas" para dicas aleatórias sem repetição.
"""

import sys
import os
import random
import threading
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from pynput import keyboard

try:
    from config import TIPS, TIP_DURATION, AUTO_INTERVAL
except Exception:
    TIPS = ["Este é o Dark Souls Buddy!"]
    TIP_DURATION = 15
    AUTO_INTERVAL = 300

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_KNIGHT = os.path.join(SCRIPT_DIR, 'KnightBuddy.gif')
ASSET_BALLOON = os.path.join(SCRIPT_DIR, 'balaoFala.png')
ASSET_TRAY_ICON = ASSET_BALLOON

class BuddyWindow(QtWidgets.QWidget):
    toggle_signal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__(None, QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)
        self.setWindowOpacity(0.9)
        self.setStyleSheet("background-color: rgba(30, 30, 50, 230); border-radius: 15px;")
        
        self.container = QtWidgets.QVBoxLayout(self)
        self.container.setContentsMargins(10, 10, 10, 10)
        self.container.setSpacing(0)

        self.text_label = QtWidgets.QLabel()
        self.text_label.setWordWrap(True)
        self.text_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.text_label.setStyleSheet("background: white; color: black; font-weight: bold; font-size: 11px; border-radius: 10px; padding: 10px;")
        self.text_label.setMinimumHeight(80)

        self.knight_label = QtWidgets.QLabel()
        self.movie = QtGui.QMovie(ASSET_KNIGHT)
        self.movie.setScaledSize(QtCore.QSize(100, 100))
        self.knight_label.setMovie(self.movie)
        self.knight_label.setAlignment(QtCore.Qt.AlignHCenter)

        self.container.addWidget(self.text_label)
        self.container.addWidget(self.knight_label)

        # ### MUDANÇA: Lógica do "Baralho de Cartas" ###
        self.shuffled_tips = [] # Começa com o baralho vazio

        # Timers e estado
        self.display_timer = QtCore.QTimer(self)
        self.display_timer.setSingleShot(True)
        self.display_timer.timeout.connect(self.hide_buddy)
        self.auto_timer = QtCore.QTimer(self)
        self.auto_timer.timeout.connect(self.show_shuffled_tip) # MUDANÇA
        self.auto_timer.start(AUTO_INTERVAL * 1000)
        
        self.daily_meeting_timer = QtCore.QTimer(self)
        self.daily_meeting_timer.timeout.connect(self.check_meeting_time)
        self.daily_meeting_timer.start(60000)
        self.meeting_tip_shown_today = False
        
        self.is_showing = False
        self.toggle_signal.connect(self.toggle_visibility)
        self.hide()

    def bottom_left_geometry(self):
        self.adjustSize()
        screen_geo = QtWidgets.QApplication.primaryScreen().availableGeometry()
        x = screen_geo.x() + 20
        y = screen_geo.y() + screen_geo.height() - self.height() - 20
        return QtCore.QRect(x, y, self.width(), self.height())
        
    def check_meeting_time(self):
        now = datetime.datetime.now().time()
        start_time = datetime.time(8, 0)
        end_time = datetime.time(8, 15)

        if now < datetime.time(0, 1):
            self.meeting_tip_shown_today = False

        if start_time <= now <= end_time and not self.meeting_tip_shown_today:
            self.show_tip("Lembre-se de entrar na reunião do Discord!")
            self.meeting_tip_shown_today = True

    def show_tip(self, text):
        if self.is_showing:
             return
        print(f"DEBUG: Mostrando dica '{text[:30]}...'")
        self.text_label.setText(text)
        self.movie.start()
        self.setGeometry(self.bottom_left_geometry())
        self.show()
        self.is_showing = True
        self.display_timer.start(TIP_DURATION * 1000)

    # ### MUDANÇA: Função principal de dicas ###
    def show_shuffled_tip(self):
        # Se o baralho estiver vazio, reembaralha
        if not self.shuffled_tips:
            print("DEBUG: Baralho de dicas vazio. Reembaralhando...")
            self.shuffled_tips = list(TIPS) # Pega uma cópia fresca da lista
            random.shuffle(self.shuffled_tips)
        
        # Pega a próxima dica do topo do baralho e a remove da lista
        tip_to_show = self.shuffled_tips.pop()
        self.show_tip(tip_to_show)

    def hide_buddy(self):
        self.hide()
        self.is_showing = False

    @QtCore.pyqtSlot()
    def toggle_visibility(self):
        if self.is_showing:
            self.hide_buddy()
        else:
            self.show_shuffled_tip() # MUDANÇA

class Application(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setQuitOnLastWindowClosed(False)
        self.buddy = BuddyWindow()

        self.tray_icon = QtWidgets.QSystemTrayIcon(QtGui.QIcon(ASSET_TRAY_ICON), self)
        tray_menu = QtWidgets.QMenu()
        show_action = tray_menu.addAction("Mostrar Dica")
        show_action.triggered.connect(self.buddy.show_shuffled_tip) # MUDANÇA
        quit_action = tray_menu.addAction("Sair")
        quit_action.triggered.connect(self.quit)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
        self.start_hotkey_listener()
        
        QtCore.QTimer.singleShot(1000, lambda: self.buddy.show_tip("Ei, não se atreva a se tornar um Hollow!"))

    def start_hotkey_listener(self):
        def on_activate():
            self.buddy.toggle_signal.emit()

        def for_canonical(f):
            return lambda k: f(listener.canonical(k))

        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<ctrl>+<alt>+<shift>+s'),
            on_activate)

        listener = keyboard.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release))
        
        listener.start()

if __name__ == '__main__':
    if not os.path.exists(ASSET_KNIGHT) or not os.path.exists(ASSET_BALLOON):
        print('Erro: Arquivos de imagem não encontrados!')
        sys.exit(1)

    app = Application(sys.argv)
    print('✅ Dark Souls Buddy (Versão Final) iniciado.')
    print('🖱️  Clique com o botão direito no ícone na bandeja do sistema para ver as opções.')
    print('⌨️  Atalho Ctrl+Alt+Shift+S (pynput) está ativo.')
    sys.exit(app.exec_())