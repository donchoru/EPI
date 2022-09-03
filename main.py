from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd
import excel_function as ef
import data_object as do

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'E:\MyProjects\EPI\excel-performance-improvements-fb5ec9002bf2.json', scope)

gc = gspread.authorize(credentials)

master_file = gc.open("EPI_MASTER").worksheet('시트1')

master_data = master_file.get_all_values()
master_data = pd.DataFrame(master_data)

do.global_data['시트1'] = master_data

data_dic = {}

need_function = []

for idx, row in master_data.iterrows():
    row_idx = 0
    for value in row:

        if value[0:1] == '=':
            fe = ef.raw_function(value, idx, row_idx, '시트1')
            need_function.append(fe)

        else:
            if idx in data_dic.keys():
                data_dic[idx][row_idx] = value
            else:
                data_dic[idx] = {row_idx:value}
        row_idx += 1