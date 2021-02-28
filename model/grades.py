class Grades:
    """This class serves as an extra layer of protection for oor data.
    All data which is required to be passed into database is firstly converted into private datatype and then
    it is passed as values. This ensures that middleman is not able to take a peak into the data when its travelling
    into our database."""

    def __init__(self, Math=None, Science=None, Nepali=None, English=None, Social=None, Computer=None, EPH=None,
                 Geography=None, UserName=None):
        self.__math = Math
        self.__science = Science
        self.__nepali = Nepali
        self.__english = English
        self.__social = Social
        self.__computer = Computer
        self.__eph = EPH
        self.__geography = Geography
        self.__username = UserName

    def set_math(self, Math):
        if type(Math) is not int:
            raise TypeError
        elif 100 < Math > 0:
            raise ValueError
        else:
            self.__math = Math

    def get_math(self):
        return self.__math

    def set_science(self, Science):
        if type(Science) is not int:
            raise TypeError
        elif 100 < Science > 0:
            raise ValueError
        else:
            self.__science = Science

    def get_science(self):
        return self.__science

    def set_nepali(self, Nepali):
        if type(Nepali) is not int:
            raise TypeError
        elif 100 < Nepali > 0:
            raise ValueError
        else:
            self.__nepali = Nepali

    def get_nepali(self):
        return self.__nepali

    def set_english(self, English):
        if type(English) is not int:
            raise TypeError
        elif 100 < English > 0:
            raise ValueError
        else:
            self.__english = English

    def get_english(self):
        return self.__english

    def set_social(self, Social):
        if type(Social) is not int:
            raise TypeError
        elif 100 < Social > 0:
            raise ValueError
        else:
            self.__social = Social

    def get_social(self):
        return self.__social

    def set_computer(self, Computer):
        if type(Computer) is not int:
            raise TypeError
        elif 100 < Computer > 0:
            raise ValueError
        else:
            self.__computer = Computer

    def get_computer(self):
        return self.__computer

    def set_eph(self, EPH):
        if type(EPH) is not int:
            raise TypeError
        elif 100 < EPH > 0:
            raise ValueError
        else:
            self.__eph = EPH

    def get_eph(self):
        return self.__eph

    def set_geography(self, Geography):
        if type(Geography) is not int:
            raise TypeError
        elif 100 < Geography > 0:
            raise ValueError
        else:
            self.__geography = Geography

    def get_geography(self):
        return self.__geography

    def set_username(self, UserName):
        self.__username = UserName

    def get_username(self):
        return self.__username
