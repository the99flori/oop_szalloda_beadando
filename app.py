'''
GDE 2023/24/2 - Objektumorientált programozás - beadandó dolgozat
Szállodai szobafoglaló alkalmazás - készítette: Demecs Flórián - HBJU1F
'''

from abc import ABC, abstractmethod

class Szalloda:
    def __init__(self, nev: str, cim: str):
        self.nev = nev
        self.cim = cim
        self.szobak = []

    def add_szoba(self, szoba: Szoba):
        self.szobak.append(szoba)

    def get_nev(self):
        return self.nev
    
    def get_cim(self):
        return self.cim

    def get_szobak(self):
        return self.szobak
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

class Foglalas:
    def __init__(self, szoba: Szoba, datum: str):
        self.szoba = szoba
        self.datum = datum

if __name__ == '__main__':

    egyagyas_szoba = EgyagyasSzoba(101)
    print(egyagyas_szoba.get_description())
    ketagyas_szoba = KetagyasSzoba(201)
    print(ketagyas_szoba.get_description())
    szalloda = Szalloda('Minta Hotel', 'Budapest, Fő utca 1.')
    szalloda.add_szoba(egyagyas_szoba)
    szalloda.add_szoba(ketagyas_szoba)
    print(f'Szálloda neve: {szalloda.get_nev()} címe: {szalloda.get_cim()} szobák száma: {len(szalloda.get_szobak())}')

    wait = input('Nyomj entert a folytatáshoz...')