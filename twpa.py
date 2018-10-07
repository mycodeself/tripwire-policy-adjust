#!/usr/bin/python

import sys
import re

LINE = '### No such file or directory\n' 
PATTERN = '### Filename: '

def create_new_policy(twpol_file, paths):
    output_file = open(twpol_file+'.adjusted', 'w') 
    with open(twpol_file) as lines:
        for line in lines:
            splitted_line = line.strip().split()
            if len(splitted_line) > 0 and splitted_line[0] in paths:
                continue
            else:
                output_file.write(line) 
    output_file.close();

def read_error_lines(errors_file):
    file_path = []
    with open(errors_file) as lines:
        previous = ''
        for line in lines:
            if line == LINE:
                file_path.append(extract_file_path(previous))
            previous = line;
        return file_path;

def extract_file_path(line):
    pattern = PATTERN + '(.+?)\n';
    matches = re.search(pattern, line)
    if matches:
        return matches.group(1)
    else:
        print('No matches found in line: '+ line)
        return null;

def parse_args():
    args = sys.argv
    length = len(args)
    if length < 3:
        print("Expected two params")
        sys.exit()
    if length > 3:
        print("only two params...")
        sys.exit()
    return args

if __name__ == '__main__':
    args = parse_args()
    errors_file = args[1]
    twpol_file = args[2]
    paths = read_error_lines(errors_file)
    print(str(len(paths))+' nonexistent files found in '+twpol_file)
    print('Creating new policy file...')
    create_new_policy(twpol_file, paths)
    print('File '+twpol_file+'.adjusted was created successfully.')
