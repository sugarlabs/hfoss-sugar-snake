# hfoss-sugar-snake
This is our final project for [RIT's HFOSS class](https://github.com/ritjoe/hfoss) in spring 2018. Our game sugar-snake is meant to be run on the Sugar operating system as an educational activity reviewing the multiplication tables for 4th grade students. It is based off of a simple snake game called [Plaked](https://github.com/amarlearning/Plaked). We are using python 3 with [pygame](https://github.com/pygame/pygame).

# Licensing
The code is under MIT license which is included in our repo. The art assets in the asset folder are under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode).

# How to Install and Run the Game

## Running the Game in Production
**If you just want to play the game these are the instructions you want to follow**; this is also the instructions you should follow if you want to distribute your own version of the game. This process will generate the .xo file necessary.
You should have Sugar running already.

First you want to open a terminal instance, (press F3 if stuck in the journal). Search for terminal to find it.

Then clone our github repo by running this command:

    git clone https://github.com/axk4545/hfoss-sugar-snake

Then cd into the root directory:

    cd hfoss-sugar-snake

Following the [Sugar Quickstart](https://github.com/FOSSRIT/sugar-quickstart), you want to run the following commands to generate an .xo file.

    ./setup genpot
    ./setup build
    ./setup dist_xo

You should now see an hfoss-snake-1.xo file when you list the contents of the folder using:

    ls -la

Now to install the .xo file run:

    sugar-install-bundle hfoss-snake-1.xo

If you restart your sugar installation you should be able to search "hfoss-snake" and be able to run the game from there.

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

