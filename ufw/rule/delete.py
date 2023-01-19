import os
import sys

original_file = sys.argv[1]
new_file = original_file.replace('.yml', '_delete.yml')

with open(original_file, 'r') as f:
    contents = f.read()

contents = contents.replace('rule: allow', 'rule: allow\n      delete: yes')

with open(new_file, 'w') as f:
    f.write(contents)
    
if not os.path.exists('./delete'):
    os.makedirs('./delete')

os.rename(new_file, './delete/' + new_file)
