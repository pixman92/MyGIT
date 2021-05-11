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


# ==========================
# Block of code -> saving SRC path
def saveSourceURL(urlMe):
    # save path to sourceFolder

    if (urlMe == "''"):
        print "\n========\nPLEASE! You need to specify an Existing Path!\n========\n"
    else:

        if urlMe[len(urlMe)-1] == '/':
            print "Uh oh, Source Path should not end with \'\\'!!"
        else:
            try:
                os.path.exists(urlMe)
            except:
                print "Source not made!"
            else:

                try:
                    os.path.isdir(urlMe)
                except:
                    print "Source Path entered! Not a URL"
                else:
                    print "Creating the URL!"
                    if os.path.exists(urlMe) == True:
                        print "already exists\nLeaving"
                    else:
                        os.makedirs(urlMe)
                        # if os.path.isdir(urlMe):
                        file_name = os.path.join(os.getcwd(), 'savedURL.txt')

                        # universal Path maker
                        tmp = file_name
                        file_name = tmp.replace('\\', '/')

                        # make the URL universal
                        tmp = urlMe
                        urlMe = tmp.replace('\\', '/')

                        with open(file_name, 'w') as data:
                            data.write(urlMe)
                            data.close()


            # else:
            #     # if it's a new Directory -> make it, else if non value dir
            #     print "\n====\nTry again, needs to be Valid Directory\n===="
            #     createDir = raw_input(
            #         "\nWould you like to create this \"" + urlMe + "\" as a New Path? ")
            #     # file_name = os.path.join(os.getcwd(), 'savedURL.txt')
            #     if(createDir == "yes"):
            #         os.mkdir(urlMe)
            #         # if os.path.isdir(urlMe):
            #         #     print "made dir, is Valid"
            #         file_name = os.path.join(urlMe, 'savedURL.txt')
            #         tmp = file_name
            #         file_name = tmp.replace('\\', '/')

            #         # make the URL universal
            #         tmp = urlMe
            #         urlMe = tmp.replace('\\', '/')

            #         with open(file_name, 'w') as data:
            #             data.write(urlMe)
            #             data.close()





def pullSourceURL():
    # pull out the path, saved in text document
    # file_name = os.path.join(os.getcwd(), 'savedURL.txt')
    try:
        file_name = os.path.join(os.getcwd(), 'savedURL.txt')
      
            # return returnMe
    except:
        print "error"
        print "you need to set Source Path"
        print file_name
        print theSource
    global theSource
    theSource = file_name
    with open(file_name, 'r') as data:
        returnMe = data.readlines()
        global sourcePathMe


        sourcePathMe = returnMe[0]

        tmp = sourcePathMe
        sourcePathMe = tmp.replace('\\', '/')

        print "sourcePathMe: ", sourcePathMe

        data.close()


def cleanSourceURL():
    # delete the whole file
    fileMe = os.path.join(os.getcwd(), 'savedURL.txt')
    os.remove(fileMe)

# ==========================


def saveDestURL(strSavedToDestURL):
    # saves a path to where you want the commits to save to, a path string

    pullSourceURL()

    # if(strSavedToDestURL == ""):
    #     print "It seems you didn't specify a PATH Directory for your source, it will now point to the root Directory, \'Saved\'"




    # import pdb; pdb.set_trace()   #debugger

    # pullSourceURL()

    # os.getcwd()
    # os.path.abspath(sourcePathMe)
    # os.chdir('..')

    # make a LEVEL UP path
    preGetPath = os.path.abspath(os.path.join(sourcePathMe, '..'))
    # end it with a slash
    preGetPath = preGetPath + '/'

    # change all slashes
    meChangedDest = preGetPath.replace('\\', '/')
    # save file path (all but filename)
    saved = os.path.join(meChangedDest, 'Saved/')
    # add filename
    file_name = os.path.join(meChangedDest, 'savedDestURL.txt')

    # import pdb; pdb.set_trace()   #debugger

    # make file_name global, to be used in pullDestURL()
    # global destPathSet
    # destPathSet = file_name
    # import pdb; pdb.set_trace()
    
    # try:
    #     os.path.exists(file_name) == False
    # except:
    #     print 'path already made'
    # else:
    #     with open(file_name, 'w') as savedDest:
    #         savedDest.write(saved)
    #         savedDest.close()
    #     print saved

    if os.path.exists(file_name) == True:
        print 'path already made'
        destPathURL = file_name
    else:
        with open(file_name, 'w') as savedDest:
            savedDest.write(saved)
            savedDest.close()
        print saved


def pullDestURL():
    # pulls up the destPathURL string
    pullSourceURL()

    # file_name = os.getcwd()
    # import pdb; pdb.set_trace()

    # try:
    # file_name = os.path.join(os.getcwd(), 'savedDestURL.txt')

    try:
        os.path.isdir(sourcePathMe)
    except:
        print "sourcePathMe undefined! Try reseting with <-changeSource> param"
    else:

        # =============================
        # make a LEVEL UP path
        preGetPath = os.path.abspath(os.path.join(sourcePathMe, '..'))
        # end it with a slash
        preGetPath = preGetPath + '/'

        # change all slashes
        meChangedDest = preGetPath.replace('\\', '/')

        global transToBranchMe
        transToBranchMe = meChangedDest

        # save file path (all but filename)
        saved = os.path.join(meChangedDest, 'Saved/')
        # add filename
        file_name = os.path.join(meChangedDest, 'savedDestURL.txt')

        # try:
        #     file_name
        # except:
        #     print 'destPathURL, could not be located!'
        # else:
        #     with open(file_name, 'r') as readingDest:
        #         returnMe = readingDest.readlines()
        #         global destPathURL
        #         destPathURL = returnMe[0]
        #         readingDest.close()
        #         print 'destPathURL', destPathURL
        #         print 'file_name', file_name
        #         # return returnMe
        # import pdb; pdb.set_trace()   #debugger

        if os.path.exists(file_name)==False:
            print 'destPathURL, could not be located!'
        else:
            with open(file_name, 'r') as readingDest:
                returnMe = readingDest.readlines()
                global destPathURL
                destPathURL = returnMe[0]
                readingDest.close()
                print 'destPathURL', destPathURL
                print 'file_name', file_name
                # return returnMe  


# ==========================


def saveAMilestone(message):
    now = datetime.datetime.now()
    with open('log.txt', 'w') as log:
        log.write(now, ' --- ', message)
        log.close()


# ==========================
def run():
    revert2('nope3')
    # pullSourceURL()
    # shutil.rmtree(sourcePathMe+'/')
# ==========================


def branchMe(name):
    pullSourceURL()
    pullDestURL()

    try:
        theSource
    except:
        print 'theSource is undefined'
    else:

        try:
            transToBranchMe
        except:
            print "branch file reference has malfunctioned"
        else:
            if not os.path.exists(transToBranchMe+'Saved/'+name):
                os.makedirs(transToBranchMe+'Saved/'+name)

            if os.path.exists(theSource) == False:
                print "Cannot Continue..."
                print "Retry \'-changeSource\' command with a destination path"
            else:

                # import pdb; pdb.set_trace()   #debugger

                # print 'sourcePathMe', sourcePathMe

                path = sourcePathMe  # this is IMPORTANT
                if not os.path.exists(transToBranchMe+'Saved'):
                    os.makedirs(transToBranchMe+'Saved')

                if not os.path.exists(transToBranchMe+'Saved/'+name):
                    os.makedirs(transToBranchMe+'Saved/'+name)

                else:

                    # use: destPathURL
                    # savedStrToReplace = sourcePathMe+ '/Saved/'+ name + '/'
                    savedStrToReplace = transToBranchMe + 'Saved/' + name
                    tmp = savedStrToReplace
                    savedStrToReplace = tmp.replace('\\', '/')

                    # =============================
                    # pulling data from Source folder <transToBranchMe>
                    fname = []
                    dir_name = []
                    i = 0
                    for root, d_names, f_names in os.walk(path):
                        print path
                    # print 'd_names', d_names
                    # gathering the data of path strings
                        for f in f_names:
                            # d = destPathURL + f

                            # converting <f_names> files (f) -> to universal URL(s)
                            tmpPath = os.path.join(root, f)
                            tmpPathUniversal = tmpPath
                            tmp = tmpPath
                            tmpPath = tmp.replace('\\', '/')
                            fname.append(tmpPath)

                            print 'fname\n', fname

                        for i in range(0, len(d_names)):
                            # logic for pooling Directory names
                            print i
                            print d_names
                            print root
                            # print f_names
                            dir_name.append(os.path.join(root, d_names[i]))

                            print dir_name
                        # for files in fname:
                        # dir_name[0]

                        # ==========================
                        # making new Directory paths
                    try:
                        dir_name
                    except:
                        print "NO directories found"
                    else:
                        for item in dir_name:
                            # logic for making Saved_folder tree structure
                            savedItemURL = item.replace(
                                sourcePathMe, savedStrToReplace)
                            print savedItemURL

                    # ==========================
                    # making the files
                    newFileData = []
                    for fileMe in fname:
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

                    oldFilePath = []
                    newFilePath = []

                    for oldFile in fname:
                        # need to extract FileNames
                        newFilePath.append(oldFile.replace(sourcePathMe, savedStrToReplace))
                    # newFilePath.append(oldFile)
                    print newFilePath

                    # now I make the Source files -> to make Destination files!
                    # print '=========================='
                    for i in range(0, len(newFilePath)):
                        # for loop -> combing file URL & it's data
                        print '====='
                        print newFilePath[i]
                        print newFileData[i]
                        print '====='

                    # new files, made and sent to Destination folder
                    # ==========================
                    dirsToMake = []
                    for item in dir_name:
                        dirsToMake.append(item.replace(sourcePathMe, savedStrToReplace))
                    print 'dirs\n', dirsToMake

                    # ==========================

                    # import pdb; pdb.set_trace()
                    # for loop for making Directory(s)
                    try:
                        dirsToMake
                    except:
                        print "no Directories to branch out!"
                    else:
                        for pathCreate in dirsToMake:
                            # tmp = os.path.join(pathCreate)
                            # os.mkdir(tmp)
                            if not os.path.exists(pathCreate) or dirsToMake is not None:
                                os.makedirs(pathCreate)
                                print pathCreate, "\ncreated!!!"
                            else:
                                print "Already exists!!!"

                        # ==============Still in use===============
                        # for loop for making Files!

                        # import pdb; pdb.set_trace()   #debugger

                    ii = 0
                    try:
                        newFilePath
                    except:
                        print "NO files found! Something wrong?"
                    else:
                        for item in newFilePath:
                            # print item

                            # with open(item, 'w') as savedDest:          # changed "saveDest" with "newFilePath"
                            #     # print 'savedDest', savedDest
                            #     # print '\n====\n', newFileData[ii]
                            #     print "item", item
                            #     savedDest.write((' '.join(newFileData[ii])))
                            #     print "written:\n", ' '.join(newFileData[ii])
                            #     savedDest.close()
                            # if(ii<len(newFilePath)):
                            #     ii+=1
                            # import pdb; pdb.set_trace()   #debugger

                            with open(item, 'w') as savedFile:
                                print 'item', item
                                savedFile.write((' '.join(newFileData[ii])))
                                print "written:\n", ' '.join(
                                    newFileData[ii])

                                savedFile.close()
                            if(ii < len(newFilePath)):
                                ii += 1

                            # tmp = item.replace(newFilePath, destPathURL+name)

                        # =============================
                        # import pdb; pdb.set_trace()

                        # ==========================


def revert2(branchName):
    pullSourceURL()
    pullDestURL()

    if os.path.exists(sourcePathMe) == False:
        print 'ran'
        os.makedirs(sourcePathMe+'/')
    # dumping into <sourcePathMe>
    # pulling from <destPathURL>

    try:
        destPathURL
    except:
        print "destPathURL undefined!"
    else:
        path = os.path.join(destPathURL, branchName)
        dumpInto = sourcePathMe

        tmp = path
        path = tmp.replace('\\', '/')

        fname = []
        dir_name = []
        i = 0
        for root, d_names, f_names in os.walk(path):
            print path
            # print 'd_names', d_names
            # gathering the data of path strings
            for f in f_names:
                # d = destPathURL + f
                fname.append(os.path.join(root, f))

                # import pdb; pdb.set_trace()
                print 'fname\n', fname

            for i in range(0, len(d_names)):
                # logic for pooling Directory names
                print i
                print d_names
                print root

                tmp = root
                root = tmp.replace('\\', '/')

                # print f_names
                dir_name.append(os.path.join(root, d_names[i]))

                print dir_name
        # =============================
        # logic that changes slashes in Path(s)
        # import pdb; pdb.set_trace()
        for i in range(0, len(fname)):
            tmp = fname[i]
            fname[i] = tmp.replace('\\', '/')

        for i in range(0, len(dir_name)):
            tmp = dir_name[i]
            dir_name[i] = tmp.replace('\\', '/')

        # =============================

        # making the files
        newFileData = []
        newFilePath = []  # could just be <dir_name> -> for directories??
        for fileMe in fname:
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

        # ==========NEEDED?===================
        # oldFilePath=[]
        for oldFile in fname:
            # need to extract FileNames
            newFilePath.append(oldFile.replace(
                destPathURL+branchName, sourcePathMe))
        print newFilePath

        # import pdb; pdb.set_trace()

        # now I make the Source files -> to make Destination files!
        # print '=========================='
        for i in range(0, len(dir_name)):
            # for loop -> combing file URL & it's data
            print '====='
            try:
                dir_name[i]
            except:
                print "no directories"
            else:
                print dir_name[i]

            try:
                newFileData[i]
            except:
                print "no files"
            else:
                print newFileData[i]
            print '====='
        # =============================
        # this may be dangerous
        # for f in sourcePathMe:
        #     os.remove(f)

        # =============================
        # making new Directory paths
        savedItemURL = []
        for item in dir_name:
            # logic for making Saved_folder tree structure
            savedItemURL.append(item.replace(
                destPathURL+branchName, sourcePathMe))
            print 'savedItemURL', savedItemURL

        # =============================
        # delete all in SourceFolder URL
        shutil.rmtree(sourcePathMe+'/')

        # ============Creating Folders==============
        dirsToMake = []
        for item in savedItemURL:
            dirsToMake.append(item)
        print 'dirs\n', dirsToMake

        # (loop) for loop for making Directory(s)
        try:
            dirsToMake
        except:
            print "No directories to Revert from."
        else:
            for pathCreate in dirsToMake:
                # tmp = os.path.join(pathCreate)
                # os.mkdir(tmp)
                if not os.path.exists(pathCreate):
                    os.makedirs(pathCreate)
                    print pathCreate, "\ncreated!!!"
                else:
                    print "Already exists!!!"


        # =============================
        # os.makedirs(sourcePathMe)
        if os.path.exists(sourcePathMe) == False:
            print 'ran'
            os.makedirs(sourcePathMe)

        # ==============Creating Files===============
        # for loop for making Files!
        ii = 0
        for item in newFilePath:
            print 'item new? ', item
            with open(item, 'w') as savedDest:
                print "savedDest", savedDest
                
                # import pdb; pdb.set_trace()
                
                
                # print '\n====\n', newFileData[ii]
                savedDest.write((' '.join(newFileData[ii])))
                print "written:\n", ' '.join(newFileData[ii])
                savedDest.close()
            if(ii < len(newFilePath)):
                ii += 1


# ====================================================
print sys.argv

# os.getcwd()

for i, argMe in enumerate(sys.argv):
        if(sys.argv[0] == ""): 
            print "\n\n==============\nYou may be new here!\n\nTo get things going, add a source PATH Location!\n\nUse the <-changeSource> command after the String of Python Path!"

    # making CLI stuff

    # if(argMe == '-source'):

        if(argMe == '-changeSource'):

            try:
                sys.argv[i+1]
            except:
                print "error with parameters"
            else:
                # cleanSourceURL()
                # if(i+1<len(sys.argv)):
                # meChanged = sys.argv[i+1].replace('\\', '/')
                saveSourceURL(sys.argv[i+1])
                pullSourceURL()
                saveDestURL('')
                pullDestURL()

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
            pullSourceURL()
            pullDestURL()
            if os.path.isdir(sourcePathMe):
                print "Source Path is good"
                print sourcePathMe
                try:
                    sys.argv[i+1]
                except:
                    print "Branch not found!\nTry creating one! \"-branch <name>\""
                else:
                    revert2(sys.argv[i+1])
            else:
                os.makedirs(sourcePathMe)
                print "Source Path (Re)Created!"

                revert2(sys.argv[i+1])

                


            # os.path.abspath(sourcePathMe)
            # os.chdir('..')
            # saved = os.path.join(os.getcwd(), 'Saved/')
            # if os.path.isdir(saved):
            #     print saved
            #     print 'path is Valid'
            # else:
            #     print 'path is Invalid'
                # print "Your options"
                # print os.listdir(sourcePathMe);/

            # srcMe = raw_input("Which branch to go back too?")

        # =============================
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
                print sourcePathMe

            print "\n"

            print "destPathURL:"
            try:
                destPathURL
            except:
                print "failed"
                print "it is undefined"
            else:
                print destPathURL
            print "========"
            # except:
            #     print 'error'
