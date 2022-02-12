import sys


def get_system_info(platform: str):
    if 'win' in platform:
        return sys.getwindowsversion()


if __name__ == '__main__':
    info = get_system_info(sys.platform)
    print(info)
