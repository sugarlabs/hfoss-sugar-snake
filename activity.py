# code your activity here
# or replace this file with your python activity file
# import statements

"""
class snakeActivity(activity.Activity):

"""


# Sugar Imports
from sugar3.activity.activity import Activity
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityButton


# Gtk Import
from gi.repository import Gtk
from gettext import gettext as _


class snakeActivity(activity.Activity):
    def __init__(self, sugar_handle):
        Activity.__init__(self, sugar_handle)

        # Create a Toolbar
        toolbar = Gtk.Toolbar()

        # Add toolbar to Sugar Activity Toolbar Space
        self.set_toolbar_box(toolbar)

        # Add Activity Button
        toolbar.insert(ActivityButton(self), -1)

        # Create & Add Separator
        separator = Gtk.SeparatorToolItem(draw=False)
        separator.set_expand(True)
        toolbar.insert(separator, -1)

        # Add Stop Button
        toolbar.insert(StopButton(self), -1)

        # Create Container
        grid = Gtk.Grid()

        # Add grid to Sugar Activity GtkWindow
        self.set_canvas(grid)

        # Show all components (otherwise none will be displayed)
        self.show_all()

        #TODO launch the game inside our window

