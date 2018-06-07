import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class StartCommandListBoxItemView(Gtk.ListBoxRow):
    def __init__(self, start, time, height):
        super(Gtk.ListBoxRow, self).__init__()
        self.start = start
        self.time = time
        self.height = height
        self.add(Gtk.Label(start))
        self.add(Gtk.Label(time))
        self.add(Gtk.Label(height))
