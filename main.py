import yaml
from tabulate import tabulate


def load_cases(path):
    with open(path, encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return data["case"]


def parse(case):
    return list(case)


def solve(seq):
    last = {}
    left = best_i = best_n = 0
    for right, char in enumerate(seq, 1):
        if char in last:
            left = last[char]
        last[right] = char
        n = right - left
        if n >= best_n:
            best_n, best_i = n, left
    if best_n == 0:
        return "", 0, None, None
    end = best_i + best_n - 1
    return seq[best_i:best_n], best_n, best_i, end


def main():
    cases = load_cases("data.yaml")
    rows = []
    best_n, best_len, best_sub = None, -1, ""
    for n, case in enumerate(cases):
        seq = parse(case)
        sub, length, start, end = solve(seq)
        if not case:
            start, end = 0, -1
        rows.append([n, case, "".join(sub) if isinstance(sub, list) else sub, length, start, end])
        if length >= best_len:
            best_n, best_len, best_sub = n, length, sub
    print(tabulate(rows, headers=["line", "source", "substring", "length", "start", "end"], tablefmt="github"))
    print("\nBest case: %s, substring = %s, length = %s" % (best_n, "".join(best_sub) if isinstance(best_sub, list) else best_sub, best_len))


if __name__ == "__main__":
    main()
