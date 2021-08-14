import tempfile
import os
import platform

# @register_cell_magic
def dockerexec(args, cell):
    cell = cell.split('\n',1)[1]
    tmpf, filename = tempfile.mkstemp(dir='.')
    os.write(tmpf, bytes(cell, "utf8"))
    if platform.system() == "Windows" :
        get_ipython().run_cell_magic("bash","","docker exec -i {0} bash < {1}".format(args, os.path.basename(filename)))
    else :
        get_ipython().system("docker exec -i {0} bash < {1}".format(args, filename))
    os.close(tmpf)
    os.remove(os.path.basename(filename))
    
def load_ipython_extension(ipython):
    """This function is called when the extension is
    loaded. It accepts an IPython InteractiveShell
    instance. We can register the magic with the
    `register_magic_function` method of the shell
    instance."""
    os.environ["PATH"] = "/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin"
    ipython.register_magic_function(dockerexec, 'cell')
