import pyfiglet, time, os

banner  = pyfiglet.figlet_format("Reporter")
print(banner)


path = os.path.dirname(os.path.realpath(__file__))
newpath = (str(path) + '/repo' )
if not os.path.exists(newpath):
    os.makedirs(newpath)
os.chdir(newpath)

# Get Repo Info
origin = input('Please enter a repo name: ')
label = input('Please enter a repo label: ')
disc = input('Please enter a repo disc: ')
    
#Create Release File.
try:
    release = open('Release', 'w')
except IOError:
    print('There was a critical error please restart the program and contact me on Twitter @newpolygons')
release.write('Origin: ' + origin + "\n")
release.write('Label: ' + label + "\n")
release.write('Suite: stable' + "\n")
release.write('Version: 1.0' + "\n")
release.write('Codename: cydia-ios' + "\n")
release.write('Architectures: iphoneos-arm' + "\n")
release.write('Components: main' + "\n")
release.write('Description: '+ disc)
release.close

#Create Deb Folder
currentDirectory = (os.getcwd() + "/debs")
if not os.path.exists(currentDirectory):
    os.makedirs(currentDirectory)
    
#Create packagescanner
try:
    scanner = open('scan-packages.sh', "w")
except IOError:
    print('There was a critical error please restart the program and contact me on Twitter @newpolygons')
scanner.write('dpkg-scanpackages -m ./debs > Packages' + '\n')
scanner.write('bzip2 Packages')
scanner.close

#Create Update file
try:
    updater = open('updateRepo.command', "w")
except IOError:
    print('There was a critical error please restart the program and contact me on Twitter @newpolygons')
updater.write('cd "$(dirname "$0")"\n')
updater.write('rm -Rf Packages.bz2\n')
updater.write('./scan-packages.sh' + '\n')
updater.write('github .')
#photos
print('Please copy photos from main folder to repo folder now')
print('...Or you can copy custom images to repo folder')
throwaway = input('just be sure to name the files like the files in main folder, press enter when done: ')
    
#allow chance to add debs
print('Please add your debs to the debs folder now. / If you dont have any yet just continue')
throwaway1 = input("Please press enter once you've added your debs: ")


creditBanner  = pyfiglet.figlet_format("Developed by: NewPolygons")
print(creditBanner)