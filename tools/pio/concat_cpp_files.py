Import("env")
import os
import glob


def concat_cpp_files(path_to_concat):

    cpp_files = []

    cpp_path = path_to_concat

    cpp_path_out = '{}_tmp'.format(path_to_concat)

    if not os.path.exists(cpp_path_out):
        os.makedirs(cpp_path_out)

    tmp_cpp_file = os.path.join(cpp_path_out, '__tmpfile.cpp')

    if os.path.exists(tmp_cpp_file):
        os.remove(tmp_cpp_file)

    for root, dirs, files in os.walk(cpp_path):
        for file in files:
            if file.endswith('.cpp'):
                fullname = os.path.join(root, file)
                cpp_files.append(fullname)
                print("Add {}".format(fullname))


    with open(tmp_cpp_file,'wb') as newf:
        for filename in cpp_files:
            with open(filename,'rb') as hf:
                newf.write(hf.read())
                #newf.write('\n\n\n')


concat_cpp_files('./src/src/ControllerQueue')
concat_cpp_files('./src/src/PluginStructs')
