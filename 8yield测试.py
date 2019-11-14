
def go():
    for i in range(10):
        for  j in range(10):
            for k in range(10):
                yield  i*100+j*10+k

test=go()
for i in range(1000):
    print(next(test))