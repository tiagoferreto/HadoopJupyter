import pandas as pd
from io import StringIO
import tempfile
import os
import pandas as pd
from io import StringIO

def csv(line, cell):
    sio = StringIO(cell)
    return pd.read_csv(sio)

# @register_cell_magic
def dockerexec(args, cell):
    tmpf, filename = tempfile.mkstemp()
    os.write(tmpf, bytes(cell, "utf8"))
    get_ipython().system("/usr/local/bin/docker exec -i {0} bash < {1}".format(args, filename))
#     !docker exec -i {args} bash < {filename}
    os.close(tmpf)

# substitute bash magic
# writes line by line to output
# @register_cell_magic
# def bash(args, cell):
#     tmpf, filename = tempfile.mkstemp()
#     os.write(tmpf, bytes(cell, "utf8"))
#     !bash < {filename}
#     os.close(tmpf)

# def dockerscreen(line, cell):
#     args = line.split()
#     if args == '
# screen -d -m -S pig -L -Logfile pig.output -s bash /opt/pig/bin/pig
# screen -S pig -p 0 -X stuff "stations = LOAD 'stations.csv' USING PigStorage(',') AS 
# (station_id:int, name:chararray, lat:float, long:float, 
#  dockcount:int, landmark:chararray, installation:chararray);\n"
# screen -S pig -p 0 -X stuff "DESCRIBE stations;\n"
# screen -S pig -X quit
# # screen documentation - https://www.gnu.org/software/screen/manual/screen.html


def write_and_run(line, cell):
    argz = line.split()
    file = argz[-1]
    mode = 'w'
    if len(argz) == 2 and argz[0] == '-a':
        mode = 'a'
    with open(file, mode) as f:
        f.write(cell)
    get_ipython().run_cell(cell)
    
def load_ipython_extension(ipython):
    """This function is called when the extension is
    loaded. It accepts an IPython InteractiveShell
    instance. We can register the magic with the
    `register_magic_function` method of the shell
    instance."""
    os.environ["PATH"] = "/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin"
    ipython.register_magic_function(csv, 'cell')
    ipython.register_magic_function(dockerexec, 'cell')

#%load_ext dockermagic
    
# dockerexec magic
# from IPython.core.magic import register_cell_magic


# @register_cell_magic
# def csv(line, cell):
#     # We create a string buffer containing the
#     # contents of the cell.
#     sio = StringIO(cell)
#     # We use Pandas' read_csv function to parse
#     # the CSV string.
#     return pd.read_csv(sio)

# @register_cell_magic
# def dockerscreen(args, cell):
#     tmpf, filename = tempfile.mkstemp()
#     os.write(tmpf, bytes(cell, "utf8"))
#     !docker exec -i {args} bash < {filename}
#     os.close(tmpf)
