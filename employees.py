import json


def user_login(userId):
    with open('employees.json') as f:
        data = json.load(f)
        f.close()
    for item in data['em']:
        if item.get('userId') == userId:
            return True
    return False


class Permissions:
    def __init__(self):
        pass

    def hire(self, userID, name, surname, telephone, calificare):
        with open('employees.json') as f:
            data = json.load(f)
            f.close()

        out = {
            "userId": int(userID),
            "name": name,
            "surname": surname,
            "telephone": telephone,
            "functie": "operator",
            "calificare": calificare
        }

        data['em'].append(out)
        with open('employees.json', 'w') as output:
            json.dump(data, output, indent=4)
            output.close()
        print('###Angajat adaugat cu succes!###\n')

    def lista_angajati(self):
        with open('employees.json') as f:
            data = json.load(f)
            f.close()

        # tabel
        space = '{:<8}{:<18}{:<10}'
        print('\n#################################')
        print(space.format('ID', 'Nume', 'Calificare'))
        for item in data['em']:
            if item.get('functie') == 'operator':
                left_aligned = str(item.get('userId'))
                center = str(item.get('name')) + ' ' + str(item.get('surname'))
                right_aligned = str(item.get('calificare')).upper()
                print(space.format(left_aligned, center, right_aligned))
        print('#################################\n')

    def modificare_calificare(self, inp, new_cal):
        with open('employees.json') as f:
            data = json.load(f)
            f.close()
        for item in data['em']:
            if item['userId'] == int(inp):
                item['calificare'] = new_cal
                with open('employees.json', 'w') as output:
                    json.dump(data, output, indent=4)
                    output.close()
                print('Calificare noua pentru: [' + str(item.get('userId')) +
                      '] ' + item.get('name') + ' ' + item.get('surname') +
                      ' ==> ' + item.get('calificare').upper() + '\n')

    def sterge_angajat(self, inp):
        count = 0
        with open('employees.json') as f:
            data = json.load(f)
            f.close()
        for item in data['em']:
            count += 1
            if item.get('userId') == int(inp):
                del data['em'][count - 1]
                with open('employees.json', 'w') as output:
                    json.dump(data, output, indent=4)
                    output.close()
                print('Anjajatul: ' + str(item.get('userId')) +
                      ' ' + item.get('name') + ' ' + item.get('surname') +
                      ' a fost sters!\n')

    def vizualizare_stock(self):
        count = 0
        with open('warehouse.json') as f:
            data = json.load(f)
            f.close()

        # tabel
        space = '{:<5}{:<12}{:<5}'
        print('\n#################################')
        print(space.format('id', 'material', 'qty'))
        for item in data.keys():
            count += 1
            left_aligned = str(count) + '.'
            center = item
            right_aligned = data[item]
            print(space.format(left_aligned, center, right_aligned))
        print('#################################\n')

    def modifica_stock(self, add_stock, qty):
        count = 0
        with open('warehouse.json') as f:
            data = json.load(f)
            f.close()
        for item in data.keys():
            count += 1
            if count == add_stock:
                data[item] += qty
                with open('warehouse.json', 'w') as output:
                    json.dump(data, output, indent=4)
                    output.close()
                print('Stock modificat pentru: ->' + item.upper() + '<- cantitate '
                                                                    'noua: ' + str(data[item]) + '\n')

    def creare_produs(self, id):
        with open('warehouse.json') as f:
            warehouse = json.load(f)
            f.close()
        with open('consumption.json') as f:
            consumption = json.load(f)
            f.close()
        with open('employees.json') as f:
            user = json.load(f)
            f.close()

        for item in user['em']:
            if item.get('userId') == id:
                prenume = item.get('name')
                nume = item.get('surname')
                calificare = item.get('calificare')

        for j in consumption[calificare]:
            for k in warehouse:
                if j == k:
                    warehouse[j] -= consumption[calificare][j]
                    with open('warehouse.json', 'w') as output:
                        json.dump(warehouse, output, indent=4)
                        output.close()

        print('\n[' + calificare.upper() + '] ### [' + nume + ' ' + prenume +
              '] ### [' + str(id) + ']')
        print('#################################')
        # tabel
        space = '{:<15}{:<10}{:<10}'
        print(space.format('Materiale', 'Stock', 'Consum'))
        for i in consumption[calificare]:
            left_aligned = str(i).upper()
            center = str(warehouse[i])
            right_aligned = str(consumption[calificare][i])
            print(space.format(left_aligned, center, right_aligned))
        print('###Produs creat cu succes!###')
        print('#################################')
