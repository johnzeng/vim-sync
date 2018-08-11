import vim
import config_loader
import subprocess

def force_sync():
    file_sync_mgr_singleton.force_sync()

def do_sync():
    file_sync_mgr_singleton.do_sync()

class file_sync_mgr:
    def __init__(self):
        self.recent_list = {}
        self.sync_timer = {}
        for element in config_loader.cfg_mgr_singlen.get_all_files():
            self.recent_list[element["dest"]] = set('')

    def force_sync(self):
        do_sync(True)

    def do_sync(self, is_force = False):
        for element in config_loader.cfg_mgr_singlen.get_all_files():
            print("check")
            if is_force is False:
                if element["dest"] in self.sync_timer:
                    self.sync_timer[element["dest"]] = self.sync_timer[element["dest"]] + 1
                    print("tick")
                else:
                    self.sync_timer[element["dest"]] = 1
                    print("init tick")

                if self.sync_timer[element["dest"]] < element["sync_frequence"]:
                    continue
                else:
                    print("reset")
                    self.sync_timer[element["dest"]] = 0

            for file_path in self.get_file(element["dest"]):
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
            self.clean_file(element["dest"])

    def add_file(self, file_name):
        if file_name == '.vim-sync':
            config_loader.cfg_mgr_singlen.reload()
            return
        if not config_loader.cfg_mgr_singlen.is_loaded():
            return
        for key in self.recent_list:
            self.recent_list[key].add(file_name)

    def get_file(self, dest):
        return self.recent_list[dest]

    def clean_file(self, dest):
        self.recent_list[dest] = set('')

file_sync_mgr_singleton = file_sync_mgr()
