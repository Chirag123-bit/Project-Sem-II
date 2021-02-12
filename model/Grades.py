
class Grades:
    def __init__(self, Math, Science, Nepali, English, Social, Computer,EPH, Geography):
        self.__math = Math
        self.__science = Science
        self.__nepali = Nepali
        self.__english = English
        self.__social = Social
        self.__computer = Computer
        self.__eph= EPH
        self.__geography = Geography

    def set_math(self,Math):
        self.__math = Math
    def get_math(self):
        return self.__math

    def set_science(self,Science):
        self.__science = Science
    def get_science(self):
        return self.__science

    def set_nepali(self,Nepali):
        self.__nepali = Nepali
    def get_nepali(self):
        return self.__nepali

    def set_english(self,English):
        self.__english= English
    def get_english(self):
        return self.__english

    def set_social(self,Social):
        self.__social = Social
    def get_social(self):
        return self.__social

    def set_computer(self,Computer):
        self.__computer = Computer
    def get_computer(self):
        return self.__computer

    def set_eph(self,EPH):
        self.__eph= EPH
    def get_eph(self):
        return self.__eph

    def set_geography(self,Geography):
        self.__geography= Geography
    def get_sgeography(self):
        return self.__geography
