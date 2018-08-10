import vim
import config_loader
import subprocess

def force_sync():
    for element in config_loader.cfg_mgr_singlen.get_all_files():
        for file_path in file_sync_mgr_singleton.get_file():
            p = subprocess.Popen([element["command"], file_path, element["dest"]],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         shell=False)
            out = p.stdout.readline()
            if out is not b'':
                print(out)
            out = p.stderr.readline()
            if out is not b'':
                print(out)
                return
        file_sync_mgr_singleton.clean_file()

class file_sync_mgr:
    def __init__(self):
        self.recent_list = set('')

    def add_file(self, file_name):
        self.recent_list.add(file_name)

    def get_file(self):
        return self.recent_list

    def clean_file(self):
        self.recent_list = set('')

file_sync_mgr_singleton = file_sync_mgr()
