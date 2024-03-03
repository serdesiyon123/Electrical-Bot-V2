from telebot.types import KeyboardButton,ReplyKeyboardMarkup

#buttons
back  = "Back"
menu = "Main Menu"
modulescm = "Modules_and_Guides"
modulescp = "Modules_and_Guides."
modulesct = "Modules_and_Guides.."
modulespw = "Modules_and_Guides_."
modulesel = "Modules_and_Guides__"
pptscm = "Worksheets_&_Exams"
pptscp = "Worksheets_&_Exams."
pptsct = "Worksheets_&_Exams.."
pptspw = "Worksheets_&_Exams_."
pptsel = "Worksheets_&_Exams__"
contribute = "Contribute....."
communication_engineering = "Communication"
computer_engineering = "Computer"
electronics_engineering = "Electronics"
control_engineering = "Control"
power_engineering = "Power"
first_sem = "1st Semester"
second_sem = "2nd Semester"
# computer engineering
dsa = "DSA"
database = "Database Systems"

se = "Software Engineering"
os = "Operating Systems"
vlsi = "VLSI Design"
ml = "Machine Learning"

trend = ("Trends in CE")
mobile_computing = "Mobile Computing"
# communication engineering
microprocessors = ("Microprocessors & Interfacing")
digital_communications = "Digital Communication Systems"
data_communication = "Data Communication"
EM_waves = "EM waves"

microwave = "Microwaves Devices"
fiber_optics = "Fiber Optics"
antennas = "Antennas & RW"
mobile_communications = "Mobile Communications"
microelectronics = "Microelectronic Devices"
tele_networks = "Telecommunication Networks"

computer_networks= "Computer Networks"
intelligent_networks = "Intelligent Networks"
# control engineering
modern_control = "Modern Control Systems"
electrical_machines2 = "Electrical Machines II"
process_control = "Process Control"

power_electronics = "Power Electronics"
electrical_install = "Electrical Installation"
embedded_systems = "Embedded Systems"
digital_control = "Digital Control"
robotics_CV = "Robotics"
industrial_automation = "Industrial Automation"

instrumentation = "Instrumentation"
ai = "AI"
industrial_eco = "Industrial Management & Economy"


#electronics engineering

analog = "Analog System"

optoelectronics = "Optoelectronics"

ic_technology = "IC Technology"
digital_design = "Digital Systems"


# power engineering
power_systems2 = "Power Systems II"

energy_conversion = "Energy Conversion"
system_protection = "System Protection"
system_automation = "System Automation"
systems_operation = "Systems Operation"



# communication  eng 4th sem 2
view_fourth_commu_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_fourth_commu_menu.row(KeyboardButton(modulescm),KeyboardButton(pptscm))
view_fourth_commu_menu.row(KeyboardButton(text=back),KeyboardButton(text=menu))

view_fourth_yr_commu_eng_subjects = ReplyKeyboardMarkup( resize_keyboard=True)
view_fourth_yr_commu_eng_subjects.row(KeyboardButton(text=microprocessors),KeyboardButton(text=digital_communications))
view_fourth_yr_commu_eng_subjects.row(KeyboardButton(text=EM_waves),KeyboardButton(text=data_communication))
view_fourth_yr_commu_eng_subjects.row(KeyboardButton(text=back),KeyboardButton(text=menu))







# computer  eng 4th sem 2
view_fourth_computer_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_fourth_computer_menu.row(KeyboardButton(modulescp),KeyboardButton(pptscp))
view_fourth_computer_menu.row(KeyboardButton(text=back),KeyboardButton(text=menu))

view_fourth_yr_computer_eng_subjects = ReplyKeyboardMarkup( resize_keyboard=True)
view_fourth_yr_computer_eng_subjects.row(KeyboardButton(text=microprocessors),KeyboardButton(text=dsa))
view_fourth_yr_computer_eng_subjects.row(KeyboardButton(text=database),KeyboardButton(text=data_communication))
view_fourth_yr_computer_eng_subjects.row(KeyboardButton(text=back),KeyboardButton(text=menu))






# control  eng 4th sem 2
view_fourth_control_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_fourth_control_menu.row(KeyboardButton(modulesct),KeyboardButton(pptsct))
view_fourth_control_menu.row(KeyboardButton(text=back),KeyboardButton(text=menu))

view_fourth_yr_control_eng_subjects = ReplyKeyboardMarkup( resize_keyboard=True)
view_fourth_yr_control_eng_subjects.row(KeyboardButton(text=modern_control),KeyboardButton(text=electrical_machines2))
view_fourth_yr_control_eng_subjects.row(KeyboardButton(text=process_control),KeyboardButton(text=microprocessors))
view_fourth_yr_control_eng_subjects.row(KeyboardButton(text=back),KeyboardButton(text=menu))



# electronics  eng 4th sem 2
view_fourth_electronics_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_fourth_electronics_menu.row(KeyboardButton(modulesel),KeyboardButton(pptsel))
view_fourth_electronics_menu.row(KeyboardButton(text=back),KeyboardButton(text=menu))

view_fourth_yr_electronics_eng_subjects = ReplyKeyboardMarkup( resize_keyboard=True)
view_fourth_yr_electronics_eng_subjects.row(KeyboardButton(text=digital_communications),KeyboardButton(text=EM_waves))
view_fourth_yr_electronics_eng_subjects.row(KeyboardButton(text=analog),KeyboardButton(text=microprocessors),KeyboardButton(text=power_electronics))
view_fourth_yr_electronics_eng_subjects.row(KeyboardButton(text=back),KeyboardButton(text=menu))





# power  eng 4th sem 2
view_fourth_power_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_fourth_power_menu.row(KeyboardButton(modulespw),KeyboardButton(pptspw))
view_fourth_power_menu.row(KeyboardButton(text=back),KeyboardButton(text=menu))

view_fourth_yr_power_eng_subjects = ReplyKeyboardMarkup( resize_keyboard=True)
view_fourth_yr_power_eng_subjects.row(KeyboardButton(text=modern_control),KeyboardButton(text=electrical_machines2))
view_fourth_yr_power_eng_subjects.row(KeyboardButton(text=power_systems2),KeyboardButton(text=microprocessors))
view_fourth_yr_power_eng_subjects.row(KeyboardButton(text=back),KeyboardButton(text=menu))





# fifth year menu
view_fifth_year_menu = ReplyKeyboardMarkup(resize_keyboard=True)
view_fifth_year_menu.row(KeyboardButton(text=computer_engineering),KeyboardButton(text=power_engineering))
view_fifth_year_menu.row(KeyboardButton(text=communication_engineering),KeyboardButton(text=electronics_engineering),KeyboardButton(text=control_engineering))
view_fifth_year_menu.row(KeyboardButton(text=contribute))
view_fifth_year_menu.row(KeyboardButton(text=back),KeyboardButton(text=menu))
