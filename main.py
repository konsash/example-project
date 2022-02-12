import sys
import time
import random


def get_system_info(platform: str):
    if 'win' in platform:
        return sys.getwindowsversion()
    else:
        return 'Linux, macOS, idk'


if __name__ == '__main__':
    start = time.time()
    info = get_system_info(sys.platform)
    time.sleep(random.randint(1, 10))
    
    print(info)
    print(f'Total time: {time.time() - start} sec')
