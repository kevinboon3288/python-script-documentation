import os
import shutil
import argparse

def copy(sourcePath, destinationPath):
    if not os.path.exists(sourcePath):
        print(f"[Not Exist] filename is {sourcePath}")
    else:
        createDirectory(destinationPath)
        shutil.copy(sourcePath, destinationPath)

def createDirectory(targetPath):
    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    else:
        print(f"Directory path already exist : {targetPath}")

def arg_Parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--function', help="use --function | Functions in File Handling Feature (eg. copy)")
    parser.add_argument('--source', help="use --sourcePath | Set the source path if any")
    parser.add_argument('--dest', help="use --destPath | Set the destination path if any")

    return parser.parse_args()

def main():
    args = arg_Parse()

    if args.function == "create":
        createDirectory(args.source)
    elif args.function == "copy":
        copy(args.source, args.dest)

if __name__ == "__main__":
    main()