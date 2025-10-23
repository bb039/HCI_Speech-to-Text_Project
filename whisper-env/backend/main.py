from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import whisper
import uvicorn
import os
import tempfile

app = FastAPI()
model = whisper.load_model("base")

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
	if not file.filename:
		raise HTTPException(status_code=400, detail="No file uploaded")

	suffix = os.path.splitext(file.filename)[1] or ".mp3"
	with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
		tmp.write(await file.read())
		tmp_path = tmp.name

	try:
		result = model.transcribe(tmp_path)
		text = result.get("text", "")
		return {"text": text}
	except Exception as e:
		raise HTTPException(status_code=500, detail=f"Transcription failed: {e}")
	finally:
		try:
			os.remove(tmp_path)
		except Exception:
			pass

if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
