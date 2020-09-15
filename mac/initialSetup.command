tput setaf 2; echo "Setting Up Reporter"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew cask install github
brew cask install the-unarchiver
brew install dpkg
pip3 install pyfiglet
github .
tput setaf 3; echo "Please login to Github Desktop then close Github Desktop"
tput setaf 3; echo "If you already had github desktop installed, just close Github Deskop now."
tput setaf 2; echo "Finished Setting Up :)"
