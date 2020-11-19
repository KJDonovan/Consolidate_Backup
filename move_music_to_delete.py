# Making similar directory structures
import os, bcf

#testfile='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation_testcopy1/music_test#_backup_consolidation/Dave Brubeck - Unsquare Dance.mp3'
#basedir_test='Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/'
#bcf.move_to_delete(testfile,basedir_test)

#mdir='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/main_test_data_backup_consolidation'
#dir2delete='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation_testcopy1'
#badir='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation'

mdir='/Volumes/Media/Music and Audio'
dir2delete='/Volumes/SUBPAR/Music and Audio'
badir='/Volumes/SUBPAR'

audio_extensions=['.mp3','.MP3','.m4a']
f2d_list=bcf.make_file_array_type(dir2delete,audio_extensions)
fim=bcf.make_file_array_type(mdir,audio_extensions)

hl_main=bcf.make_hash_array_type(fim,audio_extensions)

emptyN = 0
testedN = 0
movedN = 0
for f2d in f2d_list:
    testedN +=1
    if (os.path.getsize(f2d) == 0):
        print("empty file: "+f2d)
        emptyN +=1
        continue
    elif (bcf.dup_exists_fcmp(f2d, fim)==1 and bcf.dup_exists_hash(f2d, hl_main)==1):
        bcf.move_to_delete(f2d,badir)
        movedN +=1
    else:
        pass

print('Files examined:')
print(testedN)
print('Empty files found:')
print(emptyN)
print('Files moved:')
print(movedN)

cmd_del_empty_dirs='find '+dir2delete+' -type d -empty -delete'
#print(cmd_del_empty_dirs)
os.system(cmd_del_empty_dirs)