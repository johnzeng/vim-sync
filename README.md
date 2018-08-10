# vim-sync

Allow you to sync your file to multi dirs automaticly. 

# Config

## root file
create a file in the root of your project, name it as '.vim-sync', and the file should contain a json:

```
[
{"dest": "/path/you/wanna/sync",
"cmd": "cp by default",
"sync_frequence":60,
"marked":1},
{"dest": "/another/path/you/wanna/sync",
"cmd": "cp by default",
"sync_frequence":100}
]
```

And this script will sync your local file to the dests every ${sync_frequence} seconds.

## vim config

### ignore files
let vim_sync_ignore_files="tmp|.svn|.git|*.o"

# Command

## force to sync all
`:VimSyncAll`

## force to sync one dest

`:VimSyncOne`

Then it will pop a menu to let you select which dest you wanna sync

## force to sync to marked dest

`:VimSyncMarked`
