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

if __name__ == '__main__':
    wait = input('Nyomj entert a folytatáshoz...')