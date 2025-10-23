import React, { useState } from 'react'

export default function App() {
	const [file, setFile] = useState(null)
	const [transcript, setTranscript] = useState('')
	const [loading, setLoading] = useState(false)
	const [error, setError] = useState(null)

	async function handleUpload(e) {
		e.preventDefault()
		setError(null)
		if (!file) return setError('Please select a file')

		const form = new FormData()
		form.append('file',file)

		try {
			setLoading(true)
			const res = await fetch('https://localhost:8000/transcribe', {
				method: 'POST',
				body: form,
			})
			if (!res.ok) {
				const err = await res.json()
				throw new Error(err.detail || 'Transcription failed')
			}
			const data = await res.json()
			setTranscript(data.text || '')
		}
		catch (err) {
			setError(err.message)
		}
		finally {
			setLoading(false)
		}
	}
	function downloadTranscript() {
		const blob = new Blob([transcript], { type: 'text/plain' })
		const url = URL.createObjectURL(blob)
		const a = document.createElement('a')
		a.href = url
		a.download = (file ? file.name.replace(/\.[^.]+$/, '') : 'transcript') + '.txt'
		a.click()
		URL.revokeObjectURL(url)
	}
	
	return (
		<div style={{ maxWidth: 720, margin: '40px auto', fontFamily: 'sans-serif' }}>
			<h1>Audio Transcription</h1>
			<form onSubmit={handleUpload}>
				<div>
					<input
						type="file"
						accept="audio/*"
						onChange={(e) => setFile(e.target.files?.[0] ?? null)}
					/>
				</div>
				<div style={{ marginTop: 12 }}>
					<button type="submit" disabled={loading}>
						{loading ? 'Transcribing...' : 'Upload & Transcribe'}
					</button>
				</div>
			</form>
			
			{error && <div style={{ marginTop: 12 color: 'crimson' }}>{error}</div>}
			
			{transcript && (
				<div style={{ marginTop: 20 }}>
					<h3>Transcript</h3>
					<textarea
						value={transcript}
						readOnly
						rows={12}
						style={{ width: '100%', whiteSpace: 'pre-wrap' }}
					/>
					<div style={{ marginTop: 8 }}>
						<button onClick={downloadTranscript}>Download .txt</button>
					</div>
				</div>
			)}
		</div>
	)
}
