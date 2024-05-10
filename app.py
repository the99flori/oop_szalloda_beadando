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
        return f'Egyágyas szoba, szoba száma: {self.szama}, ára: {self.ar} Ft/éj'
    
class KetagyasSzoba(Szoba):
    def __init__(self, szama: int):
        super().__init__(ar=15000, szama=szama)

    def get_description(self):
        return f'Kétágyas szoba, szoba száma: {self.szama}, ára: {self.ar} Ft/éj'
class Szalloda:
    def __init__(self, nev: str, cim: str):
        self.nev = nev
        self.cim = cim
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba: Szoba):
        self.szobak.append(szoba)

    def add_foglalas(self, szobaszam: int, datum: str):
        for szoba in self.szobak:
            if szoba.szama == szobaszam:
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                print(f'Foglalás rögzítve: {szoba.get_description()}, dátum: {datum}')
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
        
        print(f'Foglalások: (összesen {len(self.foglalasok)} db)')
        for foglalas in self.foglalasok:
            print(f' - {foglalas.szoba.get_description()}, dátum: {foglalas.datum}')
class Foglalas:
    def __init__(self, szoba: Szoba, datum: datetime.date):
        self.szoba = szoba
        self.datum = datum

if __name__ == '__main__':

    """ Teszteléshez START """
    
    egyagyas_szoba = EgyagyasSzoba(101)
    print(egyagyas_szoba.get_description())
    ketagyas_szoba = KetagyasSzoba(201)
    print(ketagyas_szoba.get_description())
    szalloda = Szalloda('Minta Hotel', 'Budapest, Fő utca 1.')
    szalloda.add_szoba(egyagyas_szoba)
    szalloda.add_szoba(ketagyas_szoba)
    print(f'Szálloda neve: {szalloda.get_nev()} címe: {szalloda.get_cim()} szobák száma: {len(szalloda.get_szobak())}')

    szalloda.add_foglalas(102, datetime.strptime('2025.01.01.', '%Y.%m.%d.').date())
    szalloda.add_foglalas(101, datetime.strptime('2025.01.01.', '%Y.%m.%d.').date())
    szalloda.add_foglalas(201, datetime.strptime('2025.01.01.', '%Y.%m.%d.').date())

    szalloda.get_foglalasok()

    szalloda.remove_foglalas(101, datetime.strptime('2025.01.01.', '%Y.%m.%d.').date())

    szalloda.get_foglalasok()

    """ Teszteléshez END """

    wait = input('Nyomj entert a folytatáshoz...')