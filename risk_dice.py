import random


while True:
    try:
        attackers=int(input("How many units attacking? : "))
    except NameError:
        print("Not a number!")
        continue
    else:
        if (attackers < 1) | (attackers > 3):
            print("Error: please give a number in range of 1-3!")
        else:
            break

while True:
    try:
        defenders=int(input("How many units defending? : "))
    except NameError:
        print("Not a number!")
        continue
    else:
        if (defenders < 1) | (defenders > 2):
            print("Error: please give a number in range of 1-2!")
        else:
            break


att = list()
deff = list()

for i in range(attackers):
    att.insert(i, random.randrange(1, 6))

for i in range(defenders):
    deff.insert(i, random.randrange(1, 6))

att.sort(reverse=True)
deff.sort(reverse=True)

text=' - '.join(str(e) for e in att)
print("Attackers: " + text)
text=' - '.join(str(e) for e in deff)
print("Defenders: " + text)

att_loss = 0
deff_loss = 0

if ((attackers >=2) & (defenders == 2)):
    if att[0]>deff[0]:
        deff_loss += 1
    elif att[0]<deff[0]:
        att_loss += 1
    else:
        att_loss += 1

    if att[1]>deff[1]:
        deff_loss += 1
    elif att[1]<deff[1]:
        att_loss += 1
    else:
        att_loss += 1

if ((attackers >=2) & (defenders == 1)) | ((attackers == 1) & (defenders == 1)):
    if att[0]>deff[0]:
        deff_loss += 1
    elif att[0]<deff[0]:
        att_loss += 1
    else:
        att_loss += 1

print("Attackers lost %d units." % (att_loss))
print("Defenders lost %d units." % (deff_loss))