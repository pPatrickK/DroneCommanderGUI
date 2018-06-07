import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from DroneListBoxItemView import *

class ListBoxView(Gtk.ListBox):

    def __init__(self):
        Gtk.ListBox.__init__(self)
        self.set_selection_mode(Gtk.SelectionMode.NONE)

        # def sort_func(row_1, row_2, data, notify_destroy):
        #     return row_1.data.lower() > row_2.data.lower()
        #
        # def filter_func(row, data, notify_destroy):
        #     return False if row.data == 'Fail' else True
        #
        # self.set_sort_func(sort_func, None, False)
        # self.set_filter_func(filter_func, None, False)

    def addItem(self, TYPE, *args):
        self.add(TYPE(*args))
