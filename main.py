import tcod

def main()-> None:
    # Set the dimensions of the game window.
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height/2)

    # Load the tileset for the game graphics. This tileset is a 10x10 pixel tileset.
    # Make sure the file 'dejavu10x10_gs_tc.png' is in the correct directory and accessible.
    # If the file is missing or the path is incorrect, the game will not display correctly.
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # Create a new terminal window with the specified width, height, and tileset.
    # The title of the window is set to "Cruising The Baths" and vsync is enabled to
    # prevent screen tearing. If changing these settings, ensure the window size
    # remains appropriate for the game's design and that vsync matches your frame rate needs.
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Cruising The Baths",
        vsync=True,
    ) as context:
        # Create a root console with the same dimensions as the screen.
        # The order parameter 'F' is used for NumPy array order. If experiencing
        # issues with console rendering, verify this parameter is correct for your use case.
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        
        # Main game loop. To add new features or modify the game's behavior,
        # this loop will likely be the place to do so.
        while True:
            # Print the '@' character at position (1,1) on the screen.
            # This represents the player or a point of interest.
            # To change the player's position, modify the x and y parameters.
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)

            # Update the game window with the contents of root_console.
            # If changes are made to the game's graphics or UI, ensure this is called
            # to reflect those changes on the screen.
            context.present(root_console)

            # Event handling loop. Listens for events such as key presses and window close.
            # To add more event types, such as mouse clicks, expand this loop.
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    # If a QUIT event is received (e.g., closing the window),
                    # exit the game cleanly. To handle additional cleanup before exiting,
                    # insert the cleanup code before raising SystemExit.
                    raise SystemExit()
                

if __name__ == "__main__":
    # Entry point of the program. If the script is executed directly,
    # the main function is called. If importing this script, ensure that
    # it is done correctly to avoid unintended execution.
    main()
    