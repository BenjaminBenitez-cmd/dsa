arr = [4, 5, 3, 9, 8]

if len(arr) <= 0:
    print()


def smallestKth(arr, k):
    if not arr or len(arr) < 0:
        return "Invalid"

    new_arr = arr[0:k]

    for i in range(len(new_arr)):
        for j in range(len(new_arr) - i - 1):
            if new_arr[j] > new_arr[j + 1]:
                temp = new_arr[j]
                new_arr[j] = new_arr[j+1]
                new_arr[j + 1] = temp

    return new_arr[0]


def countSort(arr, n, exp):
    output = [0] * n  # Output array
    count = [0] * n

    for i in range(n):
        count[i] = 0

    # store count of occurrances in count[]
    for i in range(n):
        count[(arr[i]) // exp % n] += 1

    # change count[i] so that count[i] now contains
    # actual position of this digit in output[]

    for i in range(1, n):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        output[count[(arr[i] // exp) % n] - 1] = arr[i]
        count[(arr[i] // exp) % n] -= 1

    # copy the output array to arr[], so that
    # arr[] now contains sorted numbers according
    # to current digit
    for i in range(n):
        arr[i] = output[i]


def sort(arr, n):

    countSort(arr, n, 1)

    countSort(arr, n, n)


if __name__ == "__main__":
    # since array size is 7, elements should
    # be from 0 to 48
    k = 3
    arr = [40, 12, 45, 32, 33, 1, 22]
    # arr = arr[:k]
    n = len(arr)
    print("Given array is")
    print(*arr)

    sort(arr, n)

    print("Sorted array is")
    print(*arr)
