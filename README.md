# Space Invaders Clone

![Space Invaders Clone](game_package/images/Background2.jpg)

A Python-based clone of the classic Space Invaders game using Pygame.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Controls](#controls)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This is a clone of the classic Space Invaders game, developed using Python and the Pygame library. The game features simple graphics, sound effects, and multiple levels. It's a fun project to learn and practice game development using Python.

## Features

- Classic space invader gameplay
- Multiple enemy types
- Increasing difficulty with each level
- Sound effects and background music

## Installation

Follow the steps below to set up and run the game on your local machine.

### Prerequisites

Make sure you have Python installed on your machine. You can download Python from [python.org](https://www.python.org/).

You also need to have `pip`, Python's package installer, and `git` installed. If not, you can install them using:

- **For pip:**
  ```bash
  python -m ensurepip --upgrade
  ```

- **For git:**
  - **Windows:** [Git for Windows](https://git-scm.com/download/win)
  - **macOS:** [Git for macOS](https://git-scm.com/download/mac)
  - **Linux:** Use your package manager, e.g., `sudo apt-get install git`

### Clone the Repository

Open your terminal (Command Prompt, PowerShell, or Git Bash on Windows) and run the following command:

```bash
git clone https://github.com/paravsyal02/Space-invaders-clone-using-pygame.git
```

Navigate into the project directory:

```bash
cd Space-invaders-clone-using-pygame
```

### Create and Activate a Virtual Environment (Optional but Recommended)

It's recommended to use a virtual environment to manage dependencies. You can create one with:

- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Install Dependencies

With the virtual environment activated (if you created one), install the required dependencies:

```bash
pip install -r requirements.txt
```

### Change the Path for Images and Sounds (Optional)

If you plan to save the game files in a different location (e.g., `D:\First project\game_package`), make sure to update the paths for images and sounds in the code. Look for any file paths in the `Space Invaders Clone.py` and adjust them to the correct directory.

### Run the Game

To start the game, run the following command:

```bash
python game_package/Space\ Invaders\ Clone.py
```

The game window should appear, and you can start playing!

## How to Play

- Move your spaceship left or right using the arrow keys.
- Shoot lasers to destroy the enemies by pressing the spacebar.
- Avoid enemy fire and destroy all enemies to advance to the next level.

## Controls

- **Left Arrow Key:** Move left
- **Right Arrow Key:** Move right
- **Spacebar:** Shoot

## Project Structure

- **game_package/**
  - **images/**: Contains all image assets (e.g., background, player, enemies).
  - **sounds/**: Contains sound effects and background music.
  - **Space Invaders Clone.py**: Main game file.
  - **Space Invaders Clone.spec**: Configuration for building the game.
  - **dist/**: Contains the executable and other distribution files.
  - **build/**: Contains build-related files.

## Contributing

If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request. Contributions, issues, and feature requests are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

You can now copy this content into a `README.md` file in your project directory. This will help users set up the game properly, especially if they need to adjust file paths.
