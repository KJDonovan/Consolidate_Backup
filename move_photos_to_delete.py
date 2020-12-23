import os, sys, bcf, time, fnmatch, datetime

#These file types can be deleted:
#% find . -name ".DS_Store" -exec rm {} \;
#% find . -name ".picasa.ini" -exec rm {} \;
#% find . -name ".BridgeSort" -exec rm {} \;

#testfile='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation_testcopy1/music_test#_backup_consolidation/Dave Brubeck - Unsquare Dance.mp3'
#basedir_test='Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/'
#bcf.move_to_delete(testfile,basedir_test)

#mdir='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/main_test_data_backup_consolidation'
#dir2delete_list=['/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation_testcopy1/photos_test_backup_consolidation']
##If uncommented, the following command should cause abort
##dir2delete_list=['/Volumes/photo/Pictures KJD']
#badir='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation'

#Testing other file types for corrupt images:
nef_sample_corrupt='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/corrupted_images_backup_consolidation/DSC_8776_corrupt.NEF'
nef_sample='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/DSC_8776.NEF'

dng_sample_corrupt='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/corrupted_images_backup_consolidation/DSC_8812_corrupt.dng'
dng_sample='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/DSC_8812.dng'

gif_sample='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/IMG_0419-MOTION.gif'
gif_sample_corrupt='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/corrupted_images_backup_consolidation/IMG_0419-MOTION_corrupt.gif'

bmp_sample='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/IMG_0426.bmp'

tif_sample='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/MomGrandpaDancing.tif'

#ai_sample='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/Letter\ to\ Friends.ai'

psd_sample='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/Grad1.psd'

tiff_sample='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/Image16.tiff'

#print(bcf.jpg_png_pdf_corrupt(gif_sample))
#print(bcf.jpg_png_pdf_corrupt(gif_sample_corrupt))
#quit()

#mdir='/Volumes/photo/Pictures KJD'
#dir2delete_list=['/Users/kevindonovan/Dropbox (MIT)/Pictures KJD/Already on SUBPAR']
#badir='/Users/kevindonovan/Dropbox (MIT)'

mdir='/Volumes/photo/Pictures KJD'
dir2delete_list=['/Volumes/photo/Pictures_KJD_maybe_dupe']
badir='/Volumes/photo'

#First move the folder: unorganized\ and\ possible\ duplicates
#mdir='/Volumes/photo/Pictures KJD'
#dir2delete_list=['/Volumes/photo/Pictures_KJD_maybe_dupe']
#badir='/Volumes/photo'

#mdir='/Volumes/photo/Pictures KJD'
#dir2delete_list=['/Volumes/SUBPAR/Pictures KJD','/Volumes/SUBPAR/Walden/Pictures_HOME_DIRECTORY','/Volumes/SUBPAR/Walden/RETURN_TO_HOME_DIRECTORY_archive/Thousand Islands','/Volumes/SUBPAR/Users/kevindonovan/Dropbox (MIT)/Pictures_HOME_DIRECTORY','/Volumes/SUBPAR/Archive KJD/Pictures KJD']
#badir='/Volumes/SUBPAR'

#Add safety check: if mdir, dir2delete, and badir all on NFS, its ok to proceed
#Walden_list=["music","video","homes","photo","home"]
#stop_list=['/Volumes/'+x for x in Walden_list]
#for y in stop_list:
#    for z in dir2delete_list:
#        if (y in z): 
#            print("Can't delete from "+z+'\nAborting')
#            quit()

file_extensions=['.jpg','.jpeg','.pdf','.png','.gif','.bmp','.tif','.tiff','.nef','.dng','.thm','.svg','.pptx','.xls','.ai','.psd','.aae']
#Video files
#file_extensions=['.3gp','.3gpp','.avi','.mov','.wmv']

#print("Making file array")
#fim=bcf.make_file_array_type(mdir,file_extensions)

#Find the last time mdir was modified
last_mod=datetime.datetime.fromtimestamp(max(os.stat(root).st_mtime for root,_,_ in os.walk(mdir)))

#Find the latest fim
fl_dates=[]
fl_names=[]
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, 'file_list_mdir_*') and (open(file).readlines()[0].strip() == mdir):
        file_t=file.removesuffix('.txt').rsplit('_')[-1]
        file_dt=datetime.datetime.strptime(file_t, '%Y%m%d%H%M%S')
        fl_dates.append(file_dt)
        fl_names.append(file)
if (not fl_names) or (max(fl_dates) < last_mod):
    print('Need to create a new file list.')
    fim=bcf.make_file_array_type(mdir,file_extensions)
    fl_file=open('file_list_mdir_'+time.strftime('%Y%m%d%H%M%S')+'.txt','a')
    fl_file.write(mdir+'\n')
    for ff in fim:
        fl_file.write("%s\n" % ff)
    fl_file.close()
elif (max(fl_dates) > last_mod):
    latest_f=fl_names[fl_dates.index(max(fl_dates))]
    print('Using previously created file list.')
    print("Latest: "+str(latest_f))
    with open(latest_f) as f:
        fim = f.readlines()
    fim = [x.strip() for x in fim]
    fim.remove(mdir)

#Insert file extensions list at top of hash_list, see if these match when checking for previous
#Find the lastest hash_list
hl_dates=[]
hl_names=[]
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, 'hash_list_mdir_*') and (open(file).readlines()[0].strip() == mdir):
        file_t=file.removesuffix('.txt').rsplit('_')[-1]
        file_dt=datetime.datetime.strptime(file_t, '%Y%m%d%H%M%S')
        hl_dates.append(file_dt)
        hl_names.append(file)
if (not hl_names) or (max(hl_dates) < last_mod):
    print('Need to create a new hash list.')
    hl_main=bcf.make_hash_array_type(fim,file_extensions)
    hl_file=open('hash_list_mdir_'+time.strftime('%Y%m%d%H%M%S')+'.txt','a')
    hl_file.write(mdir+'\n')
    for hh in hl_main:
        hl_file.write("%s\n" % hh)
    hl_file.close()
elif (max(hl_dates) > last_mod):
    latest_f=hl_names[hl_dates.index(max(hl_dates))]
    print('Using previously created hash list.')
    print("Latest: "+str(latest_f))
    with open(latest_f) as f:
        hl_main = f.readlines()
    hl_main = [x.strip() for x in hl_main]
    hl_main.remove(mdir)

results_dir='./results_compare_'+time.strftime('%Y%m%d_%H%M%S')
os.mkdir(results_dir)

for dir2delete in dir2delete_list:
    f2d_list=bcf.make_file_array_type_include_corrupt(dir2delete,file_extensions)

#    cmd_del_empty_dirs='find '+dir2delete.replace(" ","\ ").replace("(","\(").replace(")","\)")+' -type d -empty -delete'
#    os.system(cmd_del_empty_dirs)

    emptyN = 0
    corruptN = 0
    testedN = 0
    movedN = 0
    uniqueN = 0
    for f2d in f2d_list:
        fnam, fext = os.path.splitext(f2d)
        testedN +=1
        if (os.path.getsize(f2d) == 0):
            print("Moving empty file: "+f2d)
            bcf.move_to_delete(f2d,badir)
            movedN +=1
            emptyN +=1
            continue
        elif (fext.lower() in ['.jpg','.jpeg','.pdf','.png','.gif','.bmp','.tif','.tiff','.nef','.dng']) and bcf.jpg_png_pdf_corrupt(f2d)==1:
            print("Moving corrupt file: "+f2d)
            bcf.move_to_delete(f2d,badir)
            movedN +=1
            corruptN +=1
            continue
        elif bcf.dup_exists_fcmp(f2d, fim) and bcf.dup_exists_hash(f2d, hl_main):
            print("Moving duplicate: "+f2d)
            bcf.move_to_delete(f2d,badir)
            movedN +=1
        else:
            print("Unique file found, leaving in place: "+f2d)
            uniqueN +=1
            bcf.write_line_to_file(results_dir+"/unique_list.txt",f2d)
            pass
#        os.system(cmd_del_empty_dirs)

    print('Completed dir2delete: '+dir2delete)
    print('Files examined:')
    print(testedN)
    print('Empty files found:')
    print(emptyN)
    print('Corrupt files found:')
    print(corruptN)
    print('Files moved:')
    print(movedN)
    print('Unique files found:')
    print(uniqueN)
    

#os.system(cmd_del_empty_dirs)