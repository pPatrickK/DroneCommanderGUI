import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from ListBoxView import *
from StartCommandListBoxItemView import *

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Drone Commander GUI")
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.droneView = ListBoxView()
        self.box.pack_start(self.droneView, True, True, 0)
        items = ["Drone 1", "Drone 2", "Drone 4", "Drone 3"]
        for item in items:
            self.droneView.addItem(DroneListBoxItemView, item)

        self.view = Gtk.Button(label="asd")
        self.box.pack_start(self.view, True, True, 0)

        self.commandView = ListBoxView()
        self.box.pack_start(self.commandView, True, True, 0)
        items = ["Command 1", "Command 2", "Command 4", "Command 3"]
        for item in items:
            self.commandView.addItem(StartCommandListBoxItemView, item, "312", "132")

def main():
    win = MyWindow()

    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
