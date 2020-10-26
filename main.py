from imports import import_ofx
import repository.filerepo as filerepo


def main():
    account = import_ofx.import_from_ofx_file('/home/patrick/Téléchargements/telechargement.ofx')
    print ('** account and transactions loaded from ofx file')
    print(account)
    for tx in account.transactions:
        print(tx)
    filerepo.save([account])
    print ('** account and transactions loaded from ofx file')
    new_accounts = filerepo.load('account.sav')
    for acc in new_accounts:
        print(acc)
        for tx in acc.transactions:
            print(tx)


if __name__ == '__main__':
    main()
