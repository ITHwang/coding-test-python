def solution(phone_book):
    n = len(phone_book)
    for i in range(n - 1):
        for j in range(i + 1, n):
            phone1 = phone_book[i]
            phone2 = phone_book[j]
            if phone1.find(phone2) == 0 or phone2.find(phone1) == 0:
                return False
    return True
