def Re(array):
    for item in array:
        if(type(item) is list):
            Re(item)
    array.reverse()
    return array


if __name__ == "__main__":
    i = [1, [12, 3, [4, [5, 16]]]]
    result = Re(i)
    print(result)
