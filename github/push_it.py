#!/usr/bin/env python3

#...
# pushing to git script
#....
# <<<<<
import os

commit_message	= input('Commit Comment: ')
working_directory = 'cd ~/mycode'
git_add		= 'git add *'
git_commit	= 'git commit -m "' + commit_message + '"'
git_push	= 'git push origin'

os.system(working_directory)
os.system(git_add)
os.system(git_commit)
os.system(git_push)
