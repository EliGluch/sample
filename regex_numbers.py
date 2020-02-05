import re

#
# def find_num_format(str):
#     """
#     finds first match of pattern number.number:number in str
#     :param str:
#     :return: string if found
#     """
#     pattern = r'\d+\.\d+:\d+'
#     search_obj = re.search(pattern, str)
#     if search_obj:
#         return search_obj.group()
#
#
# tests = ["word 12.12 34.34:44", "55.55", "66.66.77:88"]
# for test in tests:
#     print(test + " result: ", find_num_format(test))

def ex_words(my_string):
    pattern = r'\bex\w*\b' #finds all words starting with ex
    return re.findall(pattern,my_string)


tests_ex = ["exam the execution", "texas starts with ex excuse "]

for test in tests_ex:
    print(test + " result: ", ex_words(test))


def is_ipv6(my_string):
   pattern = r"((?:[1-9a-fA-F][0-9a-fA-F]{0,3})|0:){7}([1-9a-fA-F][0-9a-fA-F]{0,3})|0"
