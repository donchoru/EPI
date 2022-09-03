global_data = {}

def get_data(sheet_name, position):
    if ":" in position:
        return 2
    else:
        low, col = convert_low_col(position)
        return int(global_data[sheet_name][col][low])


def set_value(sheet_name, col, row, value):
    print(sheet_name)
    print(col)
    print(row)
    print(value)

#여기에.. AA에 대한 것도 들어가야한다..
def convert_low_col(position):
    print('position : ' + position)
    low = ''
    col = ''

    for char in list(position):
        if char.isdigit() == False:
            col += char
        else :
            low += char

    return int(low) - 1, col2num(col)

def change_col_row_type(self, col, row):
    pass




def col2num(col):
    num = 0
    for c in col:
        num = num * 26 + (ord(c.upper()) - ord('A'))
    return num

def column_num_to_string(n):
    n, rem = divmod(n - 1, 26)
    next_char = chr(65 + rem)
    if n:
        return column_num_to_string(n) + next_char
    else:
        return next_char

