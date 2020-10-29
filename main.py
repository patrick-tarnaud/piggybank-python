import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from imports import import_ofx
import repository.filerepo as filerepo
from ui.piggy_bank_window import PiggyBankWindow


def main():
    account = import_ofx.import_from_ofx_file('/home/patrick/Téléchargements/telechargement.ofx')
    filerepo.save([account])
    new_accounts = filerepo.load('account.sav')

    pbw = PiggyBankWindow()
    pbw.show_all()
    pbw.connect("destroy", Gtk.main_quit)
    pbw.set_content(new_accounts)

    Gtk.main()


if __name__ == '__main__':
    main()
