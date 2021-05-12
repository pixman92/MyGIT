# import zipfile
import pdb
import os
import shutil
# import makingCVS
import sys
import datetime


# ==========================
# sourcePathMe - check if Valid
# if os.path.isdir(sourcePathMe):

#   C:\Users\gotru\OneDrive\testFolder\

# =============================

def quickInit(initDir, sourceDir, saveDir):

    print "You are using QUICK INITIALIZE"
    print "InitDir - ", initDir
    print "SourceDir - ", sourceDir
    print "SaveDir - ", saveDir

    input = raw_input("Do you want to proceed?\n(yes/no)")
    if(input=="yes"):
        init(initDir)
        saveSourceURL(sourceDir)
        saveDestURL(saveDir)
    else:
        print 'Cancelled'



# =============================
def init(dir):


    # tmp = (os.path.join((dir.format(__file__)),'/savedGITAlternative'))
    
    # this was getting tripped up by the \t = a tab space!
    tmp = dir
    dir = tmp.replace('\t', '/t')

    tmp = dir
    tmp3 = tmp
    tmp = tmp3.replace('\\', '/')
    
    folderToMake = os.sep.join([tmp, 'savedGITAlternative'])

    tmp = folderToMake
    folderToMake = tmp.replace('\\','/')

    if(os.path.exists(tmp) == True):
        print "Alreay Exists"
    else:
        print "Make a folder to Path of: ", folderToMake
        print "???"
        input = raw_input("yes/no\n")
        if(input == 'yes'):
            os.makedirs(folderToMake)
        
    # else:
        # print "already made"
    # import pdb; pdb.set_trace()   #debugger
    
    



# ==========================
# Block of code -> saving SRC path
def saveSourceURL(urlMeToSourceCode):
    # save path to sourceFolder

    # if(os.path.exists(os.getcwd()+'/savedGITAlternative/savedURL.txt')==False):
    # file_name = os.path.join(os.getcwd(), 'savedGITAlternative/savedURL.txt')

    # replacing literal char(s)
    # tmp2 = os.getcwd()
    paramNoTab = ""
    # urlMeToSourceCode = paramNoTab
    paramNoTab = urlMeToSourceCode
    urlMeToSourceCode = paramNoTab.replace('\\t', '/t')
    
    tmp2 = os.getcwd()
    tmp = tmp2
    tmp2 = tmp.replace('\\t', '/t')


    file_name_source = os.sep.join([tmp2, 'savedGITAlternative/savedURL.txt'])


    tmp = file_name_source
    file_name_source = tmp.replace('\\', '/')



    # import pdb; pdb.set_trace()   #debugger
    with open(file_name_source, 'w') as sourceFile:
        sourceFile.write(paramNoTab)
        sourceFile.close()

# global sourcePathMe


def pullSourceURL():
    # pull out the path, saved in text document
        # file_name = os.getcwd()+'/savedGITAlternative/savedURL.txt'
        
        # tmp2 = os.getcwd()
        # tmp = tmp2
        # tmp2 = tmp.replace('\\', '/')

        

        file_name_dest = os.sep.join([os.getcwd(), 'savedGITAlternative/savedURL.txt'])

        tmpFileName = file_name_dest
        file_name_dest = tmpFileName.replace('\\t', '/t')

        tmp2 = file_name_dest
        file_name_dest = tmp2.replace('\\', '/')

        global theSource
        theSource = file_name_dest

        # import pdb; pdb.set_trace()   #debugger

        with open(file_name_dest, 'r') as data:
            returnMe = data.readlines()

            # if(returnMe[0] is not None):
            try:
                returnMe[0]
            except:
                print "Blank Source File"
            else:
                global sourcePathMe 
                sourcePathMe = returnMe[0]
                tmp = sourcePathMe
                sourcePathMe = tmp.replace('\\', '/')

                print "sourcePathMe: ", sourcePathMe

                data.close()
            # else:
            #     print "Nothing In Source Path file"


                return sourcePathMe


def cleanSourceURL():
    # delete the whole file
    fileMe = os.path.join(os.getcwd(), 'savedURL.txt')
    os.remove(fileMe)

# ==========================


def saveDestURL(strSavedToDestURL):
    # saves a path to where you want the commits to save to, a path string
    # file_name = os.path.join(os.getcwd() + '/savedGITAlternative/savedDestURL.txt')

    # replacing literal char(s)
    # tmp2 = os.getcwd()\

    # TODO - make sure the strSavedToDestURL is a valid Path

    # if(os.path.exists(strSavedToDestURL)==True):

    paramNoTab = ""
    paramNoTab = strSavedToDestURL
    strSavedToDestURL = paramNoTab.replace('\t', '/t')

    tmp2 = os.getcwd()
    tmp = tmp2
    tmp2 = tmp.replace('\\t', '/t')


    file_name = os.sep.join([tmp2, 'savedGITAlternative/savedDestURL.txt'])


    # paramNoTab = strSavedToDestURL
    strSavedToDestURL = strSavedToDestURL.replace('\\', '/')
    
    tmp3 = file_name
    file_name = tmp3.replace('\\', '/') 


    with open(file_name, 'w') as destFile:
        destFile.write(strSavedToDestURL)
        destFile.close()
      


def pullDestURL():
    # seems to be working!

    # pulls up the destPathURL string
    # pullSourceURL()

    # file_name = os.path.join(os.getcwd(), '/savedGITAlternative/savedDestURL.txt')
    file_name_dest = os.sep.join([os.getcwd(), 'savedGITAlternative/savedDestURL.txt'])



    if(os.path.exists(file_name_dest)==False):
        print "Blank Destination File Error 1 - Create a Dest File"
    else:
            # global theSource
            # theSource = file_name_dest
        with open(file_name_dest, 'r') as data:
            returnMe = data.readlines()

            try:
                returnMe[0]
            except:
                print "Blank Destination File Error 2 - Dest file - blank"
            else:

                global destPathURL
                destPathURL = returnMe[0]

                tmp = destPathURL
                destPathURL = tmp.replace('\\', '/')

                print "destPathURL: ", destPathURL

                data.close()
                return destPathURL




# ==========================


def saveAMilestone(message):
    metime = str(datetime.datetime.now())
    file_name_log = os.path.join(pullSourceURL(), 'log.txt')
    if(os.path.exists(file_name_log)==True):
        with open(file_name_log, 'a') as log:
            txt = '\n\n'+metime + ' --- ' + message
            log.write(txt)
            log.close()
            print 'Written time and message to Log.txt file'
            print txt
    else:
        with open(file_name_log, 'w') as log:
            txt = '\n\n'+metime + ' --- ' + message
            log.write(txt)
            log.close()
            print 'Written time and message to Log.txt file'
            print txt


# ==========================
def run():
    revert('goaway')

    
    # allBranches = []
    # allBranches = os.listdir(pullDestURL())
    # amIThere = False
    # for me in allBranches:
    #     if(me != 'goaway'):
    #         print 'No Mach'
    #     else:
    #         print "Matched!"
    #         amIThere = True
    # if(amIThere == True):


# ==========================


def branchMe(name):

    if(os.path.exists(os.path.join(pullDestURL(), name)))==True:
        print "Branch folder exists"
    else:
        print "Making new Branch Folder"
        os.makedirs(os.path.join(pullDestURL(), name))
         

    fname = []
    dir_name = []
    i=0
    fileNewPath = []

    path = pullSourceURL()

    global newFileData
    newFileData = []
    for root, d_names, f_names in os.walk(path):        #changed from 'path' to pullSourceURL()
        print d_names
        print f_names
        # print pullSourceURL()

        # making source File Paths! working!
        for f in f_names:
            tmp1 = os.sep.join([pullSourceURL(), f])

            tmp2 = tmp1
            tmp1 = tmp2.replace('\\', '/')
            fname.append(tmp1)



        # making New Directory Path(s) from old Paths 
        for i in range(0, len(d_names)):
            dir_name.append(os.path.join(pullDestURL()+name, d_names[i]))


        # making new directories
        # try:
        #     dir_name
        # except:
        #     print "NO directories found"
        # else:
        # if dir_name==[]:
        #     print "NO Directories found!"
        # else:
        #     for item in dir_name:
        #         # logic for making Saved_folder tree structure
        #         savedItemURL = item.replace(pullSourceURL(), pullDestURL())
        #         print savedItemURL            


        # making files, Dest Paths!
        for f in f_names:
            tmp1 = os.path.join(pullDestURL(), name)
            tmp2 = os.path.join(tmp1, f)

            tmp3 = tmp2
            tmp2 = tmp3.replace('\\', '/')
            fileNewPath.append(tmp2)

        # reading from old (files)
        newFileData = []
        for sourced in fname:
            with open(sourced, 'r') as sourceFile:
                print sourceFile
                tmp1 = sourceFile.readlines()
                newFileData.append(tmp1)
                if(tmp1==[] or tmp1 == ""):
                    print "no data in ", sourced, " !"

        # writing to New (files)
        empty = False
        for i in range(0, len(fname)):
            with open(fname[i], 'r') as amIEmpty:
                if (amIEmpty.readlines()==[]):
                    empty = True
                    print "YES empty for file: ", fname[i]

        # if(empty==True):
        #     print
        # 
        # ============================= 
        # the actual logic of creating the files!
        ii=0

        for toDest in fileNewPath:


            with open(toDest, 'w') as writingToDest:
                if(newFileData[ii]==[] or newFileData==""):
                    writingToDest.write('')
                else:
                    writingToDest.write(' '.join(newFileData[ii]))
                    writingToDest.close()
                print 'written:\n', newFileData[ii]
            if(ii <len(newFileData)):
                ii+=1

        import pdb; pdb.set_trace()   #debugger
        # =============================



def revert(branchName):
    # pullSourceURL()
    # pullDestURL()

    
    # if(os.path.exists(pullDestURL()+branchName))==True:
    #     print 'Branch to Revert from, exists!'
    
    allBranches = []
    allBranches = os.listdir(pullDestURL())
    amIThere = False
    for me in allBranches:
        if(me != branchName):
            print 'No Mach per this Name'
        else:
            print "Matched!"
            amIThere = True

    if(amIThere == False):
        print "NO Match at All"
    if(amIThere == True):
        # branchName = str(branchName)

        fromPath = pullDestURL() + '/'+ branchName
        toPath = pullSourceURL()


        # tmp = fromPath
        # path = os.path.join(pullDestURL(), branchName)

        fOldPaths = []
        dir_name = []
        newFilePath = []
        i = 0
        newFilePath_to_write=[]
        for root, d_names, f_names in os.walk(fromPath):
            # print os.path.join(pullDestURL(), 'hello')
            # print os.path.exists(os.path.join(pullDestURL(), 'hello'))
        # for root, d_names, f_names in os.walk(pullDestURL()+branchName):

            print fromPath
            print d_names, f_names

            # files from Saved Branch - to be read from
            for f in f_names:
                fOldPaths.append(os.path.join(root, f))

                print fOldPaths

            # make File Path(s) to be written, later on
            for f2 in f_names:
                newFilePath_to_write.append(os.path.join(pullSourceURL(), f2))
                print newFilePath_to_write

            for i in range(0, len(f_names)):
                tmp = newFilePath_to_write[i]
                newFilePath_to_write[i] = tmp.replace('\\', '/')

                print newFilePath_to_write

            
            # =============================
            for i in range(0, len(d_names)):
                print i

                tmp = root
                root = tmp.replace('\\', '/')

                dir_name.append(os.path.join(root, d_names[i]))

                print dir_name


            if dir_name == []:
                print "No directories to Revert From"
            else:
                # these are the OLDPaths to Saved in a branch Folders
                dirsFromSaved = []
                # for item in dir_name:
                for i in range(0, len(d_names)):
                    # logic for making Saved_folder tree structure
                    dirsFromSaved.append(os.path.join(pullSourceURL(), d_names[i]))

                for i in range(0, len(dirsFromSaved)):
                    tmp = dirsFromSaved[i]
                    dirsFromSaved[i] = tmp.replace('\\', '/')

                print 'dirsFromSaved', dirsFromSaved
                for pathCreate in dirsFromSaved:
                    # tmp = os.path.join(pathCreate)
                    # os.mkdir(tmp)
                    if not os.path.exists(pathCreate):
                        os.makedirs(pathCreate)
                        print pathCreate, "\ncreated!!!"
                    else:
                        print "Already exists!!!"




            # =============================
        # logic that changes slashes in Path(s)

        for i in range(0, len(fOldPaths)):
            tmp = fOldPaths[i]
            fOldPaths[i] = tmp.replace('\\', '/')

        # for i in range(0, len(dir_name)):
        #     tmp = dir_name[i]
        #     dir_name[i] = tmp.replace('\\', '/')

        # =============================
        # Pulling/Reading data from the files
        newFileData = []
        newFilePath = []  # could just be <dir_name> -> for directories??
        for fileMe in fOldPaths:
            with open(fileMe, 'r') as readingDest:
                global opened
                opened = readingDest.readlines()
                # global destPathURL
                # destPathURL = opened[0]
                newFileData.append(opened)
                readingDest.close()
                print "\n"+fileMe
                print opened
                # return opened
                # OLD??
                # newFilePath.append(fileMe.replace(sourcePathMe, savedStrToReplace))       
        for f in fOldPaths:
            # tmp1 = os.path.join(pullSourceURL(), branchName)
            tmp1 = os.path.join(pullSourceURL(), f)
            # tmp2 = os.path.join(tmp1, f)

            tmp2 = tmp1
            tmp1 = tmp2.replace('\\', '/')
            newFilePath.append(tmp1)

    
            # print newFilePath


        # this may be dangerous
        # for f in sourcePathMe:
        #     os.remove(f)

        # delete all in SourceFolder URL
        shutil.rmtree(pullSourceURL()+'/')

        # =============================

        

        # ============Creating Folders==============
        # dirsToMake = []
        # for item in dirsFromSaved:
        #     dirsToMake.append(item)
        # print 'dirs\n', dirsToMake        

        # (loop) for loop for making Directory(s)
        # try:
        #     dirsToMake
        # except:
        #     print "No directories to Revert from."
        # else:
            


        # =============================
        # os.makedirs(pullSourceURL())
        if os.path.exists(pullSourceURL()) == False:
            print 'ran'
            os.makedirs(pullSourceURL())



        # ==============Creating Files===============
        # for loop for making Files!
        ii = 0
        for item in newFilePath_to_write:
            print 'item new? ', item
            with open(item, 'w') as savedDest:
                print "savedDest", savedDest
                # print '\n====\n', newFileData[ii]
                savedDest.write((' '.join(newFileData[ii])))
                print "written:\n", ' '.join(newFileData[ii])
                savedDest.close()

            if(ii < len(newFilePath_to_write)):
                ii += 1





    # import pdb; pdb.set_trace()   #debugger

    # dumping into <sourcePathMe>
    # pulling from <destPathURL>

    # try:
    #     destPathURL
    # except:
    #     print "destPathURL undefined!"
    # else:
    #     path = os.path.join(destPathURL, branchName)
    #     dumpInto = sourcePathMe

    #     tmp = path
    #     path = tmp.replace('\\', '/')

    #     fOldPaths = []
    #     dir_name = []
    #     i = 0
    #     for root, d_names, f_names in os.walk(path):
    #         print path
    #         # print 'd_names', d_names
    #         # gathering the data of path strings
    #         for f in f_names:
    #             # d = destPathURL + f
    #             fname.append(os.path.join(root, f))

    #             # import pdb; pdb.set_trace()
    #             print 'fname\n', fname

    #         for i in range(0, len(d_names)):
    #             # logic for pooling Directory names
    #             print i
    #             print d_names
    #             print root

    #             tmp = root
    #             root = tmp.replace('\\', '/')

    #             # print f_names
    #             dir_name.append(os.path.join(root, d_names[i]))

    #             print dir_name
    #     # =============================
    #     # logic that changes slashes in Path(s)
    #     # import pdb; pdb.set_trace()
    #     for i in range(0, len(fname)):
    #         tmp = fname[i]
    #         fname[i] = tmp.replace('\\', '/')

    #     for i in range(0, len(dir_name)):
    #         tmp = dir_name[i]
    #         dir_name[i] = tmp.replace('\\', '/')

    #     # =============================

    #     # making the files
    #     newFileData = []
    #     newFilePath = []  # could just be <dir_name> -> for directories??
    #     for fileMe in fname:
    #         with open(fileMe, 'r') as readingDest:
    #             global opened
    #             opened = readingDest.readlines()
    #             # global destPathURL
    #             # destPathURL = opened[0]
    #             newFileData.append(opened)
    #             readingDest.close()
    #             print "\n"+fileMe
    #             print opened
    #             # return opened
    #             # OLD??
    #             # newFilePath.append(fileMe.replace(sourcePathMe, savedStrToReplace))

    #     # ==========NEEDED?===================
    #     # oldFilePath=[]
    #     for oldFile in fname:
    #         # need to extract FileNames
    #         newFilePath.append(oldFile.replace(
    #             destPathURL+branchName, sourcePathMe))
    #     print newFilePath

    #     # import pdb; pdb.set_trace()

    #     # now I make the Source files -> to make Destination files!
    #     # print '=========================='
    #     for i in range(0, len(dir_name)):
    #         # for loop -> combing file URL & it's data
    #         print '====='
    #         try:
    #             dir_name[i]
    #         except:
    #             print "no directories"
    #         else:
    #             print dir_name[i]

    #         try:
    #             newFileData[i]
    #         except:
    #             print "no files"
    #         else:
    #             print newFileData[i]
    #         print '====='
    #     # =============================
    #     # this may be dangerous
    #     # for f in sourcePathMe:
    #     #     os.remove(f)

    #     # =============================
    #     # making new Directory paths
    #     savedItemURL = []
    #     for item in dir_name:
    #         # logic for making Saved_folder tree structure
    #         savedItemURL.append(item.replace(
    #             destPathURL+branchName, sourcePathMe))
    #         print 'savedItemURL', savedItemURL

    #     # =============================
    #     # delete all in SourceFolder URL
    #     shutil.rmtree(sourcePathMe+'/')

    #     # ============Creating Folders==============
    #     dirsToMake = []
    #     for item in savedItemURL:
    #         dirsToMake.append(item)
    #     print 'dirs\n', dirsToMake

    #     # (loop) for loop for making Directory(s)
    #     try:
    #         dirsToMake
    #     except:
    #         print "No directories to Revert from."
    #     else:
    #         for pathCreate in dirsToMake:
    #             # tmp = os.path.join(pathCreate)
    #             # os.mkdir(tmp)
    #             if not os.path.exists(pathCreate):
    #                 os.makedirs(pathCreate)
    #                 print pathCreate, "\ncreated!!!"
    #             else:
    #                 print "Already exists!!!"


    #     # =============================
    #     # os.makedirs(sourcePathMe)
    #     if os.path.exists(sourcePathMe) == False:
    #         print 'ran'
    #         os.makedirs(sourcePathMe)

    #     # ==============Creating Files===============
    #     # for loop for making Files!
    #     ii = 0
    #     for item in newFilePath:
    #         print 'item new? ', item
    #         with open(item, 'w') as savedDest:
    #             print "savedDest", savedDest
                
    #             # import pdb; pdb.set_trace()
                
                
    #             # print '\n====\n', newFileData[ii]
    #             savedDest.write((' '.join(newFileData[ii])))
    #             print "written:\n", ' '.join(newFileData[ii])
    #             savedDest.close()
    #         if(ii < len(newFilePath)):
    #             ii += 1


# ====================================================
print sys.argv

# os.getcwd()

for i, argMe in enumerate(sys.argv):
        if(sys.argv[0] == ""): 
            print "\n\n==============\nYou may be new here!\n\nTo get things going, add a source PATH Location!\n\nUse the <-changeSource> command after the String of Python Path!"

        # making CLI stuff
        # =============================

        if(argMe == "-quickinit"):
        
            tmp1 = raw_input('Init Path?\n')
            tmp2 = raw_input('Source Path?\n')
            tmp3 = raw_input('Dest Path?\n')
            # quickInit(sys.argv[1], sys.argv[2], sys.argv[3])
            quickInit(tmp1, tmp2, tmp3)


        # =============================
        if(argMe == '-init'):
            try:
                sys.argv[i+1]
            except:
                print "Please define a Path! Of your Main directory"
            else:
                init(sys.argv[i+1])

        # =============================
        if(argMe == '-changeSource'):
            # cleanSourceURL()
            # if(i+1<len(sys.argv)):
            # meChanged = sys.argv[i+1].replace('\\', '/')
            saveSourceURL(sys.argv[i+1])
            pullSourceURL()
            # saveDestURL('')
            # pullDestURL()

        # =============================

        if(argMe == '-makeDest'):
            try:
                sys.argv[i+1]
            except:
                print "oops - you need a path String or just \'\'"
            else:
                if(sys.argv[i+1] == "" or sys.argv[i+1] == ''):
                    print "Making default \'Destination\'"
                    saveDestURL("")
                else:
                    saveDestURL(sys.argv[i+1])

            # =============================

        if(argMe == '-branch'):
            print 'theSource'
            pullSourceURL()
            pullDestURL()
            if(os.path.exists(theSource) == False):
                print "\n====\nNeeds a file for source path"
                print "try, -changeSource parameter"
            else:
                print 'make branch?', '\nwith this name:', sys.argv[i+1]

                branch = raw_input('Run? (yes/no) ')
                if(branch == 'yes'):
                    # branchMe(sys.argv[i+1])
                    branchMe(str(sys.argv[i+1]))

        # =============================

        if(argMe == '-revert'):
            # pullSourceURL()
            # pullDestURL()
            if os.path.isdir(pullSourceURL()):
                print "Source Path is good"
                print pullSourceURL()
                try:
                    sys.argv[i+1]
                except:
                    print "Branch not found!\nTry creating one! \"-branch <name>\""
                else:
                    revert(sys.argv[i+1])
            else:
                os.makedirs(pullSourceURL())
                print "Source Path (Re)Created!"

                revert(sys.argv[i+1])


        # =============================
        savedIndexes = []
        if(argMe == '-pullBranches'):
            pullSourceURL()
            pullDestURL()
            try:
                os.listdir(destPathURL)
            except:
                print "NO Branches, yet!"
            else:
                # branches = os.listdir(destPathURL)
                print "\nThese are your Saved Branchess"
                print os.listdir(destPathURL)
                print "----"
            
        if (argMe == '-select'):
            savedIndexes = os.listdir(pullDestURL())
            try:
                sys.argv[2]
            except:
                print "out of bounds"
            else:
                print "====\nYou will be Reverting to:"
                print savedIndexes[int(sys.argv[2])]
                print "\n"
            # import pdb; pdb.set_trace()   #debugger
                input = raw_input("Continue? (yes/no)")
                if(input == 'yes'):
                    revert(savedIndexes[int(sys.argv[2])])      # the 2nd arg - made to an int - of the index - of pulledbranches
                else:
                    print "Cancelled Reverting"


        # =============================
        if(argMe == '-log'):
            try:
                sys.argv[i+1]
            except:
                print "Please include a Message to append to Log.txt file!"
            else:
                saveAMilestone(str(sys.argv[i+1]))

        # =============================
        if(argMe == '-list'):
            pullSourceURL()
            pullDestURL()
            # try:
            print "========"
            print "sourcePathMe:"
            try:
                sourcePathMe
            except:
                print "failed"
                print "it is is undefined"
            else:
                print pullSourceURL()

            print "\n"

            print "destPathURL:"
            try:
                destPathURL
            except:
                print "failed"
                print "it is undefined"
            else:
                print pullDestURL()
            print "========"
            # except:
            #     print 'error'
        