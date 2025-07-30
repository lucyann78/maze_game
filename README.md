Raycaster ConectaFlores
A raycasting game featuring pink and purple aesthetics, built with Pygame. Get ready for a floral adventure!

Project Overview
This project is an implementation of a classic raycasting engine, reminiscent of Wolfenstein 3D, but with a unique and vibrant visual flair. It focuses on rendering a 3D-like maze environment and providing intuitive player controls.

Setup and Running the Game
Follow these steps to get Raycaster ConectaFlores up and running on your machine:

Clone the Repository:
If you haven't already, clone this repository to your local machine:

Bash

git clone [Your Repository URL Here]
cd maze_game
Navigate to the Project Directory:
Open your terminal and make sure you are in the maze_game folder.

Install Pygame:
Ensure you have Python installed (Python 3.x is recommended). Then, install the Pygame library:

Bash

pip install pygame
(Optional but Recommended: Consider using a virtual environment to manage dependencies: python3 -m venv venv then source venv/bin/activate before pip install pygame)

Run the Game:
Execute the main game file using Python:

Bash

python src/main.py
Alternatively, if you have made your run.sh script executable:

Bash

./run.sh
Controls
W / S: Move Forward / Backward

A / D: Strafe Left / Right

Left Arrow / Right Arrow: Rotate Camera Left / Right

M: Toggle Minimap (functionality to be implemented!)

Project Phases (Tasks)
The development of this project is structured into incremental phases, adding functionalities step-by-step:

Walls! (Initial rendering of maze walls)

Orientation (Player's initial facing direction)

Rotation (Player camera rotation)

Movement (Player's ability to move through the maze)

Ouch! (Collision detection with walls)

Parser (Loading map data from external sources)

Draw the Map (Rendering the overall maze structure)

Coding Style + Documentation (Ensuring clean code and proper explanations)

Textures (Applying visual textures to walls)

Multitasking! (Handling multiple game elements/processes concurrently)

Floor Textures (Rendering textures on the floor)

Weapons (Implementing player weaponry)

Enemies (Introducing hostile entities)

Let it Rain (Implementing weather effects)

Extra Option (Additional features beyond core requirements)

Enjoy your floral exploration!

