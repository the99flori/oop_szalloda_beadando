'''
GDE 2023/24/2 - Objektumorientált programozás - beadandó dolgozat
Szállodai szobafoglaló alkalmazás - készítette: Demecs Flórián - HBJU1F
'''

from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, ar:int, szama:int):
        self.ar = ar
        self.szama = szama

    @abstractmethod
    def get_description(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szama:int):
        super().__init__(ar=10000, szama=szama)

    def get_description(self):
        return f'Egyágyas szoba, szoba száma: {self.szama}, ára: {self.ar} Ft/éj'
    
class KetagyasSzoba(Szoba):
    def __init__(self, szama:int):
        super().__init__(ar=15000, szama=szama)

    def get_description(self):
        return f'Kétágyas szoba, szoba száma: {self.szama}, ára: {self.ar} Ft/éj'

if __name__ == '__main__':

    egyagyas_szoba = EgyagyasSzoba(101)
    print(egyagyas_szoba.get_description())
    ketagyas_szoba = KetagyasSzoba(201)
    print(ketagyas_szoba.get_description())
    
    wait = input('Nyomj entert a folytatáshoz...')