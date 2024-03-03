from telebot.types import KeyboardButton,ReplyKeyboardMarkup

#buttons
modules = "Modules& Guides"
ppts = "Worksheets& Exams"
back = "Back"
main_menu = "Main Menu"
apply_electronics = "Applied Electronics I"
computational_methods = "Computational Methods"
signals_systems = "Signals & Systems"
electromagnetic_fields = "Electromagnetic Fields"
oop_java = "OOP(Java)"
research_methods = "Research Methods"
workshop = "Workshop"
contribute = "Contribute..."
links = "Links"
first_semester = "1st Semester..."
second_semester = "2nd Semester..."



# Third_year_Menu
view_Third_year_Menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_Third_year_Menu.row(KeyboardButton(text=first_semester),KeyboardButton(text=second_semester),)
view_Third_year_Menu.row(KeyboardButton(text=contribute))
view_Third_year_Menu.row(KeyboardButton(text=back),KeyboardButton(text=main_menu))

# First_sem_menu
view_first_sem_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_first_sem_menu.row(KeyboardButton(modules),KeyboardButton(ppts))
view_first_sem_menu.row(KeyboardButton(text=back),KeyboardButton(text=main_menu))


# First_sem_subjects
view_first_sem_subjects = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_first_sem_subjects.row(KeyboardButton(text=apply_electronics),KeyboardButton(text=computational_methods),KeyboardButton(text=signals_systems),)
view_first_sem_subjects.row(KeyboardButton(text=electromagnetic_fields),KeyboardButton(text=oop_java),KeyboardButton(text=research_methods),)
view_first_sem_subjects.row(KeyboardButton(text=back),KeyboardButton(text=main_menu))


#


#links
view_links = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_links.row(KeyboardButton(text=links))
view_links.row(KeyboardButton(text=back),KeyboardButton(text=main_menu))







#Se