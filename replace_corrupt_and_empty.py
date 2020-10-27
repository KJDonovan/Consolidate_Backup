import sys, os, time, bcf

#corrupt_list='/Users/kevindonovan/Desktop/Back_Consolidation/scan_SUBPAR/results_corrupt_finder_20200927_162448/corrupted_images.txt'
#empty_list='/Users/kevindonovan/Desktop/Back_Consolidation/scan_SUBPAR/results_corrupt_finder_20200927_162448/empty_images.txt'
corrupt_list='/Users/kevindonovan/Desktop/Back_Consolidation/scan_test_data/results_corrupt_finder_20200930_123736/corrupted_images.txt'
empty_list='/Users/kevindonovan/Desktop/Back_Consolidation/scan_test_data/results_corrupt_finder_20200930_123736/empty_images.txt'

backups = ['/Users/kevindonovan/Dropbox (MIT)/Pictures KJD']

#Profile backups
backup_list = []
for backup in backups:
    backup_list.append(bcf.make_file_array(backup))
#print('backup_list: ',backup_list)

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
    print('Find replacements for:\n'+cpath)
    rfile.write('***** Corrupt or empty file: *****\n'+cpath+'\n')
    rfile.write('##### Possible replacements: #####\n')
    c=cpath.rstrip()
    split_path=c.split(os.sep)
    split_path.reverse()
    # Remove empty elements
    split_path=list(filter(None,split_path))
    for blist in backup_list:
        for file in blist:
            replacements=[]
            fpath=file.split(os.sep)
            fpath.reverse()
            # Remove empty elements
            fpath=list(filter(None,fpath))
            if (split_path[0] == fpath[0]):
                print('Found a match:\n'+file)
                dir_levels=min(len(split_path), len(fpath))
                if (os.path.getsize(file) == 0):
                    print('Found matching filename but file is empty')
                    break
                elif (bcf.jpg_png_empty_or_corrupt(file) == 1):
                    print('Found matching filename but file is corrupt')
                    break
                else:
                    print('Found matching filename and file is seemingly ok')
                    for i in range(dir_levels,0,-1):
                        if (split_path[0:i] == fpath[0:i]):
                            replacements.append([i,file])
#                            print('Found the most similar path!')
                            print('*******************************\n')
                            break
            if (len(replacements) != 0):
                replacements=sorted(replacements,reverse=1)
                for replace in replacements:
                    rfile.write(str(replace[0])+', '+str(replace[1])+'\n')
    rfile.write('##### End possible replacements: #####\n\n')

rfile.close()