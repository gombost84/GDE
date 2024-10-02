from Jarat import Jarat


class BelfoldiJarat(Jarat):

    def __init__(self, jegyar: int, elerhetohelyek: int, *args):

        super().__init__(*args)
        self.jegyar = jegyar
        self.elerhetohelyek = elerhetohelyek
