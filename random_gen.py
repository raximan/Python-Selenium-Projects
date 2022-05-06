import random
def gen_psw(len):
    a = "abcdefghıjklmmnoprstyuxz"
    b = "1234567890"
    c = "!'^+%&/()=?_"
    d = "ABCDEFGHIJKLMNOPRSTVYZ"
    i=0
    j=1
    psw=""
    while i!= len:
        if j==1:
            psw+= random.choice(a)
            i = i + 1
            j = j + 1
        elif j==2:
            psw+= random.choice(b)
            i = i + 1
            j = j + 1
        elif j==3:
            psw+=random.choice(c)
            i = i + 1
            j = j + 1
        elif j==4:
            psw+=random.choice(d)
            j=1
            i = i + 1
    return psw


def mail_gen(a,b):
    final=""
    num="1234567890"
    c= "abcdefghıjklmmnoprstyuxz"
    raw_full = a+b
    raw_full = raw_full.lower()
    final_full =""
    for i in raw_full:
        if i=='i':
            final_full+='ı'
        elif i=='ü':
            final_full+='u'
        elif i=='ö':
            final_full+='o'
        elif i=='ç':
            final+='c'
        elif i=='ğ':
            final+='g'
        else:
            final_full+=i
    final=f"{final_full}{random.choice(num)}{random.choice(num)}{random.choice(num)}{random.choice(num)}{random.choice(c)}{random.choice(num)}"
    return final

def full_mail_gen(a):
    a = a+"@gmail.com"
    return a




def birthyear_gen():
    birth ="199"
    b="0123456789"
    birth+=random.choice(b)
    return birth

def birthday_gen():
    first_digit="012"
    second_digit="123456789"
    birthday=random.choice(first_digit)+random.choice(second_digit)
    return birthday

def name_gen():
    a = ["Jake","Micheal","Curtis","Thomas","Dorothy","Traci","Mary","Esther"
         "Linda","Bernice","Sarah","Kevın","Chad","Darrin","Sheryl","Shawn","Erika","Erik","Dale","Mario","Flora","Elmer","Lindsay"]
    name=random.choice(a)
    return name
def surname_gen():
    a= ["Kelley","Berry","Jones","Adkins","Smith","Ingram","Wagner","Hammond","Roy","Robinson","Kelley","Berry","Jones",
                                          "Adkin","Smith","Ingram","Wagner","Hammond",
                                          "Roy","Robinson","Fite","Prater","Irizarry","Lash","Triplett","Olivo","Trask","Blocker","Shultz"]
    surname=random.choice(a)
    return surname

def full_name_gen():
    full_name=name_gen()+" "+surname_gen()
    return full_name





