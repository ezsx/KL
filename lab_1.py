def read_file():
    file = open("tolstoy.txt", "r", encoding="utf8")
    str = ""
    for i in range(1000):
        str += file.readline()
    file.close()
    return str


def task1():
    from nltk import sent_tokenize
    arr = []
    print([i.replace("\n", "") for i in sent_tokenize(read_file())])
    print(sent_tokenize(read_file()))


def task2():
    from nltk import word_tokenize
    print(word_tokenize(read_file()))


def task3():
    from nltk.corpus import stopwords

    print(stopwords.words('russian'))


def task4():
    from nltk import word_tokenize
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('russian'))
    words = word_tokenize(read_file())
    without_stop_words = [word for word in words if not word in stop_words]
    print(without_stop_words)


def task5():
    task1()
    task2()
    task4()


if __name__ == "__main__":
    task1()
    # task2()
    # task3()
    # task4()
    # task5()
    pass
