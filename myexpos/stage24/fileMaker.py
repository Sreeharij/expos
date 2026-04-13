with open("numbers.dat", "w") as f:
    for i in range(1, 2048):
        f.write(f"{i}\n")