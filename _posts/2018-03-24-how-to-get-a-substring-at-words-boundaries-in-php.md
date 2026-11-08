---
title: "Extracting Substrings at Word Boundaries in PHP"
date: 2018-03-24 11:53:54 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-get-a-substring-at-words-boundaries-in-php/
---

When truncating strings, you often need to avoid cutting off in the middle of a word. The naive `substr()` approach will break words, so you need logic to backtrack to the previous word boundary.

## The problem

Given a string like `"ab cc dde ffg ff"`, if you want a substring of maximum 7 characters starting at position 0, a simple `substr($a, 0, 7)` produces `"ab cc d"` — cutting the word `dde` in half. You need to stop at the last complete word instead: `"ab cc"`.

## Solution

The approach is straightforward: extract up to your desired length, then backtrack character by character until you hit a word boundary (end of a word). A word boundary occurs when the current character is not a space AND either it’s the string’s last character OR the next character is a space.

``` php
function is_word_end($str, $pos) {
  $len = strlen($str);

  // Position beyond string or at a space
  if ($pos >= $len || $str[$pos] === ' ') {
    return false;
  }

  // Not at end of string AND next char isn't a space
  if ($pos + 1 < $len && $str[$pos + 1] !== ' ') {
    return false;
  }

  return true;
}

function word_substr($str, $max_len) {
  $len = $max_len;

  // Backtrack until we find a word boundary
  while ($len > 0 && !is_word_end($str, $len - 1)) {
    $len--;
  }

  return $len > 0 ? substr($str, 0, $len) : '';
}
```

The `is_word_end()` function checks if a character at position `$pos` is a valid word ending. The `word_substr()` function finds the longest substring up to `$max_len` that ends on a word boundary.

## Testing

``` php
$a = "ab cc dde ffg ff";

for ($len = 1; $len < 20; ++$len) {
  echo $len . ": " . word_substr($a, $len) . "\n";
}
```

Output:

    1: 
    2: ab
    3: ab
    4: ab
    5: ab cc
    6: ab cc
    7: ab cc
    8: ab cc
    9: ab cc dde
    10: ab cc dde
    11: ab cc dde
    12: ab cc dde
    13: ab cc dde ffg
    14: ab cc dde ffg
    15: ab cc dde ffg
    16: ab cc dde ffg ff
    17: ab cc dde ffg ff
    18: ab cc dde ffg ff
    19: ab cc dde ffg ff

Note that lengths 1-4 return empty strings since no complete word fits in that space.

## Real-world considerations

**Multiple spaces or punctuation:** The implementation above assumes single spaces as delimiters. For production code handling HTML or rich text, consider using `preg_split()` or `explode()` instead:

``` php
function word_substr_robust($str, $max_len) {
  // Split on whitespace, preserving word separators
  $words = preg_split('/(\s+)/', $str, -1, PREG_SPLIT_DELIM_CAPTURE);

  $result = '';
  foreach ($words as $chunk) {
    if (strlen($result) + strlen($chunk) <= $max_len) {
      $result .= $chunk;
    } else {
      break;
    }
  }

  // Trim trailing whitespace
  return rtrim($result);
}
```

This approach handles multiple consecutive spaces and works better with natural word splitting.

**Performance:** For very long strings, avoid character-by-character backtracking. Use `strrpos()` to find the last space within your boundary:

``` php
function word_substr_fast($str, $max_len) {
  if (strlen($str) <= $max_len) {
    return $str;
  }

  $substr = substr($str, 0, $max_len);
  $last_space = strrpos($substr, ' ');

  return $last_space !== false ? substr($str, 0, $last_space) : '';
}
```

This performs a single reverse search for the last space instead of looping through characters.

**Handling edge cases:** If the first word exceeds your limit, both implementations return an empty string. You may want to return the first word regardless:

``` php
function word_substr_allow_first($str, $max_len) {
  $result = word_substr($str, $max_len);

  if ($result === '') {
    $first_space = strpos($str, ' ');
    return $first_space !== false ? substr($str, 0, $first_space) : $str;
  }

  return $result;
}
```
