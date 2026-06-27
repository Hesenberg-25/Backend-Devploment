from contextlib import contextmanager

@contextmanager
def open_file(filename,mode):
    f=open(filename,mode)
    yield f
    f.close()

with open_file('sample.txt','w') as f:
    f.write("What to write")
    print(f.closed)
    
print(f.closed)
