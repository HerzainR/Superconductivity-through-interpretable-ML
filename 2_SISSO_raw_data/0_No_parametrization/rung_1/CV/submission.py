import os

def replace_line(file_path, line_number, new_content):
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines into memory

    if 0 <= line_number < len(lines):  # Ensure line number is valid
        lines[line_number] = new_content + '\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)  # Write modified lines back

def copy_files():
    data = 'cp ../data.csv .'
    json = 'cp ../sisso.json .'

    os.system(data)
    os.system(json)

def run_sisso():
    run  = 'mpirun -n 4 /Users/herzain/sissopp/build/bin/sisso++ sisso.json > out'
    os.system(run)

indices ={
 0: [17, 31, 20, 14, 40, 47],
 1: [24, 48, 9, 56, 13, 5],
 2: [11, 42, 33, 54, 52, 49],
 3: [34, 35, 19, 30, 32, 41],
 4: [46, 16, 45, 15, 1, 26],
 5: [3, 4, 2, 10, 12, 39],
 6: [53, 29, 0, 36, 28, 37],
 7: [8, 22, 7, 51, 55],
 8: [38, 21, 43, 23, 27],
 9: [18, 6, 25, 44, 50],
}

n_tests = []

for test in range(10):
    n_tests.append(test)


for i in n_tests:
    folder = 'run_' + str(i)

    os.makedirs(folder)
    os.chdir(folder)

    copy_files()
    replace_line("sisso.json", 14,'    "leave_out_inds": '+ str(indices[i]) + ', ')
    run_sisso()

    os.chdir('..')
    
