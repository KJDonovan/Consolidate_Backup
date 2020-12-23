# Making similar directory structures
import os, bcf, time
#Python package for comparing metadata:
#import eyeD3
from compare_mp3 import compare

#testfile='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation_testcopy1/music_test#_backup_consolidation/Dave Brubeck - Unsquare Dance.mp3'
#basedir_test='Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/'
#bcf.move_to_delete(testfile,basedir_test)

#Testing for edge case where same audio files have differing metadata
#tf_2del='/Users/kevindonovan/Desktop/Music for Phone/Paul Pena - I\'m Gonna Make It All Right.mp3'
#tf_2del_diff='/Users/kevindonovan/Desktop/Music for Phone/Paul Pena - Cosmic Mirror.mp3'
#tf_om='/Volumes/Media/Music and Audio/Music Archive/Paul Pena/Paul Pena - I\'m Gonna Make It All Right.mp3'
#hl_om=bcf.make_hash_array_type(tf_om,['.mp3'])
#print(bcf.dup_exists_fcmp(tf_2del, [tf_om]))
#print(bcf.dup_exists_hash(tf_2del, hl_om))
#print(compare(tf_2del, tf_om))
#comp1=compare(tf_2del, tf_om)
#comp0=compare(tf_2del_diff, tf_om)
#print(comp1.value)
#print(comp0.value)
#if comp1.value: print('same file')
#if comp0.value: print('shouldn\'t see this')
#print(bcf.dup_exists_bitstream(tf_2del, [tf_om]))
#print(bcf.dup_exists_bitstream(tf_2del_diff, [tf_om]))
#quit()

#mdir='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/main_test_data_backup_consolidation'
#dir2delete='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation_testcopy1'
#badir='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation'

#mdir='/Volumes/Media/Music and Audio'
#dir2delete_list=['/Volumes/SUBPAR/Music and Audio','/Volumes/SUBPAR/Walden/Music from Phone','/Volumes/SUBPAR/Walden/Music_HOME_DIRECTORY']
#badir='/Volumes/SUBPAR'

mdir='/Volumes/Media/Music and Audio'
dir2delete_list=['/Users/kevindonovan/Desktop/Music for Phone']
badir='/Users/kevindonovan/Desktop'

#file_extensions=['.mp3','.MP3','.m4a']
#file_extensions=['.aa','.bmp','.doc','.itl','.jpg','.m3u','.m4a',.m4p','.mp4','.nfo','.pdf','.png','.rtf','.sfv','.txt','.wav','.wma']
file_extensions=['.mp3','.MP3']

files_to_skip=['/Volumes/Media/Music and Audio/Music Archive/Compilations/Quincy Jones - The Best/08 Just Once.mp3']

fim=bcf.make_file_array_type(mdir,file_extensions)
#hl_main=bcf.make_hash_array_type(fim,file_extensions)
#LAND TO DISK: HASH ARRAY

#write same_bitstream matches to file
sbt_file=open('same_bitstream_'+time.strftime('%Y%m%d_%H%M%S')+'.txt','w+')

for dir2delete in dir2delete_list:
    f2d_list=bcf.make_file_array_type(dir2delete,file_extensions)

    cmd_del_empty_dirs='find '+dir2delete.replace(" ","\ ").replace("(","\(").replace(")","\)")+' -type d -empty -delete'
    os.system(cmd_del_empty_dirs)

    emptyN = 0
    testedN = 0
    movedN = 0
    for f2d in f2d_list:
        testedN +=1
        if (os.path.getsize(f2d) == 0):
            print("empty file: "+f2d)
            emptyN +=1
            #Insert option to move empty files?
            continue
#        if bcf.dup_exists_fcmp(f2d, fim) and bcf.dup_exists_hash(f2d, hl_main):
#            bcf.move_to_delete(f2d,badir)
#            movedN +=1
#            continue
        d_bits=bcf.dup_exists_bitstream(f2d, fim, files_to_skip)
        if f2d.lower().endswith('.mp3') and d_bits[0]:
            bcf.move_to_delete(f2d,badir)
            movedN +=1
            sbt_file.write(bcf.path_leaf(f2d)+'\n'+bcf.path_leaf(d_bits[1])+'\n\n')
        else:
            pass
        os.system(cmd_del_empty_dirs)

    print('Completed dir2delete: '+dir2delete)
    print('Files examined:')
    print(testedN)
    print('Empty files found:')
    print(emptyN)
    print('Files moved:')
    print(movedN)

sbt_file.close()
#os.system(cmd_del_empty_dirs)