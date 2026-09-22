"""HW2P4 — Tuple unpacking and dictionary methods.

DSE I1020, Fall 2026. Fill in every section marked TODO.
Running `python hw2p4.py` must print output for all five tasks without error.
"""

import time

# Shared data for Tasks 1, 2, and 5. Do not change these values.
PAIRS = [
    ("Ada", 91),
    ("Grace", 97),
    ("Katherine", 95),
    ("Dorothy", 88),
    ("Mary", 97),
]


def task1_top_scorer(pairs):
    """Return the (name, score) tuple with the highest score.

    Use tuple unpacking in a for loop. Do NOT call max().
    If two people tie for the highest score, return the one that appears first.
    """
    # TODO: unpack each tuple as `for name, score in pairs:` and track the best so far.
    raise NotImplementedError


def task2_safe_lookup(pairs, missing_key):
    """Build a dict from `pairs` and return `.get(missing_key, <default>)`.

    Pick a sensible default and say in a comment why you chose it.
    """
    # TODO: build the dict, then use .get() with a default.
    raise NotImplementedError


def task3_merge(a, b):
    """Merge dicts `a` and `b` and return the result.

    Use dict unpacking ({**a, **b}) or .update().
    """
    # TODO: merge the two dicts.
    # TODO (comment): on a key present in BOTH dicts, whose value survives, and why?
    raise NotImplementedError


def task4_unhashable_key():
    """Demonstrate that a list cannot be used as a dict key.

    Trigger the error inside a try/except, and return the exception message as a string.
    """
    # TODO: try `{[1, 2]: "value"}` (or d[[1, 2]] = "value") inside try/except TypeError.
    # TODO (comment): what does "hashable" mean, and why is `list` not hashable?
    raise NotImplementedError


def task5_timing(pairs, repeats=100000):
    """Time the Task 1 unpacking loop against a manual index-based loop.

    Return (unpacking_seconds, index_seconds, ratio) where
    ratio = index_seconds / unpacking_seconds.
    """
    # TODO: time `for name, score in pairs:` over `repeats` iterations with time.time().
    # TODO: time `for i in range(len(pairs)):` with pairs[i][0], pairs[i][1] over `repeats`.
    # TODO: compute and return the ratio.
    raise NotImplementedError


def main():
    print("Task 1 — top scorer:", task1_top_scorer(PAIRS))

    print("Task 2 — safe lookup:", task2_safe_lookup(PAIRS, "Alan"))

    scores_a = {"Ada": 91, "Grace": 97}
    scores_b = {"Grace": 99, "Katherine": 95}
    print("Task 3 — merged:", task3_merge(scores_a, scores_b))

    print("Task 4 — unhashable key error:", task4_unhashable_key())

    unpacking_s, index_s, ratio = task5_timing(PAIRS)
    print(f"Task 5 — unpacking: {unpacking_s:.4f}s  index: {index_s:.4f}s  ratio: {ratio:.2f}")


if __name__ == "__main__":
    main()
