import tamiko
import process
import sys

tamiko.debug = False
tamiko.set_display_name(True)
tamiko.set_font_color(tamiko.Color.PINK)

tamiko.start_program()

process.run()

tamiko.finish_program()
