class Rational:
    def __init__(self, a, b=1):
        """
        :param a: чисельник, може бути типу Integer, Rational, String(26/34, наприклад)
        :param b: знаменник
        """

        if type(a) == Rational:
            self.a = a.a
            self.b = a.b

        else:
            if type(a) == str:
                arr = a.split("/")
                a, b = [int(d) for d in arr]
            else:
                assert type(a) == int and type(b) == int, "a і b повинні бути цілими"

            self.is_zero(b)
            self.a, self.b = self.divide_by_gcd(a, b)

    # region statick_methods

    @staticmethod
    def is_zero(b):
        assert b != 0, "знаменник не може бути нулем"

    @staticmethod
    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def _get_other(other) -> tuple:
        """
        This function check if param other fits to the conditions
        (It must be Rational object or Integer)
        """
        if type(other) == Rational:
            a = other.a
            b = other.b

        elif type(other) == int:
            a = other
            b = 1

        else:
            raise ValueError("Число повинно бути або цілим, або об'єктом класу Rational")

        return a, b

    # endregion

    # region main_functions

    def divide_by_gcd(self, a, b):
        """
        :param a: чисельник
        :param b: знаменник
        :return: чисельник і знаменник, поділені на їх НСД
        """
        gcd = self._gcd(a, b)
        a = a // gcd
        b = b // gcd
        return a, b

    # endregion

    # region magic_methods

    def __add__(self, other):
        """
        :param other: об'єкт класу Rational, або Intenger
        :return: новий об'єкт класу Rational
        """
        a, b = self._get_other(other)

        new_a = (self.a * b) + (a * self.b)
        new_b = b * self.b

        return Rational(new_a, new_b)

    def __sub__(self, other):
        """
        :param other: об'єкт класу Rational, або Intenger
        :return: новий об'єкт класу Rational
        """
        a, b = self._get_other(other)

        new_a = (self.a * b) - (a * self.b)
        new_b = b * self.b

        return Rational(new_a, new_b)

    def __mul__(self, other):
        """
        :param other: об'єкт класу Rational, або Intenger
        :return: новий об'єкт класу Rational
        """
        a, b = self._get_other(other)

        new_a = self.a * a
        new_b = self.b * b

        return Rational(new_a, new_b)

    def __getitem__(self, key):
        """
        :param key: str, "n" or "d"
        :return: чисельник або знаменник дробу
        """
        if key == 'n':
            return self.a

        elif key == 'd':
            return self.b

        else:
            raise ValueError("Ключ повинен бути 'n' або 'd' ")

    def __str__(self):
        return f"{self.a}/{self.b}"

    def __call__(self):
        return self

    # def __lt__(self, other):
    #     if type(other) == Rational:
    #         return self.b < other.b
    #     else:
    #         raise ValueError
    #
    # def __gt__(self, other):
    #     if type(other) == Rational:
    #         return self.b > other.b
    #     else:
    #         raise ValueError
    #
    # def __eq__(self, other):
    #     if type(other) == Rational:
    #         return self.b == other.b
    #     else:
    #         raise ValueError

    # endregion


if __name__ == '__main__':
    r1 = Rational("3/5")
    r2 = Rational(r1)
    r3 = Rational(4, 7)
    r4 = Rational(1, 9)

    r5 = r1 + r2 + r3
    print(r5)
    r5 = r5 - r4
    print(r5)