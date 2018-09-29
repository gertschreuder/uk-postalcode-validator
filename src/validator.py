import re


class Validator(object):

    def __init__(self):
        self.isValid = False
        self.pattern = r"([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})"
    
    def validate(self, postcode):
        try:
            if postcode is None:
                return self.isValid
            if isinstance(postcode, str) and postcode.find(' ') >= 0:
                postcode = postcode.replace(' ', '')
            self.isValid =  postcode.isdigit() and len(postcode) == 10
            if self.isValid:     
                self.isValid =  re.match(self.pattern, postcode, flags=0) is not None
            return self.isValid
        except Exception:
            self.isValid = False
            return self.isValid
