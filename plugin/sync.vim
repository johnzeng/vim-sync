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

command -nargs=0 VimSyncAll call VimForceSyncFun()

if !exists('g:vim_sync_exclude_list')
    let g:vim_sync_exclude_list='(tmp)|(test)|.*\.'
endif

let g:vim_sync_exclude_list = escape(g:vim_sync_exclude_list, '()|')

function Test()
    let cur_file = expand('%')
    
    echo match(cur_file, g:vim_sync_exclude_list)
endfun

function VimSyncAddFile()
    let cur_file = expand('%')
    if match(cur_file, g:vim_sync_exclude_list) != -1
        return
    endif
    let cmd = 'py3 file_syncer.file_sync_mgr_singleton.add_file("'.cur_file.'")'
    execute cmd
endfun

au BufWritePost * call VimSyncAddFile()
func SyncVimTimerHandler(timer)
    call VimForceSyncFun()
endfunc
let timer = timer_start(60000, 'SyncVimTimerHandler',
            \ {'repeat': -1})
