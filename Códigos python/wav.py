from pydub import AudioSegment

soud = AudioSegment.from_mp3("audio.mp3")
soud.export("resultado.wav", format("wav"))

