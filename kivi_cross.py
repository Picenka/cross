from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from random import randint
from coordinate import coordinate

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1000")
Config.set("graphics", "height", "1000")


class MainApp(App):
    # print(coordinate)
    def __init__(self):
        super().__init__()
        self.switch = True

    def winner (win, str_win):
        popup = ModalView(size_hint=(0.75, 0.5))
        victory_label = Label(text=str_win, font_size=50)
        popup.add_widget(victory_label)
        if win:
            sound = SoundLoader.load('win.wav')
        else:
            sound = SoundLoader.load('LOST.mp3')
        popup.open(sound.play())

    def tic_tac_toe(self, arg):
        sound = SoundLoader.load('beep-08b.wav')
        sound.play()
        end_game = False
        # ход игрока
        arg.disabled = True
        arg.text = 'X'
        # ход компа
        while True:
            rand_choice = randint(0, 99)
            if self.buttons[rand_choice].disabled == False:
                self.buttons[rand_choice].text = 'O'
                self.buttons[rand_choice].disabled = True
                break
        # формируем список отробтанных ячеек
        vector = lambda item: [self.buttons[x].text for x in item]
        # проверка на концовку игры
        for item in coordinate:
            # print(vector(item))
            losing_combination_X = ('X', 'X', 'X', 'X', 'X')
            losing_combination_O = ('O', 'O', 'O', 'O', 'O')
            if str(losing_combination_X).strip('()') in str(vector(item)).strip('[]'):
                str_win='Вы проиграли'
                end_game=True
                MainApp.winner(end_game,str_win)
            elif (str(losing_combination_O).strip('()') in str(vector(item)).strip('[]')):
                str_win = 'Вы выиграли'
                end_game = False
                MainApp.winner(end_game, str_win)
                end_game = True

            if end_game:
                # выключсение оставшихся кнопок
                for button in self.buttons:
                    button.disabled = True
                break
    # начать игру заново
    def restart(self, arg):
        self.switch = True
        for button in self.buttons:
            button.text = ""
            button.disabled = False
    # создание игрового поля
    def build(self):
        self.title = "Крестики-нолики"
        root = BoxLayout(orientation="vertical", padding=5)
        grid = GridLayout(cols=10)
        self.buttons = []
        for _ in range(100):
            button = Button(
                background_color= [2, 11, 11, 1],
                color=[252, 141, 141, 1],
                font_size=24,
                disabled=False,
                # on_release=self.tic_tac_toe
                # вызов события начало игры
                on_press = self.tic_tac_toe
            )
            self.buttons.append(button)
            grid.add_widget(button)
        root.add_widget(grid)
        # перезапуск игры
        root.add_widget(
            Button(
                text="RESTART",
                size_hint=[1, .1],
                background_color="red",
                font_size=32,
                on_press=self.restart
            )
        )
        return root



if __name__ == "__main__":
    MainApp().run()
