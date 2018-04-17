

# snakeActivity.py

from gettext import gettext as _

from gi.repository import Gtk
import pygame
from sugar3.activity import activity
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityToolbar
from gi.repository import GObject
import sugargame.canvas
import mainGame

class snakeActivity(activity.Activity):
    def __init__(self, handle):
        super(snakeActivity, self).__init__(handle)

        # Build the activity toolbar.
        self.build_toolbar()

        # Create the game instance.
        self.game = mainGame.gameClass()
       
       # Build the Pygame canvas.
        # Start the game running (self.game.run is called when the
        # activity constructor returns).
        self.game.canvas = sugargame.canvas.PygameCanvas(self,
            main=self.game.run, modules=[pygame.display, pygame.font])

        # Note that set_canvas implicitly calls read_file when
        # resuming from the Journal.
        self.set_canvas(self.game.canvas)
        self.game.canvas.grab_focus()


    def build_toolbar(self):
        toolbar_box = ToolbarBox()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        stop_button.props.accelerator = '<Ctrl><Shift>Q'
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()
        stop_button.connect('clicked', self._stop_cb)
        
        play_button = ToolButton('media-playback-start')
        play_button.props.accelerator = 'P'
        toolbar_box.toolbar.insert(play_button, -1)
        play_button.show()
        play_button.connect('clicked', self._play_cb)

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

    def read_file(self, file_path):
        score_file = open(file_path, "r")
        while score_file:
            self.score = score_file.readline()
            self.game.set_score(int(self.score))
        score_file.close()

    def write_file(self, file_path):
        score = self.game.get_score()
        f = open(file_path, 'wb')
        try:
            f.write(str(score))
        finally:
            f.close


    def _stop_cb(self, button):
        self.game.running = False
 
    def _play_cb(self, button):
        self.game.gameStarted = True
