# Quixo – Python Game (University Project for Educational Purposes)

<img src="https://pax.ulaval.ca/static/GLO-1901/images/quixo.jpg" style="display: block; margin-left: auto; margin-right: auto;" alt="Quixo" width="50%" height="auto">

Quixo is a Python application that allows you to play the strategic board game Quixo through the command line. The implementation uses API calls to interact with a remote game server, manages the game board and matches, and provides tools for automated testing and game manipulation. This project combines direct terminal interaction with online server integration.

## Features

- Create and manage Quixo matches via a third-party API.
- Command line interface to:
    - Start a new match.
    - Play moves and track game progression.
    - List and view existing matches.
    - Display the board and player legend dynamically.
- Modules for formatting and managing game components (board, matches, moves).
- Automated test suite to validate core functionalities.
- In-code documentation to facilitate understanding and extension.

## Project Structure

- `main.py`: Main entry point managing user interaction and orchestrating the game flow.
- `api.py`: Interface module for the game server; handles listing, creating, retrieving, and updating matches using secure RESTful calls.
- `quixo.py`: Utilities for game structure, graphical representation, command parsing, and board/player management.
- `tests.py`: Unit tests validating key formatting and game logic functions.
- `.gitignore`: Specifies files and directories to be excluded from version control.


---

This project was developed for educational purposes as part of a university course, providing a solid base for command-line gaming with API integration.



