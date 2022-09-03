import re
import data_object as do

class raw_function:
    def __init__(self, function_text, row, col, sheet_name):
        self.__function_text = function_text[1:]
        self.__output = [row, col]
        self.__sheet_name = sheet_name

    def run(self):
        function_type = re.split('[(),]', self.__function_text)[0]
        parameters = re.split('[(),]', self.__function_text)[1:]
        value = self.transaction(function_type, parameters)
        self.save_data(value)


    def save_data(self, value):
        do.set_value(self.__sheet_name, self.__output[1], self.__output[0],value)

    def transaction(self, function_type, parameters):
        value = 0
        if function_type == "SUM":
            print("SUM")
            for param in parameters:
                if param == '':
                    continue

                if self.is_function(param) == True:
                    value += self.run(param)
                else:
                    value += self.get_value(self.__sheet_name, param)

        elif function_type == "MINUS":
            print("MINUS")
            if self.is_function(parameters[0]) == True:
                value_0 = self.run(parameters[0])
            else:
                value_0 = self.get_value(self.__sheet_name, parameters[0])

            if self.is_function(parameters[1]) == True:
                value_1 = self.run(parameters[1])
            else:
                value_1 = self.get_value(self.__sheet_name, parameters[1])

            value = value_0 - value_1
        return value

    def get_value(self, sheet_name, position):
        return do.get_data(sheet_name, position)


    def is_function(self, str):
        if "SUM" in str:
            return True
        elif "MINUS" in str:
            return True
        else:
            False
