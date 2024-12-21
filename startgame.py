from Ui.ui import *
from Services.services import *


services = Services()
ui = UI(services)

ui.create_board()
ui.play()

