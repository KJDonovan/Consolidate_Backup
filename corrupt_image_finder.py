import os, PyPDF2, time
from PIL import Image

#scan_dir='/Users/kevindonovan/Dropbox (MIT)/Pictures KJD'
#scan_dir='/Volumes/SUBPAR/Pictures KJD'
#scan_dir='/Users/kevindonovan/Dropbox (MIT)/Pictures KJD/Already on SUBPAR/2011to2019 Pictures KJD/2011 Pictures KJD/Oct2011/2011-10-08/'
scan_dir='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation'
#scan_dir='/Volumes/photo/Pictures KJD'
 
def make_file_array(dir_path):
  file_array = []
  for path, subdirs, files in os.walk(dir_path):
    for i in files:
      file_to_check=os.path.join(path,i)
      file_array.append(file_to_check)
  return file_array

tS = time.time()
timeS = time.strftime('%X %x %Z')

files_to_scan = make_file_array(scan_dir)
#print(files_to_scan)

#files_to_scan = ['/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/corrupted_images_backup_consolidation/empty_images_backup_consolidation/AMD mule figurines.pdf']
#The file above returns an error containing the following line:
#IOError: [Errno 22] Invalid argument

#Delete file if already exists
#if os.path.exists(corrupt_images_file):
#  os.remove(corrupt_images_file)
results_dir='../results_corrupt_finder_'+time.strftime('%Y%m%d_%H%M%S')
os.mkdir(results_dir)

corrupt_images_file='corrupted_images.txt'
cfile=open(results_dir+'/'+corrupt_images_file,"a")
empty_images_file='empty_images.txt'
efile=open(results_dir+'/'+empty_images_file,"a")

corruptN = 0
emptyN = 0
testedN = 0
for filename in files_to_scan:
  print('Checking: '+filename)
  if (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.PNG')):
    testedN +=1
    if (os.path.getsize(filename) == 0):
      print("empty image file: "+filename)
      efile.write(filename+'\n')
      emptyN +=1
      continue
    try:
      img = Image.open(filename)
      img.verify() # verify that it is, in fact an image
    except (IOError, SyntaxError) as e:
      print('Bad file: '+filename)
      cfile.write(filename+'\n')
      corruptN +=1
  elif (filename.endswith('.PDF') or filename.endswith('.pdf')):
    testedN +=1
    if (os.path.getsize(filename) == 0):
      print("empty image file: "+filename)
      efile.write(filename+'\n')
      emptyN +=1
      continue
    try:
      img = open(filename,"rb")
      PyPDF2.PdfFileReader(img)
    except PyPDF2.utils.PdfReadError:
      print("invalid PDF file: "+filename)
      cfile.write(filename+'\n')
      corruptN +=1
  else:
    pass

cfile.close()

tE = time.time()
timeE = time.strftime('%X %x %Z')

sfile = results_dir+"/stats_corrupt_finder.txt"
#Delete stats files if it exists
#if os.path.exists(sfile):
#  os.remove(sfile)
stats_file=open(sfile,"a")
stats_file.write(scan_dir+'\n')
stats_file.write("Files scanned for corruption: "+str(testedN)+'\n')
stats_file.write("Empty files found: "+str(emptyN)+'\n')
stats_file.write("Corrupt files found: "+str(corruptN)+'\n')
stats_file.write("Start time: "+timeS+'\n')
stats_file.write("End time: "+timeE+'\n')
stats_file.write("Script run time (s): "+str(tE-tS)+'\n')
stats_file.close()
