# noinspection PyUnresolvedReferences
from init import Gtk


class DialogAbout(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "About", parent, 0,
                            (Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(150, 100)
        self.set_resizable(False)

        box = Gtk.VBox(spacing=6)
        box.set_border_width(10)
        box.set_hexpand(True)

        msg = Gtk.Label('')
        msg.set_markup(f'It is normal text.\n<span color="red">Just a red message</span>')
        msg.set_justify(Gtk.Justification.LEFT)

        box.pack_start(msg, True, False, 0)

        area = self.get_content_area()
        area.add(box)

        self.show_all()
