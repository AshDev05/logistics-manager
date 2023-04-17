
# Logistics Manager

This is a small python game made as a personal challenge. It is a management game in which you manage the Logistics department of a company.


## Documentation

### -- HOW IT WORKS --

To start the game, if you are on windows use 'launcher_win.bat' and enjoy! If you run Linux, install IDLE (sudo apt install idle / sudo pacman -S idle / etc...), then launch 'launcher_linux.sh'. If you haven't configured your USB to be able to run files, copy the game to your local disk and launch the script. Alternatively, you can run '00_SHELL.py' in any interpreter (You can use idle in terminal by executing 'idle -r ./00_SHELL.py' while in game directory)
From there, you will be presented by the welcome sentence. Run 'new_game()' to create a game save, or run 'load_game()' to load an existing game.\
A small tutorial exists if you run 'tutorial()' to get you into the game.

### -- SAVING --

Saving was implemented in version 0.0.1a-f1\
To save a game, use save()\
    >>> save()\
Note. Quitting a game saves automatically.

Loading has also been implemented in version 0.0.1a-f1
To load an existing saved game, use load_game() function and follow the instructions.

### -- FILE PROTECTION -- ALPHA USERS ONLY NOTICE

As of v.0.0.5a, the file protection hasn't been implemented. Dev is looking for a way of protecting the save files during the entire process of playing. Support will not be provided in case a file has been deleted.


### -- CHRONOLOGICAL ORDER --

In this game, you have to play chronologically. First you import, then you produce, then you export. You can also mass import, then produce and export as needed. On a side note, the shop (v0.0.2a and up) is only available from level 2 and up. BEWARE, prices are high but realistic.


## Changelog

### How to Read:

- --vx.x.xy-- --> Version Number
- z ... --> Additions/Implementations
- (!) a ... --> Change affects gameplay/saves
- b --> Fixes
- (M) c ... --> Minor Change
- (C) d ... --> Changes to the code structure

### --v.0.0.1a--
- Created the game (duh)
- Implemented basic gameplay actions
- Prepared saving system, no quitting nor saving yet
- THIS IS AN ALPHA VERSION, if you encounter bugs, let me know, we're friends


### --v0.0.1a-f1--
- Implemented saving ability
- Implemented easy-to-use functions (no more use of methods for creating nor loading a game)
- Implemented SAVING AND LOADING
- Implemented short tutorial (longer version in my to-do list) -> Ref. T.B.I.
- implemented welcoming screen
- THIS IS AN ALPHA VERSION, if you encounter bugs, let me know, we're friends


### --v0.0.2a--
- Fully implemented level system and economy
- Implemented vehicle and building shop
- Fixed many many bugs that made the game unplayable (special thanks to alpha testers)
- Fixed important mathematical errors that messed the prices up while importing and exporting
- Fixed typos and mistakes
- THIS IS AN ALPHA VERSION, if you encounter bugs, let me know, we're friends


### --v0.0.3a--
- NOW SUPPORTS LINUX
- Fixed economy
- Implemented function-based usage, DO NOT USE METHODS
- Implemented basic developer lock
- Fixed exporting when exported qty > 5
- Fixed a bug where it was possible to choose more vehicles than needed for export
- Implemented basic upkeep costs
- Bug fixes
- (M) Changed code stucture, added comments

### --v0.0.3a-m1--
- (M) New launchers for windows and Linux (game doesn't support MacOS *yet*)

### --v0.0.4a--
- Implemented INTERACTIVE TUTORIAL (tutorial())
- Implemented first achievements
- (M) Implemented Company summary (summary())

### --v0.0.5a-- **!WARNING! Old saves become incompatible, contact me if you want to keep them @🌈AshOnDscrd🌈 (They/Them)#5641**
- Implemented better storage
- (!) Rebuilt the save system
- (!) Rebuilt storage system
- (!) Rebuilt level-up system, better to start a new save than recalculate
- Fixed math errors again
- (M) Prepared for achievements and break downs (There's mystery code laying around)


## === T.B.I. (To Be Implemented) Alpha Only ===

- Setting your own prices
- Add events (vehicle/prod break down, detours...) and achievements -> postponed (implemented breakdowns v0.0.6a)
- Bank loans with interest, bankrupcy, game over (?)
- Advanced regular costs (time management etc...)
- GRAPHICAL INTERFACE
