from telebot.types import KeyboardButton,ReplyKeyboardMarkup



back  = "Back"
menu = "Main Menu"
modules = "Modules_and_Guides._._"
modules2 = "Modules_and_Guides_._."
ppts1 = "Worksheets_&_Exams__.."
ppts2 = "Worksheets_&_Exams..__"
contribute = "Contribute....."
first_sem = "1st Semester>-..-"
second_sem = "2nd Semester>.--."

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





# electronics eng 5th year menu
view_fifth_electronics_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_fifth_electronics_menu.row(KeyboardButton(first_sem),KeyboardButton(second_sem))
view_fifth_electronics_menu.row(KeyboardButton(text=back),KeyboardButton(text=menu))


# electronics  eng 5th sem 1
view_fifth_1st_sem_electronics_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_fifth_1st_sem_electronics_menu.row(KeyboardButton(modules), KeyboardButton(ppts1))
view_fifth_1st_sem_electronics_menu.row(KeyboardButton(text=back),KeyboardButton(text=menu))

view_fifth_1st_sem_yr_electronics_eng_subjects = ReplyKeyboardMarkup( resize_keyboard=True)
view_fifth_1st_sem_yr_electronics_eng_subjects.row(KeyboardButton(text=microwave),KeyboardButton(text=mobile_communications),KeyboardButton(text=vlsi))
view_fifth_1st_sem_yr_electronics_eng_subjects.row(KeyboardButton(text=optoelectronics),KeyboardButton(text=microelectronics))
view_fifth_1st_sem_yr_electronics_eng_subjects.row(KeyboardButton(text=back),KeyboardButton(text=menu))

# electronics  eng 5th sem 2
view_fifth_2nd_sem_electronics_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
view_fifth_2nd_sem_electronics_menu.row(KeyboardButton(modules2), KeyboardButton(ppts2))
view_fifth_2nd_sem_electronics_menu.row(KeyboardButton(text=back),KeyboardButton(text=menu))

view_fifth_2nd_sem_yr_electronics_eng_subjects = ReplyKeyboardMarkup( resize_keyboard=True)
view_fifth_2nd_sem_yr_electronics_eng_subjects.row(KeyboardButton(text=digital_design),KeyboardButton(text=ic_technology))
view_fifth_2nd_sem_yr_electronics_eng_subjects.row(KeyboardButton(text=industrial_eco))
view_fifth_2nd_sem_yr_electronics_eng_subjects.row(KeyboardButton(text=back),KeyboardButton(text=menu))

