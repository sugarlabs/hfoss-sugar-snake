# hfoss-sugar-snake
This is our final project for [RIT's HFOSS class](https://github.com/ritjoe/hfoss) in spring 2018. Our game sugar-snake is meant to be run on the Sugar operating system as an educational activity reviewing the multiplication tables for 4th grade students. It is based off of a simple snake game called [Plaked](https://github.com/amarlearning/Plaked).

# Licensing
The code is under MIT license which is included in our repo. The art assets in the asset folder are under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode).

# How to Install and Run the Game

## For Development
Run Sugar on VirtualBox. Most of us use Fedora based sugar. Make sure to remember to do a liveinst from the terminal so you have persistence on your VM.

Press F3 to go to the main menu if stuck in journal page.

Click on the search bar and search for terminal.

In the terminal run 

    git clone https://github.com/axk4545/hfoss-sugar-snake

Then cd into the root directory:

    cd hfoss-sugar-snake

To run the game run

    sugar-activity snakeActivity.snakeActivity

Note: any changes you make will show up when re-running the previous command.
