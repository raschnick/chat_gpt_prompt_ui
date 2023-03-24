import tkinter as tk

from request_service import generate_response


def button_click():
    prompt = text_input.get()
    response = generate_response(prompt)
    text_output.config(state=tk.NORMAL)
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, response)
    text_output.config(state=tk.DISABLED)


window = tk.Tk()
window.title('GPT-3.5 Prompt UI')

question_label = tk.Label(window, text='Enter your question here:')
question_label.config(font=('Arial', 14))
question_label.pack(pady=10, padx=10)

text_input = tk.Entry(window, width=100)
text_input.pack(padx=10, pady=10)

button = tk.Button(window, text='Enter', command=button_click)
button.pack()

question_label = tk.Label(window, text='Answer field:')
question_label.config(font=('Arial', 14))
question_label.pack(pady=10, padx=10)

text_output = tk.Text(window, width=75, height=30)
text_output.pack(padx=10, pady=10)
text_output.config(state=tk.DISABLED)

window.mainloop()
