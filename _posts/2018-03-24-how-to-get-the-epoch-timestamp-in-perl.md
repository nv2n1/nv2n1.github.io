---
title: "Getting Epoch Timestamps in Perl"
date: 2018-03-24 11:52:16 +0000
author: "Q A"
layout: post
categories: [programming-languages]
canonical: /how-to-get-the-epoch-timestamp-in-perl/
---

The Unix epoch (seconds since January 1, 1970 UTC) is the standard for representing time across systems. Perl gives you straightforward access to this value.

## Basic epoch timestamp

The simplest way to get the current epoch time:

``` perl
my $epoch = time();
print $epoch;  # prints something like 1735689600
```

The `time()` function returns an integer representing seconds since the Unix epoch. This is fast, lightweight, and works everywhere.

## Working with epoch timestamps

Convert an epoch timestamp to a readable format:

``` perl
my $epoch = time();
my $formatted = localtime($epoch);
print $formatted;  # prints something like: Thu Dec 31 14:00:00 2026
```

For GMT/UTC instead of local time:

``` perl
my $epoch = time();
my $formatted = gmtime($epoch);
print $formatted;  # prints something like: Thu Dec 31 19:00:00 2026
```

## Object-oriented approach with Time::Piece

For more complex time operations, use `Time::Piece`, which is part of Perl core since 5.9.5. It provides cleaner, more flexible time handling:

``` perl
use Time::Piece;

my $now = localtime();
print $now->epoch;           # get epoch seconds
print $now->strftime("%Y-%m-%d %H:%M:%S");  # custom formatting
```

Convert an epoch value to a Time::Piece object:

``` perl
use Time::Piece;

my $epoch = 1735689600;
my $time = Time::Piece->new($epoch);
print $time->strftime("%Y-%m-%d");  # 2026-12-31
```

## Microsecond precision

For higher precision, use `Time::HiRes`:

``` perl
use Time::HiRes qw(time);

my $precise_epoch = time();
print $precise_epoch;  # prints something like 1735689600.123456
```

This is useful for benchmarking and measuring small intervals.

## Comparing timestamps

Time::Piece makes date arithmetic straightforward:

``` perl
use Time::Piece;
use Time::Seconds;

my $now = localtime();
my $tomorrow = $now + ONE_DAY;
my $diff_seconds = $tomorrow->epoch - $now->epoch;

print $diff_seconds;  # 86400
```

Available constants include `ONE_SECOND`, `ONE_MINUTE`, `ONE_HOUR`, `ONE_DAY`, `ONE_WEEK`, etc.

## Parsing epoch from strings

Convert a formatted date string to epoch:

``` perl
use Time::Piece;

my $time = Time::Piece->strptime("2026-12-31 14:30:00", "%Y-%m-%d %H:%M:%S");
print $time->epoch;  # prints the epoch value
```

## Best practices

- Use `time()` when you just need the current epoch as an integer
- Use `Time::Piece` for any complex time operations, calculations, or formatting
- Remember that `localtime()` and `gmtime()` return a formatted string by default, not an object (unless used with `Time::Piece`)
- Be aware that epoch times are always in UTC; timezone conversion happens at the display/parsing stage
- For long-running scripts that need precise timing, `Time::HiRes` is more reliable than repeated `time()` calls

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
