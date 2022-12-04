from random import randint
while True:
    print("Nhap bao, bua, keo: ")
    player = input()
    may = randint(1, 3)

    if may == 1:
        may = "bao"
    if may == 2:
        may = "bua"
    if may == 3:
        may = "keo"

    print("-------------")
    print("Ban chon: " + player)
    print("May chon: " + may)
    print("-------------")

    if may == player:
        print("HOA!")
    else:
        if may == "keo":
            if player == "bua":
                print("THANG!!")
            else:
                print("THUA!!")
        elif may == "bua":
            if player == "bao":
                print("THANG!!")
            else:
                print("THUA!!")
        elif may == "keo":
            if player == "bua":
                print("THANG!!")
            else:
                print("THUA!!")
        else:
            print("Nhap sai")
    print("Ban co muon choi lai? (yes, no): ")
    a = input()
    if (a != "yes"):
        break;
print("Tam biet")


