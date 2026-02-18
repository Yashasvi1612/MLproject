import sys # this libraray is used to manipulate different parts of python runtime environment


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # this will give us the exception info, like filename and line number where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename # this will give us the file name where the error occurred
    line_number = exc_tb.tb_lineno # this will give us the line number where the error occurred
    error_message = f"Error occured in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]" # this will give us the error message
    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) 
        self.error_message = error_message_detail(error_message,error_detail) 

    def __str__(self):
        return self.error_message # this will return the error message when we print the exception