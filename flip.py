import random
def flip():
    n = int(input("Enter the number of the flipping: "))
    for i in range(0, n):
         x = random.choice([True, False])
         print(x)

if __name__ == "__main__":
    flip()



