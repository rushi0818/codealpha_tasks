import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        translator = Translator()
        src_lang = source_lang_combo.get()
        dest_lang = target_lang_combo.get()
        text = source_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return
        
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        target_text.delete("1.0", tk.END)
        target_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x400")
root.resizable(False, False)

# Labels and Text Areas
tk.Label(root, text="Enter Text:").pack(pady=5)
source_text = tk.Text(root, height=5, width=60)
source_text.pack()

# Language Selection
lang_list = list(LANGUAGES.keys())
tk.Label(root, text="From Language:").pack()
source_lang_combo = ttk.Combobox(root, values=lang_list, width=20)
source_lang_combo.pack()
source_lang_combo.set("auto")

tk.Label(root, text="To Language:").pack()
target_lang_combo = ttk.Combobox(root, values=lang_list, width=20)
target_lang_combo.pack()
target_lang_combo.set("english")

# Translate Button
translate_btn = tk.Button(root, text="Translate", command=translate_text)
translate_btn.pack(pady=10)

# Output Text Area
tk.Label(root, text="Translated Text:").pack()
target_text = tk.Text(root, height=5, width=60)
target_text.pack()

# Run GUI
root.mainloop()
