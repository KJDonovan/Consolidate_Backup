import os, hashlib, filecmp, time

#test_file1='/Users/kevindonovan/Dropbox (MIT)/Pictures KJD/Already on SUBPAR/Misc/Bandit sunbath.JPG'
#test_file1a='/Users/kevindonovan/Desktop/Back_Consolidation/differnt name test backup delete when done.JPG'

dir_to_delete='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation'
dir_main='/Users/kevindonovan/Dropbox (MIT)/Pictures KJD'

#dir_to_delete='/Users/kevindonovan/Dropbox (MIT)/Pictures KJD/Already on SUBPAR'
#dir_main='/Volumes/SUBPAR/Pictures KJD'

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

#keepers_filecmp = []
#ok_to_delete_filecmp=[]

#keepers_hash = []
#ok_to_delete_hash=[]

tS = time.time()
timeS = time.strftime('%X %x %Z')

files_to_delete = make_file_array(dir_to_delete)
files_to_deleteN = len(files_to_delete)
files_in_main = make_file_array(dir_main)
files_in_mainN = len(files_in_main)

print("Files to check for deletion: "+str(files_to_deleteN))
print("Files in main: "+str(files_in_mainN))

results_dir='./results_compare_'+time.strftime('%Y%m%d_%H%M%S')
os.mkdir(results_dir)

##########################################################################################################
tS_filecmp = time.time()
print("Beginning scan with filecmp ...")

keepers_filecmp=[]
ok2delete_filecmp=[]

#Delete results files if the exist
#filenames=["keepers_filecmp.txt","ok_to_delete_filecmp.txt","delete_list_filecmp.txt"]
#for f in filenames:
#  if os.path.exists(f):
#    os.remove(f)

findex=0
for f2d in files_to_delete:
  match_found=0
  findex +=1
  print("Searching for duplicates of: "+f2d+'\n')
  print("File "+str(findex)+" of "+str(files_to_deleteN)+'\n')
  for f1m in files_in_main:
#    print("Comparing "+f2d+" and "+f1m+'\n')
    if (filecmp.cmp(f2d,f1m)==1):
      match_found=1
      ok2delete_filecmp.append(f2d)
      write_line_to_file(results_dir+"/ok_to_delete_filecmp.txt",[f2d, f1m])
      write_line_to_file(results_dir+"/delete_list_filecmp.txt",f2d)
      print('---------------------------------------------------------------'+'\n')
      print('filecmp match found:\n'+f2d+'\n'+f1m+'\n')
      print('---------------------------------------------------------------'+'\n')
#      print("no need to keep looking\n")
      break
  if (match_found == 0):
    keepers_filecmp.append(f2d)
    write_line_to_file(results_dir+"/keepers_filecmp.txt",f2d)
    print('***************************************************************'+'\n')
    print('no filecmp match, consider saving:\n'+f2d+'\n')
    print('***************************************************************'+'\n')

tE_filecmp = time.time()
##########################################################################################################
tS_hash = time.time()
print("Beginning scan with hash ...")

keepers_hash=[]
ok2delete_hash=[]

hash_list_main=make_hash_array(files_in_main)

#Delete results files if the exist
#filenames=["keepers_hash.txt","ok_to_delete_hash.txt","delete_list_hash.txt"]
#for f in filenames:
#  if os.path.exists(f):
#    os.remove(f)

findex=0
for f2d in files_to_delete:
  findex +=1
  print("Searching for duplicates of: "+f2d+'\n')
  print("File "+str(findex)+" of "+str(files_to_deleteN)+'\n')
#  print("calculating hash for file: "+f2d)
  f2d_hash = hash_this(f2d)
#    print("Comparing hash values.")
  if (f2d_hash[0] in hash_list_main):
    ok2delete_hash.append(f2d)
    match_index=hash_list_main.index(f2d_hash[0])    
    write_line_to_file(results_dir+"/ok_to_delete_hash.txt",[f2d, files_in_main[match_index]])
    write_line_to_file(results_dir+"/delete_list_hash.txt",f2d)
    print('---------------------------------------------------------------'+'\n')
    print('hash match found:\n'+f2d+'\n'+f1m+'\n')
    print('---------------------------------------------------------------'+'\n')
  else:
    keepers_hash.append(f2d)
    write_line_to_file(results_dir+"/keepers_hash.txt",f2d)
    print('***************************************************************'+'\n')
    print('no hash match, consider saving:\n'+f2d+'\n')
    print('***************************************************************'+'\n')

tE_hash = time.time()
timeE = time.strftime('%X %x %Z')

sfile = results_dir+"/stats_compare_dirs.txt"
#Delete stats files if it exists
#if os.path.exists(sfile):
#  os.remove(sfile)
stats_file=open(sfile,"a")
stats_file.write("Files in directory for possible deletion: "+str(files_to_deleteN)+'\n')
stats_file.write("Files in main directory: "+str(files_in_mainN)+'\n')
stats_file.write("Start time: "+timeS+'\n')
stats_file.write("End time: "+timeE+'\n')
stats_file.write("Script run time (s): "+str(tE_hash-tS)+'\n')
stats_file.write("filecmp time: "+str(tE_filecmp-tS_filecmp)+'\n')
stats_file.write("hash comparison time: "+str(tE_hash-tS_hash)+'\n')
stats_file.write("Differences delete_list filecmp vs hash: "+str(len(Diff(ok2delete_filecmp, ok2delete_hash)))+'\n')
stats_file.write("Differences keepers filecmp vs hash: "+str(len(Diff(keepers_filecmp, keepers_hash)))+'\n')
stats_file.close()

