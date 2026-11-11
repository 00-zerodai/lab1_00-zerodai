# Kigali Road Simulation

A Python driving simulation from ALU Rwanda to the Kigali Convention Centre. The Python program controls the trip, and a local web page displays the car, road, speed, lane, and status in real time.

## Requirements

- Python 3
- A web browser
- Bash and `awk` to run the optional log analyser

The simulation uses Python's standard library; no extra Python packages are needed. Keep `road_simulation.py`, `transit_program.py`, `engine.py`, and `index.html` together in the same folder.

## Run the app

1. Open a terminal in the project folder.
2. Start the simulation:

   ```bash
   python3 road_simulation.py
   ```

   If your system uses `python` for Python 3, you can instead run `python road_simulation.py`.

3. Enter a driver name when prompted. Press Enter without a name to use `Driver`.
4. Use the road editor menu:
   - **1** appends a sign to the end of the road.
   - **2** inserts a sign at a segment position.
   - **3** replaces a sign at a segment index.
   - **4** displays the road and counts its signs.
   - **5** starts the trip.
5. When driving starts, the terminal prints a local URL, usually `http://127.0.0.1:8008`. Open that URL in a browser if it did not open automatically.
6. Return to the terminal and press Enter to begin driving. Keep the terminal and Python process running while the web page is open.
7. When the car arrives, the trip report appears in the terminal. Press Enter again to close the program.

## Road signs and driving behavior

The road is a Python list named `road` in `road_simulation.py`. Each item represents a 100-metre segment, starting at segment 0. The default road begins at ALU Rwanda and ends at the Convention Center.

Allowed signs are:

| Value | Meaning |
| --- | --- |
| `"20"` through `"100"` | Set the car's speed limit in km/h. Speed limits are stored as text. |
| `"zebra"` | Stop for 5 seconds at a pedestrian crossing. |
| `"bus"` | Move to the left lane to pass a bus in the right lane. |
| `"road"` | Plain road; no special action. |

Use the road editor to change the road while the program is running. It validates signs and asks for positions within the available range. The car accelerates by up to 5 km/h per simulation step and brakes by up to 20 km/h per step, without overshooting its target speed.

## Input and error handling

- Road signs must be `bus`, `zebra`, or a speed limit written as text from `20` to `100`. `road` is used for plain segments in the route.
- Menu and editor positions are requested within their valid ranges. Invalid text and out-of-range numbers show an explanation and are requested again.
- The road is checked before the program starts; an empty, non-list, or invalid road produces an error message instead of starting the simulation.
- If terminal input ends unexpectedly (for example, end-of-file), the program reports that the simulation stopped rather than showing a traceback.

## Log analyser (optional)

Each run appends events and the trip report to `transit_session.log` in the project folder. After a run, summarize the log with:

```bash
bash analyze_log.sh
```

The script reports the number of sessions, zebra crossing stops, lane changes, and the driver and top speed from the latest completed trip. To analyse another log file, pass its path:

```bash
bash analyze_log.sh /path/to/another.log
```

If the requested log file does not exist, the script prints an error and exits with status 1.

## Troubleshooting

- **`python3` is not found:** Try `python road_simulation.py`, or install Python 3.
- **The web page does not open:** Copy the URL printed in the terminal into your browser. The simulation server must still be running.
- **The page is not updating:** Keep the Python process open and press Enter in its terminal when prompted to start the drive.
- **The analyser says the log file is missing:** Run the simulation at least once, or pass the correct log file path to `analyze_log.sh`.
