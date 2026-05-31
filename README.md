[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/cm6PS4yt)
# Week 1 Homework: Evidence Desk Patterns

## Student Name

Bobby Mil0

## Summary

This homework practices common data structure patterns with a detective case file theme. The tasks include frequency counting, duplicate detection, bracket validation with a stack, and alias lookup.

## How to Run Tests

From the repository root, run:

```bash
pytest -q
```

To run one test file:

```bash
pytest -q tests/test_challenges.py
```

## Required Problems

Complete these functions in `src/challenges.py`:

1. `count_evidence`
2. `first_repeated_id`
3. `valid_tags`
4. `lookup_alias`

## Optional Challenges

These are extra practice unless your instructor tells you otherwise:

1. `process_reports`
2. `largest_time_gap`

Optional tests are skipped by default. To run them, remove the `@pytest.mark.skip(...)` line above the optional test you want to check.

---

# Problem Notes

## 1. Evidence Counter

### Pattern

Frequency counting

### Data Structure

Dictionary

### Approach

- Create an empty dictionary for counts.
- Loop through each evidence label.
- Increment the count for each label.

### Complexity

- Time: `O(n)` where `n` is the number of evidence items.
- Space: `O(k)` where `k` is the number of unique labels.

This function scans the input once and stores the number of occurrences for each label.

### Edge Cases Checked

- [x] Empty list
- [x] One item
- [x] Repeated items
- [x] Different labels

---

## 2. Repeat Suspect ID

### Pattern

Seen before

### Data Structure

Set

### Approach

- Create an empty set for IDs that have already appeared.
- Loop through each suspect ID.
- Return the ID immediately when it appears a second time.

### Complexity

- Time: `O(n)` where `n` is the number of IDs.
- Space: `O(n)` in the worst case for the set of seen IDs.

The function stops early when a repeated ID is found, so it is efficient for long lists.

### Edge Cases Checked

- [x] Empty list
- [x] No repeated IDs
- [x] First two IDs match
- [x] Multiple repeated IDs

---

## 3. Evidence Tag Validator

### Pattern

Stack matching

### Data Structure

List used as a stack

### Approach

- Use a stack to track opening brackets.
- Push opening brackets onto the stack.
- For closing brackets, verify the stack top matches the corresponding opening bracket.
- Return True only when the stack is empty at the end.

### Complexity

- Time: `O(n)` where `n` is the number of characters in the string.
- Space: `O(n)` in the worst case for nested opening brackets.

This validates balanced bracket sequences while ignoring any non-bracket characters.

### Edge Cases Checked

- [x] Empty string
- [x] Correctly nested tags
- [x] Mismatched tags
- [x] Closing tag before opening tag
- [x] Unclosed opening tag
- [x] Non-bracket characters

---

## 4. Alias Directory

### Pattern

Lookup table

### Data Structure

Dictionary

### Approach

- Use the alias dictionary to retrieve the real name.
- Return `None` if the alias is not present.

### Complexity

- Time: `O(1)` average lookup.
- Space: `O(1)` additional memory.

This function uses dictionary lookup for fast alias resolution.

### Edge Cases Checked

- [x] Known alias
- [x] Unknown alias
- [x] Empty dictionary

---

# Assistance & Sources

## AI Used?

- [x] Yes
- [ ] No

## If yes, what did AI help with?

- Implementing the required functions.
- Updating test coverage and README details.

## Other Sources

None.
