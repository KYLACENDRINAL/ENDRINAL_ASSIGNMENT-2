import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class QuestionnaireApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Questionnaire")
        self.window.geometry("400x300")

        # set_up_variables
        self.first_name_var = tk.StringVar()
        self.middle_initial_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.barangay_var = tk.StringVar()
        self.municipality_var = tk.StringVar()
        self.province_var = tk.StringVar()

        # create_and_place_components
        self.tabControl = ttk.Notebook(window)

        # name_tab
        self.name_tab = ttk.Frame(self.tabControl)
        self.setup_name_tab()
        self.tabControl.add(self.name_tab, text="Name")

        # age_tab
        self.age_tab = ttk.Frame(self.tabControl)
        self.setup_age_tab()
        self.tabControl.add(self.age_tab, text="Age")

        # address_tab
        self.address_tab = ttk.Frame(self.tabControl)
        self.setup_address_tab()
        self.tabControl.add(self.address_tab, text="Address")

        # result_tab
        self.result_tab = ttk.Frame(self.tabControl)
        self.setup_result_tab()
        self.tabControl.add(self.result_tab, text="Thank You")

        self.tabControl.pack(expand=1, fill="both")

        self.tabControl.bind("<<NotebookTabChanged>>", self.tab_changed)

        # next_button
        self.next_button = ttk.Button(window, text="Next", command=self.next_tab, state=tk.DISABLED)
        self.next_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # back_button
        self.back_button = ttk.Button(window, text="Back", command=self.prev_tab, state=tk.DISABLED)
        self.back_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # clear_button
        self.clear_button = ttk.Button(window, text="Clear", command=self.clear_form)
        self.clear_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # bind_the_closing_event_to_on_closing_function
        window.protocol("WM_DELETE_WINDOW", self.on_closing)

        # bind_enter_key_press_events
        self.window.bind("<Return>", self.enter_pressed)

        # hide_the_"Thank You"_tab
        self.tabControl.hide(3)

    def setup_name_tab(self):
        label = tk.Label(self.name_tab, text="Enter your name:")
        label.pack(pady=10)

        first_name_label = tk.Label(self.name_tab, text="First Name:")
        first_name_label.pack()
        first_name_entry = tk.Entry(self.name_tab, textvariable=self.first_name_var)
        first_name_entry.pack()
        middle_initial_label = tk.Label(self.name_tab, text="Middle Initial:")
        middle_initial_label.pack()
        middle_initial_entry = tk.Entry(self.name_tab, textvariable=self.middle_initial_var)
        middle_initial_entry.pack()

        last_name_label = tk.Label(self.name_tab, text="Last Name:")
        last_name_label.pack()
        last_name_entry = tk.Entry(self.name_tab, textvariable=self.last_name_var)
        last_name_entry.pack()

    def setup_age_tab(self):
        label = tk.Label(self.age_tab, text="Enter your age:")
        label.pack(pady=10)

        age_label = tk.Label(self.age_tab, text="Age:")
        age_label.pack()
        age_entry = tk.Entry(self.age_tab, textvariable=self.age_var)
        age_entry.pack()

    def setup_address_tab(self):
        label = tk.Label(self.address_tab, text="Enter your address:")
        label.pack(pady=10)

        barangay_label = tk.Label(self.address_tab, text="Barangay:")
        barangay_label.pack()
        barangay_entry = tk.Entry(self.address_tab, textvariable=self.barangay_var)
        barangay_entry.pack()

        municipality_label = tk.Label(self.address_tab, text="Municipality:")
        municipality_label.pack()
        municipality_entry = tk.Entry(self.address_tab, textvariable=self.municipality_var)
        municipality_entry.pack()

        province_label = tk.Label(self.address_tab, text="Province:")
        province_label.pack()
        province_entry = tk.Entry(self.address_tab, textvariable=self.province_var)
        province_entry.pack()

    def setup_result_tab(self):
        label = tk.Label(self.result_tab, text="Thank you for responding! Have a nice day.")
        label.pack(pady=10)

    def tab_changed(self, event):
        # Disable next button on the last tab
        current_tab = self.tabControl.index("current")
        next_button_state = tk.NORMAL if current_tab < 3 else tk.DISABLED
        self.next_button.config(state=next_button_state)

        # Disable back button on the first tab
        back_button_state = tk.NORMAL if current_tab > 0 else tk.DISABLED
        self.back_button.config(state=back_button_state)

    def next_tab(self, event=None):
        current_tab = self.tabControl.index("current")
        if current_tab < 3:
            if self.validate_answers(current_tab):
                self.tabControl.select(current_tab + 1)

    def prev_tab(self, event=None):
        current_tab = self.tabControl.index("current")
        if current_tab > 0:
            self.tabControl.select(current_tab - 1)

    def validate_answers(self, tab_index):
        # You can add validation logic here for each tab
        return True

    def clear_form(self):
        # Clear all entry fields
        for var in [self.first_name_var, self.middle_initial_var, self.last_name_var,
                    self.age_var, self.barangay_var, self.municipality_var, self.province_var]:
            var.set("")

    def enter_pressed(self, event):
        # Handle Enter key press events, you can implement logic if needed
        pass

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.window.destroy()

# Create the main window
root = tk.Tk()
app = QuestionnaireApp(root)

# Start the main loop
root.mainloop()

