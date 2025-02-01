from mido import MidiFile, MidiTrack, Message, MetaMessage

# Initialize a new MIDI file and track
midi = MidiFile()
track = MidiTrack()
midi.tracks.append(track)

# Define the chord progression in terms of MIDI note numbers
chords = {
   'Cm7': [48, 51, 55, 58],   # C, Eb, G, Bb
   'Fm7': [53, 56, 60, 63],   # F, Ab, C, Eb
   'G7': [55, 59, 62, 65],    # G, B, D, F
   'Abmaj7': [56, 60, 63, 67],# Ab, C, Eb, G
   'Bbmaj7': [58, 62, 65, 69] # Bb, D, F, A
}

# Rhythm settings
beats_per_chord = 4
tempo = 500000  # ~120 BPM
time_per_beat = 480  # Standard MIDI timing (ticks per beat)

# Add tempo meta message
track.append(MetaMessage('set_tempo', tempo=tempo))

# Function to add a chord
def add_chord(track, notes, duration, velocity=64):
   for note in notes:
       track.append(Message('note_on', note=note, velocity=velocity, time=0))
   for note in notes:
       track.append(Message('note_off', note=note, velocity=0, time=duration))

# Generate MIDI events
for chord_name in ['Cm7', 'Fm7', 'G7', 'Abmaj7', 'Bbmaj7', 'G7', 'Cm7', 'Fm7']:
   chord_notes = chords[chord_name]
   add_chord(track, chord_notes, time_per_beat * beats_per_chord)

# Save the MIDI file
output_path = "soul_chord_progression.mid"
midi.save(output_path)
print(f"MIDI file saved as {output_path}")
