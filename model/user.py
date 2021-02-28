class User:
    """This class serves as an extra layer of protection for oor data.
        All data which is required to be passed into database is firstly converted into private datatype and then
        it is passed as values. This ensures that middleman is not able to take a peak into the data when its travelling
        into our database."""

    def __init__(self, fname=None, lname=None, eadd=None, passwd=None, uname=None, dob=None, cls=None, sec=None,
                 suff=None):
        self.__fname = fname
        self.__lname = lname
        self.__eadd = eadd
        self.__passwd = passwd
        self.__uname = uname
        self.__dob = dob
        self.__cls = cls
        self.__sec = sec
        self.__suff = suff

    def set_fname(self, fname):
        self.__fname = fname

    def get_fname(self):
        return self.__fname

    def set_lname(self, lname):
        self.__lname = lname

    def get_lname(self):
        return self.__lname

    def set_eadd(self, eadd):
        self.__eadd = eadd

    def get_eadd(self):
        return self.__eadd

    def set_passwd(self, passwd):
        self.__passwd = passwd

    def get_passwd(self):
        return self.__passwd

    def set_uname(self, uname):
        self.__uname = uname

    def get_uname(self):
        return self.__uname

    def set_dob(self, dob):
        if type(dob) is not str:
            raise TypeError
        self.__dob = dob

    def get_dob(self):
        return self.__dob

    def set_cls(self, cls):
        self.__cls = cls

    def get_cls(self):
        return self.__cls

    def set_sec(self, sec):
        self.__sec = sec

    def get_sec(self):
        return self.__sec

    def set_suff(self, suff):
        self.__suff = suff

    def get_suff(self):
        return self.__suff
