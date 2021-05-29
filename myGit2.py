import pdb
import os
import shutil
import sys
import datetime
from os.path import dirname
import re




def removeXs(string):
    # function to remove char literal 'x0' from strings - on windows machines
    savedIndex = []
    string = repr(string)
    charLiteral = 'x0'
    tmpStr = string
    tmpStr = string.replace(charLiteral, "")
    tmpStr = removeLiterals(tmpStr)
    tmpStr = tmpStr[tmpStr.find('\'')+1: -1] 
    # import pdb; pdb.set_trace()   #debugger
    return tmpStr

# =============================
def removeLiterals(stringMe):
    stringMe = str(stringMe)
    # searchFor = '\\x0'
    # tmp = stringMe
    # stringMe = tmp.replace('\\x0', '\\')
    # import pdb; pdb.set_trace()   #debugger
    tmp = stringMe
    stringMe = tmp.replace('\\', '/')
    tmp = stringMe
    stringMe = tmp.replace('//', '/')
    tmp = stringMe
    stringMe = tmp.replace('\'', '/\'')
    tmp = stringMe
    stringMe = tmp.replace('\a', '/a')
    tmp = stringMe
    stringMe = tmp.replace('\b', '/b')
    tmp = stringMe
    stringMe = tmp.replace('\f', '/f')
    tmp = stringMe
    stringMe = tmp.replace('\n', '/n')
    tmp = stringMe
    stringMe = tmp.replace('\r', '/r')
    tmp = stringMe
    stringMe = tmp.replace('\t', '/t')
    tmp = stringMe
    stringMe = tmp.replace('\v', '/v')
    tmp = stringMe
    stringMe = tmp.replace('\a', '/a')
    tmp = stringMe
    stringMe = tmp.replace('\ooo', '/ooo')

    # arrayAlreadyThere = [r'\0', r'\1', r'\2', r'\3', r'\4', r'\5', r'\6', r'\7', r'\8', r'\9']
    # arrayAlreadyThere = ['\x0', ]
    # arrayReplace = ['/0', '/1', '/2', '/3', '/4', '/5', '/6', '7/ ', '/8', '/9']
    # for i in range(0, 9):
    #     import pdb; pdb.set_trace()   #debugger
    #     tmp = stringMe
    #     # tmp2 = str(arrayAlreadyThere[i])
    #     if(stringMe.index(arrayAlreadyThere[i])==1):
    #         stringMe = tmp.replace(tmp2, arrayReplace[i])
    #     import pdb; pdb.set_trace()   #debugger
            

    return stringMe

def removeFirstSlash(stringMe):
    stringMe = stringMe[1::]
    return stringMe

# =============================

global recursivePath 
global savedPathToGITAlternative

def savedGITAltPathReturn(pathAdd):
    # function - for Returning the Path to savedGITAlternative


    # logic - if pathAdd == "" or not
    if(pathAdd==""):
        savedPathToGITAlternative = os.path.join(os.path.realpath('.'))
        print "savedPathToGITAlternative?", savedPathToGITAlternative
    else:
        savedPathToGITAlternative = os.path.join(os.path.realpath('.'), pathAdd)
        print "savedPathToGITAlternative?", savedPathToGITAlternative

    # removing slashes
    # tmp3 = savedPathToGITAlternative
    # savedPathToGITAlternative = tmp3.replace('\\', '/')
    savedPathToGITAlternative = removeLitearls(savedGITAltPathReturn)

    # listed dirs of savedPathToGITAlternative
    arrayOfDirs = os.listdir(savedPathToGITAlternative)
    found = False
    for item in arrayOfDirs:
       if(item=='savedGITAlternative'):
           found = True
        
    if (found == False):
        print "Directory doesn't have /savedGITAlternative"
        return ""

    else:
        # return if not found
        print "savedGITAlternative dir - found!"
        return savedPathToGITAlternative


# =============================
def recursiveReturn(middle):      #TODO - add a param - for middle ground (1 level down (in folder tree), from code)
    # returns path for looping recursively through tree folders
    # recursivePath = os.path.join(os.path.realpath('.'), 'YouTube_savedForLater', 'code')

    if(middle==""):
        recursivePath = os.path.join(savedGITAltPathReturn(''), 'code')
        print "recursivePath", recursivePath
    else:
        recursivePath = os.path.join(savedGITAltPathReturn(''), middle, 'code')
        

    tmp3 = recursivePath
    recursivePath = tmp3.replace('\\', '/')
   
    return recursivePath
# =============================

def run():
    runNew("C:/Users/gotru/OneDrive/testFolder/code/heya")  
    # makeDirsAndFiles("C:/Users/gotru/OneDrive/testFolder/code/heya", '', '', 'C:/Users/gotru/OneDrive/testFolder/code/2')
    makeDirsAndFiles("C:/Users/gotru/OneDrive/testFolder/code/4")

    # dec('C:\Users\gotru\OneDrive\testFolder\code\3\asdf\aser\x04\x03\srs')
    # stuff(freedFromLiterals)

global BIGSave
BIGSave = []


def runNew(pathMeNew):      #pathMeNew = branch base (beginning - not yet recursived) source
    # TODO - turn this into a branch function
    # TODO - how to pull data
    global pulledDirs
    global pulledRoots
    pulledDirs = []
    pulledRoots = []

    global pulledFiles
    pulledFiles = []

    global savedDirsForBranch
    savedDirsForBranch = []
    global savedFilesForBranch
    savedFilesForBranch = []
    global pathMeStored 
    pathMeStored = pathMeNew


    pathMeNew = removeXs(pathMeNew)
    pathMeNew = removeLiterals(pathMeNew)
    print "pathMeNew", pathMeNew

    pathMeJoined = ""
    currentRoot = ""
    pulledRoots = []

    i=0
    for root, dirs, files in os.walk(pathMeNew):     #pathMeJoined -> pathMe
        # logic that pulls EVERYTHING - new root/dirs/and fie
        # print "\n===="
        # print "root", root
        # print "dirs", dirs
        # print "files", files
        # print "====\n"
        pulledRoots.append(root)

        root = removeLiterals(root)
        # these 2 for loops -> create pulledbranches/pulledFiles variables
        for d in dirs:
            pulledDirs.append(os.path.join(root, d))

        for f in files:
            pulledFiles.append(os.path.join(root, f))

        # =============================
        # these 2 for loops -> make just the Unique File tree to just file names
        for i in range(0, len(pulledDirs)):
            pulledDirs[i] = removeLiterals(pulledDirs[i])

        for i in range(0, len(pulledFiles)):
            # tmp = pulledFiles[i]
            # pulledFiles[i] = tmp.replace('\\', '/')
            pulledFiles[i] = removeLiterals(pulledFiles[i])
        # 
        
        
        # if i>50:
        #     break
        # else:
        #     i+=1
        currentRoot = root

        # another replace job - to be fixed later on - TODO
        tmp = currentRoot
        currentRoot = tmp.replace('\\', '/')

        # print "pulledRoots", pulledRoots
        # print "currentRoot", currentRoot
        # print "pathMe", pathMe
        # print "====="        


    print "pulledDirs", pulledDirs
    print "pulledFiles", pulledFiles        #can be used to read
    

    # ============CRITICAL CODE=================
    # picks off just the tail end of the 'dirs' & 'filenames'
    savedDirsForBranch = []
    for i in range(0, len(pulledDirs)):
        savedDirsForBranch.append(pulledDirs[i].replace(pathMeNew, ""))   #changing pullSourceURL() -> pathMeNew

    savedFilesForBranch = []
    for i in range(0, len(pulledFiles)):
        savedFilesForBranch.append(pulledFiles[i].replace(pathMeNew, ""))  #changing pullSourceURL() -> pathMeNew

    print "savedDirsForBranch", savedDirsForBranch
    print "savedFilesForBranch", savedFilesForBranch
    # import pdb; pdb.set_trace()   #debugger 
    
        


    # import pdb; pdb.set_trace()   #debugger


    # TODO - take files and directories, make them just file names
        # newText = pulledFiles[0].replace(pullSourceURL(), "")
def makeDirsAndFiles(newSinglePathToWrite): #savedPath,savedDirs, savedFiles, newFilePath_to_write
    # I have made the directories self create
    # TODO - push through and create files!
    

    # print "pulledFiles", pulledFiles

    # savedPath = os.path.join(savedPath)
    # savedPath = removeXs(savedPath)
    # savedPath -> is location of files

    # import pdb; pdb.set_trace()   #debugger

    # to be readded when source directory is established
    # print "Make branch at, ", savedPath, " location?"
    
 

    anyUnmade = True
    tmpPath = os.path.join(newSinglePathToWrite, savedDirsForBranch[0])
    for i in range(0, len(savedDirsForBranch)):
        
        # import pdb; pdb.set_trace()   #debugger

        tmpPath = os.path.join(newSinglePathToWrite, savedDirsForBranch[i])
        # tmpPath = the single path to start the transfer to a branch folder
        if os.path.isdir(tmpPath) == True:
            anyUnmade = False 
            print "Path Already Exists", tmpPath
        else:
            # if the folders don't exist? Create them!
            os.makedirs(tmpPath)
            print "Creating Path!", tmpPath
    if anyUnmade == False:
        print "There were no unmade Directories"

    # import pdb; pdb.set_trace()   #debugger                


    # =============================
    # making Directories -> branch Path
    global dirFraction
    # stripping of pullSourceURL() string
    dirFraction  = []
    newPathsToWrite = []
    for i in range(0, len(pulledDirs)):
        print "pulledDirs2", pulledDirs
        dirFraction.append(pulledDirs[i].replace(newSinglePathToWrite, ""))#saves file structure beyhond the sourcePath
        print "dirFraction", dirFraction
        





    # SUPER CRITICAL for Windows machines
    # for i in range(0, len(dirFraction)):
    #     dirFraction[i] = removeFirstSlash(dirFraction[i])
    # =============================
    # Getting Stupid Paths - working
    letsMakeDirs = []
    for item in dirFraction:
        # stripping out the PrePath level - from path too ../
        letsMakeDirs.append(os.path.join(newSinglePathToWrite, item))   # this newSinglePathToWrite -> makes the code push to a unified folder

    for i in range(0, len(letsMakeDirs)):
        letsMakeDirs[i] = removeLiterals(letsMakeDirs[i])

    # import pdb; pdb.set_trace()   #debugger

    # =============================

    # import pdb; pdb.set_trace()   #debugger
    # creating Directories - TODO - redo this later
    for item in letsMakeDirs:
        # import pdb; pdb.set_trace()   #debugger     #looking to exam: destWriteWhole
        if os.path.exists(item) == False:
            os.makedirs(item)
            print 'Creating folder structure!'
        else:
            print item, " already exists"


    # import pdb; pdb.set_trace()   #debugger

    # ============OLD???=================
    # itemSaved = ""
    # tmp =""
    # savePathMinusSlash = ""
    # # tmp = tmp.join(savedPath, savedDirs[0])
    # # for itemMe in savedDirs:
    #     # item = removeLiterals(item)


    # # Variables to be re-initiated when SourceURL is established
    # savePathMinusSlash = removeFirstSlash(savePathMinusSlash)
    # import pdb; pdb.set_trace()   #debugger
    # itemSaved = os.path.join(savedPath, savePathMinusSlash)
    # itemSaved = removeLiterals(itemSaved)   
    
    # print "itemSaved", itemSaved

    # # import pdb; pdb.set_trace()   #debugger
    # i (os.path.exists(itemSaved))==True:
    #     print "it exists!", itemSaved
    # else:
    #     print "doesn't yet exist", itemSaved
    #     print "\ncreating!", 
    #         # os.makedirs(itemSaved)
    # # import pdb; pdb.set_trace()   #debuggerf
    # =============================
    savedFileData = []


    # for loops - to take in data and write it out
    # for f in savedFiles:
    #     import pdb; pdb.set_trace()   #debugger
    #     with open(os.path.join(savedPath, f), 'w') as fileMe:
    #         fileMe.write('hey')


    # TODO - pull data from filePath 
    # store that data
    # 1 - strip filePath
        # String.replace(pullSourceURL(), filePath) 
    # 2 - add new filePath to baseline 
        # os.path.join(toSaveToURL, remainsOfStrippedString)

    # tmpFileName = os.path.join(savedPath, savedFiles[0])
    global added
    added = ""
    global savedReadData
    savedReadData = []
    # pulls in Data from pulledFiles
    print "pulledFiles 2", pulledFiles
    for i in range(0, len(pulledFiles)):
        print "i", i
        print "pulledFiles[i]", pulledFiles[i]
        with open(pulledFiles[i], 'r') as fileToRead:
            # print "reading file", fileToRead
            # fileToRead.readlines()
            # print 'data', fileToRead.readlines()
            added = fileToRead.readlines()
            savedReadData.append(added)
            fileToRead.close()

    print "savedReadData", savedReadData        # variable - with the data to be written to 'branch destination'    


    global destWriteWhole
    # stripping of pullSourceURL() string
    destWriteWhole  = []
    newPathsToWrite = []
    for i in range(0, len(pulledFiles)):
        print "pulledFiles2", pulledFiles
        
        tmp = os.path.join(newSinglePathToWrite, savedDirsForBranch[i])

        destWriteWhole.append(tmp)

        # destWriteWhole.append(pulledFiles[i].replace(newSinglePathToWrite, savedFilesForBranch[i]))    #saves file structure beyhond the sourcePath - changed pullSourceURL() -> newSinglePathToWrite
        print "destWriteWhole", destWriteWhole

    for i in range(0, len(destWriteWhole)):
        destWriteWhole[i] = removeLiterals(destWriteWhole[i])



    import pdb; pdb.set_trace()   #debugger
    
    # import pdb; pdb.set_trace()   #debugger

    # =============================
    # to be changed based on machine of OS
    # just removing '/' -> it would otherwise corrupt creating the FilePath
    # for i in range(0, len(destWriteWhole)):
    #     destWriteWhole[i] = removeFirstSlash(destWriteWhole[i])
    # print "destWriteWhole", destWriteWhole
    # =============================


    # import pdb; pdb.set_trace()   #debugger 
    # is destWriteWhole different than savedFilesForBranch??? - they are comparable - but differ based on founding file structure given
    # will sort out later

    # =============================
    # this for loop -> creates or doesn't create the directories
    # for item in storedNewPath:
    # destWriteWhole = []
    # for item in destWriteWhole:       # for all the baseline Paths - files
    #     # item = removeFirstSlash(item)   #allows for a smoother URL formation - by removing / from index of 0  # unnecessary?? 
    #     destWriteWhole.append(os.path.join(newSinglePathToWrite, item))

    # print "destWriteWhole", destWriteWhole
    # # import pdb; pdb.set_trace()   #debugger

    # for i in range(0, len(destWriteWhole)):
    #     destWriteWhole[i] = removeLiterals(destWriteWhole[i])

    # =============================
    # this code is confused - it makes file paths into directories - thus failing
    # for item in destWriteWhole:
    #     # import pdb; pdb.set_trace()   #debugger     #looking to exam: destWriteWhole
    #     if os.path.isdir(item) == False:
    #         os.makedirs(item)
    #         print 'Creating folder structure!'
    #     else:
    #         print item, " already exists"
        
    


    # pulledFiles & savedReadData = correlate by index
    # import pdb; pdb.set_trace()   #debugger
    for i in range(0, len(destWriteWhole)):
        # import pdb; pdb.set_trace()   #debugger
            try:
                with open(destWriteWhole[i], 'w') as letsWriteThis:
                    print "letsWriteThis", letsWriteThis
                    # print "savedReadData", destWriteWhole[i]

                    if savedReadData[i] == "" or savedReadData[i] == []:
                        print destWriteWhole[i] + "Is an Empty file!"
                    else:
                        letsWriteThis.write(str(savedReadData[i]))
                        letsWriteThis.close()


                    # try:
                    #     savedReadData
                    #     savedReadData[i] == []
                    # except:
                    #     print "was empty"

                    # else:
                    #     letsWriteThis.write(str(savedReadData[i]))
                    #     letsWriteThis.close()

                    # if savedReadData[i] is None:
                    #     print destWriteWhole[i] + " is an EMPTYP FILE!"
                    # else:
                    #     letsWriteThis.write(savedReadData[i])
                    #     letsWriteThis.close()
            except IOError:
                print "Error with file!"
                # if savedReadData[i] == "" or savedReadData[i] == []:
                #     raise Exception(destWriteWhole[i] + "Is an Empty file!")            
            # else:
            #     pass


            # print "letsWriteThis", letsWriteThis
            import pdb; pdb.set_trace()   #debugger


    # =============================
    # savedFiles[0] = removeFirstSlash(savedFiles[0])
    # writeFiles = os.path.join(newFilePath_to_write, savedFiles[0])
    # writeFiles = removeLiterals(writeFiles)
    # import pdb; pdb.set_trace()   #debugger

    

    # with open(writeFiles, 'w') as fileMe:
    #     print "file to write too", fileMe
    #     fileMe.write()

    # import pdb; pdb.set_trace()   #debugger


            
    

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
    # point to Settings Folder


    # tmp = (os.path.join((dir.format(__file__)),'/savedGITAlternative'))
    
    # this was getting tripped up by the \t = a tab space!
    # tmp = dir
    # if(tmp.find('\\t')!=-1):
    #     dir = tmp.replace('\t', '/t')

    # # tmp = dir
    # tmp3 = dir
    # dir = tmp3.replace('\\', '/')

    dir = removeLiterals(dir)
    
    # folderToMake = os.sep.join([tmp, 'savedGITAlternative'])

    # if(folderToMake.find('\\t')!=-1):
    #     tmp = folderToMake
    #     folderToMake = tmp.replace('\\','/')

    # import pdb; pdb.set_trace()   #debugger

    if(os.path.exists(dir)):
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
    
    
# Block of code -> saving SRC path
def saveSourceURL(urlMeToSourceCode):   #push savedPathToGITAlternative (global variable)
    # urlMeToSourceCode = 'the Path'!

    # if(os.path.exists(os.getcwd()+'/savedGITAlternative/savedURL.txt')==False):
    # file_name = os.path.join(os.getcwd(), 'savedGITAlternative/savedURL.txt')

    # replacing literal char(s)
    # tmp2 = os.getcwd()

    paramNoTab = ""

    # urlMeToSourceCode = paramNoTab


    # paramNoTab = urlMeToSourceCode

    # if(paramNoTab.find('\\t')!=-1):
    #     urlMeToSourceCode = paramNoTab.replace('\\t', '/t')

    urlMeToSourceCode = removeLiterals(urlMeToSourceCode)
    
    # tmp2 is NOT the data BUT the PATH to be written

    # import sys,os
    # tmp2 = sys.path.append(os.path.realpath('..'))
    # tmp2 =          #Path URL
    # tmp = tmp2
    # if(tmp.find('\\t')!=-1):
    #     tmp2 = tmp.replace('\\t', '/t')


    file_name_source = os.sep.join([urlMeToSourceCode, 'savedURL.txt'])


    # tmp = file_name_source
    # file_name_source = tmp.replace('\\', '/')

    file_name_source = removeLiterals(file_name_source)



    with open(file_name_source, 'w') as sourceFile:
        sourceFile.write(paramNoTab)
        print "Data written to ", sourceFile
        sourceFile.close()

    # import pdb; pdb.set_trace()   #debugger
# global sourcePathMe



# ==========================

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

def saveDestURL(strSavedToDestURL):
    # saves a path to where you want the commits to save to, a path string
    # strSavedToDestURL - is the data to be added
    # file_name is made for the standard savedGITAlternative


    

    paramNoTab = ""
    paramNoTab = strSavedToDestURL
    if(strSavedToDestURL.find('\\t')!=-1):
        strSavedToDestURL = paramNoTab.replace('\\t', '/t')

    # tmp2 = os.getcwd()
    # tmp = tmp2
    # tmp2 = tmp.replace('\\t', '/t')

    strSavedToDestURL = strSavedToDestURL.replace('\\', '/')


    file_name = os.sep.join([strSavedToDestURL, 'savedGITAlternative/savedDestURL.txt'])


    # paramNoTab = strSavedToDestURL
    
    tmp3 = file_name
    file_name = tmp3.replace('\\', '/') 

    # import pdb; pdb.set_trace()   #debugger
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

# =============================

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

        import pdb; pdb.set_trace()   #debugger     

        # making source File Paths! working!
        for f in f_names:
            tmp1 = os.sep.join([pullSourceURL(), f])

            tmp2 = tmp1
            tmp1 = tmp2.replace('\\', '/')
            fname.append(tmp1)



        # making New Directory Path(s) from old Paths 
        for i in range(0, len(d_names)):
            dir_name.append(os.path.join(pullDestURL()+'/'+name, d_names[i]))




        # for item in dir_name:
        #     # logic for making Saved_folder tree structure
        #     savedItemURL = item.replace(pullSourceURL(), pullDestURL())
        #     print savedItemURL

        for item in dir_name:
            tmp1 = item
            item = tmp1.replace('\\', '/')
            # import pdb; pdb.set_trace()   #debugger
            os.makedirs(item)


            print item
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
            # import pdb; pdb.set_trace()   #debugger
            with open(sourced, 'r') as sourceFile:
                print 'sourceFile', sourceFile
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
# ====================================================
print sys.argv

# os.getcwd()

for i, argMe in enumerate(sys.argv):
        if(sys.argv[0] == ""): 
            print "\n\n==============\nYou may be new here!\n\nTo get things going, add a source PATH Location!\n\nUse the <-changeSource> command after the String of Python Path!"

        # making CLI stuff
        # =============================

        if(argMe == "-quickinit"):
        
            tmp1 = raw_input('InitDir - (Please end with "savedGITAlternative")\n')
            tmp2 = raw_input('SourceDir - (Please end with "code")\n')
            tmp3 = raw_input('SaveDir - (Please end with "save")\n')
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
        
