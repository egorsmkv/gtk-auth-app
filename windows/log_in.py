# noinspection PyUnresolvedReferences
from init import Gtk, Notify, GLib
from util import show_msgbox


class LogInWindow(Gtk.Window):

    def __init__(self, title: str):
        Gtk.Window.__init__(self, title=title)

        self.set_size_request(150, 100)
        self.set_resizable(False)

        label = Gtk.Label('Please, enter your credentials in order'
                          "\n"
                          'to authorize in the application.')

        def new_sep():
            sep = Gtk.Separator()
            sep.set_margin_top(5)
            sep.set_margin_bottom(5)
            return sep

        form = Gtk.VBox(spacing=6)
        form.set_border_width(10)
        form.set_hexpand(True)

        self.email = Gtk.Entry()
        self.password = Gtk.Entry()
        self.password.set_visibility(False)

        submit_button = Gtk.Button(label="Enter")
        submit_button.connect("clicked", self.on_submit_button_clicked)

        form.pack_start(label, True, False, 0)
        form.pack_start(new_sep(), True, False, 0)
        form.pack_start(Gtk.Label('E-Mail'), True, False, 0)
        form.pack_start(self.email, True, False, 0)
        form.pack_start(Gtk.Label('Password'), True, False, 0)
        form.pack_start(self.password, True, False, 0)
        form.pack_start(new_sep(), True, False, 0)
        form.pack_end(submit_button, True, False, 0)

        self.add(form)

    def on_submit_button_clicked(self, widget):
        email = self.email.get_text()
        password = self.password.get_text()

        print('Email:', email)
        print('Password:', password)

        if '@' not in email:
            show_msgbox(self, 'You entered an incorrect e-mail')
        else:
            # authorize
            self.destroy()

    def __del__(self):
        print('deleted log in form')
