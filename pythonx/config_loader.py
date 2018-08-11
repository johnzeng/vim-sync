import vim
import json

class config_manager:
    def __init__(self, root_path):
        try:
            self.root_path = root_path
            self.marked = []
            self.load_array = None
            self.err = None
            with open(root_path + '/.vim-sync', 'r') as f:
                self.load_array = json.load(f)
                for element in self.load_array:
                    if element['dest'][-1] != '/':
                        element['dest'] = element['dest'] + '/'
                    if 'sync_frequence' not in element:
                        element['sync_frequence'] = 1
                    if 'command' not in element:
                        element['command'] = 'cp'

                    if 'marked' in element and element['marked'] == 1:
                        self.marked.append(element)

            self.is_load = True

        except Exception as err :
            self.err = err
            self.is_load = False
            self.load_array = []

    def reload(self):
        self.__init__(self.root_path)
        if self.err is not None:
            print(str(self.err))

    def is_loaded(self):
        return self.is_load

    def get_marked(self):
        return self.marked

    def get_all_files(self):
        return self.load_array

    def get_all_file_names(self):
        vim.command('let g:all_vim_sync_dest=[]')
        for element in self.load_array:
            vim.command('call add(g:all_vim_sync_dest, "%s")' % element["dest"])

cfg_mgr_singlen = None

def get_config_manager(root_path):
    global cfg_mgr_singlen
    if cfg_mgr_singlen is None:
        cfg_mgr_singlen = config_manager(root_path)
    return cfg_mgr_singlen

