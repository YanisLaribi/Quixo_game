Quixo – Interactive Online Game (University Python Project)
<img src="https://pax.ulaval.ca/static/GLO-1901/images/quixo.jpg" style="display: block; margin-left: auto; margin-right: auto;" alt="Quixo" width="50%" height="auto">
Quixo is a Python application that lets you play the strategic game of Quixo from the command line. It uses API calls to communicate with an online game server, manages the game board and match states, and provides tools for automated testing and game management. This project blends direct terminal interaction with real-time server integration.

Features
Creation and management of Quixo games using a third-party API.

Command line interface for:

Starting a new game.

Playing moves and tracking game progress.

Listing and viewing existing games.

Displaying the board and player legend in real time.

Modules for formatting and handling game elements (board, games, moves).

Automated test suite to ensure core modules work properly.

In-code documentation for easy onboarding and extension.

Project Structure
main.py: Main entry point, manages user interaction and coordinates the flow of a Quixo match.

api.py: Server interface module; lists, creates, retrieves, and modifies games via secure REST calls.

quixo.py: Utility functions for game structure and graphical representation, command parsing, player and board management.

tests.py: Unit tests for key formatting and manipulation functions of Quixo.

file.gitignore: List of files to ignore in version control.
