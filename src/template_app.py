import sys
import os
import json
import subprocess


def your_python_code(arg, input_path, output_path):
    """
    Paste there your code you want to execute in iExec worker
    """
    # Open input file

    # Run computation

    project_URL = "https://universeathome.pl/universe/"
    account_key = "e8157b446331fd944c93e648dc99e5a9"
    out_file = "/log_file"
    boincCommand = "/usr/bin/boinc --exit_when_idle --fetch_minimal_work --attach_project " + \
        project_URL + " " + account_key + " >> "+output_path+out_file+" 2>&1"
    subprocess.run(boincCommand,
                   shell=True, check=True,
                   executable='/bin/bash')

    # Return output path + filename
    return output_path + out_file

# ============================================


def read_input_parameter(n):
    """
    This function reads and returns input parameters from input string. Script
    arguments (if provided) are accessible via "sys.argv" array. 
    If the input parameters don't exists function returns empty string "".
    n is the number of input parameter starting at 0. 
    To read first input parameter use: `read_input_parameter(1)`
    """
    return sys.argv[n] if len(sys.argv) > 1 else ""


def handle_input_files():
    """
    This function demonstrates how to use input files in an iExec application.
    The following environment variables are used:
        - IEXEC_IN: the path to the folder where input files are located.
        - IEXEC_INPUT_FILES_NUMBER: number of available input files.
        - IEXEC_INPUT_FILE_NAME_N: the name of the Nth input file. N is between
          1 and IEXEC_INPUT_FILES_NUMBER.
    If IEXEC_INPUT_FILES_NUMBER is 0 then no input file is available.
    To access files use file_list[n].read() where n is number of the file
    you want to access starting at 0
    """
    iexec_in = os.environ['IEXEC_IN']
    iexec_input_files_number = int(os.environ['IEXEC_INPUT_FILES_NUMBER'])
    file_list = []
    for i in range(1, iexec_input_files_number + 1):
        file_path = iexec_in + "/" \
            + os.environ['IEXEC_INPUT_FILE_NAME_' + str(i)]
        if os.path.isfile(file_path):
            with open(file_path) as f:
                file_list.append(f)
    return file_list


def save_result(result_filepath):
    """
    This function shows how to save a result in an iExec application. The result
    file(s) should be written in the folder indicated by the environment
    variable IEXEC_OUT. After saving the result, the file "computed.json" must
    be created in the same folder. It must contain, at least, the path to the
    determinism file (deterministic-output-path).
    """
    iexec_out = os.environ['IEXEC_OUT']
    # result_filepath = iexec_out + '/result.txt'
    # with open(result_filepath, 'w+') as f:
    #     f.write(text)
    computed_file_content = {"deterministic-output-path": result_filepath}
    print(computed_file_content)
    with open(iexec_out + '/computed.json', 'w+') as f:
        json.dump(computed_file_content, f)


if __name__ == '__main__':
    # Print environment variables for this computation
    iexec_in = os.environ['IEXEC_IN']
    print('IEXEC_IN: ' + iexec_in)
    iexec_out = os.environ['IEXEC_OUT']
    print('IEXEC_OUT: ' + iexec_out)
    iexec_input_files_number = int(os.environ['IEXEC_INPUT_FILES_NUMBER'])
    print('IEXEC_INPUT_FILES_NUMBER: ' + str(iexec_input_files_number))

    # Read args
    args = read_input_parameter(1)
    print('args: ' + args)

    # Trigger computation
    result_path = your_python_code(args, "", iexec_out)
    save_result(result_path)
