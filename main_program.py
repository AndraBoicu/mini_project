import menu
import employees as emp

# afiseaza meniu default
menu.default()


def input_from_user(value):
    if value == 'intiger':
        while True:
            try:
                inp = int(input('> '))
            except:
                print('\n* se pot introduce doar numere intregi *\n')
                continue
            return inp

    if value == 'string':
        inp = str(input('> '))
        return inp


new_user = emp.Permissions()
id_manager = 9822
id_gestionar = 8654

# Login
while True:
    id = input_from_user('intiger')
    # verifica id in json
    user = emp.user_login(id)
    if not user:
        print('* ID-ul introdus nu exista *')
        continue
    break
# OPERATOR
if id != id_manager and id != id_gestionar:
    while True:
        menu.operator()
        oInput = input_from_user('intiger')
        # Exit
        if oInput == 2:
            print('\nB####')
            print('Y###')
            print('E##')
            break
        # Creare produs
        if oInput == 1:
            new_user.creare_produs(id)
            continue
# MANAGER
if id == id_manager:
    while True:
        menu.manager()
        mInput = input_from_user('intiger')
        # Adaugare angajat
        if mInput == 1:
            print('\n###Angajeaza operator!###')
            profile = ['User ID', 'Name', 'Surname', 'Telephone', 'Calificare']
            out = []
            for i in range(len(profile)):
                print(str(i + 1) + '. ' + profile[i] + ':')
                out.append(input_from_user('string'))
            new_user.hire(out[0], out[1], out[2], out[3], out[4])
            continue
        # Vizualizare lista angajati
        if mInput == 4:
            new_user.lista_angajati()
            continue
        # Modificare calificare
        if mInput == 3:
            calificare = ['1. electrician', '2. instalator', '3. frigotehnist']
            new_user.lista_angajati()
            print('Calificarile actuale: |' + calificare[0].upper() + '|' +
                  calificare[1].upper() + '|' + calificare[2].upper() + '|')
            print('ID-ul dorit pentru modificare calificare:')
            inp = input_from_user('intiger')
            print('Noua calificare: (1-3)')
            new_cal = input_from_user('intiger')
            if new_cal == 1:
                new_cal = 'electrician'
            elif new_cal == 2:
                new_cal = 'instalator'
            elif new_cal == 3:
                new_cal = 'frigotehnist'
            new_user.modificare_calificare(inp, new_cal)
            continue
        # Exit
        if mInput == 5:
            print('\nB####')
            print('Y###')
            print('E##')
            break

        # Stergere angajat
        if mInput == 2:
            new_user.lista_angajati()
            print('ID-ul angajatului:')
            inp = input_from_user('intiger')
            new_user.sterge_angajat(inp)
            continue
# GESTIONAR
if id == id_gestionar:
    while True:
        menu.magazioner()
        gInput = input_from_user('intiger')
        # Exit
        if gInput == 3:
            print('\nB####')
            print('Y###')
            print('E##')
            break
        # Vizualizare stock
        if gInput == 2:
            new_user.vizualizare_stock()
            continue
        # Adauga materie prima
        if gInput == 1:
            new_user.vizualizare_stock()
            print('Modifica stock pentru urmatorul material (ID):')
            add_stock = input_from_user('intiger')
            print('Cantitate: (numarul introdus se +- la stock-ul existent)')
            qty = input_from_user('intiger')
            new_user.modifica_stock(add_stock, qty)
            continue