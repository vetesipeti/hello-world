from operator import itemgetter
import operator

#by=b'\xe9\xb2'
#izé = by.decode('utf-8')
izé = "🦂"
izé2 = "🤗"
#'🀎🀎🀎🀀🀀🀀🀀🀀🀀🀀🀀🀀🀀🀀'

inv = {'rope': 1, 'torch': 6, 'gold coin': 1612, 'dagger': 1, 'arrow': 12, '🤗':12}
dragon_loot = ['gold coin',izé, 'gold coin', 'gold coin', 'by','🦀','𐄷','🤗🤗🤗🤗🤗🤗🤗']


def display_inventory(inventory):
    count = 0
    for key in inventory:
        count += inventory[key]
        print(inventory[key], key)
        
    print("Total number of items: " ,count)


def add_to_inventory(inventory, added_items):
    for x in added_items:
        if x in inventory:
            inventory[x] += 1
        else:
            inventory.update({x:1})
    return inventory


def max_item_lenght(dictionary):
    lenghts = []
    
    for x in dictionary:
        spec_char_counter = 0
        for a in x:
            if len(a.encode()) > 2:
                spec_char_counter += 1

        lenghts.append((len(x)+spec_char_counter))
    longest = sorted(lenghts)[-1]

    return longest


def print_table(order=""):
    #DEFINING VARIABLES
    item_counter = 0
    MIN_SPACE = 3
    dash_lenght = 7 + MIN_SPACE + max_item_lenght(inv)
    dash_line = "-"*dash_lenght
    running_title_space = " "*(dash_lenght-16)
   
    #PRINTING TITLE
    print("Inventory:\n  %s%s%s" % ("count",running_title_space,"item name"))
    print(dash_line)
    
    #PRINTING THE INVENTORY
    if order == "":
        for x in inv:
            spec_char_counter = 0
            for a in x:
                if len(a.encode()) > 2:
                    spec_char_counter += 1
            space_multip = (max_item_lenght(inv) - (len(i)+spec_char_counter) + MIN_SPACE)
            dynamic_space = space_multip*" "
            print("%7d%s%s" % (inv[x],dynamic_space,x))
            item_counter += x
    else:
        if order == "count,asc":
            desc = False
        elif order == "count,desc":
            desc = True
        for i,x in sorted(inv.items(),key=operator.itemgetter(1),reverse=desc):
            spec_char_counter = 0
            for a in i:
                if len(a.encode()) > 2:
                    spec_char_counter += 1
            space_multip =  (max_item_lenght(inv) - (len(i)+spec_char_counter) + 3)
            dynamic_space =space_multip*" "
            print("%7d%s%s  %d" % (x,dynamic_space,i,space_multip))
            item_counter += x

    #PRINTING THE SUM OF ITEMS INVENTORY HAS
    print(dash_line)
    print("Total number of items: ",item_counter)

def import_inventory(filename="import_inventory.csv"):
    with open(filename) as fobj:
        a = fobj.readlines()
        #b = a[0].split("\n")
    c = []
    for v in range(1,len(a)):
        if ',' in a[v]:
            a[v] = a[v][:-1]
            c.append(a[v].split(',',1))
    d=dict(c)
    for i in d:
        if i in inv:
            inv[i] += int(d[i])
        else:
            inv.update({i:int(d[i])})

def export_inventory(filename="export_inventory.csv"):
    with open(filename, "w") as fobj:
        fobj.write("item_name,count\n")
        for x in inv:
            line = x + "," + str(inv[x]) + "\n"
            fobj.write(line)





display_inventory(inv)
inv = add_to_inventory(inv,dragon_loot)
print()
display_inventory(inv)
print()
print_table("count,desc")
import_inventory()
print()
print_table("count,desc")
export_inventory()
print(izé)
print("Byte lenght: ",izé2.encode('utf-8'))
a1 = '深'
Z1 = "Z"
Z = Z1.encode("utf-8")
a= a1.encode("utf-8")
print(a)
print(Z)