# ✈️ Flight 247

### A Python Text-Based Aviation Emergency Simulation

Flight 247 is an interactive, command-line adventure game developed in Python. Players assume the role of an airline captain navigating a series of critical in-flight situations, where every decision influences the aircraft's risk level and ultimately determines the outcome of the flight.

The project demonstrates fundamental Python programming concepts through a decision-based simulation featuring branching storylines, input validation, risk calculations, and persistent game results.

## Features

- **Interactive Gameplay:** Navigate three chapters involving an engine emergency, flight diversion, and final approach.
- **Branching Decisions:** Player choices influence subsequent scenarios and available decisions.
- **Risk Assessment System:** Each decision contributes to a cumulative risk score.
- **Multiple Endings:** The final outcome depends on the player's accumulated risk.
- **Input Validation:** Handles invalid menu selections and validates captain names using regular expressions.
- **Replay Functionality:** Players can restart the simulation without relaunching the application.
- **JSON Data Storage:** Saves the captain's name, decisions, risk score, and final outcome to a local JSON file.
- **Console Management:** Clears the terminal between chapters for a cleaner gameplay experience.

## Technologies Used

- **Python 3** — Core application development
- **JSON** — Persistent storage of gameplay results
- **Regular Expressions (`re`)** — Input validation
- **OS Module (`os`)** — Terminal screen management

No third-party Python packages are required.

## Getting Started

### Prerequisites

- Python 3 installed on your computer
- A terminal or Python-compatible development environment

### Installation

Clone the repository:

```bash
git clone https://github.com/sjbonilla/flight-247.git
```

Navigate into the project directory:

```bash
cd flight-247
```

### Run the Game

```bash
python3 Flight247_pythonGame.py
```

Follow the on-screen instructions to enter your captain's name, make decisions, and complete the simulation.

## Gameplay Structure

The simulation consists of three chapters:

**Chapter 1 — Engine Emergency**

The player encounters an overheating engine and must determine how to respond.

**Chapter 2 — Flight Diversion**

Based on the previous decision, the captain evaluates the available flight options and whether to continue toward the original destination or divert.

**Chapter 3 — Final Approach**

The player makes the final operational decision, completing the flight scenario.

### Risk and Outcomes

Each decision contributes between 0 and 2 risk points. The cumulative score determines one of three possible outcomes:

| Total Risk | Outcome |
|---|---|
| 0–2 | Successful Landing |
| 3–4 | Emergency Landing |
| 5–6 | Aircraft Crash |

## Project Structure

```text
flight-247/
├── Flight247_pythonGame.py
└── README.md
```

During gameplay, the application also generates `flight247_results.json` to store the most recent game results.

## Programming Concepts Demonstrated

This project applies several foundational software development concepts:

- Modular programming with reusable functions
- Conditional statements and branching logic
- Loops and program flow control
- Lists and dictionaries
- Input validation and exception handling
- File handling and JSON serialization
- Basic game-state management

## Future Improvements

Potential enhancements include:

- Additional emergency scenarios and branching storylines
- A historical record of previous flights
- A leaderboard based on player performance
- More detailed aircraft systems and decision consequences
- A graphical user interface

## Author

**Steven Bonilla**

Computer Science Student

[GitHub — sjbonilla](https://github.com/sjbonilla)

---

*Flight 247 is an educational programming project and is not intended to represent real-world aviation emergency procedures.*