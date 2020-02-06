"""Нужно написать функцию, которая позволит Вам конвертировать указанное Вами число секунд
в формат записи дни:часы:минуты:секунды"""


def fun_watch(sec):
    """fun_watch converts the specified number of seconds into format dd:hh:mm:ss"""
    dd = sec // (3600 * 24)
    hh = sec % (3600 * 24) // 3600
    mm = sec % (3600 * 24) % 3600 // 60
    ss = sec % (3600 * 24) % 3600 % 60
    print("Your", sec, "seconds in dd:hh:mm:ss format are: ", dd, ":", hh, ":", mm, ":", ss)
    return


Sec = int(input("Input the number of seconds:\n"))
fun_watch(Sec)
