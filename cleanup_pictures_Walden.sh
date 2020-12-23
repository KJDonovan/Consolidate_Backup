#!/bin/sh

scriptdir=/Users/kevindonovan/Desktop/Back_Consolidation/scan_Media/Consolidate_Backup

mdir=/Volumes/photo/Pictures\ KJD
dir2delete_list=/Volumes/photo/Pictures_KJD_maybe_dupe
badir=/Volumes/photo

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
#clear_clutter $badir/ok_to_delete

cd $scriptdir

python3 move_photos_to_delete.py

cd $dir2delete_list
find . -type d -empty -delete

cd $scriptdir