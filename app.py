'''
GDE 2023/24/2 - Objektumorientált programozás - beadandó dolgozat
Szállodai szobafoglaló alkalmazás - készítette: Demecs Flórián - HBJU1F
'''

from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, ar: int, szama: int):
        self.ar = ar
        self.szama = szama

    @abstractmethod
    def get_description(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szama: int):
        super().__init__(ar=10000, szama=szama)

    def get_description(self):
        return f'Egyágyas szoba, száma: {self.szama}, ára: {self.ar} Ft/éj'
    
class KetagyasSzoba(Szoba):
    def __init__(self, szama: int):
        super().__init__(ar=15000, szama=szama)

    def get_description(self):
        return f'Kétágyas szoba, száma: {self.szama}, ára: {self.ar} Ft/éj'
class Szalloda:
    def __init__(self, nev: str, cim: str):
        self.nev = nev
        self.cim = cim
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba: Szoba):
        self.szobak.append(szoba)

    def add_foglalas(self, szobaszam: int, datum: str, ui: bool = True):
        for szoba in self.szobak:
            if szoba.szama == szobaszam:
                for foglalas in self.foglalasok:
                    if foglalas.szoba.szama == szobaszam and foglalas.datum == datum:
                        print(f'A megadott szobaszám ({szobaszam}) és dátum ({datum}) párosítás már foglalt!')
                        return None
                    
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                if ui==True: print(f'Foglalás rögzítve: {szoba.get_description()}, dátum: {datum}')
                return foglalas
        
        print(f'A megadott szobaszám ({szobaszam}) nem létezik!')
        return None
    
    def remove_foglalas(self, szobaszam: int, datum: datetime.date):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szama == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                print(f'Foglalás törölve: {foglalas.szoba.get_description()}, dátum: {foglalas.datum}')
                return foglalas
        
        print(f'A megadott szobaszám ({szobaszam}) és dátum ({datum}) párosítás nem létezik!')
        return None

    def get_nev(self):
        return self.nev
    
    def get_cim(self):
        return self.cim

    def get_szobak(self):
        return self.szobak
    
    def get_foglalasok(self):
        if len(self.foglalasok) == 0:
            print('Nincsenek foglalások!')
            return
        
        print(f'(összesen {len(self.foglalasok)} db)')
        for foglalas in self.foglalasok:
            print(f' - {foglalas.szoba.get_description()}, dátum: {foglalas.datum}')
class Foglalas:
    def __init__(self, szoba: Szoba, datum: datetime.date):
        self.szoba = szoba
        self.datum = datum

def input_valid_szoba(prompt):
    while True:
        try:
            szobaszam = int(input(prompt))
            for szoba in szalloda.get_szobak():
                if szoba.szama == szobaszam:
                    return szobaszam
            raise AttributeError
        
        except ValueError:
            print('Hibás szobaszám formátum!')
        
        except AttributeError:
            print('A megadott szobaszám nem létezik!')

def input_valid_date(prompt):
    while True:
        try:
            date = datetime.strptime(input(prompt), '%Y-%m-%d').date()
            if date > datetime.now().date():
                return date
            raise AttributeError
        
        except ValueError:
            print('Hibás dátum formátum!') 
        
        except AttributeError:
            print('A megadott dátumnak jövőbeni időpontnak kell lennie!')

def user_interface(szalloda: Szalloda):
    print(f'--- {szalloda.get_nev()} ({szalloda.get_cim()}) ---')
    print('Üdvözöljük a szállodai szobafoglaló alkalmazásban!')
    
    while True:
        print('\n --- Menü ---')
        print('1 - Foglalás rögzítése')
        print('2 - Foglalás törlése')
        print('3 - Foglalások listázása')
        print('0 - Kilépés')
        valasz = input('\nKérem válasszon a menüpontok közül: ')

        if valasz == '1':
            print('\n --- Foglalás rögzítése ---')
            print('Szobatípusok:')
            for szoba in szalloda.get_szobak():
                print(f' - {szoba.get_description()}')
            szobaszam = (input_valid_szoba('Kérem adja meg a szobaszámot: '))
            datum = input_valid_date('Kérem adja meg a dátumot (éééé-hh-nn): ')
            szalloda.add_foglalas(szobaszam, datum)

        elif valasz == '2':
            print('\n --- Foglalás törlése ---')
            szobaszam = (input_valid_szoba('Kérem adja meg a szobaszámot: '))
            datum = input_valid_date('Kérem adja meg a dátumot (éééé-hh-nn): ')
            szalloda.remove_foglalas(szobaszam, datum)

        elif valasz == '3':
            print('\n --- Foglalások listázása ---')
            szalloda.get_foglalasok()

        elif valasz == '0':
            print('\nViszlát!')
            break

        else:
            print('Hibás menüpont választás!')

if __name__ == '__main__':

    szalloda = Szalloda('Minta Hotel', 'Budapest, Fő utca 1.')

    szalloda.add_szoba(EgyagyasSzoba(101))
    szalloda.add_szoba(EgyagyasSzoba(102))
    szalloda.add_szoba(KetagyasSzoba(201))

    szalloda.add_foglalas(101, datetime.strptime('2025-01-01', '%Y-%m-%d').date(), False)
    szalloda.add_foglalas(102, datetime.strptime('2025-01-01', '%Y-%m-%d').date(), False)
    szalloda.add_foglalas(201, datetime.strptime('2025-01-01', '%Y-%m-%d').date(), False)
    szalloda.add_foglalas(101, datetime.strptime('2025-02-02', '%Y-%m-%d').date(), False)
    szalloda.add_foglalas(201, datetime.strptime('2025-02-02', '%Y-%m-%d').date(), False)

    user_interface(szalloda)