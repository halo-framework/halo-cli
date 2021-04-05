import os
import shutil
import sys

#directory = 'C:\\dev\\projects\\halo\halo-cli\\tests\\gen4\\BIAN_APIs_Release9.0'
#dest = 'C:\\dev\\projects\\halo\halo-cli\\tests\\gen4\\BIAN9'

directory = sys.argv[1]
dest = sys.argv[2]
do_copy = False
#[print(x[0]) for x in os.walk(directory)]
cnt = 1
for x in os.walk(directory):
    dir_files = x[2]
    if len(dir_files) == 0:
        continue
    sd_name = None
    f_name = None
    json_name = None
    for f in dir_files:
        if f.endswith('json'):
            f_name = f.replace('.json','')
            obj_str = '"'+str(cnt)+'": { \
                "f_name": "'+ f_name.strip() +'", \
                "name": "'+ f_name.strip() +'", \
                "service_domain": true, \
                "swagger": true \
            },'
            print(obj_str)
            #print(str(cnt)+' '+f_name)
            cnt = cnt+1
        if f.endswith('.json'):
            json_name = x[0]+'\\'+f
    if os.path.isfile(json_name) and do_copy:
        shutil.copy(json_name, dest+'\\'+f_name+'.json')


