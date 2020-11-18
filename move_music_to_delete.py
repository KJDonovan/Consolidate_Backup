# Making similar directory structures
import os, bcf

#def move_to_delete(file_path, basedir):
#    sp=file_path.split(os.sep)
#    split_path=[i for i in sp if i]
#    bd=basedir.split(os.sep)
#    bdir=[i for i in bd if i]
#    diff_path=['ok_to_delete']+[i for i in split_path if i not in bdir]
#    print(split_path)
#    print(bdir)
#    print(diff_path)
#    new_path=(''.join([('/'+str(elem)) for elem in bdir]))
#    print(new_path)
#    for folder in diff_path:
#       new_path=new_path+'/'+folder
#        if (folder==split_path[-1]) and os.path.exists(new_path):
#            print('This file already exists. Something may not be right. Aborting.')
#            quit()
#        elif (folder==split_path[-1]) and not os.path.exists(new_path):
#            os.rename(file_path,new_path)
#        else:
#            if not os.path.exists(new_path):
#                os.makedirs(new_path)
#    return new_path

testfile='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation_testcopy1/music_test_backup_consolidation/Dave Brubeck - Unsquare Dance.mp3'
basedir_test='Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/'
bcf.move_to_delete(testfile,basedir_test)

#mdir=
#dir2delete=