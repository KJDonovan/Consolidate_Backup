#!/bin/sh

scriptdir=/Users/kevindonovan/Desktop/Back_Consolidation/scan_Media/Consolidate_Backup

mdir=/Volumes/photo
dir2delete_list=/Users/kevindonovan/Dropbox\ \(MIT\)/Pictures\ KJD/Already\ on\ SUBPAR
badir=/Users/kevindonovan/Dropbox\ \(MIT\)

clear_clutter()
{
    dir2clear=$1
    cd $dir2clear
    pwd
    find . -name ".DS_Store" -exec rm {} \;
    find . -name ".picasa.ini" -exec rm {} \;
    find . -name "*.ini" -exec rm {} \;
    find . -name ".BridgeSort" -exec rm {} \;
    find . -type d -empty -delete
}

clear_clutter $dir2delete_list
clear_clutter $badir/ok_to_delete

cd $scriptdir

python3 move_photos_to_delete.py

