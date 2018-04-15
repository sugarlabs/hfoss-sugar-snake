

# DemoiselleActivity.py

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

        view_toolbar = ViewToolbar()
        view_toolbar.connect('go-fullscreen',
                self.view_toolbar_go_fullscreen_cb)
        view_toolbar.show()
        view_toolbar_button = ToolbarButton(
            page=view_toolbar,
            icon_name='toolbar-view')
        toolbar_box.toolbar.insert(view_toolbar_button, -1)
        view_toolbar_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        stop_button.props.accelerator = '<Ctrl><Shift>Q'
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

    def view_toolbar_go_fullscreen_cb(self, view_toolbar):
        self.fullscreen()

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

class ViewToolbar(Gtk.Toolbar):
    __gtype_name__ = 'ViewToolbar'

    __gsignals__ = {
        'needs-update-size': (GObject.SIGNAL_RUN_FIRST,
                              GObject.TYPE_NONE,
                              ([])),
        'go-fullscreen': (GObject.SIGNAL_RUN_FIRST,
                          GObject.TYPE_NONE,
                          ([]))
    }

    def __init__(self):
        Gtk.Toolbar.__init__(self)
        self.fullscreen = ToolButton('view-fullscreen')
        self.fullscreen.set_tooltip(_('Fullscreen'))
        self.fullscreen.connect('clicked', self.fullscreen_cb)
        self.insert(self.fullscreen, -1)
        self.fullscreen.show()

    def fullscreen_cb(self, button):
        self.emit('go-fullscreen')

