#Trzaskowski Jakub - 163187
import tkinter as tk
from tkinter import messagebox
from music21 import stream, note, midi, chord
import os

def generate_music(mood):
    s = stream.Stream()

    if mood == "Wesoły":
        melody_pattern = ['C5', 'D5', 'E5', 'G5', 'A5', 'E5', 'G5', 'A5']
        bass_pattern = ['C3', 'D3', 'E3', 'G3', 'A3']
    elif mood == "Smutny":
        melody_pattern = ['C4', 'D4', 'Eb4', 'G4', 'Ab4', 'G4', 'Ab4']
        bass_pattern = ['C2', 'D2', 'Eb2', 'G2', 'Ab2']
    elif mood == "Zły":
        melody_pattern = ['E4', 'F4', 'G#4', 'B4', 'C5', 'F4', 'B4', 'C5', 'B4', 'C5']
        bass_pattern = ['E2', 'F2', 'G#2', 'B2', 'C3']
    elif mood == "Zmęczony":
        melody_pattern = ['C4', 'E4', 'G4', 'B4', 'G4', 'B4', 'E4', 'E4']
        bass_pattern = ['C2', 'E2', 'G2', 'B2']
    elif mood == "Skupiony":
        melody_pattern = ['C4', 'D4', 'F4', 'A4', 'D4', 'F4', 'D5', 'E5', 'G5']
        bass_pattern = ['C2', 'D2', 'F2', 'A2', 'D5', 'E5', 'G8']

    min_duration = 60
    note_duration = 0.25
    num_repeats = int((min_duration / note_duration) / len(melody_pattern)) + 1

    extended_melody_pattern = melody_pattern * num_repeats
    extended_bass_pattern = bass_pattern * num_repeats

    for p in extended_melody_pattern:
        s.append(note.Note(p, quarterLength=note_duration))

    for p in extended_bass_pattern:
        s.append(note.Note(p, quarterLength=note_duration))

    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') # Windows
    music_folder_path = os.path.join(desktop_path, 'Python_music')

    if not os.path.exists(music_folder_path):
        os.makedirs(music_folder_path)

    file_path = os.path.join(music_folder_path, f'{mood}_music.mid')

    mf = midi.translate.music21ObjectToMidiFile(s)
    mf.open(file_path, 'wb')
    mf.write()
    mf.close()

    messagebox.showinfo("Informacja", f"Muzyka została wygenerowana i zapisana jako '{file_path}'.")
    print(f"Plik zapisano w: {file_path}")

def on_button_click(mood):
    generate_music(mood)

root = tk.Tk()
root.title("Generator muzyczki - Trzaskowski Jakub - nr.albumu:163187")

root.geometry("600x600")

root.configure(bg="orange")

label = tk.Label(root, text="Wybierz w jakim nastroju chcesz utworzyc muzyczkę:", bg="orange", fg="black", font=("Helvetica", 17))
label.pack(pady=20)

moods = ["Wesoły", "Smutny", "Zły", "Zmęczony", "Skupiony"]
for mood in moods:
    button = tk.Button(root, text=mood, command=lambda m=mood: on_button_click(m), bg="black", fg="orange", font=("Helvetica", 16), width=20)
    button.pack(pady=10)

root.mainloop()