class Controlador():
    def __init__(self, volume, power_on, playing, muted):
        self.on = False
        self.volume = 10
        self.playing = False
        self.muted = False

    def toggle_on(self):
        self.on = not self.on

    def add_volume(self):
        if self.on:
            self.muted = False
            self.volume += 1
        else:
            print(' Desligado')
    
    def rm_volume(self):
        if self.on and self.volume > 0:
            self.volume -= 1
        else:
            print(' Desligado')
        if self.volume == 0:
            self.muted = True            

    def toggle_mute(self):
            self.toggle_mute = not self.toggle_mute

    def toggle_play(self):
            self.playing = not self.playing

    def print_status(self):
        print('--------------------------------------------------------------------')
        print('Ligado: ', self.on)
        print('Volume: ', self.volume)
        print('Tocando: ', self.playing)
        print('Mutado: ',self.muted)
        print('')

    def print_command(self):
        print('Comandos:')
        print('1 - Ligar/Desligar')
        print('2 - Volume +')
        print('3 - Volume -')
        print('4 - Mudo')
        print('5 - Desmutar')
        print('6 - Play')
        print('')
        print('0 - Fechar')
        print('')

    def get_option(self):
        return int(input('Digite Comando: '))