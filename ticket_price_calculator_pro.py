import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from datetime import datetime


# -------------------- Core Logic --------------------
def calculate_ticket_price(age):
    base_price = 10.00
    if age < 0:
        return None, "You haven't been born yet."
    elif age == 0:
        return None, "You have just been born."
    elif age < 18:
        return base_price * 0.5, "You are a child."
    elif age < 65:
        return base_price, "You are an adult."
    else:
        return base_price * 0.75, "You are a senior citizen."


# -------------------- Button Functions --------------------
def on_calculate():
    try:
        age = int(age_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for age.")
        return

    has_ticket = ticket_var.get()
    price, message = calculate_ticket_price(age)
    result_text = message + "\n"

    if price:
        result_text += f"🎫 Ticket Price: ${price:.2f}\n"

    if age > 0:
        if has_ticket:
            result_text += "✅ You may enter, You have a ticket."
        else:
            result_text += "❌ You need to buy a ticket first."

    result_label.config(text=result_text)
    save_button.configure(state=NORMAL)
    update_status("✅ Calculation complete. Ready to save.")


def on_clear():
    age_entry.delete(0, ttk.END)
    ticket_var.set(True)
    result_label.config(text="")
    save_button.configure(state=DISABLED)
    update_status("🧼 Cleared all fields.")


def on_save():
    result_text = result_label.cget("text")
    if not result_text:
        messagebox.showwarning("No Data", "Please calculate a result before saving.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}]\n{result_text}\n{'-'*45}\n"

    try:
        with open("ticket_results.txt", "a", encoding="utf-8") as file:
            file.write(entry)
        update_history_panel(new_entry=entry)
        messagebox.showinfo("Saved", "✅ Result successfully saved to 'ticket_results.txt'.")
        update_status(f"💾 Last saved at {timestamp}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file:\n{e}")
        update_status("❌ Error during save operation.")


def on_clear_history():
    confirm = messagebox.askyesno(
        "Confirm Clear History 🧹",
        "Are you sure you want to permanently delete all saved results?"
    )
    if not confirm:
        return

    try:
        # Delete the history file
        if os.path.exists("ticket_results.txt"):
            os.remove("ticket_results.txt")

        # Clear history display completely
        history_box.config(state=NORMAL)
        history_box.delete("1.0", ttk.END)
        history_box.insert(ttk.END, "📭 No history available.\n")
        history_box.config(state=DISABLED)
        app.update_idletasks()  # 🔥 Force instant visual refresh

        # Disable button and update status
        clear_history_btn.configure(state=DISABLED)
        update_status("🧹 History cleared successfully. Viewer refreshed.")
        messagebox.showinfo("Cleared ✅", "All history has been deleted successfully.")

    except Exception as e:
        messagebox.showerror("Error ❌", f"Could not clear history:\n{e}")
        update_status("❌ Error clearing history.")


# -------------------- History Management --------------------
def update_history_panel(new_entry=None):
    history_box.config(state=NORMAL)
    if new_entry:
        history_box.insert(ttk.END, new_entry + "\n")
    else:
        history_box.delete("1.0", ttk.END)
        try:
            with open("ticket_results.txt", "r", encoding="utf-8") as file:
                content = file.read()
                if content.strip():
                    history_box.insert(ttk.END, content)
                    clear_history_btn.configure(state=NORMAL)
                else:
                    history_box.insert(ttk.END, "📭 No history available.\n")
                    clear_history_btn.configure(state=DISABLED)
        except FileNotFoundError:
            history_box.insert(ttk.END, "📭 No history available.\n")
            clear_history_btn.configure(state=DISABLED)
    history_box.config(state=DISABLED)
    app.update_idletasks()  # ✅ Force UI update each time


# -------------------- Status Bar --------------------
def update_status(text):
    status_label.config(text=text)
    app.update_idletasks()  # Refresh label instantly


# -------------------- Window Setup --------------------
app = ttk.Window(themename="morph")
app.title("🎟️ Ticket Price Calculator — Pro Edition")
app.geometry("520x590")
app.resizable(False, False)

# -------------------- Title --------------------
title_label = ttk.Label(app, text="🎟️ Ticket Price Calculator", font=("Segoe UI", 17, "bold"))
title_label.pack(pady=10)

# -------------------- Frame for Inputs --------------------
frame = ttk.Frame(app)
frame.pack(pady=5)

age_label = ttk.Label(frame, text="Enter your age:", font=("Segoe UI", 11))
age_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

age_entry = ttk.Entry(frame, font=("Segoe UI", 11), width=10)
age_entry.grid(row=0, column=1, padx=10, pady=5)

ticket_var = ttk.BooleanVar(value=True)
ticket_checkbox = ttk.Checkbutton(frame, text="I have a ticket", variable=ticket_var)
ticket_checkbox.grid(row=1, column=0, columnspan=2, pady=5)

# -------------------- Button Frame --------------------
btn_frame = ttk.Frame(app)
btn_frame.pack(pady=8)

calculate_btn = ttk.Button(btn_frame, text="Calculate", command=on_calculate)
calculate_btn.grid(row=0, column=0, padx=10)

save_button = ttk.Button(btn_frame, text="Save Result", command=on_save, state=DISABLED)
save_button.grid(row=0, column=1, padx=10)

clear_button = ttk.Button(btn_frame, text="Clear All", command=on_clear)
clear_button.grid(row=0, column=2, padx=10)

# -------------------- Result Label --------------------
result_label = ttk.Label(app, text="", font=("Segoe UI", 11), wraplength=450, justify="left")
result_label.pack(pady=10)

# -------------------- History Viewer --------------------
history_frame = ttk.Labelframe(app, text="📜 History Viewer", padding=10)
history_frame.pack(fill=BOTH, expand=True, padx=15, pady=10)

history_box = ttk.Text(history_frame, height=8, font=("Consolas", 10))
history_box.pack(fill=BOTH, expand=True, padx=5, pady=5)
history_box.config(state=DISABLED)

clear_history_btn = ttk.Button(
    history_frame,
    text="🧹 Clear History",
    command=on_clear_history,
    state=DISABLED
)
clear_history_btn.pack(pady=5)

# -------------------- Footer & Status --------------------
footer_frame = ttk.Frame(app)
footer_frame.pack(fill=X, pady=(5, 3))

status_label = ttk.Label(
    footer_frame,
    text="Ready.",
    font=("Segue UI", 9, "italic")
)
status_label.pack(side=LEFT, padx=10)

footer_label = ttk.Label(
    footer_frame,
    text="Developed by Aminul Islam © 2025",
    font=("Segue UI", 9, "italic")
)
footer_label.pack(side=RIGHT, padx=10)

# -------------------- Run App --------------------
update_history_panel()
app.mainloop()
