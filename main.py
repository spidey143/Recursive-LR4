import os


def way():
    pass


def dictionary(path):
    res = {}
    for filename in os.listdir(path):
        current_path = os.path.join(path, filename)
        if os.path.isdir(current_path):
            res.update(dictionary(current_path))
        else:
            res.update({current_path: os.path.getsize(current_path)})
    return res


def duplicate():
    pass


def my_print():
    pass


if __name__ == '__main__':
    pass
