import subprocess
import bz2


def createFiles(origin, label, description):
    
    # Get Repo Info
    origin = input('Please enter a repo name: ')
    label = input('Please enter a repo label: ')
    disc = input('Please enter a repo disc: ')

    #Create Release File.
    try:
        release = open('repo/Release', 'w')
        release.write('Origin: ' + origin + "\n")
        release.write('Label: ' + label + "\n")
        release.write('Suite: stable' + "\n")
        release.write('Version: 1.0' + "\n")
        release.write('Codename: cydia-ios' + "\n")
        release.write('Architectures: iphoneos-arm' + "\n")
        release.write('Components: main' + "\n")
        release.write('Description: '+ disc)
        release.close
    except IOError:
        print('There was a critical error please restart the program. If this continues file an issue on github')
    
    return

def createRepo():
    '''
    
    create repo + enable github pages using only terminal?

    '''
    return

def updateRepo(filePaths):

    # implement copy of file uploads to repo folder
    subprocess.check_output(['rm', '-Rf', 'repo/Packages.bz2'])
    scanPackages()

    return 

def scanPackages():
    subprocess.check_output(['dpkg-scanpackages', '-m', 'repo/debs', '>', 'repo/debs/Packages'])
    
    '''
        Below untested actual implementation may be:

        with bz2.open("myfile.bz2", "wb") as f:
            unused = f.write(data)

        or something like that.

    '''
    
    bz2.compress('repo/debs/Packages')
    
    return