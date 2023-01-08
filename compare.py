from functions import lev_dist, normalization
import argparse
import os


def parsing():
    parser = argparse.ArgumentParser(prog='Anti-plagiarism', description='Similarity of two files')
    parser.add_argument("input_path", type=str, help='Input direction')
    parser.add_argument("output_path", type=str, help='Output direction')
    arguments = parser.parse_args()

    return arguments


if __name__ == '__main__':
    args = parsing()

    try:
        input = open(f'{args.input_path}', 'r')
        output = open(f'{args.output_path}', 'w')
    except FileNotFoundError:
        print("One of the files is missing")

    for line in input.readlines():
        if '\n' in line:
            str1, str2 = line[:-1].split()
        else:
            str1, str2 = line.split()

        if '.py' in str1 and '.py' in str2:
            str1 = open(str1, encoding='UTF-8').read()
            str2 = open(str2, encoding='UTF-8').read()

            str1 = normalization(str1)
            str2 = normalization(str2)

            output.write(str(lev_dist(str1, str2)) + '\n')

    input.close()
    output.close()

    os.startfile("scores.txt")
