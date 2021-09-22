#!/usr/bin/env python3
'''
   Date: September 22, 2021
   Subject: push_it.py
push_it.py is a simple process to knock out a "git push" to GitHub. 
'''
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
import os

commit_message    = input('Commit Comment: ')
#working_directory = 'cd ~/mycode'
working_directory = '/home/student/mycode'
git_add           = 'git add *'
git_commit        = 'git commit -m "' + commit_message + '"' 
git_push          = 'git push origin'
#os.system(working_directory)
os.chdir(working_directory)
os.system(git_add)
os.system(git_commit)
os.system(git_commit)
os.system(git_push)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

