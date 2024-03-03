from telebot.types import KeyboardButton,ReplyKeyboardMarkup

#buttons
modules = "Modules & Guides"
ppts = "Worksheets & Exams"
back = "Back"
main_menu = "Main Menu"
applied_electronics = "Applied Electronics II"
logic_design = "Logic Design"
signal_processing = "Signal Processing"
network_analysis = "Network Analysis"
electrical_machines = "Electrical Machines I"
workshop2 = "Workshop II"
links = "Links"


# Second_sem_menu
view_second_sem_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_second_sem_menu.row(KeyboardButton(modules),KeyboardButton(ppts))
view_second_sem_menu.row(KeyboardButton(text=back),KeyboardButton(text=main_menu))


# Second_sem_modules
view_Second_sem_subjects = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_Second_sem_subjects.row(KeyboardButton(text=applied_electronics),KeyboardButton(text=logic_design),KeyboardButton(text=signal_processing),)
view_Second_sem_subjects.row(KeyboardButton(text=network_analysis),KeyboardButton(text=electrical_machines))
view_Second_sem_subjects.row(KeyboardButton(text=back),KeyboardButton(text=main_menu))



#links
view_links = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_links.row(KeyboardButton(text=links))
view_links.row(KeyboardButton(text=back),KeyboardButton(text=main_menu))
