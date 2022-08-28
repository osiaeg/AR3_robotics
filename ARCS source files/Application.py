import tkinter as tk
from tkinter import ttk
from loguru import logger


def insert_line():
    pass


def replace_line():
    pass


def get_selected_row():
    pass


def teach_new_position():
    pass


def modify_position():
    pass


def wait_time():
    pass


def wait_input_off():
    pass


def wait_input_on():
    pass


def set_output_on():
    pass


def set_output_off():
    pass


def tab_num():
    pass


def jump_to_tab():
    pass


def get_vision():
    pass


def if_on_jump_to_tab():
    pass


def if_off_jump_to_tab():
    pass


def servo_command():
    pass


def insert_call_program():
    pass


def insert_return():
    pass


def set_teensy_port():
    pass


def set_arduino_port():
    pass


def load_program():
    pass


def delete_line():
    pass


def run_program():
    pass


def stop_program():
    pass


def step_forward():
    pass


def step_back():
    pass


def insert_register_command():
    pass


def if_register_jump_to_tab():
    pass


def insert_calibration_command():
    pass


def jog_joint_1(direction: str):
    if direction == '-':
        logger.debug(f"Move J1 reverse")
    elif direction == '+':
        logger.debug(f"Move J1 direct")


def jog_joint_2(direction: str):
    if direction == '-':
        logger.debug(f"Move J2 reverse")
    elif direction == '+':
        logger.debug(f"Move J2 direct")


def jog_joint_3(direction: str):
    if direction == '-':
        logger.debug(f"Move J3 reverse")
    elif direction == '+':
        logger.debug(f"Move J3 direct")


def jog_joint_4(direction: str):
    if direction == '-':
        logger.debug(f"Move J4 reverse")
    elif direction == '+':
        logger.debug(f"Move J4 direct")


def jog_joint_5(direction: str):
    if direction == '-':
        logger.debug(f"Move J5 reverse")
    elif direction == '+':
        logger.debug(f"Move J5 direct")


def jog_joint_6(direction: str):
    if direction == '-':
        logger.debug(f"Move J6 reverse")
    elif direction == '+':
        logger.debug(f"Move J6 direct")


def store_position():
    pass


def get_robot_position():
    pass


def x_jog_minus():
    pass


def x_jog_plus():
    pass


def y_jog_minus():
    pass


def y_jog_plus():
    pass


def z_jog_minus():
    pass


def z_jog_plus():
    pass


def rx_jog_minus():
    pass


def rx_jog_plus():
    pass


def ry_jog_minus():
    pass


def ry_jog_plus():
    pass


def rz_jog_minus():
    pass


def rz_jog_plus():
    pass


def track_jog_minus():
    pass


def track_jog_plus():
    pass


def tx_jog_minus():
    pass


def tx_jog_plus():
    pass


def ty_jog_minus():
    pass


def ty_jog_plus():
    pass


def tz_jog_minus():
    pass


def tz_jog_plus():
    pass


def trx_jog_minus():
    pass


def trx_jog_plus():
    pass


def try_jog_minus():
    pass


def try_jog_plus():
    pass


def trz_jog_minus():
    pass


def trz_jog_plus():
    pass


class Application(tk.Tk):
    APP_WIDTH = 1440
    APP_HEIGHT = 720

    def __init__(self):
        super().__init__()
        self.geometry(self._calculate_geometry())
        self.wm_title("ARCS - Annin Robotics Control Software Ver 1.0")
        self.iconbitmap('./img/AR.ico')
        self.resizable(False, False)

        self.tabs = self._create_tabs()
        self.jog_steps_status = tk.IntVar()
        self.draw_tab_1(self.tabs[0])
        self.current_steps = [12, 14, 300, 234, 34, 324]

    def _calculate_geometry(self) -> str:
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_offset = int(screen_width / 2) - int(self.APP_WIDTH / 2)
        y_offset = int(screen_height / 2) - int(self.APP_HEIGHT / 2)
        return f'{self.APP_WIDTH}x{self.APP_HEIGHT}+{x_offset}+{y_offset}'

    def _create_tabs(self) -> list:
        tabs_controller = ttk.Notebook(self, width=self.APP_WIDTH, height=self.APP_HEIGHT)
        tabs_controller.pack(padx=5, pady=5)

        tabs_name = [
            'Main Controls',
            'Calibration',
            'Inputs Outputs',
            'Registers',
            'Vision',
            'Log',
            'Info',
            'Testing',
        ]
        tabs = [ttk.Frame(self) for _ in tabs_name]

        for index, tab in enumerate(tabs):
            tabs_controller.add(tab, text=tabs_name[index])

        return tabs

    def display_steps(self):
        for i, label in enumerate(self.steps_labels):
            label['text'] = self.current_steps[i]
        # TODO:  метод должен обращаться к списку джоинтов. Из них брать поочередно занчения current_steps и
        #   записывать их в нужные Label

    def draw_tab_1(self, tab1=None):
        self.status_label = tk.Label(tab1, text="SYSTEM READY - NO ACTIVE ALARMS",
                                     bg="cornflowerblue").place(x=10, y=10)
        self.program_status_label = tk.Label(tab1, text="PROGRAM STOPPED", bg="red").place(x=20, y=150)

        # xbcStatusLab = tk.Label(tab1, text="Xbox OFF", bg="salmon")
        # xbcStatusLab.place(x=1335, y=200)

        tk.Label(tab1, text="Current Row  = ").place(x=220, y=150)
        tk.Label(tab1, font=("Arial", 6), text="Manual Program Entry").place(x=630, y=630)
        tk.Label(tab1, font=("Arial", 6), text="Input           Tab").place(x=1092, y=348)
        tk.Label(tab1, font=("Arial", 6), text="Input           Tab").place(x=1092, y=388)
        tk.Label(tab1, font=("Arial", 6), text="Register         Num (++/- -)").place(x=1077, y=467)
        tk.Label(tab1, font=("Arial", 6), text="Register             Num              Jump to Tab").place(x=1077, y=507)
        tk.Label(tab1, font=("Arial", 6), text="Number      Position").place(x=1092, y=428)
        tk.Label(tab1, text="TEENSY-3.5 COM PORT:").place(x=310, y=40)
        tk.Label(tab1, text="MEGA-2560 COM PORT:").place(x=310, y=65)
        tk.Label(tab1, text="Program:").place(x=10, y=45)
        tk.Label(tab1, text="Robot Speed    (%)").place(x=356, y=100)
        tk.Label(tab1, text="ACC(dur/speed %)").place(x=356, y=125)
        tk.Label(tab1, text="DEC(dur/speed %)").place(x=356, y=150)

        for i in range(6):
            tk.Label(tab1, font=("Arial", 18), text=f"J{i + 1}").place(x=660 + (90 * i), y=5)

        # STEPS LABELS BLUE
        step_color = "SteelBlue4"

        tk.Label(tab1, font=("Arial", 8), fg=step_color, text="/step").place(x=620, y=40)

        self.steps_labels = [tk.Label(tab1, font=("Arial", 8), fg=step_color) for _ in range(6)]
        for i, steps_label in enumerate(self.steps_labels):
            steps_label.place(x=695 + (90 * i), y=40)

        tk.Label(tab1, font=("Arial", 18), text=" X").place(x=660, y=125)
        tk.Label(tab1, font=("Arial", 18), text=" Y").place(x=750, y=125)
        tk.Label(tab1, font=("Arial", 18), text=" Z").place(x=840, y=125)
        tk.Label(tab1, font=("Arial", 18), text=" W").place(x=930, y=125)
        tk.Label(tab1, font=("Arial", 18), text=" P").place(x=1020, y=125)
        tk.Label(tab1, font=("Arial", 18), text=" R").place(x=1110, y=125)
        tk.Label(tab1, font=("Arial", 18), text="Track").place(x=1217, y=125)

        tk.Label(tab1, font=("Arial", 18), text="Tx").place(x=660, y=250)
        tk.Label(tab1, font=("Arial", 18), text="Ty").place(x=750, y=250)
        tk.Label(tab1, font=("Arial", 18), text="Tz").place(x=840, y=250)
        tk.Label(tab1, font=("Arial", 18), text="Tw").place(x=930, y=250)
        tk.Label(tab1, font=("Arial", 18), text="Tp").place(x=1020, y=250)
        tk.Label(tab1, font=("Arial", 18), text="Tr").place(x=1110, y=250)

        tk.Label(tab1, text="Current Angle:").place(x=540, y=40)
        tk.Label(tab1, text="Current Position:").place(x=540, y=160)
        tk.Label(tab1, text="Degrees to Jog:").place(x=540, y=65)
        tk.Label(tab1, text="Millimeters to Jog:").place(x=540, y=185)
        tk.Label(tab1, text="JOG ROBOT").place(x=540, y=92)
        tk.Label(tab1, text="JOG ROBOT").place(x=540, y=212)
        tk.Label(tab1, text="Millimeters to Jog:").place(x=540, y=285)
        tk.Label(tab1, text="JOG ROBOT").place(x=540, y=310)

        for i in range(5):
            tk.Label(tab1, text="=").place(x=855, y=360 + (i * 40))

        tk.Label(tab1, text="=").place(x=1355, y=360)
        tk.Label(tab1, text="=").place(x=1355, y=400)

        tk.Label(tab1, text="=").place(x=1075, y=360)
        tk.Label(tab1, text="=").place(x=1075, y=400)
        tk.Label(tab1, text="=").place(x=1075, y=440)

        tk.Label(tab1, text="=").place(x=695, y=560)
        tk.Label(tab1, text="=").place(x=1117, y=481)
        tk.Label(tab1, text="=").place(x=1117, y=561)
        tk.Label(tab1, text="=").place(x=1117, y=521)

        tk.Label(tab1, text="Stored Position  = ").place(x=542, y=400)
        tk.Label(tab1, font=("Arial", 6), text="StorePos            Element          Num (++/- -)").place(x=1077, y=547)

        # BUTTONS
        tk.Button(tab1, borderwidth=3, text="Insert", height=1, width=6, command=insert_line).place(x=1220, y=641)
        tk.Button(tab1, borderwidth=3, text="Replace", height=1, width=6, command=replace_line).place(x=1280, y=641)
        tk.Button(tab1, borderwidth=3, text="Get Selected", height=1, width=10,
                  command=get_selected_row).place(x=540, y=641)

        option_list = ["Move J", "OFFS J", "Move L", "Move A Beg", "Move A Mid", "Move A End",
                       "Move C Center", "Move C Start", "Move C Plane", "Move SP", "OFFS SP", "Teach SP"]
        options = tk.StringVar(tab1)
        options.set(option_list[0])
        tk.OptionMenu(tab1, options, *option_list).place(x=540, y=360)

        tk.Button(tab1, borderwidth=3, text="Teach New Position", height=1, width=20,
                  command=teach_new_position).place(x=540, y=440)
        tk.Button(tab1, borderwidth=3, text="Modify Position", height=1, width=20,
                  command=modify_position).place(x=540, y=480)
        tk.Button(tab1, borderwidth=3, text="Wait Time (seconds)", height=1, width=20,
                  command=wait_time).place(x=700, y=360)
        tk.Button(tab1, borderwidth=3, text="Wait Input ON", height=1, width=20,
                  command=wait_input_on).place(x=700, y=400)
        tk.Button(tab1, borderwidth=3, text="Wait Input OFF", height=1, width=20,
                  command=wait_input_off).place(x=700, y=440)
        tk.Button(tab1, borderwidth=3, text="Set Output On", height=1, width=20,
                  command=set_output_on).place(x=700, y=480)
        tk.Button(tab1, borderwidth=3, text="Set Output OFF", height=1, width=20,
                  command=set_output_off).place(x=700, y=520)
        tk.Button(tab1, borderwidth=3, text="If On Jump", height=1, width=20,
                  command=if_on_jump_to_tab).place(x=920, y=360)
        tk.Button(tab1, borderwidth=3, text="If Off Jump", height=1, width=20,
                  command=if_off_jump_to_tab).place(x=920, y=400)
        tk.Button(tab1, borderwidth=3, text="Call Program", height=1, width=20,
                  command=insert_call_program).place(x=540, y=560)

        tk.Button(tab1, borderwidth=3, text="Create Tab", height=1, width=14, command=tab_num).place(x=1240, y=360)
        tk.Button(tab1, borderwidth=3, text="Jump to Tab", height=1, width=14, command=jump_to_tab).place(x=1240, y=400)
        tk.Button(tab1, borderwidth=3, text="Get Vision", height=1, width=14, command=get_vision).place(x=1240, y=440)
        tk.Button(tab1, borderwidth=3, text="Servo", height=1, width=20, command=servo_command).place(x=920, y=440)
        tk.Button(tab1, borderwidth=3, text="Return", height=1, width=20, command=insert_return).place(x=540, y=600)

        # Set com ports
        tk.Button(tab1, borderwidth=3, text="Set Com", font=("Arial", 7), height=0, width=7,
                  command=set_teensy_port).place(x=473, y=35)
        tk.Button(tab1, borderwidth=3, text="Set Com", font=("Arial", 7), height=0, width=7,
                  command=set_arduino_port).place(x=473, y=65)

        tk.Button(tab1, borderwidth=3, text="Load Program", height=0, width=12,
                  command=load_program).place(x=202, y=42)

        tk.Button(tab1, borderwidth=3, text="Delete", height=1, width=20, command=delete_line).place(x=540, y=520)

        runProgBut = tk.Button(tab1, borderwidth=3, height=60, width=60, command=run_program)
        playPhoto = tk.PhotoImage(file="img/play-icon.gif")
        runProgBut.config(image=playPhoto, width="60", height="60")
        runProgBut.place(x=20, y=80)

        stopProgBut = tk.Button(tab1, borderwidth=3, height=60, width=60, command=stop_program)
        stopPhoto = tk.PhotoImage(file="img/stop-icon.gif")
        stopProgBut.config(image=stopPhoto, width="60", height="60")
        stopProgBut.place(x=200, y=80)

        tk.Button(tab1, borderwidth=3, text="FWD", height=3, width=4, command=step_forward).place(x=100, y=80)
        tk.Button(tab1, borderwidth=3, text="REV", height=3, width=4, command=step_back).place(x=150, y=80)

        # xboxBut = tk.Button(tab1, borderwidth=3, height=43, width=60, command=xbox)
        # xboxPhoto = tk.PhotoImage(file="img/xbox.gif")
        # xboxBut.config(image=xboxPhoto, width="60", height="43")
        # xboxBut.place(x=1330, y=140)

        tk.Button(tab1, borderwidth=3, text="Register", height=1, width=20,
                  command=insert_register_command).place(x=920, y=480)
        tk.Button(tab1, borderwidth=3, text="If Register Jump", height=1, width=20,
                  command=if_register_jump_to_tab).place(x=920, y=520)
        tk.Button(tab1, borderwidth=3, text="Auto Calibrate CMD", height=1, width=20,
                  command=insert_calibration_command).place(x=700, y=600)

        # TODO: нужно объединить функуции jog_joint_{x} в одну или две
        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3,
                  command=lambda: jog_joint_1('-')).place(x=642, y=90)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3,
                  command=lambda: jog_joint_1('+')).place(x=680, y=90)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3,
                  command=lambda: jog_joint_2('-')).place(x=732, y=90)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3,
                  command=lambda: jog_joint_2('+')).place(x=770, y=90)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3,
                  command=lambda: jog_joint_3('-')).place(x=822, y=90)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3,
                  command=lambda: jog_joint_3('+')).place(x=860, y=90)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3,
                  command=lambda: jog_joint_4('-')).place(x=912, y=90)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3,
                  command=lambda: jog_joint_4('+')).place(x=950, y=90)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3,
                  command=lambda: jog_joint_5('-')).place(x=1002, y=90)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3,
                  command=lambda: jog_joint_5('+')).place(x=1040, y=90)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3,
                  command=lambda: jog_joint_6('-')).place(x=1092, y=90)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3,
                  command=lambda: jog_joint_6('+')).place(x=1130, y=90)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=x_jog_minus).place(x=642, y=210)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=x_jog_plus).place(x=680, y=210)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=y_jog_minus).place(x=732, y=210)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=y_jog_plus).place(x=770, y=210)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=z_jog_minus).place(x=822, y=210)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=z_jog_plus).place(x=860, y=210)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=rx_jog_minus).place(x=912, y=210)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=rx_jog_plus).place(x=950, y=210)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=ry_jog_minus).place(x=1002, y=210)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=ry_jog_plus).place(x=1040, y=210)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=rz_jog_minus).place(x=1092, y=210)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=rz_jog_plus).place(x=1130, y=210)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=track_jog_minus).place(x=1212, y=210)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=track_jog_plus).place(x=1250, y=210)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=tx_jog_minus).place(x=642, y=310)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=tx_jog_plus).place(x=680, y=310)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=ty_jog_minus).place(x=732, y=310)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=ty_jog_plus).place(x=770, y=310)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=tz_jog_minus).place(x=822, y=310)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=tz_jog_plus).place(x=860, y=310)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=trx_jog_minus).place(x=912, y=310)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=trx_jog_plus).place(x=950, y=310)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=try_jog_minus).place(x=1002, y=310)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=try_jog_plus).place(x=1040, y=310)

        tk.Button(tab1, borderwidth=3, text="-", height=1, width=3, command=trz_jog_minus).place(x=1092, y=310)
        tk.Button(tab1, borderwidth=3, text="+", height=1, width=3, command=trz_jog_plus).place(x=1130, y=310)

        tk.Checkbutton(tab1, text="Jog joints in steps", variable=self.jog_steps_status).place(x=1230, y=15)

        tk.Button(tab1, borderwidth=3, text="Check Robot Position", height=1, width=20,
                  command=get_robot_position).place(x=1230, y=45)
        tk.Button(tab1, borderwidth=3, text="Stored Position", height=1, width=20,
                  command=store_position).place(x=920, y=560)

        # ENTRY FIELDS
        self.current_row_entry = tk.Entry(tab1, width=5)
        self.current_row_entry.place(x=310, y=150)

        self.command_entry = tk.Entry(tab1, width=95)
        self.command_entry.place(x=630, y=645)

        self.program_name_entry_field = tk.Entry(tab1, width=20, justify=tk.CENTER)
        self.program_name_entry_field.place(x=70, y=45)

        self.teensy_port_entry_field = tk.Entry(tab1, width=2, justify=tk.CENTER)
        self.teensy_port_entry_field.place(x=450, y=40)

        self.arduino_port_entry_field = tk.Entry(tab1, width=2, justify=tk.CENTER)
        self.arduino_port_entry_field.place(x=450, y=65)

        self.speed_entry_field = tk.Entry(tab1, width=3)
        self.speed_entry_field.place(x=465, y=100)

        self.acc_duration_entry_field = tk.Entry(tab1, width=3)
        self.acc_duration_entry_field.place(x=465, y=125)

        self.dec_duration_field = tk.Entry(tab1, width=3)
        self.dec_duration_field.place(x=465, y=150)

        self.acc_speed_field = tk.Entry(tab1, width=3)
        self.acc_speed_field.place(x=490, y=125)

        self.dec_speed_field = tk.Entry(tab1, width=3)
        self.dec_speed_field.place(x=490, y=150)

        self.wait_time_entry_field = tk.Entry(tab1, width=5)
        self.wait_time_entry_field.place(x=872, y=363)

        self.save_position_entry_field = tk.Entry(tab1, width=5)
        self.save_position_entry_field.place(x=650, y=402)

        self.wait_input_entry_field = tk.Entry(tab1, width=5)
        self.wait_input_entry_field.place(x=872, y=403)

        self.wait_input_off_entry_field = tk.Entry(tab1, width=5)
        self.wait_input_off_entry_field.place(x=872, y=443)

        self.output_on_entry_field = tk.Entry(tab1, width=5)
        self.output_on_entry_field.place(x=872, y=483)

        self.output_off_entry_field = tk.Entry(tab1, width=5)
        self.output_off_entry_field.place(x=872, y=523)

        self.tab_num_entry_field = tk.Entry(tab1, width=5)
        self.tab_num_entry_field.place(x=1375, y=363)

        self.jump_tab_entry_field = tk.Entry(tab1, width=5)
        self.jump_tab_entry_field.place(x=1375, y=403)

        self.if_on_jump_input_tab_entry_field = tk.Entry(tab1, width=5)
        self.if_on_jump_input_tab_entry_field.place(x=1092, y=363)

        self.if_on_jump_number_tab_entry_field = tk.Entry(tab1, width=5)
        self.if_on_jump_number_tab_entry_field.place(x=1132, y=363)

        self.if_off_jump_input_tab_entry_field = tk.Entry(tab1, width=5)
        self.if_off_jump_input_tab_entry_field.place(x=1092, y=403)

        self.if_off_jump_number_tab_entry_field = tk.Entry(tab1, width=5)
        self.if_off_jump_number_tab_entry_field.place(x=1132, y=403)

        self.servo_num_entry_field = tk.Entry(tab1, width=5)
        self.servo_num_entry_field.place(x=1092, y=443)

        self.servo_position_entry_field = tk.Entry(tab1, width=5)
        self.servo_position_entry_field.place(x=1132, y=443)

        self.call_program_entry_field = tk.Entry(tab1, width=22)
        self.call_program_entry_field.place(x=712, y=563)

        self.register_num_entry_field = tk.Entry(tab1, width=5)
        self.register_num_entry_field.place(x=1080, y=483)

        self.register_eq_entry_field = tk.Entry(tab1, width=5)
        self.register_eq_entry_field.place(x=1132, y=483)

        self.register_num_jmp_entry_field = tk.Entry(tab1, width=5)
        self.register_num_jmp_entry_field.place(x=1080, y=523)

        self.register_eq_jmp_entry_field = tk.Entry(tab1, width=5)
        self.register_eq_jmp_entry_field.place(x=1132, y=523)

        self.register_tab_jmp_entry_field = tk.Entry(tab1, width=5)
        self.register_tab_jmp_entry_field.place(x=1184, y=523)

        self.store_position_num_entry_field = tk.Entry(tab1, width=5)
        self.store_position_num_entry_field.place(x=1080, y=563)

        self.store_position_el_entry_field = tk.Entry(tab1, width=5)
        self.store_position_el_entry_field.place(x=1132, y=563)

        self.store_position_value_entry_field = tk.Entry(tab1, width=5)
        self.store_position_value_entry_field.place(x=1184, y=563)

        self.joint_current_angle_entry_fields = [tk.Entry(tab1, width=5) for _ in range(6)]
        for i, item in enumerate(self.joint_current_angle_entry_fields):
            item.place(x=660 + (i * 90), y=40)

        self.joint_jog_degree_entry_fields = [tk.Entry(tab1, width=5) for _ in range(6)]
        for i, item in enumerate(self.joint_jog_degree_entry_fields):
            item.place(x=660 + (i * 90), y=65)

        self.current_position_entry_fields = {
            'X': tk.Entry(tab1, width=5),
            'Y': tk.Entry(tab1, width=5),
            'Z': tk.Entry(tab1, width=5),
            'Rx': tk.Entry(tab1, width=5),
            'Ry': tk.Entry(tab1, width=5),
            'Rz': tk.Entry(tab1, width=5)
        }
        for i, (key, value) in enumerate(self.current_position_entry_fields.items()):
            value.place(x=660 + (i * 90), y=160)

        self.jog_entry_fields = {
            'X': tk.Entry(tab1, width=5),
            'Y': tk.Entry(tab1, width=5),
            'Z': tk.Entry(tab1, width=5),
            'Rx': tk.Entry(tab1, width=5),
            'Ry': tk.Entry(tab1, width=5),
            'Rz': tk.Entry(tab1, width=5)
        }
        for i, (key, value) in enumerate(self.jog_entry_fields.items()):
            value.place(x=660 + (i * 90), y=185)

        self.t_jog_entry_fields = {
            'tx': tk.Entry(tab1, width=5),
            'ty': tk.Entry(tab1, width=5),
            'tz': tk.Entry(tab1, width=5),
            'trx': tk.Entry(tab1, width=5),
            'try': tk.Entry(tab1, width=5),
            'trz': tk.Entry(tab1, width=5)
        }
        for i, (key, value) in enumerate(self.t_jog_entry_fields.items()):
            value.place(x=660 + (i * 90), y=285)

        # Track
        track_current_entry_field = tk.Entry(tab1, width=5)
        track_current_entry_field.place(x=1230, y=160)

        track_jog_entry_field = tk.Entry(tab1, width=5)
        track_jog_entry_field.place(x=1230, y=185)


def main():
    app = Application()
    logger.info("Application is started.")
    app.mainloop()


if __name__ == "__main__":
    main()
