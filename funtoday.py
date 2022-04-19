import datetime


def make_dictionary():
    file = open("data.txt", 'r')
    lines = file.readlines()
    count = 0
    dictionary = dict()
    new = []
    for i in lines:
        line = i.strip('\n')
        if line != '':
            new.append(line)
    while count < len(new):
        date = new[count]
        text = new[count + 1].strip('\n')
        dictionary[date] = text
        count += 2
    return dictionary


def read():
    dictionary=make_dictionary()
    for date,text in dictionary.items():
        print(f"Date: {date}")
        while len(text)>100:
            print(text[:100])
            text=text[100:]
        print(text)
        print()



def write():
    file=open('data.txt', 'a')
    date=datetime.datetime.now()
    if file.readlines()==[]:
        pass
    else:
        file.write('\n\n')
    file.write(date.strftime('%m/%d/%Y')+'\n')
    stuff=input("Whats new today?\n")
    file.write(stuff)
    print()
    file.close()

def append():
    file=open("data.txt", 'a')
    stuff=input("What else do you want to add?\n")
    file.write(stuff)
    print()
    file.close()

def lookup():
    date=input("Enter date MM/DD/YYYY\n")
    print()
    dictionary=make_dictionary()
    try:
        print(f"Date: {date}")
        text=dictionary[date]
    except KeyError:
        print("No value exists for this date")
        return
    while len(text) > 100:
        print(text[:100])
        text = text[100:]
    print(text)

def main():
    whatdo=input("r for read, w for write, l for lookup, a for append, q for quit\n")
    file=open("data.txt")
    file.close()
    while whatdo != 'q':
        if whatdo == "r":
            print()
            read()
        elif whatdo == 'w':
            print()
            write()
        elif whatdo == 'l':
            print()
            lookup()
        elif whatdo == 'a':
            print()
            append()
        else:
            print("error, exiting")
            return
        print()
        whatdo = input("r for read, w for write, l for lookup, a for append, q for quit\n")

    print("goodbye")



main()