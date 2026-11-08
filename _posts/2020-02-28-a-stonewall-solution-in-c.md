---
title: "Stack-Based Algorithm for the Skyline Problem"
date: 2020-02-28 11:47:02 +0000
modified: 2026-04-11 17:11:49 +0000
author: "David Yang"
layout: post
categories: [languages-frameworks]
canonical: /a-stonewall-solution-in-c/
---

The StoneWall problem is a classic algorithmic challenge that tests your ability to recognize when a stack data structure enables a greedy O(N) solution.

## The Problem

Given an array of wall heights, determine the minimum number of distinct stone blocks needed to construct that height profile. Each stone block can be placed multiple times at different positions, but a block placed at position i cannot extend above the target height at that position.

For example, with heights `[8, 8, 5, 7, 9, 8, 7, 6, 5]`, you need to find the minimum count of reusable stones that can build this exact profile.

## Why This Matters

This isn’t just interview trivia—understanding the stack-based approach teaches you how to recognize LIFO patterns in real problems. Similar logic applies to problems like removing duplicate letters, simplifying paths, and validating parentheses.

## The Key Insight

As you move left to right through the heights, you only need to track which heights could potentially be reused later. When you encounter a height lower than your current maximum, all taller walls become blocked—they can’t extend further and will never be reused.

This LIFO (Last In, First Out) pattern is exactly what a stack solves.

## The Solution

``` cpp
#include <stack>
#include <vector>

int solution(std::vector<int>& H) {
    int stones = 0;
    std::stack<int> heights;

    for (int h : H) {
        // Remove all walls taller than current height
        while (!heights.empty() && h < heights.top()) {
            heights.pop();
        }

        // Add new stone if needed
        if (heights.empty() || h > heights.top()) {
            heights.push(h);
            ++stones;
        }
    }

    return stones;
}
```

## How It Works

For each wall height `h` in the input:

1.  **Pop taller heights**: Remove all heights from the stack that are taller than `h`. These represent blocked walls that can’t be reused.

2.  **Check what’s left on the stack**:
    - Stack is empty: This is a new height we haven’t seen before. Push it and increment the stone count.
    - `h` equals the top: This height already exists on the stack with a clear path to reuse it. Don’t push, don’t increment.
    - `h` is greater than the top: This is a new height above anything currently available. Push it and increment the stone count.

## Why It’s Optimal

The stack maintains a strict increasing order. This invariant ensures:

- We never count the same height twice (skip when `h == heights.top()`)
- We only keep heights that could appear again and require separate blocks
- Popping happens for valid reasons (a lower height blocks taller ones)
- Each height is pushed and popped exactly once, guaranteeing O(N) time

## Complexity Analysis

**Time: O(N)** — Each element is pushed exactly once and popped exactly once across all iterations. Despite the nested loop, the total work is linear.

**Space: O(N)** — Worst case when heights are strictly increasing, the stack holds all N elements. Typically much smaller.

## Worked Example

Input: `[8, 8, 5, 7, 9, 8, 7, 6, 5]`

| Height | Action                    | Stack       | Stones |
|--------|---------------------------|-------------|--------|
| 8      | Push (empty)              | \[8\]       | 1      |
| 8      | h equals top, skip        | \[8\]       | 1      |
| 5      | Pop 8, push 5             | \[5\]       | 2      |
| 7      | 7 \> 5, push              | \[5, 7\]    | 3      |
| 9      | 9 \> 7, push              | \[5, 7, 9\] | 4      |
| 8      | Pop 9, 8 \> 7, push       | \[5, 7, 8\] | 5      |
| 7      | Pop 8, h equals top, skip | \[5, 7\]    | 5      |
| 6      | Pop 7, push 6             | \[5, 6\]    | 6      |
| 5      | Pop 6, h equals top, skip | \[5\]       | 6      |

**Result: 6 stones**

## Edge Cases

**Empty input**: Returns 0.

**All same height**: Returns 1 (one stone covers the entire wall).

**Strictly increasing**: Returns N (each new height requires a distinct block).

**Strictly decreasing**: Returns N (each position needs its own stone as the stack empties).

**Repeated consecutive heights**: Handled efficiently—we skip the push when `h == heights.top()`, avoiding duplicate counting.

## Production Considerations

For real code, add:

- **Input validation**: Check for negative heights or values exceeding your integer type’s range.
- **Type safety**: Use `long long` if heights can exceed 2^31-1.
- **Empty vectors**: Explicitly handle before calling the function.
- **Comments**: The algorithm is elegant but non-obvious; document the stack invariant.

## Related Problems

Once you master this, you can apply the same stack-based greedy approach to:

- Removing duplicate letters
- Simplifying file paths
- Trapping rain water (variant with additional logic)
- Daily temperatures

The pattern: *use a stack when you need to undo recent decisions based on new information*.
