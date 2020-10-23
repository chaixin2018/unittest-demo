import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='a')
# mode=w 为覆盖，mode=a 为追加

# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename='my.log', level=logging.WARNING, format=LOG_FORMAT)
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warn message')
# logging.error('error message')
# logging.critical('critical message')

# logging.basicConfig(level=logging.ERROR)
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warn message')
# logging.error('error message')
# logging.critical('critical message')


logger = logging.getLogger()
logger.setLevel('DEBUG')
BASIC_FORMAT = "%(asctime)s:%(levelname)s:%(message)s"
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
chlr = logging.StreamHandler() # 输出到控制台的handler
chlr.setFormatter(formatter)
chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level
fhlr = logging.FileHandler('example.log') # 输出到文件的handler
fhlr.setFormatter(formatter)
logger.addHandler(chlr)
logger.addHandler(fhlr)
logger.info('this is info')
logger.debug('this is debug')
