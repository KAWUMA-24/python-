import tkinter as tk
from tkinter import ttk

class StudentRegistrationForm(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Student Registration Form")
        self.geometry("600x600")

        # Labels and Entry Widgets for each field
        self.create_widgets()

    def create_widgets(self):
        labels = [
            "First Name:", "Last Name:", "Age:", "Gender:", "Email:", 
            "Phone:", "Address:", "City:", "State:", "Zip Code:",
            "Previous School /Institution :","A Level Points :",  "Course :" ,"Session :"
        ]
        self.entries = {}

        for i, label in enumerate(labels):
            ttk.Label(self, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            if label =="Gender:":
                self.entries[label] = tk.StringVar()
                ttk.Combobox(self, textvariable=self.entries[label], values=["Male", "Female", "Other"]).grid(row=i, column=1, padx=10, pady=5)
            elif label =="Session :":
            
               self.entries[label] = tk.StringVar()
               ttk.Combobox(self, textvariable=self.entries[label], values=["Day", "Evening", "Weekend"]).grid(row=i, column=1, padx=10, pady=5)
            elif label=="Course :":
               self.entries[label] = tk.StringVar()
               ttk.Combobox(self, textvariable=self.entries[label], values=["DCS", "ITB", "DEE","DCE"]).grid(row=i, column=1, padx=10, pady=5)
           
           
           
            else:
                
                entry = ttk.Entry(self)
                entry.grid(row=i, column=1, padx=10, pady=5)
                self.entries[label] = entry

        # Submit Button
        ttk.Button(self, text="Submit", command=self.submit).grid(row=len(labels), column=0, columnspan=2, pady=20)

    def submit(self):
        # Retrieve the data from the entries and print them
        for key, value in self.entries.items():
            if isinstance(value, tk.StringVar):
                print(f"{key} {value.get()}")
            else:
                print(f"{key} {value.get()}")

if __name__ == "__main__":
    app = StudentRegistrationForm()
    app.mainloop()
