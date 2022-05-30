# Import libraries
import sys

sys.path.insert(0, '../../')

import os
import pygame
import pygame_menu


# -----------------------------------------------------------------------------
# Constants and global variables
# -----------------------------------------------------------------------------
FPS = 60.0
WINDOW_SIZE = (800, 600)

sound = None  # type: pygame_menu.sound.Sound
surface = None  # type: pygame.Surface
main_menu = None  # type: pygame_menu.Menu


# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------
def main_background():
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.

    :return: None
    """
    surface.fill((40, 40, 40))


def check_name_test(value):
    """
    This function tests the text input widget.

    :param value: The widget value
    :type value: str
    :return: None
    """
    print('User name: {0}'.format(value))


# noinspection PyUnusedLocal
def update_menu_sound(value, enabled):
    """
    Update menu sound.

    :param value: Value of the selector (Label and index)
    :type value: tuple
    :param enabled: Parameter of the selector, (True/False)
    :type enabled: bool
    :return: None
    """
    if enabled:
        main_menu.set_sound(sound, recursive=True)
        print('Menu sounds were enabled')
    else:
        main_menu.set_sound(None, recursive=True)
        print('Menu sounds were disabled')


def main(test=False):
    """
    Main program.

    :param test: Indicate function is being tested
    :type test: bool
    :return: None
    """

    # -------------------------------------------------------------------------
    # Globals
    # -------------------------------------------------------------------------
    global main_menu
    global sound
    global surface

    # -------------------------------------------------------------------------
    # Init pygame
    # -------------------------------------------------------------------------
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Create pygame screen and objects
    surface = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption('Logic Gate Simulator')
    clock = pygame.time.Clock()

    # -------------------------------------------------------------------------
    # Set sounds
    # -------------------------------------------------------------------------
    sound = pygame_menu.sound.Sound()

    # Load example sounds
    sound.load_example_sounds()

    # Disable a sound
    sound.set_sound(pygame_menu.sound.SOUND_TYPE_ERROR, None)

    # -------------------------------------------------------------------------
    # Create menus: Settings/Options
    # -------------------------------------------------------------------------
    settings_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    settings_menu_theme.title_offset = (5, -2)
    settings_menu_theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT
    settings_menu_theme.widget_font = pygame_menu.font.FONT_FRANCHISE
    settings_menu_theme.widget_font_size = 20

    settings_menu = pygame_menu.Menu(
        height=600,
        width=800,
        onclose=pygame_menu.events.NONE ,
        theme=settings_menu_theme,
        title='Settings'
    )
    settings_menu.add.button('Return to main menu', pygame_menu.events.BACK,
                             align=pygame_menu.locals.ALIGN_CENTER)


    #mode selector
    #logic gate
    logic_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    logic_menu_theme.title_offset = (5, -2)
    logic_menu_theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT
    logic_menu_theme.widget_font = pygame_menu.font.FONT_OPEN_SANS_LIGHT
    logic_menu_theme.widget_font_size = 20

    logic_menu = pygame_menu.Menu(
        height=600,
        width=800,
        onclose=pygame_menu.events.NONE,
        theme=logic_menu_theme,
        title='Logic Gates'
    )



    pygame.display.flip()


    logic_menu.add.button('Back', pygame_menu.events.BACK,
                          align=pygame_menu.locals.ALIGN_CENTER)
    #karnough maps
    #help
    help_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    help_menu_theme.title_offset = (5, -2)
    help_menu_theme.widget_alignment = pygame_menu.locals.ALIGN_LEFT
    help_menu_theme.widget_font = pygame_menu.font.FONT_OPEN_SANS_LIGHT
    help_menu_theme.widget_font_size = 20

    help_menu = pygame_menu.Menu(
        height=600,
        width=800,
        onclose=pygame_menu.events.NONE,
        theme=help_menu_theme,
        title='Help'
    )
    #add text
    font = pygame.font.SysFont("arial_cyrilic", 72)
    text = font.render("", True, (0, 128, 0))

    help_menu.add.button('Return to main menu', pygame_menu.events.BACK,
                         align=pygame_menu.locals.ALIGN_CENTER)


    # -------------------------------------------------------------------------
    # Create menus: Main menu
    # -------------------------------------------------------------------------
    main_menu_theme = pygame_menu.themes.THEME_DARK.copy()
    main_menu_theme.widget_offset = (0, 0.09)
    main_menu_theme.title_font = pygame_menu.font.FONT_COMIC_NEUE
    main_menu_theme.widget_font = pygame_menu.font.FONT_COMIC_NEUE
    main_menu_theme.widget_font_size = 30

    main_menu = pygame_menu.Menu(
        columns=4,
        rows=2,
        height=600,
        width=800,
        onclose=pygame_menu.events.EXIT,  # User press ESC button
        title='Main menu',
        theme=main_menu_theme,
    )

    #main_menu.add.selector('Modes :', [('ЭКРАН', 1), ('Karnaugh Maps', 2)], onchange=None)
    main_menu.add.button('Logic Gates', logic_menu)
    main_menu.add.button("Help", help_menu)
    main_menu.add.button('Settings', settings_menu)
    main_menu.add.selector('Menu sounds ',
                           [('Off', False), ('On', True)],
                           onchange=update_menu_sound)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)

    # -------------------------------------------------------------------------
    # Main loop
    # -------------------------------------------------------------------------
    while True:

        # Tick
        clock.tick(FPS)

        # Paint background
        main_background()

        # Main menu
        main_menu.mainloop(surface, main_background, disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()