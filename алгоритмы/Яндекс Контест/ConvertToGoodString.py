# import re
# def convert_to_good_string(probably_bad_string: str) -> str:
#     newpbs = 0
#     pbs = re.sub(r"(?-i:([a-zA-Z])(?!\1)(?i:\1))", "", probably_bad_string)
#     while len(pbs) != newpbs:
#         newpbs = len(pbs)
#         pbs = re.sub(r"(?-i:([a-zA-Z])(?!\1)(?i:\1))", "", pbs)
#
#     return ''.join(pbs)
#
# probably_bad_string = input()
# print(convert_to_good_string(probably_bad_string))


def convert_to_good_string(probably_bad_string: str) -> str:
    pbs = list(probably_bad_string)
    index = []
    newpbs = 0
    i = 0
    upperalpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while i < len(pbs):
        if str(pbs[i]) in upperalpha:
            index.append(i)
            i += 1
        else:
            i += 1

    while len(pbs) != newpbs:
        newpbs = len(pbs)
        indexnew = []
        for j in index:
            if str(pbs[j].lower()) == str(pbs[j-1]) and j > 0:
                del(pbs[j], pbs[j-1])
            else:
                indexnew.append(j)
        print (indexnew)
        index = indexnew.copy()
    return ''.join(pbs)

probably_bad_string = input()
print(convert_to_good_string(probably_bad_string))