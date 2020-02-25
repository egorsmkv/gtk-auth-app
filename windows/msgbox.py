# noinspection PyUnresolvedReferences
from init import Gtk, Notify, GLib


class MsgBox(Gtk.Dialog):
    def __init__(self, parent, message):
        Gtk.Dialog.__init__(self, "Error", parent, 0,
                            (Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(150, 100)
        self.set_resizable(False)

        box = Gtk.VBox(spacing=6)
        box.set_border_width(10)
        box.set_hexpand(True)

        msg = Gtk.Label('')
        msg.set_markup(f'<span color="red">{message}</span>')
        msg.set_justify(Gtk.Justification.CENTER)

        box.pack_start(msg, True, False, 0)

        area = self.get_content_area()
        area.add(box)

        self.show_all()
