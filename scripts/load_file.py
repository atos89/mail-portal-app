import os
import glob
import json

def get_program_all():
    file_paths = glob.glob('./program-data/*.json')
    programs = []
    for file_path in file_paths:
        program = get_program(file_path)
        programs.append(program)

    return programs

def get_program(file_path):
    f = open(file_path, 'r')
    program = json.load(f)
    f.close()

    return program
