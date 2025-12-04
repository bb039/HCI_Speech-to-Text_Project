import whisper
import os
import ttkbootstrap as ttk
import sounddevice as sd
import time
import tkinter.simpledialog as sdialog
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from scipy.io.wavfile import write

model = whisper.load_model("base")

is_recording = False
recorded_frames = []
stream = None

def browse_file():
	# Open file dialog to select audio file
	filename = filedialog.askopenfilename(
		title = "Select audio file",
		filetypes=[("Audio Files", "*.mp3 *.wav *.m4a *.flac *.ogg *.mp4")]
	)
	if filename:
		entry.delete(0, END)
		entry.insert(0, filename)

def transcribe():
	# Transcribe selected audio file using Whisper
	text_box.delete("1.0","end")

	file_path = entry.get()
	if not file_path or not os.path.isfile(file_path):
		messagebox.showerror("Error", "No valid file selected")
		return

	try:
		transcribe_btn.config(state=DISABLED)
		text_box.delete(1.0, END)
		text_box.insert(END, "Transcribing, please wait...\n")
		root.update()

		result = model.transcribe(file_path)
		transcription = result.get("text", "")

		text_box.delete(1.0, END)
		text_box.insert(END, transcription)

		save_btn.config(state=NORMAL)

	except Exception as e:
		messagebox.showerror("Error",f"Transcription failed:\n{e}")

	finally:
		transcribe_btn.config(state=NORMAL)

def record_toggle():
	global is_recording, recorded_frames, stream

	if not is_recording:
		# Start recording
		text_box.delete("1.0", END)
		text_box.insert("end","Recording... Press again to stop.\n")
		root.update()

		recorded_frames = []

		def callback(indata, frames, time, status):
			recorded_frames.append(indata.copy())

		stream = sd.InputStream(
			samplerate=44100,
			channels=1,
			callback=callback
		)
		stream.start()

		# Flip UI state
		is_recording = True
		record_btn.config(text="Stop Recording", bootstyle=DANGER)
	else:
		stream.stop()
		stream.close()

		is_recording = False
		record_btn.config(text="Record & Transcribe", bootstyle=INFO)

		if not recorded_frames:
			messagebox.showerror("Error", "No audio was captured.")

		import numpy as np
		audio_data = np.concatenate(recorded_frames, axis=0)

		filename = os.path.join(os.getcwd(), "recorded_audio.wav")
		write(filename, 44100, audio_data)

		text_box.insert("end", f"Recording saved as {filename}\n")

		entry.delete(0,"end")
		entry.insert(0,filename)

		transcribe()

def save_transcription():
	# Save transcription after transcription preview
	content = text_box.get("1.0", END).strip()

	if not content:
		messagebox.showerror("Error", "There is no transcription to save.")
		return

	save_path = filedialog.asksaveasfilename(
		title="Save Transcription",
		defaultextension=".txt",
		filetypes=[("Text files",".txt")]
	)

	if save_path:
		try:
			with open(save_path, "w", encoding="utf-8") as f:
				f.write(content)
			messagebox.showinfo("Success",f"Transcription saved to:\n{save_path}")
		except Exception as e:
			messagebox.showerror("Error",f"Failed to save:\n{e}")
root = ttk.Window(themename="cosmo")
root.title("Whisper Transcriber")

frame = ttk.Frame(root, padding=10)
frame.pack(fill=BOTH, expand=True)

browse_frame = ttk.Frame(frame)
browse_frame.grid(row=0, column=0, padx=5, pady=5)
frame.columnconfigure(0, weight=1)

entry = ttk.Entry(browse_frame, width=50)
entry.grid(row=0, column=0, padx=5, pady=5)

browse_btn = ttk.Button(browse_frame, text="Browse", bootstyle=PRIMARY, command=browse_file)
browse_btn.grid(row=0, column=1, padx=5, pady=5)

transcribe_btn = ttk.Button(frame, text="Transcribe", bootstyle=SUCCESS, command=transcribe, width=20)
transcribe_btn.grid(row=1, column=0, columnspan=2, pady=10)

text_box = ScrolledText(root, height=15, width=70, wrap="word")
text_box.pack(padx=10, pady=5, fill=BOTH, expand=True)

save_btn = ttk.Button(root, text="Save Transcription", bootstyle=PRIMARY, command=save_transcription)
save_btn.pack(pady=5)
save_btn.config(state=DISABLED)

record_btn = ttk.Button(frame, text="Record & Transcribe", bootstyle=INFO, command=record_toggle)
record_btn.grid(row=2, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
	root.mainloop()
