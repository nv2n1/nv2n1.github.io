---
title: "Checking if Files and Directories Exist in Go"
date: 2018-07-01 07:43:51 +0000
layout: post
canonical: https://www.systutorials.com/how-to-test-a-file-or-directory-exists-in-go/
---

Go doesn’t have a dedicated `FileExists()` function. Instead, use `os.Stat()` to retrieve file metadata and inspect the error type to determine what actually happened.

## Basic File Existence Check

``` go
import "os"

func fileExists(path string) bool {
    _, err := os.Stat(path)
    return !os.IsNotExist(err)
}
```

`os.Stat()` returns an error only if something goes wrong. The key is using `os.IsNotExist()` to distinguish between “file not found” and other errors like permission denied or I/O failures.

## Why Check Error Type Instead of Just err != nil?

`os.Stat()` can fail for several reasons:

- File doesn’t exist
- Permission denied
- Disk read errors
- Invalid path

If you only check `err != nil`, permission errors and missing files both return `false`. That’s wrong—they’re different conditions:

``` go
// Wrong: treats all errors the same
func fileExists(path string) bool {
    _, err := os.Stat(path)
    return err == nil  // false for permission errors AND missing files
}

// Correct: only false if file truly doesn't exist
func fileExists(path string) bool {
    _, err := os.Stat(path)
    return !os.IsNotExist(err)
}
```

With the correct approach, if you lack read permissions, the function returns `true` (the file exists, but you can’t access it). If the file is actually missing, it returns `false`.

## Checking Directories vs Regular Files

The same function works for both files and directories. To specifically verify you have a directory:

``` go
func dirExists(path string) bool {
    info, err := os.Stat(path)
    return err == nil && info.IsDir()
}

func isRegularFile(path string) bool {
    info, err := os.Stat(path)
    return err == nil && info.Mode().IsRegular()
}
```

Check `info.Mode()` for other file types like symlinks:

``` go
func isSymlink(path string) bool {
    info, err := os.Lstat(path)  // Lstat doesn't follow symlinks
    return err == nil && info.Mode()&os.ModeSymlink != 0
}
```

Note: Use `os.Lstat()` for symlinks since `os.Stat()` follows them automatically.

## Using io/fs for Abstraction (Go 1.16+)

For new code, use `io/fs.Stat()`. It works with local filesystems, embedded files, and custom implementations:

``` go
import (
    "io/fs"
    "os"
)

func fileExists(fsys fs.FS, path string) bool {
    _, err := fs.Stat(fsys, path)
    return !os.IsNotExist(err)
}

// With OS filesystem
fileExists(os.DirFS("."), "config.json")

// With embedded files
import "embed"

//go:embed all:templates
var templates embed.FS

fileExists(templates, "base.html")
```

This abstraction means you write the function once and use it everywhere—local disk, memory, or cloud storage backends.

## Checking Multiple File Attributes

If you need existence *and* metadata, fetch both at once:

``` go
func getFileInfo(path string) (os.FileInfo, bool) {
    info, err := os.Stat(path)
    return info, !os.IsNotExist(err)
}

// Usage
info, exists := getFileInfo("data.txt")
if exists {
    fmt.Printf("Size: %d bytes, Modified: %s\n", 
        info.Size(), info.ModTime())
}
```

## Performance Tips

`os.Stat()` always hits the filesystem. In hot paths:

- **Cache the result** if you need both existence and metadata.
- **Batch operations** with `filepath.WalkDir()` instead of calling `os.Stat()` repeatedly:

``` go
// Inefficient: stat each file individually
for _, name := range largeFileList {
    if fileExists(name) {
        // process
    }
}

// Better: walk once
filepath.WalkDir(".", func(path string, d fs.DirEntry, err error) error {
    if err != nil {
        return err
    }
    // Process d directly, no extra stat call needed
    fmt.Println(path, d.IsDir())
    return nil
})
```

- **Avoid redundant checks** in error handling. If a function already returns `os.FileInfo`, you know the file exists.

## Handling Race Conditions

A file can be deleted between your existence check and when you actually use it. Don’t rely on a separate existence check—attempt the operation and handle the error:

``` go
// Bad: TOCTOU (time-of-check to time-of-use) race
if fileExists(path) {
    data, err := os.ReadFile(path)  // File might be gone now
}

// Good: just try to read
data, err := os.ReadFile(path)
if err != nil {
    // Handle missing file or other errors
}
```
