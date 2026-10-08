# I KNOW BALL — Portable Smart Basketball Shot Counter

A beginner-friendly Python + ESP32 prototype for counting **made baskets**, not attempts or misses.

## Product goal

1. Pair the hoop sensor to a device over Bluetooth Low Energy (BLE).
2. Install the tracker on the **rear of the rim** using a detachable telescoping pole.
3. Verify accuracy with 10 layups.
4. Reset the count to zero.
5. Shoot, track makes live, and save workout sessions.

The tracker must never obstruct the basketball's path, the rim opening, or normal net movement.

## Project structure

- `app.py` — Python desktop counter with **Simulate Make**, Reset, and Save Session. Works now without hardware.
- `ble_monitor.py` — optional BLE diagnostic listener for ESP32 notifications, intended for Mac/Windows/Linux.
- `firmware/shot_tracker.ino` — experimental ESP32 Arduino firmware; counts a digital optical sensor trigger and publishes the count over BLE.
- `HARDWARE_SPEC.md` — mechanical design requirements and outstanding engineering tests.
- `requirements.txt` — Python dependency for BLE diagnostics.

## Step 1: Run the desktop prototype

In a terminal in this folder:

```bash
python3 app.py
```

Click **Simulate Make** to increment the counter, **Reset** to start a workout, and **Save Session** to store a JSON record in `sessions.json`.

On macOS, Tkinter normally comes with an appropriate Python installation. If it is missing, install a Python distribution that includes Tk support.

## Step 2: Test Bluetooth (after ESP32 is programmed)

```bash
python3 -m pip install -r requirements.txt
python3 ble_monitor.py
```

The monitor discovers a device advertised as `IKNOWBALL` and prints counter notifications. It does **not** yet update the desktop app.

## Step 3: Test optical hardware

The firmware expects a digital sensor signal on GPIO 4 (active LOW). **This is only a development assumption**, not a validated basketball detection method. Check sensor voltage and GPIO compatibility before wiring. Use 3.3 V-safe signals; do not apply 5 V directly to ESP32 GPIO.

One sensor crossing may cause repeated counts, miss off-center shots, or misread net movement. Validate detection on a safe test rig before attaching anything to a 10-foot hoop.

## Scope and status

- [x] Desktop count/reset/session-saving simulation
- [x] BLE diagnostic script and experimental ESP32 example
- [ ] Reliable made-basket detection, tested with real shots
- [ ] Universal safe rim clamp and ladder-free installation pole
- [ ] Bluetooth-connected live counter inside desktop/mobile app
- [ ] iPhone/Android app

**Safety:** Never test an unsecured prototype over people. The proposed 5/8-inch clamp fit, 50G shock tolerance, universal compatibility, sub-150g weight, and optical performance are targets requiring measurement—not verified specifications.
