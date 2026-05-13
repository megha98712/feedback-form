import tkinter as tk
from tkinter import messagebox, ttk

def submit_feedback():
    name = entry_name.get().strip()
    rating = combo_rating.get()
    comments = text_comments.get("1.0", tk.END).strip()

    if not name or not comments:
        messagebox.showwarning("Incomplete Data", "Please fill in all the details before submitting.")
        return

    try:
        # Saving with encoding to handle special characters
        with open("feedback_logs.txt", "a", encoding="utf-8") as f:
            f.write(f"Name: {name}\nRating: {rating}\nComments: {comments}\n{'='*30}\n")
        
        messagebox.showinfo("Success", f"Thank you, {name}! Your feedback has been recorded.")
        
        # UI reset logic
        entry_name.delete(0, tk.END)
        text_comments.delete("1.0", tk.END)
        combo_rating.set("5 - Excellent") # Reset to default
    except Exception as e:
        messagebox.showerror("File Error", f"Could not save feedback: {e}")

# --- Main Window Setup ---
root = tk.Tk()
root.title("Client Feedback Portal v2.0")
root.geometry("450x550")
root.configure(bg="#f0f2f5") # Subtle grey background

# Professional Styling using ttk
style = ttk.Style()
style.configure("TLabel", background="#f0f2f5", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10, "bold"))

# Main Container Frame (Adds padding around everything)
main_frame = tk.Frame(root, bg="white", padx=30, pady=30, highlightthickness=1, highlightbackground="#d1d1d1")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# --- Title Section ---
tk.Label(main_frame, text="SHARE YOUR EXPERIENCE", bg="white", fg="#333", font=("Segoe UI", 14, "bold")).pack(pady=(0, 20))

# --- Name Field ---
ttk.Label(main_frame, text="Full Name").pack(anchor="w")
entry_name = ttk.Entry(main_frame, width=40)
entry_name.pack(fill="x", pady=(5, 15))

# --- Rating Selection (Professional Dropdown) ---
ttk.Label(main_frame, text="Overall Satisfaction").pack(anchor="w")
rating_options = ["5 - Excellent", "4 - Good", "3 - Average", "2 - Poor", "1 - Terrible"]
combo_rating = ttk.Combobox(main_frame, values=rating_options, state="readonly")
combo_rating.set(rating_options[0]) # Default to Excellent
combo_rating.pack(fill="x", pady=(5, 15))

# --- Comments Section ---
ttk.Label(main_frame, text="Detailed Feedback").pack(anchor="w")
text_comments = tk.Text(main_frame, height=6, width=40, font=("Segoe UI", 9), relief="solid", bd=1)
text_comments.pack(fill="x", pady=(5, 20))

# --- Submit Button ---
# Using standard button for easier custom coloring
btn_submit = tk.Button(main_frame, text="SUBMIT FEEDBACK", command=submit_feedback, 
                       bg="#1a73e8", fg="white", font=("Segoe UI", 10, "bold"), 
                       padx=20, pady=8, relief="flat", cursor="hand2")
btn_submit.pack(fill="x")

# Footer Note
tk.Label(main_frame, text="We value your privacy.", bg="white", fg="#888", font=("Segoe UI", 8)).pack(pady=(15, 0))

root.mainloop()