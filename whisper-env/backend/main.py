import whisper
import os
import tkinter as tk
from tkinter import filedialog, messagebox

model = whisper.load_model("base")

def browse_file():
	"""Open a file dialog to select an audio file."""
	filename = filedialog.askopenfilename(
		title = "Select audio file",
		filetypes=[("Audio Files", "*.mp3 *.wav *.m4a *.flac *.ogg *.mp4")]
	)
	if filename:
		entry.delete(0, tk.END)
		entry.insert(0, filename)

def transcribe():
	"""Transcribe the selected audio file using Whisper."""
	file_path = entry.get()
	if not file_path or not os.path.isfile(file_path):
		messagebox.showerror("Error", "No valid file selected")
		return

	try:
		transcribe_btn.config(state=tk.DISABLED)
		text_box.delete(1.0, tk.END)
		text_box.insert(tk.END, "Transcribing, please wait...\n")
		root.update()

		result = model.transcribe(file_path)
		transcription = result.get("text", "")

		text_box.delete(1.0, tk.END)
		text_box.insert(tk.END, transcription)

		save_path = os.path.join(os.path.dirname(file_path), "transcription.txt")
		with open(save_path, "w", encoding="utf-8") as f:
			f.write(transcription)
		messagebox.showinfo("Success", f"Transcription saved to:\n{save_path}")

	except Exception as e:
		messagebox.showerror("Error",f"Transcription failed:\n{e}")

	finally:
		transcribe_btn.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Whisper Transcriber")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=50)
entry.grid(row=0, column=0, padx=5, pady=5)

browse_btn = tk.Button(frame, text="Browse", command=browse_file)
browse_btn.grid(row=0, column=1, padx=5, pady=5)

transcribe_btn = tk.Button(frame, text="Transcribe", command=transcribe, width=20)
transcribe_btn.grid(row=1, column=0, columnspan=2, pady=10)

text_box = tk.Text(root, height=15, width=70)
text_box.pack(padx=10, pady=5)

if __name__ == "__main__":
	root.mainloop()
