import logging

logging.basicConfig(level=logging.DEBUG)

def hap(a, b):
    ret = a + b
    # print(a, b, ret)     # 함수의 입/출력 확인을 위한 print 구문
    logging.debug(f'debug:{ret}')
    logging.info(f'info:{ret}')
    logging.warning(f'warning:{ret}')
    logging.error(f'error:{ret}')
    logging.critical(f'critical:{ret}')
    
    return ret

result = hap(3, 4)
