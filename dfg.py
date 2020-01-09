import datetime

# Lista zawierająca krotki z datami. Mozna dodawać
# nieskończenie wiele zachowując format (YYYY, M, D)
dates = [(2017, 9, 24), (2017, 10, 1)]


def date_fomat_generator(input_list):
    # Separatory wystepujace w datach:
    sep = ["/", "-", ".", " ", "\\"]

    da = ['%d']
    mo = ['%b', '%B', '%m']
    ye = ['%y', '%Y']

    combo_dates = []
    dates_list = []

    # Pętla tworząca listę z różnymi kombinacjami dat
    for y in ye:
        for m in mo:
            for d in da:
                date_format_list = [[y, m, d], (d, m, y), (m, d, y)]
                for f in date_format_list:
                    combo_dates.append(f)

    # Pętla podstawiająca konkretne daty pod listę z kombinacjami
    for date in input_list:
        date_obj = datetime.datetime(date[0], date[1], date[2])
        for c in combo_dates:
            for s in sep:
                dates_list.append(date_obj.strftime(s.join(c)))
                # dates_list.append(date_obj.strftime(s.join(c)).lstrip('0'))
    write_to_file(dates_list)
    return dates_list


def write_to_file(dl):
    file = open('Dates_list.txt', 'w')

    try:
        # Jeżeli chcesz aby daty były oddzielone jakimś wyrażeniem
        # np. 'or', 'and', '||', '&&' należy zmodyfikować poniższą
        # linię.
        # Daty oddzielone spacją:
        file.write(' '.join(dl))
        # Daty oddzielone 'or':
        # file.write(' or '.join(dl))

        # Każda data w nowym wierszu:
        # file.write('\n'.join(dl))

    finally:
        file.close()


def read_file():
    file = open('Dates_list.txt', 'r')
    try:
        d = file.read()
    finally:
        file.close()
    return d


date_fomat_generator(dates)
print(read_file())
