DEBUG = True


def console(*args):
    if DEBUG:
        print(args)


def console_class_type(clas: object):
    if DEBUG:
        print('type({}) = []'.format(clas, type(clas)))
