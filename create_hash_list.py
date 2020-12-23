import time, bcf

#Create hash_list and land it to disk
hl_main=bcf.make_hash_array_type(fim,file_extensions)
hl_key='testdata'
hl_file=open('hash_list_'+hl_key+'_'+time.strftime('%Y%m%d_%H%M%S')+'.txt','a')