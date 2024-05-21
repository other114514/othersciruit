count=0
with open("saiddoli.txt","rb") as f:
    for i in range(9):
        print(f.read(3).decode('utf-8'))
