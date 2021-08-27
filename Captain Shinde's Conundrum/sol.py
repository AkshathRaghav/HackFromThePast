#!/bin/env python


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        num_colors = int(input())
        colors_sequence = [int(x) for x in input().split()]

        print(process_test(colors_sequence))


def process_test(colors_sequence):
    left = 0
    right = 0

    num_switches = 0

    for i in range(len(colors_sequence)):
        if colors_sequence[i] == left or colors_sequence[i] == right:
            continue
        else:
            picked = False
            for j in colors_sequence[i+1:]:
                if j == left:
                    # pick right
                    num_switches += 1
                    right = colors_sequence[i]
                    picked = True
                    break
                elif j == right:
                    # pick left
                    num_switches += 1
                    left = colors_sequence[i]
                    picked = True
                    break
                else:
                    continue

            if not picked:
                # default left
                num_switches += 1
                left = colors_sequence[i]

    return num_switches


main()
