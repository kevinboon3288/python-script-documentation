import os
import argparse

def convert_accessModifier(line):
    if "public" in line:
        return "+"
    elif "private" in line or "internal" in line:
        return "-"
    elif "protected" in line:
        return "#"       

def convert_objectType(line):
    return line.split(' ')[1]

def convert_objectName(line):
    name = line.replace(";", " ").split()
    if len(name) >= 3:
        result = ' '.join(name[2:])
        if "=" in result:
            result = result.split("=")[0].strip()        
        return result
    else:
        return name[2]

def converter(filename):
    with open(filename) as file:
        for line in file:
            access_modifier = convert_accessModifier(line)
            objectType = convert_objectType(line)
            objectName = convert_objectName(line)
            print(f"{access_modifier} {objectName}: {objectType}")

def main():
    converter("resources/variables.txt")
    return

if __name__ == "__main__":
    main()