def insertion_sort(data):
    try:
        for index in range(1, len(data)):
            insertion_item = data[index]  # Куда будем вставлять
            prev_element = index - 1  # Указатель для предыдущего элемента (Индекс)
            while prev_element >= 0 and data[prev_element] > insertion_item:
                data[prev_element + 1] = data[prev_element]  # Меняем меньший на больший
                prev_element -= 1  # Берём индекс большего элемента
            data[prev_element + 1] = insertion_item  # Ставим меньший элемент
        return data
    except TypeError:
        print('Неверный тип входных данных!')
        return 'Error'