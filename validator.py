class Validator:

    def validuj_heslo(self, heslo):
        if len(heslo) <= 5:
           return False
        if not any(znak.isdigit() for znak in heslo):
           return False

        return True

