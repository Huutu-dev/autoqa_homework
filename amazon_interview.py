from collections import defaultdict


def first_unique_letter(s):
    dd = defaultdict(int)
    for c in s:
        dd[c.lower()] += 1
    return next((k for k, v in dd.items() if v == 1), "")


assert first_unique_letter("Google") == 'l'
assert first_unique_letter("Amazon") == 'm'