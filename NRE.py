import Str
import Args
import Var

src = open('Main.n', 'r')

while True:
    ln = src.readline()
    if ln.startswith('write:'):
        msgs = Args.args(ln, 'write:', '&')
        Str.write(msgs)
    elif ln.startswith('var:'):
        args = Args.args(ln, 'var:', '=')
        Var.var(args)

    elif ln.startswith('end'):
        break
