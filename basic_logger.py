import inspect
import logging
import os
import test
# Step 1: Import your program here

filename = 'my_log.log'

def main():
    if os.path.isfile(filename):
        os.remove(filename)

    logging.basicConfig(filename=filename, format='%(asctime)s %(message)s',
                        level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started logging')                             
    
    # Step 2: 
    # In the other program, 
    # import logging, 
    # import inspector
    # from debug_line import DEBUG_LINE
    
    # Whereever you want to log, add the line
    # logging.debug(DEBUG_LINE.format(inspect.stack()[0][3], __name__, 
    #                                 inspect.stack()[1][3]))

    # Step 3: Call the other program
    
    test.func()

    logging.info('Finished logging')


if __name__ == '__main__':
    main()