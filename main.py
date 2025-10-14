from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.align import Align
from pynput import keyboard
import time

console = Console(color_system="truecolor")

def display_title_screen():

    title_content =Align.center( 
        Text(
            

            "APP TITLE\n\nAPP SUBTITLE"


            , 
        justify="center") ,
        vertical="middle" )

    #centered_content = Align.center(title_content, vertical="middle")

    main_panel = Panel(
        title_content,
        border_style="#FE8019",
        expand=True,
        highlight=True
    )

    layout = Layout(main_panel)

    with Live(layout, screen=True, redirect_stderr=False) as live:
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    display_title_screen()
