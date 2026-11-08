---
title: "Error Handling in Go: Converting Errors to Strings"
date: 2018-03-24 11:50:41 +0000
layout: post
canonical: https://www.systutorials.com/in-golang-how-to-convert-an-error-to-a-string/
---

Error handling is fundamental to Go development. Often you’ll need to convert an error to a string for logging, displaying to users, or including in API responses. Go provides several straightforward approaches.

### Using the Error() Method

Every error in Go implements the `error` interface, which has a single method: `Error() string`. The simplest conversion is calling this method directly:

``` go
package main

import (
    "fmt"
    "os"
)

func main() {
    file, err := os.Open("nonexistent.txt")
    if err != nil {
        errorString := err.Error()
        fmt.Println("Error:", errorString)
    }
}
```

This outputs: `Error: open nonexistent.txt: no such file or directory`

### Using fmt Package

The `fmt` package automatically calls `Error()` when you format an error with `%v`, `%s`, or `%q`:

``` go
fmt.Println(err)                    // Uses %v implicitly
fmt.Printf("Error: %v\n", err)      // Explicit %v
fmt.Printf("Error message: %s\n", err)  // Using %s
fmt.Printf("Quoted: %q\n", err)     // Quoted output
```

For debugging, `%#v` shows the underlying type:

``` go
fmt.Printf("Debug: %#v\n", err)
```

### Structured Logging with slog

Modern Go applications should use the standard `log/slog` package for structured logging, available since Go 1.21:

``` go
package main

import (
    "log/slog"
    "os"
)

func main() {
    logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))

    file, err := os.Open("missing.txt")
    if err != nil {
        logger.Error("Failed to open file", "error", err)
    }
}
```

This produces structured JSON output that’s easy to parse in log aggregation systems:

``` json
{"time":"2026-01-15T10:30:45.123Z","level":"ERROR","msg":"Failed to open file","error":"open missing.txt: no such file or directory"}
```

### Working with Error Wrapping

Go 1.13 introduced error wrapping with `%w`. When converting wrapped errors to strings, you get the full context:

``` go
package main

import (
    "errors"
    "fmt"
)

func process(filename string) error {
    file, err := os.Open(filename)
    if err != nil {
        return fmt.Errorf("process: failed to open %s: %w", filename, err)
    }
    defer file.Close()
    // ... processing logic
    return nil
}

func main() {
    err := process("data.txt")
    if err != nil {
        fmt.Println(err.Error())  // Full wrapped message
    }
}
```

Output: `process: failed to open data.txt: open data.txt: no such file or directory`

### Type Assertions for Detailed Information

When you need specific details from an error, use type assertions:

``` go
if pathErr, ok := err.(*os.PathError); ok {
    fmt.Printf("Op: %s, Path: %s, Err: %s\n", pathErr.Op, pathErr.Path, pathErr.Err)
}
```

For checking specific error types:

``` go
if errors.Is(err, os.ErrNotExist) {
    fmt.Println("File does not exist")
}
```

### Custom Error Types

Define custom errors as structs implementing the `error` interface:

``` go
type ValidationError struct {
    Field string
    Value interface{}
}

func (e ValidationError) Error() string {
    return fmt.Sprintf("validation failed: %s=%v", e.Field, e.Value)
}

func main() {
    err := ValidationError{"age", -5}
    fmt.Println(err.Error())  // validation failed: age=-5
}
```

### Handling Nil Errors

Always check if an error is nil before converting:

``` go
if err != nil {
    message := err.Error()
    // Process message
}
```

Calling `Error()` on a nil error will panic. If you need a safe default:

``` go
var message string
if err != nil {
    message = err.Error()
} else {
    message = "success"
}
```

### Performance Considerations

Converting errors to strings happens during logging or I/O operations, which are typically slow. The string conversion itself is negligible. However, avoid repeated conversions in tight loops:

``` go
// Good: convert once
errorMsg := err.Error()
for i := 0; i < 1000000; i++ {
    logger.Error(errorMsg)  // Reuse converted string
}

// Avoid: convert repeatedly
for i := 0; i < 1000000; i++ {
    logger.Error(err.Error())  // Converts on each iteration
}
```

For production services, use structured logging with `slog` and let the logging handler manage serialization efficiently.
