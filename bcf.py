import os, hashlib, filecmp, PyPDF2
from PIL import Image

BLOCKSIZE = 65536

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

def make_hash_array(files_array):
  hash_array=[]
  for ff in files_array:
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
def jpg_png_empty_or_corrupt(filename):
    if (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.PNG')):
        try:
            img = Image.open(filename)
            img.verify() # verify that it is, in fact an image
            return 0
        except (IOError, SyntaxError) as e:
            return 1
    elif (filename.endswith('.PDF') or filename.endswith('.pdf')):
        try:
            img = open(filename,"rb")
            PyPDF2.PdfFileReader(img)
            return 0
        except PyPDF2.utils.PdfReadError:
            return 1