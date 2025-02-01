# Music Generation Project

This project generates MIDI files for chord progressions and melodies using Python and the `mido` library.

## Project Structure

- `chords/`: Contains the script and Dockerfile for generating chord progressions.
- `melody/`: Contains the script and Dockerfile for generating melodies.
- `requirements.txt`: Lists the Python dependencies for the project.

## Requirements

- Docker
- Python 3.9 (if running locally)
- `mido` library (specified in `requirements.txt`)

## Building and Running the Docker Containers

### Chord Progression

1. Navigate to the `chords` directory:
    ```sh
    cd chords
    ```

2. Build the Docker image:
    ```sh
    docker build -t chords-image -f Dockerfile.chords .
    ```

3. Run the Docker container:
    ```sh
    docker run --rm -v $(pwd):/app chords-image
    ```

### Melody Generation

1. Navigate to the `melody` directory:
    ```sh
    cd melody
    ```

2. Build the Docker image:
    ```sh
    docker build -t melody-image -f Dockerfile.melody .
    ```

3. Run the Docker container:
    ```sh
    docker run --rm -v $(pwd):/app melody-image
    ```

## Running Locally

1. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the chord progression script:
    ```sh
    python chords/chord_progression.py
    ```

3. Run the melody generation script:
    ```sh
    python melody/generate_melody.py
    ```

## Output

- The chord progression script generates a MIDI file named `soul_chord_progression.mid` in the [chords](http://_vscodecontentref_/7) directory.
- The melody generation script generates a MIDI file named [neo_soul_melody.mid](http://_vscodecontentref_/8) in the [melody](http://_vscodecontentref_/9) directory.

## License

This project is licensed under the MIT License.