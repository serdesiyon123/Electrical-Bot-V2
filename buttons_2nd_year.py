from telebot.types import KeyboardButton,ReplyKeyboardMarkup


# buttons
second_semester = "2nd Semester.."
back = "Back"
main_menu = "Main Menu"
applied = "Applied III"
fundamentals_ee = "Fundamentals of EE"
probability = "Probability"
dynamics = "Dynamics"
thermodynamics = "Thermodynamics"
history = "History"
contribute = "Contribute.."
modules = "Modules&Guides"
ppts = "Worksheets&Exams"
links = "Useful Links"

# Second_year_Menu
view_Second_year_Menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_Second_year_Menu.row(KeyboardButton(text=second_semester),KeyboardButton(text=contribute))
view_Second_year_Menu.row(KeyboardButton(text=back),KeyboardButton(text=main_menu))

# Second_sem_menu
view_second_sem_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_second_sem_menu.row(KeyboardButton(modules),KeyboardButton(ppts))
view_second_sem_menu.row(KeyboardButton(text=back),KeyboardButton(text=main_menu))


# Second_sem_modules
view_Second_sem_subjects = ReplyKeyboardMarkup(resize_keyboard=True )
view_Second_sem_subjects.row(KeyboardButton(text=fundamentals_ee),KeyboardButton(text=applied),KeyboardButton(text=probability),)
view_Second_sem_subjects.row(KeyboardButton(text=dynamics),KeyboardButton(text=thermodynamics),KeyboardButton(text=history),)
view_Second_sem_subjects.row(KeyboardButton(text=back),KeyboardButton(text=main_menu))




#contribute
view_contibute = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_contibute.row(KeyboardButton(text=fundamentals_ee),KeyboardButton(text=applied),KeyboardButton(text=probability),)
view_contibute.row(KeyboardButton(text=dynamics),KeyboardButton(text=thermodynamics),KeyboardButton(text=history),)
view_contibute.row(KeyboardButton(text=back),(KeyboardButton(text=links)),KeyboardButton(text=main_menu))


#links
view_links = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_links.row(KeyboardButton(text=links))
view_links.row(KeyboardButton(text=back),KeyboardButton(text=main_menu))
