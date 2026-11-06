import os
from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips

print("Loading audio...")
audio = AudioFileClip("voice.mp3")
audio_duration = audio.duration

print("Finding images...")
# Find all jpg files and sort them by number
image_files = [f for f in os.listdir('.') if f.endswith('.jpg')]
image_files.sort(key=lambda f: int(f.split('.')[0]))

# Calculate how long each image should stay on screen
time_per_image = audio_duration / len(image_files)
clips = []

print("Sizing images...")
for img in image_files:
    clip = ImageClip(img).set_duration(time_per_image)
    # Force the image to be vertical Shorts size (1080x1920)
    clip = clip.resize(height=1920)
    clip = clip.crop(x1=clip.w/2 - 540, y1=0, x2=clip.w/2 + 540, y2=1920)
    clips.append(clip)

print("Stitching video together...")
video = concatenate_videoclips(clips, method="compose")
video = video.set_audio(audio)

print("Saving final video...")
video.write_videofile("final_video.mp4", fps=24, codec="libx264", audio_codec="aac")
print("Done!")
