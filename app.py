import blessings

def draw_window(term, x, y, width, height, title='', text_content=''):
    with term.location(x, y):
        print('┌' + '─' * (width - 2) + '┐')
    for i in range(1, height - 1):
        with term.location(x, y + i):
            print('│' + ' ' * (width - 2) + '│')

    with term.location(x, y + height - 1):
        print('└' + '─' * (width - 2) + '┘')
    if title:
        title_x = x + (width - len(title)) // 2
        with term.location(title_x, y):
            print(term.bold + ' ' + title + ' ' + term.normal)
    if text_content:
        lines = text_content.split('\n')
        for i, line in enumerate(lines):
            if i < height - 2:
                with term.location(x + 2, y + i + 1):
                    print(line[:width - 4])

if __name__ == '__main__':
    term = blessings.Terminal()
    print(term.clear)
    draw_window(term, 2, 0, 50, 15)
    with term.location(50, 2):
        print(term.bold_blue("Ola"))

