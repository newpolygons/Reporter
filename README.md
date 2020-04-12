# Reporter
 A simple python script to get you up and running with a Cydia Repo

# Welcome to Reporter Version 1.0!
Please direct any bugs or feature requests to @NewPolygons on twitter!

!! Run initialSetup.command file !!
(Only do this step one time when first downloading Reporter.)

CREATING A NEW REPO 

Step 1: Create a github account and verify the email account linked to it. 

Step 2 : Run createRepo.command file
Please enter information (This info will appear on Cydia)
Copy custom photos or included photos to repo folder. (Press enter when finished)
Copy deb files to deb folder now if you have any. (Press enter when finished)

Step 3 : Github will now open, click (create a repository here instead in small blue text).
Name the repo 'repo' and add a description for the repo (this is what will appear on github.)
No other options need to be configured.
Click Create repository.
Make sure your new repo is selected in the top bar and click Publish Repository button.
You may have to change to name of the repo to 'repo' and set the description of the repo one more time.
#!(UNCHECK KEEP THIS CODE PRIVATE)#!
Now click publish repository.

Step 4 : Go to github.com in your browser of choice and navigate to your newly created repo.
Click settings at the top of the page.
Scroll down until you see github pages
Under sources click none and change it to master branch ( the page will refresh), scroll back down.
Under github pages you will now see the link to your repo, add this to cydia sources 
i.e (Your site is ready to be published at https://newpolygons.github.io/repo/ ) < it will look something like this.


# UPDATING PREVIEOUSLY CREATED REPO

You will notice a updateRepo.command file in your repo folder.
Add any new deb files you want to the debs folder.
New run updateRepo.command file. 
Github desktop will open, click commit to master button on the bottom left. 
Then click update repository button at the top.
Your repo will now have the new packages.