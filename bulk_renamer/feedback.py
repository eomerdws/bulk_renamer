from sty import fg, bg, ef, rs, RgbFg


class Feedback:
    def __init__(self):
        self.msg = None
        self.type = ('log', 'warn', 'error')

    def log(self, msg):
        print(msg)

    def warn(self, msg):
        print(fg.yellow + msg + fg.rs)

    def error(self, msg):
        print(fg.red + msg + fg.rs)
