# data format: lineNumber AcctNo lineNumberForEachAcctNo TableName TimeStamp # FieldName=FieldValue FieldValue=FieldValue ...

# parse the part before #


def parse_front(line):
    front = line.split('#')[0]
    list = []
    for element in front.split(): # split with whitespace, add each into a list
        list.append(element)
    if len(list) != 6:
        print("unpexceted data length, error list: ") # check the length of the list
        print(list)
        return -1
    datetime = list[4]+' '+list[5] # merge the date and time into datetime
    list[4] = datetime
    del list[5]
    return list


# parse the part after #

def parse_rear(line):
    rear = line.split('#')[1]
    dict = {}
    for element in rear.split(): # put every pair into a dict, if there are several pairs that hav the same fieldname, the latter overlaps the previous
        f_name = element.split('=')[0]
        f_value = element.split('=')[1]
        dict[f_name]=f_value
    return dict

