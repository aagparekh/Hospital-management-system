import re

class Regex:
    def __init__(self,str):
        self.str=str
        self.pattern=r""
    def isPatientId(self):
        self.pattern=r"[0-9]{7}"
        if re.fullmatch(self.pattern,self.str):
            return True
        else:
            return False
    def isAlphabet(self):
        self.pattern=r"^[A-Za-z\s]+$"
        if re.fullmatch(self.pattern,self.str):
            return True
        else:
            return False
    def isAlphaNum(self):
        self.pattern=r"^[A-Za-z0-9\s]+$"
        if re.fullmatch(self.pattern,self.str):
            return True
        else:
            return False
    def isNumber(self):
        self.pattern=r"[0-9]+$"
        if re.fullmatch(self.pattern,self.str):
            return True
        else:
            return False
    def isContactNo(self):
        self.pattern=r"[0-9]{10}"
        if re.fullmatch(self.pattern,self.str):
            return True
        else:
            return False
    def isMedicineID(self):
        self.pattern=r"[0-9]{5}"
        if re.fullmatch(self.pattern,self.str):
            return True
        else:
            return False
    def isEmployeeID(self):
        self.pattern=r"[0-9]{6}"
        if re.fullmatch(self.pattern,self.str):
            return True
        else:
            return False