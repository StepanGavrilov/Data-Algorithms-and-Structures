import array
import memory_profiler
from loguru import logger

logger.add('debug_DynamicArray.log', format='{time} {level} {message}', level='DEBUG')


class DynamicArrayListBased:
    __slots__ = ('storage', 'len')

    def __init__(self):
        self.storage = []
        self.len = 0

    def add_element(self, element):
        """Добавление элемента в конец"""
        self.storage.append(element)
        self.len += 1

    def pop_element(self):
        """Удаление последнего элемента"""
        if len(self.storage) == 0:
            logger.debug('Dynamic Array debug')
            logger.info('Ошибка, удаление невозможно, так как список пуст.')
            logger.error('IndexError')
            raise IndexError('Ошибка, удаление невозможно, так как список пуст.')
        return self.storage.pop()

    def remove_element(self, element_index):
        if element_index > self.len:
            logger.debug('Dynamic Array debug')
            logger.info('Ошибка, данный индекс больше длины массива.')
            logger.error('IndexError')
            raise IndexError('Ошибка, данного индекса не сщуествует (array.len -> максимальный индекс).')
        del self.storage[element_index]

    def get_element(self, element_index: int):
        """Получить элемент по индексу"""
        if element_index > self.len:
            logger.debug('Dynamic Array debug')
            logger.info('Ошибка, данный индекс больше длины массива.')
            logger.error('IndexError')
            raise IndexError('Ошибка, данного индекса не сщуествует (array.len -> максимальный индекс).')
        return self.storage[element_index]

    def insert_element(self, element, element_index: int, /):
        """Вставка элемента по индексу"""
        if element_index > self.len:
            logger.debug('Dynamic Array debug')
            logger.info('Ошибка, данный индекс больше длина массива.')
            logger.error('IndexError')
            raise IndexError('Ошибка, данного индекса не сщуествует (array.len -> максимальный индекс).')
        self.storage.insert(element_index, element)

    def get_sort(self):
        """Отсортировать массив"""
        return self.storage.sort()

    def clear_array(self):
        """Очистить массив"""
        self.storage.clear()

    def show_storage(self):
        """Показать содержимое массива"""
        print(self.storage)


class DynamicArrayPythonArrayBased:

    def __init__(self, array_type):
        self.storage = array.array(array_type)
        self.len = 0

    def add_element(self, element):
        self.storage.append(element)
        self.len += 1

    def pop_element(self):
        """Удаление последнего элемента"""
        if len(self.storage) == 0:
            logger.debug('Dynamic Array debug')
            logger.info('Ошибка, удаление невозможно, так как список пуст.')
            logger.error('IndexError')
            raise IndexError('Ошибка, удаление невозможно, так как список пуст.')
        return self.storage.pop()

    def remove_element(self, element_index):
        if element_index > self.len:
            logger.debug('Dynamic Array debug')
            logger.info('Ошибка, данный индекс больше длины массива.')
            logger.error('IndexError')
            raise IndexError('Ошибка, данного индекса не сщуествует (array.len -> максимальный индекс).')
        del self.storage[element_index]

    def get_element(self, element_index: int):
        """Получить элемент по индексу"""
        if element_index > self.len:
            logger.debug('Dynamic Array debug')
            logger.info('Ошибка, данный индекс больше длины массива.')
            logger.error('IndexError')
            raise IndexError('Ошибка, данного индекса не сщуествует (array.len -> максимальный индекс).')
        return self.storage[element_index]

    def insert_element(self, element, element_index: int, /):
        """Вставка элемента по индексу"""
        if element_index > self.len:
            logger.debug('Dynamic Array debug')
            logger.info('Ошибка, данный индекс больше длина массива.')
            logger.error('IndexError')
            raise IndexError('Ошибка, данного индекса не сщуествует (array.len -> максимальный индекс).')
        self.storage.insert(element_index, element)

    def clear_array(self):
        """Очистить массив"""
        self.storage.clear()

    def show_storage(self):
        """Показать содержимое массива"""
        print(self.storage)


def dynamic_array_based_list():
    l1 = DynamicArrayListBased()
    l1.add_element(1)
    l1.add_element(10)
    l1.add_element(100)
    l1.show_storage()
    l1.insert_element(0, 1)
    l1.get_element(1)
    return l1


def dynamic_array_based_python_array():
    l1 = DynamicArrayPythonArrayBased('i')
    l1.add_element(1)
    l1.add_element(10)
    l1.add_element(100)
    l1.show_storage()
    return l1


if __name__ == '__main__':
    dynamic_array_based_list()
    dynamic_array_based_python_array()
