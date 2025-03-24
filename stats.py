def get_num_words(string_of_words):
    return len(string_of_words.split())

def get_num_chars(string_of_words):
    result_dict = {}
    for char in string_of_words:
        if char.lower() not in result_dict.keys():
            result_dict[char.lower()] = 1
        else:
            result_dict[char.lower()] += 1
    return result_dict

def get_sorted_chars(input_dict):
    output_list = []
    for key, value in input_dict.items():
        if key.isalpha():
            output_list.append({"char": key, "num": value})
    
    def sort_on(dict):
        return dict["num"]

    output_list.sort(reverse=True, key=sort_on)
    return output_list