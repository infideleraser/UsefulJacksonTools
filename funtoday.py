import datetime


def make_dictionary(filename):
    file = open(filename, 'r')
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



def write(filename):
    file=open(filename, 'a')
    date=datetime.datetime.now()
    file.write('\n\n')
    file.write(date.strftime('%m/%d/%Y')+'\n')
    stuff=input("Whats new today?\n")
    file.write(stuff)
    print()
    file.close()

def append(filename):
    file=open(filename, 'a')
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
    filename=input("enter filename - edit FILENAME variable in code and "
          "comment out this line to skip this step")
    whatdo=input("r for read, w for write, l for lookup, a for append, q for quit\n")
    while whatdo != 'q':
        if whatdo == "r":
            print()
            read(filename)
        elif whatdo == 'w':
            print()
            write(filename)
        elif whatdo == 'l':
            print()
            lookup()
        elif whatdo == 'a':
            print()
            append(filename)
        else:
            print("error, exiting")
            return
        whatdo = input("r for read, w for write, l for lookup, a for append, q for quit\n")

    print("goodbye")



main()