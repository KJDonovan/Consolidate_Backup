#!/bin/sh

scriptdir=/Users/kevindonovan/Desktop/Back_Consolidation/scan_Media/Consolidate_Backup

mdir=/Volumes/photo/Pictures\ KJD
dir2delete1=/Volumes/SUBPAR/Pictures\ KJD
dir2delete2=/Volumes/SUBPAR/Walden/Pictures_HOME_DIRECTORY
dir2delete3=/Volumes/SUBPAR/Walden/RETURN_TO_HOME_DIRECTORY_archive/Thousand\ Islands
dir2delete4=/Volumes/SUBPAR/Users/kevindonovan/Dropbox\ \(MIT\)/Pictures_HOME_DIRECTORY
dir2delete5=/Volumes/SUBPAR/Archive\ KJD/Pictures\ KJD
badir=/Volumes/SUBPAR

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

clear_clutter $dir2delete1
clear_clutter $dir2delete2
clear_clutter $dir2delete3
clear_clutter $dir2delete4
clear_clutter $dir2delete5
#clear_clutter $badir/ok_to_delete

cd $scriptdir

python3 move_photos_to_delete_SUBPAR.py

cd $dir2delete1
find . -type d -empty -delete
cd $dir2delete2
find . -type d -empty -delete
cd $dir2delete3
find . -type d -empty -delete
cd $dir2delete4
find . -type d -empty -delete
cd $dir2delete5
find . -type d -empty -delete

cd $scriptdir