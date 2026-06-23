# Turtle Crossing

A simple arcade-style game built with Python's turtle module. Guide the turtle across the road while avoiding moving cars. The game is used to practice event handling, collision detection, and object-oriented structure in a small GUI game.

## Features
- Player-controlled turtle that moves up, down, left, and right
- Randomly spawning cars that move horizontally
- Collision detection between the turtle and cars
- Level-up mechanic: each successful crossing increases difficulty (cars move faster / spawn more often)
- Score or level display

## Gameplay / Controls
- Objective: Move the turtle from the bottom of the screen to the top without being hit by cars.
- Controls:
  - Up arrow: move up
  - Down arrow: move down
  - Left arrow: move left
  - Right arrow: move right
- Each time you reach the top, you level up and the cars speed up or spawn more frequently.
- If the turtle collides with a car, the game ends (or you lose a life, if implemented).

## Project Structure

- main.py                : game entrypoint
- player.py              : Player / Turtle class and movement
- car_manager.py         : Car spawning and movement logic
- scoreboard.py          : Score / level display
