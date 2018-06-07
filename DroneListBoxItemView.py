import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DroneListBoxItemView(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))
