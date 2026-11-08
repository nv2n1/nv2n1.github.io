---
title: "Extracting Directory and Filename from a Path in C"
date: 2018-03-24 08:21:21 +0000
modified: 2026-04-11 17:40:28 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /how-to-get-the-directory-path-and-file-name-from-a-absolute-path-in-c-on-linux/
---

Parsing directory and filename components from an absolute path is a common task in systems programming. Linux provides `dirname()` and `basename()` functions for this purpose, but they have implementation-specific behaviors that can cause bugs if you’re not careful.

## Using dirname() and basename()

The POSIX standard defines both functions, though the implementations vary. Here’s the safest approach:

``` c
#include <libgen.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(void) {
    const char *path = "/foo/bar/baz.txt";

    char *path_copy = strdup(path);
    char *filename_copy = strdup(path);

    char *dir = dirname(path_copy);
    char *filename = basename(filename_copy);

    printf("Directory: %s\n", dir);      // Output: /foo/bar
    printf("Filename: %s\n", filename);  // Output: baz.txt

    free(path_copy);
    free(filename_copy);

    return 0;
}
```

**Critical implementation details:**

- Both `dirname()` and `basename()` may modify their input strings
- You **must** call `strdup()` on the original path before passing to either function
- Do **not** free the pointers returned by `dirname()` or `basename()`—they point into the duplicated strings you allocated
- Always `free()` the `strdup()` allocations when done

## Testing edge cases

``` c
#include <libgen.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void parse_path(const char *path) {
    char *dir_copy = strdup(path);
    char *file_copy = strdup(path);

    char *dir = dirname(dir_copy);
    char *filename = basename(file_copy);

    printf("Path: %s\n", path);
    printf("  Dir: %s\n", dir);
    printf("  File: %s\n", filename);

    free(dir_copy);
    free(file_copy);
}

int main(void) {
    parse_path("/foo/bar/baz.txt");    // Dir: /foo/bar, File: baz.txt
    parse_path("/foo/bar/");           // Dir: /foo/bar, File: (empty)
    parse_path("file.txt");            // Dir: ., File: file.txt
    parse_path("/");                   // Dir: /, File: /
    parse_path("/etc/.hidden");        // Dir: /etc, File: .hidden

    return 0;
}
```

**Edge cases to understand:**

- **Trailing slashes**: `dirname("/foo/bar/")` returns `/foo/bar`, but `basename("/foo/bar/")` returns an empty string
- **Root directory**: `dirname("/")` returns `/`, and `basename("/")` returns `/`
- **Filename only**: `dirname("file.txt")` returns `.`, and `basename("file.txt")` returns `file.txt`
- **Hidden files**: Work as expected—`dirname("/etc/.hidden")` returns `/etc`, `basename("/etc/.hidden")` returns `.hidden`

## Manual string parsing alternative

If you need more control, fewer dependencies, or want to avoid the string modification quirks of `dirname()`/`basename()`, manually parse using `strrchr()`:

``` c
#include <string.h>
#include <stdio.h>

void split_path(const char *path) {
    const char *last_slash = strrchr(path, '/');

    if (last_slash == NULL) {
        // No slash found, file is in current directory
        printf("Directory: .\n");
        printf("Filename: %s\n", path);
    } else if (last_slash == path) {
        // Slash at beginning (root path)
        printf("Directory: /\n");
        printf("Filename: %s\n", last_slash + 1);
    } else {
        // Normal case: print everything before the last slash
        size_t dir_len = last_slash - path;
        printf("Directory: %.*s\n", (int)dir_len, path);
        printf("Filename: %s\n", last_slash + 1);
    }
}

int main(void) {
    split_path("/foo/bar/baz.txt");   // Directory: /foo/bar, Filename: baz.txt
    split_path("file.txt");            // Directory: ., Filename: file.txt
    split_path("/root.txt");           // Directory: /, Filename: root.txt
    split_path("/.hidden");            // Directory: /, Filename: .hidden

    return 0;
}
```

This approach uses `strrchr()` to find the last forward slash, then calculates offsets with `%.*s` format specifier for precise substring printing. It’s more explicit about what’s happening and doesn’t modify the original path.

## Comparing approaches

| Approach | Pros | Cons |
|----|----|----|
| `dirname()`/`basename()` | Standard library, widely known | Modifies input, requires `strdup()`, POSIX behavior varies |
| Manual string parsing | No string modification, explicit, more portable | Slightly more code, need to handle edge cases manually |

For production code, choose the manual approach if you need predictable behavior across different Unix systems or want to avoid the `strdup()` overhead. Use `dirname()`/`basename()` if your codebase already depends on libgen.h and you can carefully manage the string copies.

## Compilation and testing

``` bash
gcc -Wall -Wextra -o pathparse pathparse.c
./pathparse
```

Note: Both approaches handle `strdup()` allocation failures identically—neither checks for NULL returns in these examples. In production code, you should check `strdup()` return values when error handling is required.
