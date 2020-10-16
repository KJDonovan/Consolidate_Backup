import sys, os, PyPDF2, time, bcf
from PIL import Image

#corrupt_list='/Users/kevindonovan/Desktop/Back_Consolidation/scan_SUBPAR/results_corrupt_finder_20200927_162448/corrupted_images.txt'
#empty_list='/Users/kevindonovan/Desktop/Back_Consolidation/scan_SUBPAR/results_corrupt_finder_20200927_162448/empty_images.txt'
corrupt_list='/Users/kevindonovan/Desktop/Back_Consolidation/scan_test_data/results_corrupt_finder_20200930_123736/corrupted_images.txt'
empty_list='/Users/kevindonovan/Desktop/Back_Consolidation/scan_test_data/results_corrupt_finder_20200930_123736/empty_images.txt'

backups = ['/Users/kevindonovan/Dropbox (MIT)/Pictures KJD']

#Profile backups
backup_list = []
for backup in backups:
    backup_list.append(bcf.make_file_array(backup))

tS = time.time()
timeS = time.strftime('%X %x %Z')

#Read corrupt and empty file lists
cfile=open(corrupt_list,"r")
efile=open(empty_list,"r")
clist=cfile.readlines()
elist=efile.readlines()

celist=clist+elist

results_dir='../results_replacement_finder_'+time.strftime('%Y%m%d_%H%M%S')
os.mkdir(results_dir)

replacements_file='replacement_images.txt'
rfile=open(results_dir+'/'+replacements_file,"a")

for cpath in celist:
    rfile.write('***** Corrupt or empty file: *****\n'+cpath+'\n')
    rfile.write('##### Possible replacements: #####\n')
    c=cpath.rstrip()
    print('Next path:')
    print(cpath)
#    [parentdir, filename]=os.path.split(c)
#    print(filename)
#    print(parentdir)
    split_path=c.split(os.sep)
    split_path.reverse()
#    print(split_path[-1])
#    print(split_path[-2])
    for blist in backup_list:
        for file in blist:
            replacements=[]
            fpath=file.split(os.sep)
            fpath.reverse()
            dir_levels=min(len(split_path), len(fpath))
            for i in range(dir_levels,1):
                if (split_path[0:i] == fpath[0:i]):
                    print(file)
                    score = len(fpath)
                    #Is it corrupt or empty?
                    if (os.path.getsize(filename) == 0):
                        print('Found matching path but file is empty')
                    elif (bcf.jpg_png_empty_or_corrupt(filename) == 1):
                        print('Found matching path but file is corrupt')
                    else:
                        print('Found matching path with file seemingly ok')
                        replacements.append([score,file])
            replacements=sorted(replacements)
            for replace in replacements:
                rfile.write(replace[1]+'\n')
    rfile.write('##### End possible replacements: #####\n\n')

rfile.close()