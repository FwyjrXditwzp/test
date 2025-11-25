def gen(x):
    counter = 1
    while True:
        if counter == x : break
        yield counter **2
        counter += 1 


for i in gen(5):
    print(i)