from Controle import Controlador

controle1 = Controlador(False, 10, False, False)

opt = 99
while opt != 0:
    controle1.print_status()
    controle1.print_command()
    opt = controle1.get_option()

    if opt == 1:
        controle1.toggle_on()

    elif opt == 2:
        controle1.add_volume()

    elif opt == 3:
        controle1.rm_volume()

    elif opt == 4:
        controle1.toggle_mute()

    elif opt == 6:
        controle1.toggle_play()

    elif opt == 7:
        controle1.pause()    