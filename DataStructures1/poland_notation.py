from DataStructures1.dynamic_array import DynamicArrayListBased

operators = ['+', '-', '/', '*']


def to_poland_notation(expression: str):
    number_stack = DynamicArrayListBased()
    operations = DynamicArrayListBased()

    for i in expression:
        if i in operators:
            operations.add_element(i)
        else:
            number_stack.add_element(i)

    for i in operations.storage:
        number_stack.add_element(i)

    print(number_stack.storage)


print(to_poland_notation('3+4*7'))
