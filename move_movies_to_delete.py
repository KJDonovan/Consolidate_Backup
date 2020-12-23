# Making similar directory structures
import os, bcf

mdir='/Volumes/home/Drive/Just Movies'
dir2delete_list=['/Volumes/SUBPAR/Just Movies']
badir='/Volumes/SUBPAR'

file_extensions=['.mp4','.avi','.AVI','.mkv','.mov','.m4v','.wmv','.txt','.jpg','.jpeg','.png','.srt','.mpg','.MPG','.mpeg','.xls','.sub','.VOB','.flv','.idx','.ogv']

fim=bcf.make_file_array_type(mdir,file_extensions)
hl_main=bcf.make_hash_array_type(fim,file_extensions)

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
            continue
        elif (bcf.dup_exists_fcmp(f2d, fim)==1 and bcf.dup_exists_hash(f2d, hl_main)==1):
            bcf.move_to_delete(f2d,badir)
            movedN +=1
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

#os.system(cmd_del_empty_dirs)