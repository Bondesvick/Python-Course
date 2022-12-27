print([1, 2, 3, 4, 5] + [6, 7, 8, 9])


def flatten(arr):
    if len(arr) == 0:
        return []

    if type(arr[0]) == int:
        return [arr[0]] + flatten(arr[1:])

    if type(arr[0]) == list:
        return [] + flatten(arr[0]) + flatten(arr[1:])


print(flatten([1, 2, 3, [4, 5]]))
print(flatten([1, [2, [3, 4], [5], 6, [[7]]]]))

obj1 = {
    "outer": 2,
    "obj": {
        "inner": 2,
        "otherObj": {
            "superInner": 2,
            "notANumber": True,
            "alsoNotANumber": "yup"
        }
    }
}


def nested_even_sum(obj):
    if len(list(obj.values())) == 0:
        return 0

    # print(list(obj.values())[1].values())
    # print(type(obj) == dict)

    if type(list(obj.values())[0]) != int:
        print(obj)
        return 0 + nested_even_sum(dict(list(obj.values())[0])) + nested_even_sum(dict(list(obj.values())[1:]))

    if type(list(obj.values())[0]) == int:
        print(obj)
        print(obj.values())
        print(list(obj.values())[1:])
        return list(obj.values())[0] + nested_even_sum(dict(list(obj.values())[1:]))


print(nested_even_sum(obj1))
