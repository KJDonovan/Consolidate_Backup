import os, hashlib, time, filecmp

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

pic='/Users/kevindonovan/Dropbox (MIT)/Pictures KJD/Already on SUBPAR/Misc/Bandit sunbath.JPG'
print('pic: '+str(os.stat(pic)))
pic2='/Users/kevindonovan/Dropbox (MIT)/Pictures KJD/Already on SUBPAR/Misc/Bandit.jpg'
print('pic2: '+str(os.stat(pic2)))
pic3='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/differnt name test backup delete when done.JPG'
print('pic3: '+str(os.stat(pic3)))
pic4='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/differnt name test backup delete when done modified.JPG'
print('pic4: '+str(os.stat(pic4)))
pic5='/Users/kevindonovan/Desktop/Back_Consolidation/test_data_backup_consolidation/dir2delete_test_data_backup_consolidation/photos_test_backup_consolidation/corrupted_images_backup_consolidation/looks like an angel.jpg'
print('pic5: '+str(os.stat(pic5)))
pic6='/Users/kevindonovan/Dropbox (MIT)/Pictures KJD/Already on SUBPAR/Cat Pics from Mom/looks like an angel.jpg'
print('pic6: '+str(os.stat(pic6)))

BLOCKSIZE = 65536

print('---------------- Different Pictures ------------------')
#compare hash digest
print('Comparing hash digests:')
print(hash_this(pic)[0] == hash_this(pic2)[0])

#compare with filecmp
print('The result of filecmp:')
print(filecmp.cmp(pic,pic2))

print('---------------- Same Picture Different Name ------------------')

#compare hash digest
print('Comparing hash digests:')
print(hash_this(pic)[0] == hash_this(pic3)[0])

#compare with filecmp
print('The result of filecmp:')
print(filecmp.cmp(pic,pic3))

print('---------------- Same Picture with Modifications ------------------')

#compare hash digest
print('Comparing hash digests:')
print(hash_this(pic3)[0] == hash_this(pic4)[0])

#compare with filecmp
print('The result of filecmp:')
print(filecmp.cmp(pic3,pic4))

print('---------------- Same Picture but one is corrupted ------------------')

#compare hash digest
print('Comparing hash digests:')
print(hash_this(pic5)[0] == hash_this(pic6)[0])

#compare with filecmp
print('The result of filecmp:')
print(filecmp.cmp(pic5,pic6))

