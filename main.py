"""
This module is the main entry point for a roguelike game. It handles the
initialization of the game, the main game loop, rendering, and event handling.
It also includes functionality for saving the game state.
"""

import traceback

import tcod

import color
import exceptions
import setup_game
import input_handlers


def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """
    Saves the current game state to a file if
    the current event handler has an associated engine.

    Parameters:
    - handler: The current event handler,
        which may contain an engine with the game state.
    - filename: The name of the file where the game state will be saved.

    Returns:
    None
    """
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")


def main() -> None:
    """
    Initializes the game window and enters the main game loop.

    This function sets up the game window, loads the tileset, and
    initializes the game's event handler. It then enters an infinite loop where
    it handles rendering and event processing until a quit event
    is encountered.

    Returns:
    None
    """
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(
            screen_width, screen_height, order="F")
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                        )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            save_game(handler, "savegame.sav")
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise


if __name__ == "__main__":
    main()
