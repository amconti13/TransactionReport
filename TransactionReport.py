import re
import sys
import os
import os.path as osp
from operator import itemgetter
nameTest = ["Fname Lname",
            "Fname Lname Sr",
            "Fname Lname Jr",
            "Fname Lname II",
            "Fname Lname III",
            "Fname Lname IV",
            "Fname Lname Sr.",
            "Fname Lname Jr.",
            "Fname I Lname",
            "Fname I Lname Sr",
            "Fname I Lname Jr",
            "Fname I Lname III",
            "Fname I Lname IV",
            "Fname I Lname Sr.",
            "Fname I Lname Jr.",
            "Fname I. Lname",
            "Fname I. Lname",
            "Fname I. Lname Sr",
            "Fname I. Lname Jr",
            "Fname I. Lname III",
            "Fname I. Lname IV",
            "Fname I. Lname Sr.",
            "Fname I. Lname Jr.",
            "Fname . Lname",
            "Fname",
            "Fname I.",
            "Lname, Fname",
            "I. Lname",
            "Fname Lname S.",
            "Fname Lname r.",
            "Fname Lname .",
            "Fname Lname I"]


def testName() :

    for name in nameTest :
        nameValid = re.match(r"([a-zA-Z]+) (([a-zA-Z]|[a-zA-Z].)? )?([a-zA-Z]+)"
                             + "( ([JS]r\.?|III?|IV))?", name)
        if (nameValid != None) and (nameValid.group() == name) :
                             
            print("1 ", nameValid.group())
                         #print(name, "\t", nameValid.group())
        else :
            print("0 ", name)

dateTest = ["Month 10, 2016",
        "Month 1, 1999",
        "Month 12, 1917",
        "Month 01, 2000",
        "01-01-00",
        "12-1-99",
        "1-1-17",
        "09/09/1999",
        "9/9/2000",
        "8-09/17",
        "8-/09-17",
            "80917"]

def testDate() :
    for date in dateTest :
        dateValid = re.match(r"(([a-zA-Z]+ ([0-9]|[0-2][1-9]|3[01])+, "
                         "(19[1-9][7-9]|20[0-9][0-9]))|"
                         "(([0-9]|0[1-9]|1[0-2])((-|/))([0-9]|[0-2][1-9]|3[01]))"
                         "((-|/))(19[1-9][7-9]|20[0-9][0-9]|[0-9][0-9]))",date)
        if (dateValid != None) :
            print("1 ", dateValid.group())
        else :
            print("0 ", date)
#print(dateValid)
#testDate()
#([0-9]|0[1-9]|1[0-2]) MM-/DD-/YY
#([a-zA-Z]+ [0123]?[0-9]+, (19[1-9][7-9]|20[0-9][0-9])) Month DD, YYYY

amountTest = ["$20.00","$20","20.00","20", "0", "20.0", ".00", "0.000"]

def testAmount() :
    for amount in amountTest :
        amountValid = re.match(r"^\$?(\d+(\.\d{2}|\.)?) ", amount + " ")
        #0-9]+\.?([0-9][0-9])?
        if (amountValid != None) :
            print("1 ", amountValid.group())
        #print(name, "\t", nameValid.group())
        else :
            print("0 ", amount)

#testAmount()

cardTest = ["4000 0000 0000 0000",
            "4000000000000000","4000-0000-0000-0000","400000000 0000000",
            "5100000000000000",
            "5500000000000000","5500 0000 0000 0000","5500-0000-0000-0000",
            "5600000000000000","2721000000000000","2221000000000000",
            "2720000000000000", "2721-0000-0000-0000","2721 0000 0000 0000",
            "2721-0000-00000","27210-0000-0000-0000",
            "340000000000000", "370000000000000", "3400 000000 00000",
            "3400-000000-00000","330000000000000"]
def testCard() :
    for card in cardTest :
        cardValid = re.match(r"(4\d{15}|4\d{3}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}|"
                             "5[1-5]\d{14}|5[1-5]\d{2}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}|"
                             "2[2-7]2[01][ -]?\d{4}[ -]?\d{4}[ -]?\d{4}|"
                             "3[47]\d{13}|3[47]\d{2}[ -]?\d{6}[ -]?\d{5})", card)
        if (cardValid != None) :
            print("1 ", cardValid.group())
        #print(name, "\t", nameValid.group())
        else :
            print("0 ", card)

#testCard()
#visa
#re.match(r"4\d{3}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}",x)
#mastercard
#print(re.match(r"5[1-5]\d{2}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}",x))
#r"2[2-7]2[01][ -]?\d{4}[ -]?\d{4}[ -]?\d{4}",x

#americanexpress
#>>> print(re.match(r"3[47]\d{2}[ -]?\d{6}[ -]?\d{5}",x))

#name:date:amount:card
'''
for a in nameTest :
    for b in dateTest :
        for c in amountTest :
            for d in cardTest :
                x = a + ":" + b + ":" + c + ":" + d
                y = re.match(r"(([a-zA-Z]+) (([a-zA-Z]|[a-zA-Z].)? )?([a-zA-Z]+)( ([JS]r\.?|III?|IV))?):"
                 "(([a-zA-Z]+ ([0-9]|[0-2][1-9]|3[01])+, "
                 "(19[1-9][7-9]|20[0-9][0-9]))|"
                 "(([0-9]|0[1-9]|1[0-2])((-|/))([0-9]|[0-2][1-9]|3[01]))"
                 "((-|/))(19[1-9][7-9]|20[0-9][0-9]|[0-9][0-9])):"
                 "\$?(\d+(\.\d{2}|\.)?):"
                 "(4\d{15}|4\d{3}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}|"
                 "5[1-5]\d{14}|5[1-5]\d{2}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}|"
                 "2[2-7]2[01][ -]?\d{4}[ -]?\d{4}[ -]?\d{4}|"
                 "3[47]\d{13}|3[47]\d{2}[ -]?\d{6}[ -]?\d{5})",x)
                print(x)
                '''
        #for c in amountTest :
        #   for d in cardTest :
        #x = a + ":" + b + ":" + c + ":" + d
#print(a + ":" + b + ":" + c + ":" + d)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
monthDictionary = {'January':'01','February':'02','March':'03',
                    'April':'04','May':'05','June':'06',
                    'July':'07','August':'08','September':'09',
                    'October':'10','November':'11', 'December':'12'}

tAE = []
tMC = []
tV = []

#-------------------------------------------------------------------------------

def checkValidityReturnLines() :
    if len(sys.argv) != 2:
        print("Incorrect amount of arguments")
        sys.exit()
    file = open(sys.argv[1],"r")
    lines = file.readlines()
    file.close()
    return lines

#-------------------------------------------------------------------------------

def generalMatch(x) :
    y = re.match(r"(([a-zA-Z]+) (([a-zA-Z]|[a-zA-Z].)? )?([a-zA-Z]+)( ([JS]r\.?|III?|IV))?):"
                 "(([a-zA-Z]+ ([0-9]|[0-2][1-9]|3[01])+, "
                 "(19[2-9][0-9]|20[0-9][0-9]|191[7-9]))|"
                 "(([0-9]|0[1-9]|1[0-2])((-|/))([0-9]|[0-2][1-9]|3[01]))"
                 "((-|/))(191[7-9]|19[2-9][0-9]|20[0-9][0-9]|[0-9][0-9])):"
                 "\$?(\d+(\.\d{2}|\.)?):"
                 "(4\d{15}|4\d{3}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}|"
                 "5[1-5]\d{14}|5[1-5]\d{2}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}|"
                 "2[2-7]2[01][ -]?\d{4}[ -]?\d{4}[ -]?\d{4}|"
                 "3[47]\d{13}|3[47]\d{2}[ -]?\d{6}[ -]?\d{5})(\s|\Z)",x)
    if (y != None) :
        return y.group().split(':')
    else :
        print("invalid something")
        print (x)

#-------------------------------------------------------------------------------

def cardName(number) :
    if(None != re.match(r"4\d{15}|4\d{3}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}",number)) :
        return "Visa"
    elif(None != re.match(r"5[1-5]\d{14}|5[1-5]\d{2}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4}|"
            "2[2-7]2[01][ -]?\d{4}[ -]?\d{4}[ -]?\d{4}",number)) :
        return "Mastercard"

    elif(None != re.match(r"(3(4|7)\d{13}|3(4|7)\d{2}[ -]?\d{6}[ -]?\d{5})", number)) :
        return "American Express"
    else :
        return None

#-------------------------------------------------------------------------------

def reformatCardNumber(number, cName) :
    #print("in reformatCardNumber: number", number, "cName", cName)
    card,num  = "",""
    counter = 0
    number = number.split("-")#" "
    for x in range(0,len(number)) :
        num = num + number[x]
    number = num.replace("", " ").split()
    if (cName == "American Express") :
        for x in number :
            card = card + x
            if (counter == 3) or (counter == 9) :
                card = card + " "
            counter+=1
    else :
        for x in number :
            card = card + x
            if (counter == 3) or (counter == 7) or (counter == 11):
                card = card + " "
            counter+=1
    return card

#-------------------------------------------------------------------------------

def reformatDate(date) :
    #Month day, year
    if(None!=re.match(r"([a-zA-Z]+ ([0-9]|[0-2][1-9]|3[01])+, (191[7-9]|19[2-9][0-9]|20[0-9][0-9]))", date)) :
        d = date.split()
        d[1] = d[1].strip(",")
        if(d[0] in monthDictionary) :
            d[0] = monthDictionary[d[0]]
        else :
            print("Invalid Month")
            return None
        if (len(d[1]) == 1) :
            d[1] = '0' + d[1]
        yyyy = d[2]
    elif(None!=re.match(r"(([0-9]|0[1-9]|1[0-2])((-|/))([0-9]|[0-2][1-9]|3[01]))((-|/))(191[7-9]|19[2-9][0-9]|20[0-9][0-9]|[0-9][0-9])",date)) :
        d = date.split("/")
        if(len(d)!=3):
            d = date.split("-")
        if (len(d[0]) == 1) :
            d[0] = '0' + d[0]
        if (len(d[1]) == 1) :
            d[1] = '0' + d[1]
        if (int(d[2])<100):
            if (int(d[2]) <= 16):
                d[2] = '20' + d[2]
            else :
                d[2] = '19' + d[2]
            d = "/".join(d)
            return d
        elif(int(d[2]) >= 2017) or (int(d[2]) <= 1916):
            print("Invalid Year")
            return None
    else :
        return None

    d = "/".join(d)
    return d
#-------------------------------------------------------------------------------

def reformatName(name) :
    n = name.strip(".")
    n = name.split()
    for x in range(0,len(n)):
        n[x] = n[x].strip(".")
    if len(n) == 3 :
        if len(n[1]) == 1:
            n[1] = n[1] + '.'
            n = n[2] + ", " + n[0] + " " + n[1]
        else:
            n[2] = n[2] + '.'
            n = n[1] + " " + n[2] + ", " + n[0]
    elif len(n) == 4:
        n[1] = n[1] + '.'
        n[3] = n[3] + '.'
        n = n[2] + " " + n[3] + ", " + n[0] + " " + n[1]
    else:
        n = n[1] + ", " + n[0]

    return n

#-------------------------------------------------------------------------------

def reformatAmount(amount) :
    money = amount.strip("$")
    money = money.split(".")
    a = "$" + money[0] + "."
    
    if  len(money) == 1 or money[1] == '' :
        a = a + "00"
    else:
        a = a + money[1]
    return a
#-------------------------------------------------------------------------------

def transaction(info) :
    global tAE
    global tMC
    global tV
    date = reformatDate(info[1])
    if date != None :
        cName = cardName(info[3])
        if cName == "American Express" :
            card = reformatCardNumber(info[3], cName)
            name = reformatName(info[0])
            amount = reformatAmount(info[2])
            tAE.append([card, date, name, amount])
        elif cName == "Mastercard" :
            card = reformatCardNumber(info[3], cName)
            name = reformatName(info[0])
            amount = reformatAmount(info[2])
            tMC.append([card, date, name, amount])
        elif cName == "Visa" :
            card = reformatCardNumber(info[3], cName)
            name = reformatName(info[0])
            amount = reformatAmount(info[2])
            tV.append([card, date, name, amount])
        else :
            print("Something is wrong in transaction(info):", info)
#-------------------------------------------------------------------------------




transactions = checkValidityReturnLines()

for t in transactions :
    information = generalMatch(t)
    if (information != None):
        (transaction(information))

#print("tAE: \n", tAE)
#print("tMC: \n", tMC)
#print("tV:  \n", tV)

tAE = sorted(tAE,key=itemgetter(1,2,3))
tMC = sorted(tMC,key=itemgetter(1,2,3))
tV = sorted(tV,key=itemgetter(1,2,3))

finalReport = tAE + tMC + tV


file = open("Report.txt","w")
for t in finalReport :
    file.write(t[0] + "\t"+ t[1]+ "\t"+ t[2]+ "\t"+ t[3] + "\n")
    print(t[0], "\t", t[1], "\t", t[2], "\t", t[3])#print(t)





