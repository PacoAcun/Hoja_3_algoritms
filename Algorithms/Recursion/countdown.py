import time
def count(seg):

    print(seg)
    time.sleep(1)

    if seg == 1:
        return 0

    else:
        return count(seg - 1)