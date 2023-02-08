import sys
import argparse
from pathlib import Path


def main(args: list[str]) -> int:
    # Setup CLI argument parser
    parser = argparse.ArgumentParser(
        prog="comm_rm.py", description="Remove comments from C++ code"
    )
    parser.add_argument(
        "in_file",
        nargs="?",
        metavar="input file",
        type=str,
        help="Remove C++ comments from this file",
    )
    parser.add_argument(
        "out_file",
        nargs="?",
        metavar="output file",
        type=str,
        help="Output file name for C++ code without comments",
    )
    p_args = parser.parse_args(args)

    # check if ends in cpp
    try:
        p_args.in_file.index(".cpp")
        p_args.out_file.index(".cpp")
    except ValueError:
        print("Not a C++ file")
        return -1

    in_file = Path(p_args.in_file).resolve()

    out_string: str = remove_comments(in_file.read_text().strip())
    # print(in_file.read_text().index('"'))

    with open(Path(p_args.out_file).resolve(), "w") as f:
        f.writelines(out_string)

    return 0


def remove_comments(code):
    # if in a long comment block
    long_comment_flag = False
    # if within a string variable
    string_comment_flag = False
    result = []
    i = 0
    while i < len(code):
        if not string_comment_flag:
            if code[i : i + 1] == '"':
                string_comment_flag = True
                result.append(code[i])
            # comment remove code
            elif not long_comment_flag:
                if code[i : i + 2] == "/*":
                    long_comment_flag = True
                    i += 1
                elif code[i : i + 2] == "//":
                    i = code.find("\n", i)
                else:
                    result.append(code[i])
            elif long_comment_flag:
                if code[i : i + 2] == "*/":
                    long_comment_flag = False
                    i += 1
        elif string_comment_flag:
            if code[i : i + 1] == '"':
                string_comment_flag = False
            result.append(code[i])
        i += 1

    return "".join(result)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
