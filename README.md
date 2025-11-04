Code came from student development, online forums and generative AI for full product.
While generative AI was used to experiment with simple GUI development, actual creation choices were determined by student input.
Python backend development is also student driven, using online tutorials and generative AI as a guideline to show how to structure
code, it has not been relied on for full development.

The locally deployable version of the transcriber is a smaller scope than the main branch
due to difficulty in deployment to a web application using an EC2 instance. Major difficulties laid
in the limited capacity of memory for the instance and the larger memory requirements of the Whisper
API dependencies.

GUI implementation is accomplished through the use of Python's tkinter, tk, toolkit. This choice was made for ease of implementation and accessibility
out of the box. Screen has a noticeable lack of polish regarding visual fidelity. A higher quality product could be accomplished if web
deployment were not so memory intensive for the project's dependencies. Possible packages include to keep local deployment possible include:
 - PyQt6 / PySide6
 - Dear PyGui
 - ttkbootstrap
 - CustomTkinter

 Dependencies:
 - PortAudio (Sys)
 - ffmpeg (Sys)
 - PyTorch (Python)
 - OpenAI-Whisper (Python)
 - TKinter (Python)
 - TTKBootstrap (Python)
 - SoundDevice (Python)
 - scipy (Python)
