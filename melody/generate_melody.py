from mido import Message, MidiFile, MidiTrack

# Create a new MIDI file for the melody
melody_mid = MidiFile()
melody_track = MidiTrack()
melody_mid.tracks.append(melody_track)

# Define timing constants for the melody
ticks_per_beat = melody_mid.ticks_per_beat
note_duration = ticks_per_beat // 2  # Each note lasts half a beat

# Define melody notes with their timing and velocity
melody = [
    # Over Dm9
    (69, 64, 0),  # A
    (72, 64, note_duration),  # C
    (76, 64, note_duration),  # E
    (77, 64, note_duration),  # F
    (74, 64, note_duration),  # D
    # Over Gm9
    (70, 64, note_duration),  # Bb
    (74, 64, note_duration),  # D
    (69, 64, note_duration),  # A
    (67, 64, note_duration),  # G
    (65, 64, note_duration),  # F
    # Over Cm9
    (63, 64, note_duration),  # Eb
    (67, 64, note_duration),  # G
    (74, 64, note_duration),  # D
    (65, 64, note_duration),  # F
    (72, 64, note_duration),  # C
    # Over Fm9
    (68, 64, note_duration),  # Ab
    (72, 64, note_duration),  # C
    (79, 64, note_duration),  # G
    (75, 64, note_duration),  # Eb
    (77, 64, note_duration),  # F
]

# Add melody notes to the track
for note, velocity, duration in melody:
    melody_track.append(Message('note_on', note=note, velocity=velocity, time=0))
    melody_track.append(Message('note_off', note=note, velocity=0, time=duration))

# Save the melody MIDI file
melody_mid.save("neo_soul_melody.mid")
