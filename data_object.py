global_data = {}

def get_data(sheet_name, position):
    if ":" in position:
        return 2
    else:
        low, col = convert_low_col(position)
        return int(global_data[sheet_name][col][low])

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

    return int(low) - 1, int(ord(col))-65

