import argparse
import os



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--create', type=bool, default=False, 
                        help="Create a new repository.")
    parser.add_argument('--update', type=bool, defulat=False, 
                        help="Update your existing repository.")
    args = parser.parse_args()

    if args.create:
        from src import createFunctions
        repoName = createFunctions.main()
        print(f"Created {repoName} in repo/")
    elif args.update:
        from src import updateFunctions
        repoName = updateFunctions.main()
        print(f"Updated {repoName} in repo/")
    else:
        print("Please either add --create or --update after main.py.")



        
if __name__ == '__main__':
    main()