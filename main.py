import pygame
import sys
import customtkinter as ctk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
import screeninfo

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Inicializa PyGame
pygame.init()

# Define la función para obtener la lista de todos los monitores disponibles
def get_monitors():
    monitors = []
    monitor_info = screeninfo.get_monitors()
    for i, monitor in enumerate(monitor_info):
        monitors.append(f"Monitor {i+1}: {monitor.width}x{monitor.height}")
    return monitors

# Define la función para cargar una imagen como variable global
def load_background_image():
    global background_image
    file_path = askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg;*.gif')])
    if file_path:
        background_image = pygame.image.load(file_path).convert()


        # # Establece la resolución de la ventana PyGame según el tamaño de la imagen cargada
        # window_size = background_image.get_size()
        # window_flags = pygame.NOFRAME | pygame.SCALED
        # screen = pygame.display.set_mode(window_size, window_flags)
        #
        # # Establece el bucle principal de PyGame
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             sys.exit()
        #
        #     # Dibuja la imagen de fondo en la pantalla
        #     screen.blit(background_image, (0, 0))
        #
        #     # Actualiza la pantalla
        #     pygame.display.flip()
        #
        #     # Establece la posición de la ventana PyGame a la posición del monitor selecionado en el combobox
        #     monitor_index = monitors_listbox.current()
        #     if monitor_index != -1:
        #         monitor_info = screeninfo.get_monitors()[monitor_index]
        #         window_position = monitor_info.x, monitor_info.y
        #         pygame.display.window_pos = window_position
        #
        #
        #     # Asegura que la ventana de CustomTkinter esté en primer plano
        #     window.attributes('-topmost', True)
        #     window.update()

# Define la función para setear la posicion de la imagen en el monitor seleccionado
def update_monitors():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0, 0))
        pygame.display.flip()


        monitor_index = monitors_combobox.current()
        if monitor_index != -1:
            monitor_info = screeninfo.get_monitors()[monitor_index]
            window_position = monitor_info.x, monitor_info.y
            pygame.display.window_pos = window_position


        # Asegura que la ventana de CustomTkinter esté en primer plano
        window.attributes('-topmost', True)
        window.update()



# Crea una ventana CustomTkinter con una etiqueta y un botón para cargar una imagen
window = ctk.CTk()
window.title('Fakewally')
window.geometry('400x400')
window.resizable(False, False)

title_label = ctk.CTkLabel(window, text='Select Image ')
title_label.pack()

load_button = ctk.CTkButton(window, text='Load imagen', command=load_background_image)
load_button.pack(pady=10)

monitors_label = ctk.CTkLabel(window, text='Monitors:')
monitors_label.pack()

monitors_combobox = ctk.CTkComboBox(window, height=5, values=get_monitors())
monitors_combobox.pack(pady=5)

update_monitors_button = ctk.CTkButton(window, text='Update Monitors', command=update_monitors)
update_monitors_button.pack(pady=5)

# Establece la imagen de fondo predeterminada
background_image = pygame.Surface((1, 1))
background_image.fill((255, 255, 255))

# Establece la resolución de la ventana PyGame según la imagen predeterminada
window_size = background_image.get_size()
window_flags = pygame.NOFRAME | pygame.SCALED
screen = pygame.display.set_mode(window_size, window_flags)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Dibuja la imagen de fondo en la pantalla
    screen.blit(background_image, (0, 0))

    # Actualiza la pantalla
    pygame.display.flip()

    # Establece la posición de la ventana PyGame a la posición del monitor seleccionado
    monitor_index = monitors_combobox.cget('values').index(monitors_combobox.get())
    if monitor_index != -1:
        monitor_info = screeninfo.get_monitors()[monitor_index]
        window_position = monitor_info.x, monitor_info.y
        pygame.display.window_pos = window_position


    # Asegura que la ventana de CustomTkinter esté en primer plano
    window.attributes('-topmost', True)
    window.update()
