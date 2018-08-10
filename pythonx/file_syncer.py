import vim
import config_loader
import subprocess


def force_sync():
    for element in config_loader.cfg_mgr_singlen.get_all_files():
        p = subprocess.Popen([element["command"], "-r", "a.out", element["dest"]],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE,
                     shell=False)
        out = p.stdout.readline()
        if out is not b'':
            print(out)
        out = p.stderr.readline()
        if out is not b'':
            print(out)

