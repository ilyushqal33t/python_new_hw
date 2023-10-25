import os
from collections import namedtuple
import logging

logger = logging.getLogger(__name__)
my_format = '{asctime:<20} - {levelname:<10} - {msg}'
logging.basicConfig(filename='mylog.log', filemode='w', encoding='UTF-8', level=logging.INFO,
                    format=my_format, style='{')


def walker(path: str = os.getcwd()):
    File = namedtuple('File', ['name', 'extension', 'is_dir', 'root'])
    Directory = namedtuple('Directory', ['name', 'is_dir', 'root'])
    for root, dir, file in os.walk(path):
        for name in file:
            final_name = name.split('.')[0]
            extension = name.split('.')[1]
            new_file = File(final_name, extension, False, root)
            logger.info(msg=f'Type obj: {type(new_file)}. File name: {new_file.name}, '
                            f'extension: {new_file.extension}, is dir: {new_file.is_dir}, root: {new_file.root}')

        for name in dir:
            new_dir = Directory(name, True, root)
            logger.info(msg=f'Type obj: {type(new_dir)}. File name: {new_dir.name}, '
                            f'is dir: {new_dir.is_dir}, root: {new_dir.root}')


walker()