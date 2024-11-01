for n in range(1,17):
    binn = bin(n)[2:]
    if len(binn) % 2 == 0:
        binn = binn[:len(binn)//2] + '1' + binn[len(binn)//2:]
    if int(binn,2) > 26:
        print(n)
        