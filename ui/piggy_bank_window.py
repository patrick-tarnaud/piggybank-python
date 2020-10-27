import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from model.account import Account


class PiggyBankWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PiggyBank")
        self.set_size_request(1200, 800)

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(True)
        scrolled_window.set_vexpand(True)
        
        self.textview = Gtk.TextView()
        scrolled_window.add(self.textview)
        self.add(scrolled_window)

        self.show_all()

    def set_content(self, textview: [Account]):
        s = ""
        for acc in textview:
            s += acc.__str__() + "\n"
            for tx in acc.transactions:
                s += tx.__str__() + "\n"
        textbuffer = self.textview.get_buffer()
        textbuffer.set_text(s)
