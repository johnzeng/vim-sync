
if ! has('python3')
    exit
endif

"load config loader
py3 import config_loader
py3 import file_syncer

let cwd = getcwd()
let load_cmd = 'py3 config_loader.get_config_manager("'.cwd.'")'

execute load_cmd

function VimForceSyncFun()
    py3 file_syncer.force_sync()
endfun

command -nargs=0 VimForceSync call VimForceSyncFun()

function VimSyncAddFile()
    let cur_file = expand('%')
    let cmd = 'py3 file_syncer.file_sync_mgr_singleton.add_file("'.cur_file.'")'
    execute cmd
endfun

au BufWritePost * call VimSyncAddFile()
