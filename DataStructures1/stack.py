from DataStructures1.dynamic_array import DynamicArrayListBased


class Stack(DynamicArrayListBased):
    def __init__(self):
        super().__init__()

    def insert_element(self, element, index: int):
        raise NotImplementedError('This is stack')

    def remove_element(self, element_index):
        raise NotImplementedError('This is stack')

    def get_element(self, element_index: int):
        raise NotImplementedError('This is stack')

    def clear_array(self):
        raise NotImplementedError('This is stack')


# stack1 = Stack()
# for i in range(10):
#     stack1.add_element(1)
# stack1.show_storage()