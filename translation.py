import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        source_text = source_text_box.get("1.0", tk.END).strip()
        source_lang = source_lang_combo.get()
        target_lang = target_lang_combo.get()

        if not source_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        translator = Translator()
        translated = translator.translate(source_text, src=source_lang, dest=target_lang)
        target_text_box.delete("1.0", tk.END)
        target_text_box.insert(tk.END, translated.text)

    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Source Text
source_text_label = ttk.Label(root, text="Source Text:")
source_text_label.grid(row=0, column=0, padx=10, pady=10)

source_text_box = tk.Text(root, height=10, width=40)
source_text_box.grid(row=1, column=0, padx=10, pady=10)

# Source Language
source_lang_label = ttk.Label(root, text="Source Language:")
source_lang_label.grid(row=2, column=0, padx=10, pady=10)

source_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()), state="readonly")
source_lang_combo.grid(row=3, column=0, padx=10, pady=10)
source_lang_combo.current(21)  # Default to English

# Target Language
target_lang_label = ttk.Label(root, text="Target Language:")
target_lang_label.grid(row=2, column=1, padx=10, pady=10)

target_lang_combo = ttk.Combobox(root, values=list(LANGUAGES.values()), state="readonly")
target_lang_combo.grid(row=3, column=1, padx=10, pady=10)
target_lang_combo.current(26)  # Default to Hindi

# Translate Button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Target Text
target_text_label = ttk.Label(root, text="Translated Text:")
target_text_label.grid(row=0, column=1, padx=10, pady=10)

target_text_box = tk.Text(root, height=10, width=40)
target_text_box.grid(row=1, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
