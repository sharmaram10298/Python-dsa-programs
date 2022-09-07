class InvalidAge(Exception):
    def __init__(self,arg): #  def is constractor !
        self.arg = arg
a = int(input("Enter Your Age: "))
try:
    if(a>18):
        print("Welcome to vote!")
    else:
        raise InvalidAge("No Allowed To Vote")
except InvalidAge as i:
    print(i.arg)
