# arr1 = [1, 2, 3, 4]
# arr2 = list(range(len(arr1)))

# print(len(arr2))
# for i in range(0, len(arr1)):
#     temp = 0
#     if i != 0:
#         for j in range(0, i):
#             temp = temp + arr1[j]
#     arr2[i] = temp

def sumPrev(arr, n):
    if n == 1:
        return arr[0]
    else:
        return arr[n - 1] + sumPrev(arr, n - 1)


# def sumofprevelems(arr1):
#     n = len(arr1)
#     arr2 = list(range(n))

#     start = 0
#     for i in range(start, len(arr1)):
#         if i == 0:
#             arr2[0] == 0
#         else:
#             arr2[i] = sumPrev(arr1[start: i], i)

#     return arr2


# def sumofprevrec(arr1, arr2, n):

#     if n == 0:
#         return arr2
#     else:
#         if n == 1:
#             arr2.insert(0, 0)
#             return
#         if n == 2:
#             arr2.insert(0, arr1[0])
#         else:
#             arr2.insert(0, sumPrev(arr1, n - 1))

#         sumofprevrec(arr1, arr2, n - 1)
#     # else:
#     #     total = arr1[0] + sumofprevelems(arr1, arr2)
#     #     arr2.append(total)
#     #     return total


def sumofprevrec(arr1, n):
    if n == 1:
        return [0]
    else:
        sum = sumPrev(arr1, n - 1)
        return sumofprevrec(arr1[:n-1], n - 1) + [sum]


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    n = 4

    print(sumofprevrec(arr1, n))
