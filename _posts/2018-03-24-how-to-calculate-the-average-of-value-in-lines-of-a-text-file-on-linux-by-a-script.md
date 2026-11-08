---
title: "Calculate Average Values from Text Files Using awk, sed, and Python"
date: 2018-03-24 11:41:06 +0000
layout: post
canonical: https://www.systutorials.com/how-to-calculate-the-average-of-value-in-lines-of-a-text-file-on-linux-by-a-script/
---

`awk` is the most efficient approach for this task. It processes the file in a single pass and doesn’t load data into memory:

``` bash
awk '{ total += $5; count++ } END { print total/count }' file.txt
```

This assumes your numeric value is the 5th whitespace-delimited field. For a file like:

    Run 0: Time used: 22.235331711 seconds.
    Run 1: Time used: 20.784491219 seconds.
    Run 2: Time used: 21.851638876 seconds.

The output would be `21.6237547`.

Format output to specific decimal places:

``` bash
awk '{ total += $5; count++ } END { printf "%.2f\n", total/count }' file.txt
```

If the numeric field is in a different position, adjust the field number (`$5` becomes `$6`, `$7`, etc.).

Add descriptive labels to output:

``` bash
awk '{ total += $5; count++ } END { printf "Average time: %.3f seconds\n", total/count }' file.txt
```

## Extract values with regex pattern matching

When values aren’t at a fixed field position, use regex extraction. This is more robust for inconsistent formatting:

``` bash
awk '/Time used:/ { 
    match($0, /Time used: ([0-9.]+)/, arr)
    total += arr[1]
    count++
} END { 
    if (count > 0) print total/count 
}' file.txt
```

## Using grep and awk

Extract numeric values and pipe to awk:

``` bash
grep -oP 'Time used: \K[\d.]+' file.txt | awk '{sum+=$1} END {print sum/NR}'
```

The `-oP` flags enable Perl regex and print only the matched portion.

## Using sed and awk

Extract with sed’s substitution, then average:

``` bash
sed -n 's/.*Time used: \([0-9.]*\).*/\1/p' file.txt | awk '{sum+=$1} END {print sum/NR}'
```

## Using Python

For more complex processing, Python’s flexibility is valuable:

``` python
import re

total = 0
count = 0

with open('file.txt', 'r') as f:
    for line in f:
        match = re.search(r'Time used: ([\d.]+)', line)
        if match:
            total += float(match.group(1))
            count += 1

if count > 0:
    print(f"Average time: {total/count:.3f} seconds")
```

This approach handles edge cases cleanly and scales well for more complex statistics.

## Handling edge cases

**Empty files or no matches:**

``` bash
awk '{ total += $5; count++ } END { 
    if (count > 0) 
        printf "Average: %.3f\n", total/count 
    else 
        print "No data found" 
}' file.txt
```

**Skipping header lines:**

``` bash
awk 'NR > 1 { total += $5; count++ } END { print total/count }' file.txt
```

This skips the first line (`NR > 1` means “line number greater than 1”).

**Calculate average, minimum, and maximum simultaneously:**

``` bash
awk '{ 
    total += $5; 
    count++
    if ($5 < min || NR == 1) min = $5
    if ($5 > max) max = $5
} END { 
    printf "Average: %.3f, Min: %.3f, Max: %.3f\n", total/count, min, max 
}' file.txt
```

Initialize `min` on the first record to avoid comparison errors with undefined variables.

## Performance notes

For files with millions of lines, `awk` remains the fastest option because it processes in a single pass and uses constant memory. Avoid piping through multiple tools when a single awk command will do.

Python is slower than awk but more readable for complex logic. Use it when calculation rules are intricate or when you need the data structure flexibility.

For very large files where you need to compute multiple statistics, the combined awk approach above is more efficient than running multiple separate commands.
