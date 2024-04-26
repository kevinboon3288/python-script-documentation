import os
import shutil
import argparse

def create(targetPath):
    if not os.path.exists(targetPath):
        with open(targetPath, 'w') as file:
            file.write('')
        if os.path.exists(targetPath):
            print(f"{targetPath} created successfully")
        else:
            print(f"{targetPath} not created successfully")
        
def delete(targetPath):
    if os.path.exists(targetPath):
        os.remove(targetPath)
        if not os.path.exists(targetPath):
            print(f"{targetPath} deleted successfully")
        else:
            print(f"{targetPath} not deleted successfully")

def copy(sourcePath, destinationPath):
    if not os.path.exists(sourcePath):
        print(f"filename is {sourcePath}")
    else:
        makeDirectory(destinationPath)
        shutil.copy(sourcePath, destinationPath)

def makeDirectory(targetPath):
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)

def arg_Parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', help="use --f | Functions in File Handling Feature (eg. copy)")
    parser.add_argument('--s', help="use --s | Set the source path if any")
    parser.add_argument('--d', help="use --d | Set the destination path if any")

    return parser.parse_args()

def main():
    args = arg_Parse()

    if args.f == "directory":
        makeDirectory(args.s)
    elif args.f == "create":
        create(args.s)
    elif args.f == "delete":
        delete(args.s)
    elif args.f == "copy":
        copy(args.s, args.d)

if __name__ == "__main__":
    main()
