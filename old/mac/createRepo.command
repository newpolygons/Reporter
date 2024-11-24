cd "$(dirname "$0")"
python3 createRepo.py
cd repo
chmod +x Release
chmod +x scan-packages.sh
chmod +x updateRepo.command
tput setaf 3; echo "Files setup"
tput setaf 3; echo "Please check readme for more instructions."
./scan-packages.sh
tput setaf 3; echo "Scanning..."
tput setaf 2; echo "Complete"
github .