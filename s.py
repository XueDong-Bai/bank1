def product (c) :
    c.send(None)

    for i in range(5) :
        print("生产者产生数据%s" %i)
        r= c.send(str(i))
        print("消费者消费数据%s" % r)
    c.close();

def customer() :
    data = ""
    while True :
        n = yield data
        if not n :
            return
        print("消费者消费数据-%s" % n)
        data = 200


c = customer()
product(c)