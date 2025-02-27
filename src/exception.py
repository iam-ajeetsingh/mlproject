# sys package is used to manipulate the python runtime environment information.
import sys 
#import logging   # this is the generic logging module.
from src.logger import logging  # we are suppoed to use the logging object from the logger module not the genric logging module. 


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in Python script name [{0}] line number [{1}] error message [{2}]".format(
     file_name, exc_tb.tb_lineno, str(error))
    return error_message



class Custom_Exception(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail= error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        a = 5/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise Custom_Exception(e, sys)