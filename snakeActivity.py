# -*- coding: utf-8 -*-
# MIT License
# 
# Copyright (c) 2016 Amar Prakash Pandey
# Copyright (c) 2018 Aidan Kahrs
# Copyright (c) 2018 Regina Locicero
# Copyright (c) 2018 Calvin Wu
# Copyright (c) 2018 Quintin Reed
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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

# import the game
import mainGame

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

def main():
    pygame.init()
    pygame.display.set_mode((1200,900), pygame.RESIZABLE) # 1200,900 is the XO's screen resolution.
    game = mainGame.main()
    game()

if __name__ == '__main__':
    main()
