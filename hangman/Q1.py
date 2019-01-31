import random


def play(y, a):
    guess = 10
    score = 0
    word = []
    cor = []
    wrg = set()
    rword = y[a-1]
    count = len(rword)
    print("Hint: "+(str)(y[a-1+(int)(len(y)/2)]))
    for i in range(len(y[a-1])):
        word.append("_ ")
    print("".join(word)+":score "+str(score) +
          ", remaining wrong guess: "+str(guess))
    while guess > 0:
        b = input(">>")
        idx = y[a-1].find(b)
        if b.isalpha() and len(b) == 1:
            if idx != -1:
                for i in range(len(y[a-1])):
                    if rword[i] == b and (b not in cor):
                        word[i] = b+" "
                        score = score+10
                        count = count-1
                cor.append(b)
            else:
                wrg.add(b+" ")
                guess = guess-1
            print("".join(word)+":score "+str(score)+", remaining wrong guess: " +
                  str(guess)+", wrong guessed: "+"".join(wrg))
            if count == 0:
                print("You are WIN!")
                break
        else:
            print("Please input one alphabet from a-z")


def main():
    while True:
        y = [e.rstrip() for e in open("sport.txt", "r")]
        z = [e.rstrip() for e in open("typesOfMovie.txt", "r")]
        x = int(input("Select Category:"+"\n"+"1.sport"+"\n" +
                      "2.types of movie"+"\n"+"choose number >>"))
        if x == 1:
            a = random.randint(1, (int)(len(y)/2))
            print(a)
            play(y, a)
        elif x == 2:
            a = random.randint(1, (int)(len(z)/2))
            play(z, a)
        else:
            print("plaes input the number of the categories.")


if __name__ == '__main__':
    main()
