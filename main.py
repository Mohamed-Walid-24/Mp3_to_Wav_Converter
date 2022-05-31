#ffmpeg must exist
import subprocess

subprocess.call(['ffmpeg', '-i', 'Moniur.mp3','Moniur.wav'])
