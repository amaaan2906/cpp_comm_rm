import sys
import argparse


def main(args: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="balance.py",
        description="Computes the minimum number of edit operations to balance a string",
    )
    parser.add_argument(
        "in_string",
        nargs="?",
        metavar="input string",
        type=str,
        help="String of parentheses' to check for balancing",
    )
    p_args = parser.parse_args(args)

    # Check if string is balanced
    # if isBalanced(p_args.in_string):
    #     print("-" * 11 + "Balanced" + "-" * 11)
    #     print(f"d=0, balanced string: {p_args.in_string}")
    # else:
    #     min_edits, balanced_string = myBalance(p_args.in_string)
    #     print("-" * 10 + "Unbalanced" + "-" * 10)
    #     print(f"d={min_edits}, balanced string: {balanced_string}")
    min_edits, balanced_string = myBalance(p_args.in_string)
    print(
        f"d={min_edits}, balanced string: {balanced_string if len(balanced_string) < 100 else balanced_string[:100] + '...'}"
    )
    return 0


def myBalance(string: str):
    """
    1. if open & close > 0 (i.e there are unmatched opens and closes)
      - pop each stack equal time and flip that location
      - if there are extra in any stack, delete them
    2. if only close has values (even)
      - pop first half
      - pop and flip second half
    2. if only open has values (even)
      - pop and flip first half
      - pop second half
    3. if only one stack has odd values
      - pop and delete
      - follow step for even
    """
    open_stack: list[int] = []  # unmatched open (
    close_stack: list[int] = []  # unmatched close )
    s_len = len(string)
    # build unmatched open close stacks
    # O(n) time complexity
    for i in range(s_len):
        if string[i] == "(":
            # append unmatched opens
            open_stack.append(i)
        elif string[i] == ")" and len(open_stack) > 0:
            # remove matching opens
            open_stack.pop()
        else:
            # append unmatched close
            close_stack.append(i)

    open_len: int = len(open_stack)
    close_len: int = len(close_stack)
    edit_moves: int = 0
    final_string: str = f"{string}"
    if open_len == 0 and close_len == 0:
        # balanced string
        return 0, string

    elif open_len > 0 and close_len > 0:
        """
        1. if open & close > 0 (i.e there are unmatched opens and closes)
          - pop each stack equal time and flip that location
          - if there are extra in any stack, delete them
        """
        edit_moves += 2 * (min(open_len, close_len))
        # flip brackets
        for _ in range(int(edit_moves / 2)):
            open: int = open_stack.pop()
            final_string = final_string[:open] + ")" + final_string[open + 1 :]
            close: int = close_stack.pop()
            final_string = final_string[:close] + "(" + final_string[close + 1 :]
        # delete extras
        while len(open_stack) > 0:
            edit_moves += 1
            open: int = open_stack.pop()
            final_string = final_string[:open] + final_string[open + 1 :]
        while len(close_stack) > 0:
            edit_moves += 1
            close: int = close_stack.pop()
            final_string = final_string[:close] + final_string[close + 1 :]

    elif open_len > 0:
        """
        2. if only open has values (even)
          - pop and flip first half
          - pop second half
        3. if only one stack has odd values
          - pop and delete
          - follow step for even
        """
        if open_len % 2 != 0:
            edit_moves += 1
            open: int = open_stack.pop()
            final_string = final_string[:open] + final_string[open + 1 :]
        new_open_len = len(open_stack)
        for _ in range(int(new_open_len / 2)):
            # flip first half
            edit_moves += 1
            open: int = open_stack.pop()
            final_string = final_string[:open] + ")" + final_string[open + 1 :]
        for _ in range(int(new_open_len / 2)):
            # pop second half
            # edit_moves += 1
            open: int = open_stack.pop()
            # final_string = final_string[:open] + final_string[open + 1 :]

    elif close_len > 0:
        """
        2. if only close has values (even)
          - pop first half
          - pop and flip second half
        3. if only one stack has odd values
          - pop and delete
          - follow step for even
        """
        if close_len % 2 != 0:
            edit_moves += 1
            close: int = close_stack.pop()
            final_string = final_string[:close] + final_string[close + 1 :]
        new_close_len = len(close_stack)
        for _ in range(int(new_close_len / 2)):
            # pop fist half
            # edit_moves += 1
            close: int = close_stack.pop()
            # final_string = final_string[:close] + final_string[close + 1 :]
        for _ in range(int(new_close_len / 2)):
            # flip second half
            edit_moves += 1
            close: int = close_stack.pop()
            final_string = final_string[:close] + "(" + final_string[close + 1 :]

    return edit_moves, final_string


def isBalanced(string: str) -> bool:
    s_len = len(string)
    bracket_stack = []
    for i in range(s_len):
        if string[i] == "(":
            bracket_stack.append(1)
        elif string[i] == ")" and len(bracket_stack) > 0:
            bracket_stack.pop()
        else:
            return False

    if len(bracket_stack) > 0:
        return False
    return True


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
