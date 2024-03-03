from telebot.types import KeyboardButton,ReplyKeyboardMarkup


# buttons
first_sem = "1st Semester...."
special = "Fields"
back  = "Back"
menu = "Main Menu"
modules = "Modules_and_Guides"
ppts = "Worksheets_&_Exams"
contribute = "Contribute...."
communication_systems= "Communication Systems"
computer_architecture = "Computer Architecture"
control_systems = "Control Systems"
electrical_measurement = "Electrical Measurement"
power_systems = "Power Systems"

computer_engineering = "Computer Engineering"
electronics_engineering = "Electronics Engineering"
control_engineering = "Control Engineering"
communication_engineering = "Communication Engineering"
power_engineering = "Power Engineering"

# Fourth_year_Menu
view_fourth_year_Menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_fourth_year_Menu.row(KeyboardButton(text=first_sem),KeyboardButton(text=special))
view_fourth_year_Menu.row(KeyboardButton(text=contribute))
view_fourth_year_Menu.row(KeyboardButton(text=back),KeyboardButton(text=menu))

# Fourth_first_menu
view_fourth_first_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_fourth_first_menu.row(KeyboardButton(modules),KeyboardButton(ppts))
view_fourth_first_menu.row(KeyboardButton(text=back),KeyboardButton(text=menu))


# Fourth_first_modules
view_fourth_first_subjects = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_fourth_first_subjects.row(KeyboardButton(text=communication_systems),KeyboardButton(text=computer_architecture),KeyboardButton(text=control_systems))
view_fourth_first_subjects.row(KeyboardButton(text=electrical_measurement),KeyboardButton(text=power_systems))
view_fourth_first_subjects.row(KeyboardButton(text=back),KeyboardButton(text=menu))

# specialization field list
view_special_courses = ReplyKeyboardMarkup(resize_keyboard=True)
view_special_courses.row(KeyboardButton(text=computer_engineering),KeyboardButton(text=power_engineering))
view_special_courses.row(KeyboardButton(text=communication_engineering),KeyboardButton(text=electronics_engineering),KeyboardButton(text=control_engineering))
view_special_courses.row(KeyboardButton(text=back),KeyboardButton(text=menu))


#links
view_links = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_links.row(KeyboardButton(text="Links"))
view_links.row(KeyboardButton(text="Back"),KeyboardButton(text="Main Menu"))


