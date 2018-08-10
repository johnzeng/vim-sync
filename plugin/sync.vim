
if ! has('python3')
    exit
endif

"load config loader
py3 import config_loader

let cwd = getcwd()
let load_cmd = 'py3 config_loader.get_config_manager("'.cwd.'")'

execute load_cmd


