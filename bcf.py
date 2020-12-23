import os, hashlib, filecmp, PyPDF2, time, ntpath
from PIL import Image
from compare_mp3 import compare

BLOCKSIZE = 65536

#Find the filename from a path
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

#Split a path into a vector
def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

def hash_this(filename):
  hasher = hashlib.md5()
#  hasher = hashlib.sha256()
  with open(filename, 'rb') as file:
    t0 = time.time()
    buf = file.read(BLOCKSIZE)
    while len(buf) > 0:
      hasher.update(buf)
      buf = file.read(BLOCKSIZE)
    tN = time.time()
    hash_time = tN - t0
  return [hasher.hexdigest(), hash_time]

#print(hash_this(test_file1))
#quit()

def hash_cmp(fil1,fil2):
  return hash_this(fil1)[0] == hash_this(fil2)[0]

#print(hash_comp(test_file1, test_file1a))
#quit()

def make_file_array(dir_path):
  file_array = []
  for path, subdirs, files in os.walk(dir_path):
    for i in files:
      file_to_check=os.path.join(path,i)
      file_array.append(file_to_check)
  return file_array

#print(make_file_array(dir_main))
#quit()

#makes list of files with extensions given in the list ext
#excludes corrupt or empty files
def make_file_array_type(dir_path,ext):
    file_array = []
    exten=[i.lower() for i in ext]
    for path, subdirs, files in os.walk(dir_path):
        for fi in files:
            f2c=os.path.join(path,fi)
            filename, file_extension = os.path.splitext(f2c)
            if (file_extension.lower() in exten):
                if os.path.getsize(f2c) == 0:
                    print('Found empty file while making file list: '+f2c)
                    continue
                elif (file_extension.lower() in ['.jpg','.jpeg','.png','.gif','.bmp','.tif','.tiff','.nef','.dng']) and jpg_png_pdf_corrupt(f2c):
                    print('Found corrupt file while making file list: '+f2c)
                    continue
                else:
                    file_array.append(f2c)
    return file_array

#makes list of files with extensions given in the list ext
#includes corrupt or empty files
def make_file_array_type_include_corrupt(dir_path,ext):
    file_array = []
    exten=[i.lower() for i in ext]
    for path, subdirs, files in os.walk(dir_path):
        for fi in files:
            f2c=os.path.join(path,fi)
            filename, file_extension = os.path.splitext(f2c)
            if (file_extension.lower() in exten):
                file_array.append(f2c)
    return file_array

def make_hash_array(files_array):
  hash_array=[]
  for ff in files_array:
    hash_array.append(hash_this(ff)[0])
  return hash_array

#make hash array for files with extensions given in the list ext
def make_hash_array_type(files_array,ext):
    hash_array=[]
    exten=[i.lower() for i in ext]
    for ff in files_array:
        filename, file_extension = os.path.splitext(ff)
        if (file_extension.lower() in exten):
            if os.path.getsize(ff) == 0:
                print('Found empty file while making hash array: '+ff)
                continue
            elif (file_extension.lower() in ['.jpg','.jpeg','.png','.gif','.bmp','.tif','.tiff','.nef','.dng']) and jpg_png_pdf_corrupt(ff):
                print('Found corrupt file while making hash array: '+ff)
                continue
            else:
                hash_array.append(hash_this(ff)[0])
    return hash_array

def write_line_to_file(filename, line):
  results_file=open(filename,"a")
  results_file.write("%s\r\n"% line)
  results_file.close()

def write_results_to_file(filename, result):
  if os.path.exists(filename):
    os.remove(filename)
  results_file=open(filename,"w+")
  for i in result: results_file.write("%s\r\n"% i)
  results_file.close()

def Diff(li1, li2): 
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

#Returns 0 if jpg/png is valid, 1 if corrupt
def jpg_png_empty_or_corrupt(filename):
    try:
        img = Image.open(filename)
        img.verify() # verify that it is, in fact an image
        return 0
    except (IOError, SyntaxError) as e:
        return 1

#Returns 0 if pdf is valid, 1 if corrupt
def pdf_empty_or_corrupt(filename):
    try:
        img = open(filename,"rb")
        PyPDF2.PdfFileReader(img)
        return 0
    except PyPDF2.utils.PdfReadError:
        return 1

#Returns 0 if jpg/png/pdf is valid, 1 if corrupt
def jpg_png_pdf_corrupt(filename):
    fname, file_extension = os.path.splitext(filename)
    if (file_extension.lower() in ['.jpg','.jpeg','.png','.gif','.bmp','.tif','.tiff','.nef','.dng']):
        try:
            img = Image.open(filename)
            img.verify() # verify that it is, in fact an image
#            print('Image file appears to be ok')
            return 0
        except (IOError, SyntaxError) as e:
#            print('Image file appears to be corrupt')
            return 1
    elif (file_extension.lower() == '.pdf'):
        try:
            img = open(filename,"rb")
            PyPDF2.PdfFileReader(img)
            return 0
        except PyPDF2.utils.PdfReadError:
            return 1

#Moves a file to a parallel directory structure
def move_to_delete(file_path, basedir):
    sp=file_path.split(os.sep)
    split_path=[i for i in sp if i]
    bd=basedir.split(os.sep)
    bdir=[i for i in bd if i]
    diff_path=['ok_to_delete']+[i for i in split_path if i not in bdir]
    new_path=(''.join([('/'+str(elem)) for elem in bdir]))
    for folder in diff_path:
        new_path=new_path+'/'+folder
        if (folder==split_path[-1]) and os.path.exists(new_path):
            print('This file already exists. Something may not be right. Aborting.')
            quit()
        elif (folder==split_path[-1]) and not os.path.exists(new_path):
            os.rename(file_path,new_path)
        else:
            if not os.path.exists(new_path):
                os.makedirs(new_path)
    return new_path

#searches for a dup of file_path in file_list with filecmp
def dup_exists_fcmp(file_path, file_list):
    match_found=0
    for f1m in file_list:
#    print("Comparing "+f2d+" and "+f1m+'\n')
        if (filecmp.cmp(file_path,f1m)==1):
            match_found=1
            break
    return match_found

def dup_exists_hash(file_path, hash_array):
    f2d_hash = hash_this(file_path)
#    print(f2d_hash[0])
#    print(hash_array[0])
    if (f2d_hash[0] in hash_array):
        return 1
    else:
        return 0

def dup_exists_bitstream(file_path, file_list, f2s):
    match_found=0
    matching_file=''
    for f1m in file_list:
#    print("Comparing "+f2d+" and "+f1m+'\n')
        if (f1m in f2s) or (os.path.getsize(f1m) == 0):
            continue
        elif (compare(file_path,f1m).value):
            match_found=1
            matching_file=f1m
            break
    return [match_found, matching_file]

        