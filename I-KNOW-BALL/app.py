"""I KNOW BALL desktop counter — Phase 1 simulation (no hardware required)."""

import json
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

SESSIONS_FILE = Path(__file__).with_name("sessions.json")


class ShotCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("I KNOW BALL — Shot Counter")
        self.root.geometry("390x380")
        self.root.configure(bg="#151515")
        self.makes = 0
        self.started_at = datetime.now().astimezone()
        self.count_text = tk.StringVar(value="0")
        self.status_text = tk.StringVar(value="SIMULATION MODE — no sensor connected")

        tk.Label(root, text="I KNOW BALL", bg="#151515", fg="#ff842b",
                 font=("Arial", 23, "bold")).pack(pady=(25, 5))
        tk.Label(root, text="MADE BASKETS", bg="#151515", fg="white",
                 font=("Arial", 12)).pack()
        tk.Label(root, textvariable=self.count_text, bg="#151515", fg="white",
                 font=("Arial", 80, "bold")).pack(pady=4)
        tk.Label(root, textvariable=self.status_text, bg="#151515", fg="#bbbbbb",
                 font=("Arial", 9)).pack(pady=(0, 16))

        tk.Button(root, text="Simulate Make +1", command=self.add_make,
                  bg="#ff842b", fg="black", font=("Arial", 13, "bold"),
                  width=23).pack(pady=4)
        tk.Button(root, text="Reset Count", command=self.reset,
                  font=("Arial", 12), width=25).pack(pady=4)
        tk.Button(root, text="Save Session", command=self.save_session,
                  font=("Arial", 12), width=25).pack(pady=4)

    def add_make(self):
        self.makes += 1
        self.count_text.set(str(self.makes))

    def reset(self):
        self.makes = 0
        self.started_at = datetime.now().astimezone()
        self.count_text.set("0")

    def save_session(self):
        session = {
            "started_at": self.started_at.isoformat(timespec="seconds"),
            "saved_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "made_baskets": self.makes,
            "mode": "simulation",
        }
        try:
            if SESSIONS_FILE.exists():
                with SESSIONS_FILE.open("r", encoding="utf-8") as file:
                    sessions = json.load(file)
                if not isinstance(sessions, list):
                    raise ValueError("sessions.json must contain a list")
            else:
                sessions = []
            sessions.append(session)
            with SESSIONS_FILE.open("w", encoding="utf-8") as file:
                json.dump(sessions, file, indent=2)
        except (OSError, ValueError, json.JSONDecodeError) as exc:
            messagebox.showerror("Save failed", str(exc))
            return
        messagebox.showinfo("Session saved", f"Saved {self.makes} makes to sessions.json")


if __name__ == "__main__":
    window = tk.Tk()
    ShotCounterApp(window)
    window.mainloop()
