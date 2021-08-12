import tempfile
import os

# @register_cell_magic
def dockerexec(args, cell):
    tmpf, filename = tempfile.mkstemp()
    os.write(tmpf, bytes(cell, "utf8"))
    get_ipython().system("docker exec -i {0} bash < {1}".format(args, filename))
    os.close(tmpf)
    
def load_ipython_extension(ipython):
    """This function is called when the extension is
    loaded. It accepts an IPython InteractiveShell
    instance. We can register the magic with the
    `register_magic_function` method of the shell
    instance."""
    os.environ["PATH"] = "/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin"
    ipython.register_magic_function(dockerexec, 'cell')
