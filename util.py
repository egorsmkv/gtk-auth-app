# noinspection PyUnresolvedReferences
from init import Gtk
from windows.msgbox import MsgBox


def show_msgbox(parent, message):
    mbox = MsgBox(parent, message)
    response = mbox.run()

    if response == Gtk.ResponseType.OK:
        mbox.destroy()
