from textwrap import wrap

def pretty_print(*content):
    width = 50

    print('\n+-' + '-' * width + '-+')

    for c in content:
        for line in wrap(c, width):
            print('| {0:^{1}} |'.format(line, width))
        print('+-' + '-'*(width) + '-+')
