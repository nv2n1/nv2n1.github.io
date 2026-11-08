---
title: "Getting Unix Timestamp in Go"
date: 2018-03-24 11:52:16 +0000
author: "Eric Ma"
layout: post
categories: [languages-frameworks]
canonical: /how-to-get-the-epoch-timestamp-in-go-lang/
---

Getting the current epoch timestamp is straightforward using the `time` package:

``` go
package main

import (
    "fmt"
    "time"
)

func main() {
    epoch := time.Now().Unix()
    fmt.Println(epoch)
}
```

The `time.Now().Unix()` call returns the number of seconds since January 1, 1970 UTC as an `int64`.

## Getting nanosecond precision

If you need higher resolution, use `UnixNano()` for nanoseconds since epoch:

``` go
package main

import (
    "fmt"
    "time"
)

func main() {
    nanoEpoch := time.Now().UnixNano()
    fmt.Println(nanoEpoch)
}
```

This is useful for benchmarking, precise timing, or distributed tracing where clock synchronization matters.

## Converting a time string to epoch

Parse a time string first, then call `Unix()`:

``` go
package main

import (
    "fmt"
    "time"
)

func main() {
    // Parse RFC3339 format
    t, err := time.Parse(time.RFC3339, "2012-11-01T22:08:41Z")
    if err != nil {
        panic(err)
    }

    epoch := t.Unix()
    fmt.Println(epoch)
}
```

## Parsing different time formats

Go’s `time.Parse()` requires an exact layout string. Use the reference time `Mon Jan 2 15:04:05 MST 2006` as the pattern — this specific date/time is how Go handles format specifications.

Common layouts:

``` go
// RFC3339 with timezone
time.Parse(time.RFC3339, "2012-11-01T22:08:41+00:00")

// RFC3339Nano includes nanoseconds
time.Parse(time.RFC3339Nano, "2012-11-01T22:08:41.123456789Z")

// Unix date format
time.Parse(time.UnixDate, "Thu Nov  1 22:08:41 UTC 2012")

// Custom format
time.Parse("2006-01-02 15:04:05", "2012-11-01 22:08:41")
```

## Converting epoch back to a readable time

Use `time.Unix()` to create a `time.Time` from an epoch value:

``` go
package main

import (
    "fmt"
    "time"
)

func main() {
    epoch := int64(1351800521)
    t := time.Unix(epoch, 0)
    fmt.Println(t)                    // 2012-11-01 22:08:41 +0000 UTC
    fmt.Println(t.Format(time.RFC3339)) // 2012-11-01T22:08:41Z
}
```

The second argument to `time.Unix()` specifies nanoseconds. Pass `0` for second-precision timestamps.

## Handling timezones

Always be explicit about timezones. The `Z` suffix in RFC3339 indicates UTC; without it, you’re treating the time as local:

``` go
// Both of these parse correctly but represent different times
utcTime, _ := time.Parse(time.RFC3339, "2012-11-01T22:08:41Z")
localTime, _ := time.Parse("2006-01-02T15:04:05", "2012-11-01T22:08:41")

fmt.Println(utcTime.Unix())   // Always the same
fmt.Println(localTime.Unix()) // Depends on system timezone
```

If you need to work with a specific timezone, use `time.LoadLocation()`:

``` go
loc, _ := time.LoadLocation("America/New_York")
t := time.Now().In(loc)
epoch := t.Unix() // Same epoch, different local time representation
```

## Performance considerations

Calling `time.Now()` is relatively cheap, but in tight loops or high-frequency operations, cache the value if you don’t need sub-second granularity. The `Unix()` and `UnixNano()` conversions are negligible compared to the `Now()` call itself.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
