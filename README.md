# vim-sync

Allow you to sync your file to multi dirs automaticly. 

# Config

## root file
create a file in the root of your project, name it as '.vim-sync', and the file should contain a json:

```
[
{"dest": "/path/you/wanna/sync",
"cmd": "cp by default",
"sync_frequence":1,
"marked":1},
{"dest": "/another/path/you/wanna/sync",
"cmd": "cp by default",
"sync_frequence":2}
]
```

And this script will sync your local file to the dests every ${sync_frequence} minutes.


Field | Type | Desc
------- | ------- | -------  
dest | string | the dest dir you wanna copy to, can be relative path or real path,  event a net address is support
cmd | string | the command you wanna call when sync is triggered
marked | int | 0 by default. 0: not marked, 1: marked. A marked dest can be synced by VimSyncMarked command
sync_frequence | int | how frequently this dest will be synced in minutes

## vim config

### ignore files
let g:vim_sync_exclude_list='(tmp)|(test)|.*\.'
support regular exp

# Command

## force to sync all
`:VimSyncAll`

## force to sync one dest

`:VimSyncOne`

Then it will pop a menu to let you select which dest you wanna sync

## force to sync to marked dest

`:VimSyncMarked`


