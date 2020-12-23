#!/bin/sh

find . -name ".DS_Store" -exec rm {} \;
find . -name ".picasa.ini" -exec rm {} \;
find . -name "*.ini" -exec rm {} \;
find . -name "*.torrent*" -exec rm {} \;
find . -name "*.nfo*" -exec rm {} \;
find . -name "*.NFO*" -exec rm {} \;
find . -name "*.qpw*" -exec rm {} \;
find . -name "*.BUP*" -exec rm {} \;
find . -name "*.IFO*" -exec rm {} \;

find . -name "Torrent downloaded from AhaShare.com.txt" -exec rm {} \;
find . -name "Torrent downloaded from Demonoid.com.txt" -exec rm {} \;
find . -name "Torrent Downloaded From Extra Torrent.txt" -exec rm {} \;
find . -name "Read.Carefully.txt" -exec rm {} \;
find . -name "IMPORTANT.Read carefully before enjoy this movie.txt" -exec rm {} \;
find . -name "DupeDB.com.txt" -exec rm {} \;

find . -type d -empty -delete

#grep -R orrent .
#grep -R ownload .
#grep -R "AhaShare.com" .
#grep -R "Demonoid.com" .
