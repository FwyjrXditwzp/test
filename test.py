def gen(x):
    counter = 1
    while True:
        if counter == x : break
        counter *= 2
        yield counter 


for i in gen(5):
    print(i)