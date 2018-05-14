import sys
from pathlib import Path
import os
from os import listdir
from os.path import isfile,isdir,join
import ntpath

bakext=['.bak', '.bk1','.bk2']

# file with extensions same dictionary
fileExtensionDir={}
# file with extension in extension bakext array
fileDir={}

# print out the extesnsion same path
def output(file1, file2):
    time1=os.path.getmtime(file1)
    time2=os.path.getmtime(file2)
    if(time1<time2):
        basename=ntpath.basename(os.path.splitext(file1)[0])
        fileExtensionDir[basename]=file2
        print("{} may be superseded by {}".format(file1, file2))
    else:
        print("{} may be superseded by {}".format(file2, file1))
        
# print out the extension like bak, ba1, ba2 path        
def outputext(source, target):
    targetext= os.path.splitext(target)[1] in bakext
    if targetext:
        print('{0} may be superseded by {1}'.format(target, fileDir[source]))
    else:
        if os.path.splitext(fileDir[source])[1] in bakext:
            print('{0} may be superseded by {1}'.format(fileDir[source], target))
            fileDir[source]=target

#main compare function
def comparefile(pathdir):
    for f in listdir(pathdir):
        tmpdir=join(pathdir,f)
        if isfile(tmpdir):
            if f in fileExtensionDir:
                output(fileExtensionDir[f], tmpdir)
            elif os.path.splitext(f)[0] in fileDir:
                # print(tmpdir)
                outputext(os.path.splitext(f)[0], tmpdir)
            else:
                basename=ntpath.basename(f)
                fileExtensionDir[basename]=tmpdir
                fileDir[os.path.splitext(basename)[0]]=tmpdir
        elif isdir(tmpdir):
            comparefile(tmpdir)

if __name__=="__main__":
    print('The path search:', sys.argv[1])
    print("The list of probably similar files:")
    comparefile(sys.argv[1])