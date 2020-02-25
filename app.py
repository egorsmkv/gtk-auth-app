import os

# noinspection PyUnresolvedReferences
from init import Gtk, Notify, GLib
from windows.about import DialogAbout
from windows.log_in import LogInWindow


# https://lazka.github.io/pgi-docs/Gtk-3.0/constants.html

def get_resource_path(rel_path):
    current_folder = os.path.dirname(__file__)
    file_rel_path = os.path.join(current_folder, rel_path)
    return os.path.abspath(file_rel_path)


class MainWindow(Gtk.Window):
    def __init__(self, title: str):
        Notify.init(title)

        Gtk.Window.__init__(self, title=title)

        self.set_icon()
        self.set_size_request(500, 200)
        self.set_resizable(False)

        app_panel = Gtk.Table(1, 2, True)

        help_text = Gtk.Label()
        help_text.set_label("Welcome to My Application!\n\n"
                            "This app is built for one purpose - log in and"
                            "\n"
                            "sign up an account."
                            "\n\n\n"
                            "URL: <a href='https://www.app.com'>www.app.com</a>.")
        help_text.set_use_markup(True)

        left_block = Gtk.Table(1, 1, True)
        left_block.attach(help_text, 0, 1, 0, 1)
        # left_block.attach(about, 0, 1, 1, 2)

        app_panel.attach(left_block, 0, 1, 0, 1)

        margin = 20
        help_text.set_margin_left(margin)
        help_text.set_margin_right(margin)
        help_text.set_margin_top(margin)
        help_text.set_margin_bottom(margin)

        login_button = Gtk.Button(label='')
        login_button.connect("clicked", self.on_log_in_clicked)
        child = login_button.get_children()[0]
        child.set_label("<b>Log in</b>")
        child.set_use_markup(True)

        sign_up_button = Gtk.Button(label="Sign up")

        auth_box = Gtk.VBox(spacing=6)
        auth_box.set_border_width(10)
        auth_box.set_hexpand(True)
        # auth_box.set_margin_top(50)

        forgot_password = Gtk.Label()
        forgot_password.set_label(
            "If you forgot the password then <a href='https://www.app.com'>reset it</a>.")
        forgot_password.set_use_markup(True)

        sep = Gtk.Separator()
        sep.set_margin_top(5)
        sep.set_margin_bottom(5)

        auth_box.pack_start(login_button, True, False, 0)
        auth_box.pack_start(sign_up_button, True, False, 0)
        auth_box.pack_start(sep, True, False, 0)
        auth_box.pack_end(forgot_password, False, False, 0)

        g = Gtk.Grid()
        g.set_valign(Gtk.Align.CENTER)
        g.attach(auth_box, 0, 0, 1, 1)

        app_panel.attach(g, 1, 2, 0, 1)

        about_button = Gtk.Button(label='About')
        about_button.connect("clicked", self.on_about_clicked)

        help_button = Gtk.Button(label='Help')
        help_button.set_margin_left(10)
        help_button.connect("clicked", self.on_about_clicked)

        bottom_panel = Gtk.Grid()
        bottom_panel.set_halign(Gtk.Align.START)
        bottom_panel.set_margin_left(20)
        bottom_panel.set_margin_bottom(20)

        bottom_panel.attach(about_button, 0, 0, 1, 1)
        bottom_panel.attach(help_button, 1, 0, 1, 1)

        all_panels = Gtk.Table(2, 1, False)
        all_panels.attach(app_panel, 0, 1, 0, 1)
        all_panels.attach(bottom_panel, 0, 1, 1, 2)

        self.add(all_panels)

        self.notify('Info', 'All is okay')

    @staticmethod
    def on_log_in_clicked(_):
        LogInWindow('Log In').show_all()

    def on_about_clicked(self, _):
        dialog = DialogAbout(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            dialog.destroy()

    def set_icon(self):
        try:
            self.set_icon_from_file(get_resource_path('icon.png'))
        except GLib.Error:
            pass

    @staticmethod
    def notify(title, text, file_path_to_icon=''):
        n = Notify.Notification.new(title, text, file_path_to_icon)
        n.show()


def run():
    win = MainWindow('My Application')
    win.connect("destroy", Gtk.main_quit)
    win.show_all()

    Gtk.main()


if __name__ == '__main__':
    run()
