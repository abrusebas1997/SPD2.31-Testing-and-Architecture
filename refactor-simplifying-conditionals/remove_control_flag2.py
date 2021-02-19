n = 16
file = 'foobar.file'

def readfile(file, n):
    with open(file, 'rb') as fp:
        chunk = fp.read(n)
        if chunk == '': # end of file, stop running.
            return
        print(chunk)
        # process(chunk)

readfile(file, n)
