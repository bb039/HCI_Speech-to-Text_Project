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

Update list:
### Milestone 1: 
- Team structure and role assignments set up.
- local readme set up
- currently using online model framework
### Status Rep 1:
- focus directed towards building front-end for whisper interaction
- added to dependency list
- API cost feasibility concerns
### Milestone 2:
- reframed as a generalized transcription tool due to hardware constraints in web development.
- looked at local deployment options
### Status Rep 2:
- officially moved to local deployment for cost concerns
- designing local app rather than using API means some refactoring and installing of the Whisper model.
- main functionality works at this step, just refining it.
### Status Rep 3:
- focused on having it work out-of-the-box
- researched installer approach to remove friction with installing all dependencies required.
- sculpted usability test plan for testing
### Milestone 3:
- usability test plan finished and currently testing
### Status Rep 4:
- finished implementation of installer package
- added start/stop recording for live recording
- added device selection(microphone)
### Milestone 4:
- added saving of transcription to user-chosen location
- changed colors and added responsive UI elements
- added status/error messaging and button enable/disable logic
  
