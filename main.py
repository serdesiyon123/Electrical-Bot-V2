import os

from dotenv import load_dotenv
import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
import buttons_2nd_year as b2s2
import buttons_3rd_yr_1st_sem as b3s1
import buttons_3rd_yr_2nd_sem as b3s2
import buttons_4th_yr_1st_sem as b4s1
import buttons_4th_yr_2nd_sem as b4s2
import fifth_year_power as p5
import fifth_year_control as ct5
import fifth_year_computer as cp5
import fifth_year_electronics as e5
import fifth_year_communication as cm5

load_dotenv('api_key.env')
API_KEY = os.getenv('API_KEY')
CHANNEL_ID = os.getenv('CHANNEL_ID')
CONTRIBUTE = os.getenv('contributionpage')

mybot = telebot.TeleBot(token=API_KEY)
user_state = {
}


def append_state(chat_id, state):
    if chat_id in user_state:
        user_state[chat_id].append(state)
    else:
        user_state[chat_id] = [state]


# buttons
second_year = "2nd Year(Sophomore)"
third_year = "3rd Year(Junior)"
fourth_year = "4th Year(Senior)"
fifth_year = "5th Year(GC)"
back = "Back"
menu = "Main_Menu"
# Main_Menu
view_menu = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, )
view_menu.row(KeyboardButton(text=second_year), KeyboardButton(text=third_year))
view_menu.row(KeyboardButton(text=fourth_year), KeyboardButton(text=fifth_year))


@mybot.message_handler(commands=['start'])
def hello(message):
    mybot.send_message(message.chat.id,
                       "Hello, welcome to the Electrical_Bot.\nWhich year resource are you looking for? ",
                       reply_markup=view_menu)


@mybot.message_handler(commands=['menu'])
def menu(message):
    mybot.send_message(message.chat.id,
                       "Which year resource are you looking for? ",
                       reply_markup=view_menu)


@mybot.message_handler(func=lambda message: message.text == second_year)
def second_year_menu(message):
    append_state(message.chat.id, second_year)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b2s2.view_Second_year_Menu)


@mybot.message_handler(func=lambda message: message.text == b2s2.second_semester)
def second_year_second_sem_menu(message):
    append_state(message.chat.id, b2s2.second_semester)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b2s2.view_Second_sem_subjects)


@mybot.message_handler(func=lambda message: message.text == b2s2.fundamentals_ee)
def second_year_second_sem_modules_menu(message):
    append_state(message.chat.id, b2s2.fundamentals_ee)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b2s2.view_second_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b2s2.applied)
def second_year_second_sem_modules_menu(message):
    append_state(message.chat.id, b2s2.applied)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b2s2.view_second_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b2s2.dynamics)
def second_year_second_sem_modules_menu(message):
    append_state(message.chat.id, b2s2.dynamics)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b2s2.view_second_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b2s2.thermodynamics)
def second_year_second_sem_modules_menu(message):
    append_state(message.chat.id, b2s2.thermodynamics)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b2s2.view_second_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b2s2.probability)
def second_year_second_sem_modules_menu(message):
    append_state(message.chat.id, b2s2.probability)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b2s2.view_second_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b2s2.history)
def second_year_second_sem_modules_menu(message):
    append_state(message.chat.id, b2s2.history)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b2s2.view_second_sem_menu)


# third year
@mybot.message_handler(func=lambda message: message.text == third_year)
def third_year_menu(message):
    append_state(message.chat.id, third_year)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s1.view_Third_year_Menu)


@mybot.message_handler(func=lambda message: message.text == b3s1.first_semester)
def third_year_first_sem_menu(message):
    append_state(message.chat.id, b3s1.first_semester)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s1.view_first_sem_subjects)


@mybot.message_handler(func=lambda message: message.text == b3s1.apply_electronics)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b3s1.apply_electronics)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s1.view_first_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b3s1.computational_methods)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b3s1.computational_methods)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s1.view_first_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b3s1.signals_systems)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b3s1.signals_systems)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s1.view_first_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b3s1.electromagnetic_fields)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b3s1.electromagnetic_fields)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s1.view_first_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b3s1.oop_java)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b3s1.oop_java)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s1.view_first_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b3s1.research_methods)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b3s1.research_methods)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s1.view_first_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b3s1.second_semester)
def third_year_first_sem_menu(message):
    append_state(message.chat.id, b3s1.second_semester)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s2.view_Second_sem_subjects)


@mybot.message_handler(func=lambda message: message.text == b3s2.applied_electronics)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b3s2.applied_electronics)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s2.view_second_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b3s2.logic_design)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b3s2.logic_design)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s2.view_second_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b3s2.signal_processing)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b3s2.signal_processing)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s2.view_second_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b3s2.network_analysis)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b3s2.network_analysis)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s2.view_second_sem_menu)


@mybot.message_handler(func=lambda message: message.text == b3s2.electrical_machines)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b3s2.electrical_machines)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b3s2.view_second_sem_menu)


# fourth year first sem
@mybot.message_handler(func=lambda message: message.text == fourth_year)
def third_year_menu(message):
    append_state(message.chat.id, fourth_year)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s1.view_fourth_year_Menu)


@mybot.message_handler(func=lambda message: message.text == b4s1.first_sem)
def third_year_first_sem_menu(message):
    append_state(message.chat.id, b4s1.first_sem)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s1.view_fourth_first_subjects)


@mybot.message_handler(func=lambda message: message.text == b4s1.communication_systems)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b4s1.communication_systems)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s1.view_fourth_first_menu)


@mybot.message_handler(func=lambda message: message.text == b4s1.computer_architecture)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b4s1.computer_architecture)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s1.view_fourth_first_menu)


@mybot.message_handler(func=lambda message: message.text == b4s1.control_systems)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b4s1.control_systems)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s1.view_fourth_first_menu)


@mybot.message_handler(func=lambda message: message.text == b4s1.electrical_measurement)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b4s1.electrical_measurement)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s1.view_fourth_first_menu)


@mybot.message_handler(func=lambda message: message.text == b4s1.power_systems)
def third_year_first_sem_modules_menu(message):
    append_state(message.chat.id, b4s1.power_systems)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s1.view_fourth_first_menu)


@mybot.message_handler(func=lambda message: message.text == b4s1.special)
def third_year_first_sem_menu(message):
    append_state(message.chat.id, b4s1.special)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s1.view_special_courses)


# fourth year second sem

# communication eng
@mybot.message_handler(func=lambda message: message.text == b4s1.communication_engineering)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s1.communication_engineering)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_yr_commu_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == b4s2.microprocessors)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.microprocessors)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_commu_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.digital_communications)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.digital_communications)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_commu_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.EM_waves)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.EM_waves)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_commu_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.data_communication)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.data_communication)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_commu_menu)


# computer eng
@mybot.message_handler(func=lambda message: message.text == b4s1.computer_engineering)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s1.computer_engineering)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_yr_computer_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == b4s2.microprocessors)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.microprocessors)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_computer_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.dsa)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.dsa)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_computer_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.database)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.database)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_computer_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.data_communication)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.data_communication)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_computer_menu)


# control eng
@mybot.message_handler(func=lambda message: message.text == b4s1.control_engineering)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s1.control_engineering)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_yr_control_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == b4s2.modern_control)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.modern_control)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_control_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.electrical_machines2)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.electrical_machines2)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_control_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.process_control)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.process_control)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_control_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.microprocessors)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.microprocessors)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_control_menu)


# electronics eng
@mybot.message_handler(func=lambda message: message.text == b4s1.electronics_engineering)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s1.electronics_engineering)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_yr_electronics_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == b4s2.digital_communications)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.digital_communications)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_electronics_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.EM_waves)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.EM_waves)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_electronics_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.microprocessors)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.microprocessors)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_electronics_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.power_electronics)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.power_electronics)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_electronics_menu)


# power eng
@mybot.message_handler(func=lambda message: message.text == b4s1.power_engineering)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s1.power_engineering)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_yr_power_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == b4s2.modern_control)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.modern_control)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_power_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.electrical_machines2)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.electrical_machines2)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_power_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.power_systems2)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.power_systems2)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_power_menu)


@mybot.message_handler(func=lambda message: message.text == b4s2.microprocessors)
def fourth_year_sec_sem_menu(message):
    append_state(message.chat.id, b4s2.microprocessors)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fourth_power_menu)


# fifth year
@mybot.message_handler(func=lambda message: message.text == fifth_year)
def fifth_year_menu(message):
    append_state(message.chat.id, fifth_year)
    mybot.send_message(message.chat.id, ">>>", reply_markup=b4s2.view_fifth_year_menu)


# communication eng
# first sem
@mybot.message_handler(func=lambda message: message.text == b4s2.communication_engineering)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, b4s2.communication_engineering)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_commu_menu)


@mybot.message_handler(func=lambda message: message.text == cm5.first_sem)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, cm5.first_sem)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_1st_sem_yr_commu_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == cm5.microwave)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, cm5.microwave)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_1st_sem_commu_menu)


@mybot.message_handler(func=lambda message: message.text == cm5.fiber_optics)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, cm5.fiber_optics)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_1st_sem_commu_menu)


@mybot.message_handler(func=lambda message: message.text == cm5.antennas)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, cm5.antennas)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_1st_sem_commu_menu)


@mybot.message_handler(func=lambda message: message.text == cm5.mobile_communications)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, cm5.mobile_communications)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_1st_sem_commu_menu)


@mybot.message_handler(func=lambda message: message.text == cm5.microelectronics)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, cm5.microelectronics)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_1st_sem_commu_menu)


@mybot.message_handler(func=lambda message: message.text == cm5.tele_networks)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, cm5.tele_networks)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_1st_sem_commu_menu)


# first sem
@mybot.message_handler(func=lambda message: message.text == b4s2.communication_engineering)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, b4s2.communication_engineering)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_commu_menu)


@mybot.message_handler(func=lambda message: message.text == cm5.second_sem)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, cm5.first_sem)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_2nd_sem_yr_commu_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == cm5.intelligent_networks)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, cm5.intelligent_networks)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_2nd_sem_commu_menu)


@mybot.message_handler(func=lambda message: message.text == cm5.computer_networks)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, cm5.computer_networks)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_2nd_sem_commu_menu)


@mybot.message_handler(func=lambda message: message.text == cm5.industrial_eco)
def fifth_commu_eng_year_menu(message):
    append_state(message.chat.id, cm5.industrial_eco)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cm5.view_fifth_2nd_sem_commu_menu)


# computer eng

# first sem
@mybot.message_handler(func=lambda message: message.text == b4s2.computer_engineering)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, b4s2.computer_engineering)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_computer_menu)


@mybot.message_handler(func=lambda message: message.text == cp5.first_sem)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, cp5.first_sem)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_1st_sem_yr_computer_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == cp5.se)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, cp5.se)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_1st_sem_computer_menu)


@mybot.message_handler(func=lambda message: message.text == cp5.os)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, cp5.os)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_1st_sem_computer_menu)


@mybot.message_handler(func=lambda message: message.text == cp5.embedded_systems)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, cp5.embedded_systems)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_1st_sem_computer_menu)


@mybot.message_handler(func=lambda message: message.text == cp5.ml)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, cp5.ml)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_1st_sem_computer_menu)


@mybot.message_handler(func=lambda message: message.text == cp5.vlsi)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, cp5.vlsi)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_1st_sem_computer_menu)


@mybot.message_handler(func=lambda message: message.text == cp5.robotics_CV)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, cp5.robotics_CV)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_1st_sem_computer_menu)


# second sem

@mybot.message_handler(func=lambda message: message.text == cp5.second_sem)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, cp5.second_sem)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_2nd_sem_yr_computer_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == cp5.industrial_eco)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, cp5.industrial_eco)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_2nd_sem_computer_menu)


@mybot.message_handler(func=lambda message: message.text == cp5.mobile_computing)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, cp5.mobile_computing)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_2nd_sem_computer_menu)


@mybot.message_handler(func=lambda message: message.text == cp5.trend)
def fifth_computer_eng_year_menu(message):
    append_state(message.chat.id, cp5.trend)
    mybot.send_message(message.chat.id, ">>>", reply_markup=cp5.view_fifth_2nd_sem_computer_menu)


# control eng
# first sem
@mybot.message_handler(func=lambda message: message.text == b4s2.control_engineering)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, b4s2.control_engineering)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_control_menu)


@mybot.message_handler(func=lambda message: message.text == ct5.first_sem)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, ct5.first_sem)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_1st_sem_yr_control_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == ct5.power_electronics)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, ct5.power_electronics)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_1st_sem_control_menu)


@mybot.message_handler(func=lambda message: message.text == ct5.electrical_install)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, ct5.electrical_install)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_1st_sem_control_menu)


@mybot.message_handler(func=lambda message: message.text == ct5.embedded_systems)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, ct5.embedded_systems)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_1st_sem_control_menu)


@mybot.message_handler(func=lambda message: message.text == ct5.industrial_automation)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, ct5.industrial_automation)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_1st_sem_control_menu)


@mybot.message_handler(func=lambda message: message.text == ct5.digital_control)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, ct5.digital_control)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_1st_sem_control_menu)


@mybot.message_handler(func=lambda message: message.text == ct5.robotics_CV)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, ct5.robotics_CV)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_1st_sem_control_menu)


# second sem

@mybot.message_handler(func=lambda message: message.text == ct5.second_sem)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, ct5.second_sem)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_2nd_sem_yr_control_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == ct5.industrial_eco)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, ct5.industrial_eco)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_2nd_sem_control_menu)


@mybot.message_handler(func=lambda message: message.text == ct5.ai)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, ct5.ai)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_2nd_sem_control_menu)


@mybot.message_handler(func=lambda message: message.text == ct5.instrumentation)
def fifth_control_eng_year_menu(message):
    append_state(message.chat.id, ct5.instrumentation)
    mybot.send_message(message.chat.id, ">>>", reply_markup=ct5.view_fifth_2nd_sem_control_menu)


# electronics eng
# first sem
@mybot.message_handler(func=lambda message: message.text == b4s2.electronics_engineering)
def fifth_electronics_eng_year_menu(message):
    append_state(message.chat.id, b4s2.electronics_engineering)
    mybot.send_message(message.chat.id, ">>>", reply_markup=e5.view_fifth_electronics_menu)


@mybot.message_handler(func=lambda message: message.text == e5.first_sem)
def fifth_electronics_eng_year_menu(message):
    append_state(message.chat.id, e5.first_sem)
    mybot.send_message(message.chat.id, ">>>", reply_markup=e5.view_fifth_1st_sem_yr_electronics_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == e5.microwave)
def fifth_electronics_eng_year_menu(message):
    append_state(message.chat.id, e5.microwave)
    mybot.send_message(message.chat.id, ">>>", reply_markup=e5.view_fifth_1st_sem_electronics_menu)


@mybot.message_handler(func=lambda message: message.text == e5.mobile_communications)
def fifth_electronics_eng_year_menu(message):
    append_state(message.chat.id, e5.mobile_communications)
    mybot.send_message(message.chat.id, ">>>", reply_markup=e5.view_fifth_1st_sem_electronics_menu)


@mybot.message_handler(func=lambda message: message.text == e5.vlsi)
def fifth_electronics_eng_year_menu(message):
    append_state(message.chat.id, e5.vlsi)
    mybot.send_message(message.chat.id, ">>>", reply_markup=e5.view_fifth_1st_sem_electronics_menu)


@mybot.message_handler(func=lambda message: message.text == e5.optoelectronics)
def fifth_electronics_eng_year_menu(message):
    append_state(message.chat.id, e5.optoelectronics)
    mybot.send_message(message.chat.id, ">>>", reply_markup=e5.view_fifth_1st_sem_electronics_menu)


@mybot.message_handler(func=lambda message: message.text == e5.microelectronics)
def fifth_electronics_eng_year_menu(message):
    append_state(message.chat.id, e5.microelectronics)
    mybot.send_message(message.chat.id, ">>>", reply_markup=e5.view_fifth_1st_sem_electronics_menu)


# second sem

@mybot.message_handler(func=lambda message: message.text == e5.second_sem)
def fifth_electronics_eng_year_menu(message):
    append_state(message.chat.id, e5.second_sem)
    mybot.send_message(message.chat.id, ">>>", reply_markup=e5.view_fifth_2nd_sem_yr_electronics_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == e5.industrial_eco)
def fifth_electronics_eng_year_menu(message):
    append_state(message.chat.id, e5.industrial_eco)
    mybot.send_message(message.chat.id, ">>>", reply_markup=e5.view_fifth_2nd_sem_electronics_menu)


@mybot.message_handler(func=lambda message: message.text == e5.digital_design)
def fifth_electronics_eng_year_menu(message):
    append_state(message.chat.id, e5.digital_design)
    mybot.send_message(message.chat.id, ">>>", reply_markup=e5.view_fifth_2nd_sem_electronics_menu)


@mybot.message_handler(func=lambda message: message.text == e5.ic_technology)
def fifth_electronics_eng_year_menu(message):
    append_state(message.chat.id, e5.ic_technology)
    mybot.send_message(message.chat.id, ">>>", reply_markup=e5.view_fifth_2nd_sem_electronics_menu)


# power engineering
# first sem
@mybot.message_handler(func=lambda message: message.text == b4s2.power_engineering)
def fifth_power_eng_year_menu(message):
    append_state(message.chat.id, b4s2.power_engineering)
    mybot.send_message(message.chat.id, ">>>", reply_markup=p5.view_fifth_power_menu)


@mybot.message_handler(func=lambda message: message.text == p5.first_sem)
def fifth_power_eng_year_menu(message):
    append_state(message.chat.id, p5.first_sem)
    mybot.send_message(message.chat.id, ">>>", reply_markup=p5.view_fifth_1st_sem_yr_power_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == p5.energy_conversion)
def fifth_power_eng_year_menu(message):
    append_state(message.chat.id, p5.energy_conversion)
    mybot.send_message(message.chat.id, ">>>", reply_markup=p5.view_fifth_1st_sem_power_menu)


@mybot.message_handler(func=lambda message: message.text == p5.power_electronics)
def fifth_power_eng_year_menu(message):
    append_state(message.chat.id, p5.power_electronics)
    mybot.send_message(message.chat.id, ">>>", reply_markup=p5.view_fifth_1st_sem_power_menu)


@mybot.message_handler(func=lambda message: message.text == p5.system_protection)
def fifth_power_eng_year_menu(message):
    append_state(message.chat.id, p5.system_protection)
    mybot.send_message(message.chat.id, ">>>", reply_markup=p5.view_fifth_1st_sem_power_menu)


@mybot.message_handler(func=lambda message: message.text == p5.system_automation)
def fifth_power_eng_year_menu(message):
    append_state(message.chat.id, p5.system_automation)
    mybot.send_message(message.chat.id, ">>>", reply_markup=p5.view_fifth_1st_sem_power_menu)


@mybot.message_handler(func=lambda message: message.text == p5.electrical_install)
def fifth_power_eng_year_menu(message):
    append_state(message.chat.id, p5.electrical_install)
    mybot.send_message(message.chat.id, ">>>", reply_markup=p5.view_fifth_1st_sem_power_menu)


# second sem

@mybot.message_handler(func=lambda message: message.text == p5.second_sem)
def fifth_power_eng_year_menu(message):
    append_state(message.chat.id, p5.second_sem)
    mybot.send_message(message.chat.id, ">>>", reply_markup=p5.view_fifth_2nd_sem_yr_power_eng_subjects)


@mybot.message_handler(func=lambda message: message.text == p5.industrial_eco)
def fifth_power_eng_year_menu(message):
    append_state(message.chat.id, p5.industrial_eco)
    mybot.send_message(message.chat.id, ">>>", reply_markup=p5.view_fifth_2nd_sem_power_menu)


@mybot.message_handler(func=lambda message: message.text == p5.systems_operation)
def fifth_power_eng_year_menu(message):
    append_state(message.chat.id, p5.systems_operation)
    mybot.send_message(message.chat.id, ">>>", reply_markup=p5.view_fifth_2nd_sem_power_menu)


@mybot.message_handler(func=lambda message: message.text == p5.instrumentation)
def fifth_power_eng_year_menu(message):
    append_state(message.chat.id, p5.instrumentation)
    mybot.send_message(message.chat.id, ">>>", reply_markup=p5.view_fifth_2nd_sem_power_menu)


# Back button handler
back_button_handlers = ({
    second_year: lambda message: mybot.send_message(message.chat.id, "Which year resource are you looking for?",
                                                    reply_markup=view_menu),
    fifth_year: lambda message: mybot.send_message(message.chat.id, "Which year resource are you looking for?",
                                                   reply_markup=view_menu),
    b2s2.second_semester: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                             reply_markup=b2s2.view_Second_year_Menu),
    b2s2.fundamentals_ee: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                             reply_markup=b2s2.view_Second_sem_subjects),
    b2s2.applied: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                     reply_markup=b2s2.view_Second_sem_subjects),
    b2s2.dynamics: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                      reply_markup=b2s2.view_Second_sem_subjects),
    b2s2.thermodynamics: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                            reply_markup=b2s2.view_Second_sem_subjects),
    b2s2.probability: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                         reply_markup=b2s2.view_Second_sem_subjects),
    b2s2.history: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                     reply_markup=b2s2.view_Second_sem_subjects),
    b2s2.contribute: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                        reply_markup=b2s2.view_Second_year_Menu),
    third_year: lambda message: mybot.send_message(message.chat.id, "<<<", reply_markup=view_menu),
    b3s1.first_semester: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                            reply_markup=b3s1.view_Third_year_Menu),
    b3s1.apply_electronics: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                               reply_markup=b3s1.view_first_sem_subjects),
    b3s1.computational_methods: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                   reply_markup=b3s1.view_first_sem_subjects),
    b3s1.signals_systems: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                             reply_markup=b3s1.view_first_sem_subjects),
    b3s1.electromagnetic_fields: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                    reply_markup=b3s1.view_first_sem_subjects),
    b3s1.oop_java: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                      reply_markup=b3s1.view_first_sem_subjects),
    b3s1.research_methods: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                              reply_markup=b3s1.view_first_sem_subjects),
    b3s1.second_semester: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                             reply_markup=b3s1.view_Third_year_Menu),
    b3s2.applied_electronics: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                 reply_markup=b3s2.view_Second_sem_subjects),
    b3s2.logic_design: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                          reply_markup=b3s2.view_Second_sem_subjects),
    b3s2.signal_processing: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                               reply_markup=b3s2.view_Second_sem_subjects),
    b3s2.network_analysis: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                              reply_markup=b3s2.view_Second_sem_subjects),
    b3s2.electrical_machines: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                 reply_markup=b3s2.view_Second_sem_subjects),
    fourth_year: lambda message: mybot.send_message(message.chat.id, "<<<", reply_markup=view_menu),
    b4s1.first_sem: lambda message: mybot.send_message(message.chat.id, "<<<", reply_markup=b4s1.view_fourth_year_Menu),
    b4s1.communication_systems: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                   reply_markup=b4s1.view_fourth_first_subjects),
    b4s1.computer_architecture: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                   reply_markup=b4s1.view_fourth_first_subjects),
    b4s1.control_systems: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                             reply_markup=b4s1.view_fourth_first_subjects),
    b4s1.electrical_measurement: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                    reply_markup=b4s1.view_fourth_first_subjects),
    b4s1.power_systems: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                           reply_markup=b4s1.view_fourth_first_subjects),
    b4s1.special: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                     reply_markup=b4s1.view_fourth_first_subjects),
    b4s1.communication_engineering: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                       reply_markup=b4s1.view_fourth_year_Menu),
    b4s2.microprocessors: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                             reply_markup=b4s2.view_fourth_commu_menu),
    b4s2.digital_communications: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                    reply_markup=b4s2.view_fourth_commu_menu),
    b4s2.EM_waves: lambda message: mybot.send_message(message.chat.id, "<<<", reply_markup=b4s2.view_fourth_commu_menu),
    b4s2.data_communication: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                reply_markup=b4s2.view_fourth_commu_menu),
    b4s1.computer_engineering: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                  reply_markup=b4s1.view_fourth_year_Menu),
    b4s2.microprocessors: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                             reply_markup=b4s2.view_fourth_computer_menu),
    b4s2.dsa: lambda message: mybot.send_message(message.chat.id, "<<<", reply_markup=b4s2.view_fourth_computer_menu),
    b4s2.database: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                      reply_markup=b4s2.view_fourth_computer_menu),
    b4s2.data_communication: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                reply_markup=b4s2.view_fourth_computer_menu),
    b4s1.control_engineering: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                 reply_markup=b4s1.view_fourth_year_Menu),
    b4s2.modern_control: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                            reply_markup=b4s2.view_fourth_control_menu),
    b4s2.electrical_machines2: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                  reply_markup=b4s2.view_fourth_control_menu),
})
back_button_handlers.update({
    b4s2.process_control: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                             reply_markup=b4s2.view_fourth_control_menu),
    b4s2.microprocessors: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                             reply_markup=b4s2.view_fourth_control_menu),
    b4s1.electronics_engineering: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                     reply_markup=b4s1.view_fourth_year_Menu),
    b4s2.digital_communications: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                    reply_markup=b4s2.view_fourth_electronics_menu),
    b4s2.EM_waves: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                      reply_markup=b4s2.view_fourth_electronics_menu),
    b4s2.microprocessors: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                             reply_markup=b4s2.view_fourth_electronics_menu),
    b4s2.power_electronics: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                               reply_markup=b4s2.view_fourth_electronics_menu),
    b4s1.power_engineering: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                               reply_markup=b4s1.view_fourth_year_Menu),
    b4s2.modern_control: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                            reply_markup=b4s2.view_fourth_power_menu),
    b4s2.electrical_machines2: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                  reply_markup=b4s2.view_fourth_power_menu),
    b4s2.power_systems2: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                            reply_markup=b4s2.view_fourth_power_menu),
    b4s2.microprocessors: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                             reply_markup=b4s2.view_fourth_power_menu),
    b4s2.communication_engineering: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                       reply_markup=b4s2.view_fifth_year_menu),
    cm5.first_sem: lambda message: mybot.send_message(message.chat.id, "<<<", reply_markup=cm5.view_fifth_commu_menu),
    cm5.modules: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                    reply_markup=cm5.view_fifth_1st_sem_commu_menu),
    cm5.second_sem: lambda message: mybot.send_message(message.chat.id, "<<<", reply_markup=cm5.view_fifth_commu_menu),
    cm5.modules2: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                     reply_markup=cm5.view_fifth_2nd_sem_commu_menu),
    b4s2.computer_engineering: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                  reply_markup=b4s2.view_fifth_year_menu),
    cp5.first_sem: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                      reply_markup=cp5.view_fifth_computer_menu),
    cp5.modules: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                    reply_markup=cp5.view_fifth_1st_sem_computer_menu),
    cp5.second_sem: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                       reply_markup=cp5.view_fifth_computer_menu),
    cp5.modules2: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                     reply_markup=cp5.view_fifth_2nd_sem_computer_menu),
    b4s2.control_engineering: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                 reply_markup=b4s2.view_fifth_year_menu),
    ct5.first_sem: lambda message: mybot.send_message(message.chat.id, "<<<", reply_markup=ct5.view_fifth_control_menu),
    ct5.modules: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                    reply_markup=ct5.view_fifth_1st_sem_control_menu),
    ct5.second_sem: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                       reply_markup=ct5.view_fifth_control_menu),
    ct5.modules2: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                     reply_markup=ct5.view_fifth_2nd_sem_control_menu),
    b4s2.electronics_engineering: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                                     reply_markup=b4s2.view_fifth_year_menu),
    e5.first_sem: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                     reply_markup=e5.view_fifth_electronics_menu),
    e5.modules: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                   reply_markup=e5.view_fifth_1st_sem_electronics_menu),
    e5.second_sem: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                      reply_markup=e5.view_fifth_electronics_menu),
    e5.modules2: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                    reply_markup=e5.view_fifth_2nd_sem_electronics_menu),
    b4s2.power_engineering: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                               reply_markup=b4s2.view_fifth_year_menu),
    p5.first_sem: lambda message: mybot.send_message(message.chat.id, "<<<", reply_markup=p5.view_fifth_power_menu),
    p5.modules: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                   reply_markup=p5.view_fifth_1st_sem_power_menu),
    p5.second_sem: lambda message: mybot.send_message(message.chat.id, "<<<", reply_markup=p5.view_fifth_power_menu),
    p5.modules2: lambda message: mybot.send_message(message.chat.id, "<<<",
                                                    reply_markup=p5.view_fifth_2nd_sem_power_menu),
})


@mybot.message_handler(func=lambda message: message.text == back)
def handle_back(message):
    while len(user_state.get(message.chat.id)) > 0:
        current_state = user_state.get(message.chat.id).pop()
        if current_state in back_button_handlers:
            back_button_handlers[current_state](message)
            break


# Main Menu Handler
@mybot.message_handler(func=lambda message: message.text.strip() == "Main Menu")
def main_menu_handler(message):
    mybot.send_message(message.chat.id, "...", reply_markup=view_menu)


# Forwarding files on request
@mybot.message_handler(func=lambda message: message.text == b2s2.dynamics)
def dynamics_file(message):
    mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=2, message_thread_id=True)
    mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=6, message_thread_id=True)


# Back button handler
@mybot.message_handler(func=lambda message: message.text == back)
def handle_back(message):
    if len(user_state.get(message.chat.id)) > 0:
        current_state = user_state.get(message.chat.id).pop()
        if current_state in back_button_handlers:
            back_button_handlers[current_state](message)
            # Update the user_state when back button is pressed
            append_state(message.chat.id, current_state)


# Handler for "Modules and Guides" button of second year
@mybot.message_handler(func=lambda message: message.text == b2s2.modules)
def handle_modules_and_guides(message):
    chat_id = message.chat.id
    current_state = user_state.get(chat_id)[-1] if len(user_state.get(chat_id)) > 0 else None

    if current_state == b2s2.fundamentals_ee:
        mybot.send_message(chat_id, "Fundamentals of EE Books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=71, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=72, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=73, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=74, message_thread_id=True)
    elif current_state == b2s2.applied:
        mybot.send_message(chat_id, "Applied III Books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=37, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=38, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=46, message_thread_id=True)
    elif current_state == b2s2.dynamics:
        mybot.send_message(chat_id, "Dynamics Books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=57, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=58, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=59, message_thread_id=True)
    elif current_state == b2s2.thermodynamics:
        mybot.send_message(chat_id, "Thermodynamics Books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=65, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=62, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=63, message_thread_id=True)
    elif current_state == b2s2.probability:
        mybot.send_message(chat_id, "Probability Books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=67, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=68, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=69, message_thread_id=True)
    elif current_state == b2s2.history:
        mybot.send_message(chat_id, "History Books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=78, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=76, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=77, message_thread_id=True)

    else:
        mybot.send_message(chat_id, "Please select a subject first.")


# Handler for "Worksheets and Exams" button of second year
@mybot.message_handler(func=lambda message: message.text == b2s2.ppts)
def handle_worksheets_and_exams(message):
    chat_id = message.chat.id
    current_state = user_state.get(chat_id)[-1] if len(user_state.get(chat_id)) > 0 else None

    if current_state == b2s2.fundamentals_ee:
        mybot.send_message(chat_id, "Fundamentals of EE Exams.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=93, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=94, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=95, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=96, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=97, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=98, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=100, message_thread_id=True)


    elif current_state == b2s2.applied:
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=39)
        mybot.send_message(chat_id, "Applied III Exams.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=40, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=41, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=42, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=43, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=44, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=45, message_thread_id=True)

    elif current_state == b2s2.dynamics:
        mybot.send_message(chat_id, "Dynamics Exams.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=49, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=50, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=51, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=52, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=53, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=54, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=55, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=56, message_thread_id=True)

    elif current_state == b2s2.thermodynamics:
        mybot.send_message(chat_id, "Thermodynamics Exams.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=80, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=81, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=82, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=83, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=84, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=85, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=86, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=87, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=88, message_thread_id=True)

    elif current_state == b2s2.probability:
        mybot.send_message(chat_id, "Probability Exams.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=102, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=103, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=104, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=105, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=106, message_thread_id=True)

    elif current_state == b2s2.history:
        mybot.send_message(chat_id, "History Exams.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=89, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=90, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=91, message_thread_id=True)

    else:
        mybot.send_message(chat_id, "Please select a subject first.")


# Handler for "Modules and Guides" button of third year first semester
@mybot.message_handler(func=lambda message: message.text == b3s1.modules)
def handle_modules_and_guides(message):
    chat_id = message.chat.id
    current_state = user_state.get(chat_id)[-1] if len(user_state.get(chat_id)) > 0 else None

    if current_state == b3s1.apply_electronics:
        mybot.send_message(chat_id, "Applied Electronics I Books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=112, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=113, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=114, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=115, message_thread_id=True)


    elif current_state == b3s1.computational_methods:
        mybot.send_message(chat_id, "Computational Methods Books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=146, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=147, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=148, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=149, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=154, message_thread_id=True)

    elif current_state == b3s1.signals_systems:
        mybot.send_message(chat_id, "Signals and Systems Books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=163, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=164, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=165, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=166, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=167, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=168, message_thread_id=True)

    elif current_state == b3s1.electromagnetic_fields:
        mybot.send_message(chat_id, "Electromagnetic Fields books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=120, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=121, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=122, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=123, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=124, message_thread_id=True)
    elif current_state == b3s1.oop_java:
        mybot.send_message(chat_id, "OOP(Java) Books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=127, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=128, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=129, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=130, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=131, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=132, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=133, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=134, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=135, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=136, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=137, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=138, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=139, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=140, message_thread_id=True)


    elif current_state == b3s1.research_methods:
        mybot.send_message(chat_id, "Research Methods Books.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=171, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=172, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=173, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=174, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=175, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=176, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=177, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=178, message_thread_id=True)
    else:
        mybot.send_message(chat_id, "Please select a subject first.")


# Handler for "Worksheets and Exams" button of third year first semester
@mybot.message_handler(func=lambda message: message.text == b3s1.ppts)
def handle_worksheets_and_exams(message):
    chat_id = message.chat.id
    current_state = user_state.get(chat_id)[-1] if len(user_state.get(chat_id)) > 0 else None

    if current_state == b3s1.apply_electronics:
        mybot.send_message(chat_id, "Applied Electronics I Exams.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=116, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=117, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=118, message_thread_id=True)

    elif current_state == b3s1.computational_methods:
        mybot.send_message(chat_id, "Computational Methods Exams.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=155, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=156, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=157, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=158, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=159, message_thread_id=True)
    elif current_state == b3s1.signals_systems:
        mybot.send_message(chat_id, "Signals and Systems Exams.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=169, message_thread_id=True)
    elif current_state == b3s1.electromagnetic_fields:
        mybot.send_message(chat_id, "Electromagnetic Fields Exams.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=125, message_thread_id=True)

    elif current_state == b3s1.oop_java:
        mybot.send_message(chat_id, "OOP(Java) Exams.")
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=141, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=142, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=143, message_thread_id=True)
        mybot.forward_message(chat_id=message.chat.id, from_chat_id=CHANNEL_ID, message_id=144, message_thread_id=True)

    elif current_state == b3s1.research_methods:
        mybot.send_message(chat_id, "Research Methods Exams.")
    else:
        mybot.send_message(chat_id, "Please select a subject first.")

empty = "It's empty at moment.\n please send us anything that might be helpful for this course.\n Thank you"
# Handler for "Modules and Guides" button of third year second semester
@mybot.message_handler(func=lambda message: message.text == b3s2.modules)
def handle_modules_and_guides(message):
    chat_id = message.chat.id
    current_state = user_state.get(chat_id)[-1] if len(user_state.get(chat_id)) > 0 else None

    if current_state == b3s2.applied_electronics:
        mybot.send_message(chat_id, f"Applied Electronics {empty}")
    elif current_state == b3s2.logic_design:
        mybot.send_message(chat_id, f"Logic Design {empty}")
    elif current_state == b3s2.signal_processing:
        mybot.send_message(chat_id, f"Signal Processing {empty}")
    elif current_state == b3s2.network_analysis:
        mybot.send_message(chat_id, f"Network Analysis {empty}")
    elif current_state == b3s2.electrical_machines:
        mybot.send_message(chat_id, f"Electrical Machines {empty}")
    else:
        mybot.send_message(chat_id, "Please select a subject first.")


# Handler for "Worksheets and Exams" button of third year second semester
@mybot.message_handler(func=lambda message: message.text == b3s2.ppts)
def handle_worksheets_and_exams(message):
    chat_id = message.chat.id
    current_state = user_state.get(chat_id)[-1] if len(user_state.get(chat_id)) > 0 else None

    if current_state == b3s2.applied_electronics:
        mybot.send_message(chat_id, f"Applied Electronics {empty}")
    elif current_state == b3s2.logic_design:
        mybot.send_message(chat_id, f"Logic Design {empty}")
    elif current_state == b3s2.signal_processing:
        mybot.send_message(chat_id, f"Signal Processing {empty}")
    elif current_state == b3s2.network_analysis:
        mybot.send_message(chat_id, f"Network Analysis {empty}")
    elif current_state == b3s2.electrical_machines:
        mybot.send_message(chat_id, f"Electrical Machines {empty}")
    else:
        mybot.send_message(chat_id, "Please select a subject first.")


# Handler for "Modules and Guides" button of fourth year first semester
@mybot.message_handler(func=lambda message: message.text == b4s1.modules)
def handle_modules_and_guides(message):
    chat_id = message.chat.id
    current_state = user_state.get(chat_id)[-1] if len(user_state.get(chat_id)) > 0 else None

    if current_state == b4s1.communication_systems:
        mybot.send_message(chat_id, f"Communication Systems {empty}")
    elif current_state == b4s1.computer_architecture:
        mybot.send_message(chat_id, f"Computer Architecture {empty}")
    elif current_state == b4s1.control_systems:
        mybot.send_message(chat_id, f"Control Systems {empty}")
    elif current_state == b4s1.electrical_measurement:
        mybot.send_message(chat_id, f"Electrical Measurement {empty}")
    elif current_state == b4s1.power_systems:
        mybot.send_message(chat_id, f"Power Systems {empty}")
    else:
        mybot.send_message(chat_id, "Please select a subject first.")


# Handler for "Worksheets and Exams" button of fourth year first semester
@mybot.message_handler(func=lambda message: message.text == b4s1.ppts)
def handle_worksheets_and_exams(message):
    chat_id = message.chat.id
    current_state = user_state.get(chat_id)[-1] if len(user_state.get(chat_id)) > 0 else None

    if current_state == b4s1.communication_systems:
        mybot.send_message(chat_id, f"Communication Systems {empty}")
    elif current_state == b4s1.computer_architecture:
        mybot.send_message(chat_id, f"Computer Architecture {empty}")
    elif current_state == b4s1.control_systems:
        mybot.send_message(chat_id, f"Control Systems {empty}")
    elif current_state == b4s1.electrical_measurement:
        mybot.send_message(chat_id, f"Electrical Measurement {empty}")
    elif current_state == b4s1.power_systems:
        mybot.send_message(chat_id, f"Power Systems {empty}")
    else:
        mybot.send_message(chat_id, "Please select a subject first.")


'''
# Handler for "Modules and Guides" button of fourth year second semester for Computer Engineering
@mybot.message_handler(func=lambda message: message.text == b4s2.modulescp)
def handle_modules_and_guides(message):
    chat_id = message.chat.id
    current_state = user_state.get(chat_id)[-1] if len(user_state.get(chat_id)) > 0 else None

    if current_state == b4s2.microprocessors:
        mybot.send_message(chat_id, "You are in the Microprocessors subject.")
    elif current_state == b4s2.dsa:
        mybot.send_message(chat_id, "You are in the Data Structures and Algorithms subject.")
    elif current_state == b4s2.database:
        mybot.send_message(chat_id, "You are in the Database Systems subject.")
    elif current_state == b4s2.data_communication:
        mybot.send_message(chat_id, "You are in the Data Communication subject.")
    else:
        mybot.send_message(chat_id, "Please select a subject first.")



# Handler for "Worksheets and Exams" button of fourth year second semester for Computer Engineering
@mybot.message_handler(func=lambda message: message.text == b4s2.pptscp)
def handle_worksheets_and_exams(message):
    chat_id = message.chat.id
    current_state = user_state.get(chat_id)[-1] if len(user_state.get(chat_id)) > 0 else None

    if current_state == b4s2.microprocessors:
        mybot.send_message(chat_id, "You are in the Microprocessors subject.")
        # Add the code to handle the "Worksheets and Exams" button for the Microprocessors subject here
    elif current_state == b4s2.dsa:
        mybot.send_message(chat_id, "You are in the Data Structures and Algorithms subject.")
        # Add the code to handle the "Worksheets and Exams" button for the Data Structures and Algorithms subject here
    elif current_state == b4s2.database:
        mybot.send_message(chat_id, "You are in the Database subject.")
        # Add the code to handle the "Worksheets and Exams" button for the Database subject here
    elif current_state == b4s2.data_communication:
        mybot.send_message(chat_id, "You are in the Data Communication subject.")
        # Add the code to handle the "Worksheets and Exams" button for the Data Communication subject here
    else:
        mybot.send_message(chat_id, "Please select a subject first.")


'''


# Handler for "Contribute" button for second year
@mybot.message_handler(func=lambda message: message.text == b2s2.contribute)
def handle_contribute(message):
    mybot.send_message(message.chat.id, "Please send the file (pdf, doc, ppt) or link you want to contribute.")


# Handler for documents
@mybot.message_handler(content_types=['document'])
def handle_document(message):
    file_info = mybot.get_file(message.document.file_id)
    file_extension = os.path.splitext(message.document.file_name)[1]

    if file_extension in ['.pdf', '.doc', '.ppt', '.docx', '.pptx']:
        mybot.forward_message(chat_id=CONTRIBUTE, from_chat_id=message.chat.id, message_id=message.message_id)


# Handler for links
@mybot.message_handler(func=lambda message: message.entities is not None)
def handle_links(message):
    for entity in message.entities:
        if entity.type == "url":
            mybot.forward_message(chat_id=CONTRIBUTE, from_chat_id=message.chat.id, message_id=message.message_id)


# Handler for "Contribute" button for third year
@mybot.message_handler(func=lambda message: message.text == b3s1.contribute)
def handle_contribute(message):
    mybot.send_message(message.chat.id, "Please send the file (pdf, doc, ppt) or link you want to contribute.")


# Handler for documents
@mybot.message_handler(content_types=['document'])
def handle_document(message):
    file_info = mybot.get_file(message.document.file_id)
    file_extension = os.path.splitext(message.document.file_name)[1]

    if file_extension in ['.pdf', '.doc', '.ppt', '.docx', '.pptx']:
        mybot.forward_message(chat_id=CONTRIBUTE, from_chat_id=message.chat.id, message_id=message.message_id)


# Handler for links
@mybot.message_handler(func=lambda message: message.entities is not None)
def handle_links(message):
    for entity in message.entities:
        if entity.type == "url":
            mybot.forward_message(chat_id=CONTRIBUTE, from_chat_id=message.chat.id, message_id=message.message_id)


# Handler for "Contribute" button for fourth year
@mybot.message_handler(func=lambda message: message.text == b4s1.contribute)
def handle_contribute(message):
    mybot.send_message(message.chat.id, "Please send the file (pdf, doc, ppt) or link you want to contribute.")


# Handler for documents
@mybot.message_handler(content_types=['document'])
def handle_document(message):
    file_info = mybot.get_file(message.document.file_id)
    file_extension = os.path.splitext(message.document.file_name)[1]

    if file_extension in ['.pdf', '.doc', '.ppt', '.docx', '.pptx']:
        mybot.forward_message(chat_id=CONTRIBUTE, from_chat_id=message.chat.id, message_id=message.message_id)


# Handler for links
@mybot.message_handler(func=lambda message: message.entities is not None)
def handle_links(message):
    for entity in message.entities:
        if entity.type == "url":
            mybot.forward_message(chat_id=CONTRIBUTE, from_chat_id=message.chat.id, message_id=message.message_id)


# Handler for "Contribute" button for fifth year
@mybot.message_handler(func=lambda message: message.text == b4s2.contribute)
def handle_contribute(message):
    mybot.send_message(message.chat.id, "Please send the file (pdf, doc, ppt) or link you want to contribute.")


# Handler for documents
@mybot.message_handler(content_types=['document'])
def handle_document(message):
    file_info = mybot.get_file(message.document.file_id)
    file_extension = os.path.splitext(message.document.file_name)[1]

    if file_extension in ['.pdf', '.doc', '.ppt', '.docx', '.pptx']:
        mybot.forward_message(chat_id=CONTRIBUTE, from_chat_id=message.chat.id, message_id=message.message_id)


# Handler for links
@mybot.message_handler(func=lambda message: message.entities is not None)
def handle_links(message):
    for entity in message.entities:
        if entity.type == "url":
            mybot.forward_message(chat_id=CONTRIBUTE, from_chat_id=message.chat.id, message_id=message.message_id)


if __name__ == '__main__':
    print("Polling")
    try:
        mybot.infinity_polling()
    except Exception as e:
        print(e)
