Instructions for Linux:
(Intended use with Ubuntu message me on twitter @NewPolygons if having issues with another build.)

Step 1: Using inital setup

- Right click the directory with inital setup file and select open in terminal.
- Enter "chmod +x initalSetup" without the quotes.
- Enter "./initalSetup" without the quotes.
- Enter the Sudo password for the computer.
- Leave terminal window open we will still be using it.

THIS STEP ONLY HAS TO BE DONE THE FIRST TIME USING REPORTER IT IS USED FOR INSTALLING Dependencys!
If you want to manually install dependencys open this file in a text editor and see what must be installed.


Step 2: Setup createRepo file

- Enter "chmod +x createRepo" without the quotes.
- Enter "./createRepo" without the quotes. This will begin the repo creation process.
- When prompted enter a name for your new repo.
- When prompted enter a label for your new repo.
- When prompted enter a disc for your new repo.
- Copy the images from the main directory to the newly created repo folder (or add your own photos im not your boss)
- Now click enter to get to the next prompt.
- Now add your deb files (tweaks) to the deb folder within the repo folder.
- Click enter again to finish the repo creation process.

(Note)
!In the terminal window you should see something along the lines of this if you added a deb to the deb folder!
(dpkg-scanpackages: info: Wrote 1 entries to output Packages file.)


Step 3: Getting the repo on Github for free hosting
- Create a new repo on Github.
- Give a name to the repo.
- Give it a description (optional).
- MAKE SURE THE REPO IS PUBLIC and not private!
- All settings under (Initialize this repository with:) are optional.
- Upload the contents of the repo folder we just created to the repo on Github.
- Then commit the changes.
- Go to the repo you created in Github.
- Select the settings tab at the top and scroll down until you see the pages tab.
- Select the main branch then /(root) and then click save.
- You should now see a link at the top of the pages section. Go to your favorite package manager on your device IE (Cydia).
- Now add the repository which is this link!
- Enjoy sharing your tweaks with your friends and the Jailbreak community!



(Additonal Notes)

If you have any issues or bugs to report please message me on twitter @NewPolygons


EXTRA STEP: Updating your repo when you create new tweaks

- Navigate to the repo folder on your system.
- Add any new deb files you would like to the debs folder now.
- Right click and select open in terminal.
- Enter "chmod +x updateRepo" without the quotes.
- Enter "./updateRepo" without the quotes.
- Push new changes to your repo on Github.
- Try out those fancy new tweaks!
