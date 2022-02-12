# Example-project
![license](https://img.shields.io/github/license/NikMatyukhin/example-project?style=for-the-badge)
![telegram](https://img.shields.io/badge/Telegram-%40nmatyuhin-blue?style=for-the-badge)
![issues](https://img.shields.io/github/issues/NikMatyukhin/example-project?color=red&style=for-the-badge)

## Introduction
A example project's description is a high-level overview of why you’re doing a project.
Its main features are:
- Funny commit history
- Using `sys` module
- I need this project for one lecture
- Cool license

## Example
This is the entire source code for this project:
```python
import sys

def get_system_info(platform: str):
    if 'win' in platform:
        return sys.getwindowsversion()

if __name__ == '__main__':
    info = get_system_info(sys.platform)
    print(info)
```

## License
This project is licensed under the terms of the <a href="https://github.com/NikMatyukhin/example-project/blob/e9b789d3d584a9f2ad8e729fc80d7c84488fc094/LICENSE" target="_blank">MIT license</a>.
