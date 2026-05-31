"""Week 1 Homework: Evidence Desk Patterns.

Complete each function using the data structure pattern named in the docstring.

Rules:
- Python 3.11+
- Standard library only
- Do not change function names or parameters
- Run tests with: pytest -q
"""

from collections import deque


# -----------------------------------------------------------------------------
# Required Problem 1
# -----------------------------------------------------------------------------

def count_evidence(evidence: list[str]) -> dict[str, int]:
    """Return a dictionary counting how many times each evidence label appears.

    Pattern: frequency counting
    Data structure: dictionary
    """
    counts: dict[str, int] = {}

    for item in evidence:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


# -----------------------------------------------------------------------------
# Required Problem 2
# -----------------------------------------------------------------------------

def first_repeated_id(ids: list[str]) -> str | None:
    """Return the first suspect ID that appears a second time.

    Pattern: seen before
    Data structure: set
    """
    seen: set[str] = set()

    for suspect_id in ids:
        if suspect_id in seen:
            return suspect_id
        seen.add(suspect_id)

    return None


# -----------------------------------------------------------------------------
# Required Problem 3
# -----------------------------------------------------------------------------

def valid_tags(tags: str) -> bool:
    """Return True if all bracket-style evidence tags are balanced.

    Pattern: stack matching
    Data structure: list used as a stack
    """
    bracket_pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack: list[str] = []

    for char in tags:
        if char in bracket_pairs.values():
            stack.append(char)
        elif char in bracket_pairs:
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0


# -----------------------------------------------------------------------------
# Required Problem 4
# -----------------------------------------------------------------------------

def lookup_alias(aliases: dict[str, str], alias: str) -> str | None:
    """Return the real name connected to an alias.

    Pattern: lookup table
    Data structure: dictionary
    """
    return aliases.get(alias)


# -----------------------------------------------------------------------------
# Optional Challenge 1
# -----------------------------------------------------------------------------

def process_reports(reports: list[str]) -> list[str]:
    """Return case reports in first-in, first-out processing order.

    Pattern: queue processing
    Data structure: collections.deque
    """
    queue = deque(reports)
    processed: list[str] = []

    while queue:
        processed.append(queue.popleft())

    return processed


# -----------------------------------------------------------------------------
# Optional Challenge 2
# -----------------------------------------------------------------------------

def largest_time_gap(times: list[int]) -> int:
    """Return the largest gap between neighboring event times after sorting.

    Pattern: sorting + scan
    Data structure: list
    """
    if len(times) < 2:
        return 0

    sorted_times = sorted(times)
    max_gap = 0

    for first, second in zip(sorted_times, sorted_times[1:]):
        gap = second - first
        if gap > max_gap:
            max_gap = gap

    return max_gap
