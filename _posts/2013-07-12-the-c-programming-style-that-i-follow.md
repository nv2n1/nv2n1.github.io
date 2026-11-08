---
title: "C Code Organization: Structuring Headers and Source Files"
date: 2013-07-12 16:47:45 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /the-c-programming-style-that-i-follow/
---

C allows flexibility in coding style, but discipline matters. Consistent structure makes code readable, maintainable, and less prone to bugs. Here’s a practical approach that scales from small utilities to large projects.

## One Header Per Source File

Pair each source file (*.c) with a corresponding header file (*.h). The header serves as the module’s public interface, declaring what’s available to other compilation units.

    math_utils.h
    math_utils.c

This 1:1 mapping makes dependencies clear and keeps related declarations and definitions grouped logically. It also simplifies build systems and makes it obvious which headers export which functionality.

## Header Guards and Pragma Once

Always prevent multiple inclusion. Use the standard `#ifndef` pattern:

``` c
#ifndef MATH_UTILS_H
#define MATH_UTILS_H

// declarations here

#endif // MATH_UTILS_H
```

Avoid leading underscores in guard names — identifiers starting with underscore followed by an uppercase letter are reserved by the C standard. Use `MATH_UTILS_H` instead of `_MATH_UTILS_H`.

Modern alternative: `#pragma once` is non-standard but supported by all major compilers (GCC, Clang, MSVC). It’s simpler and avoids naming collisions:

``` c
#pragma once
```

Choose one consistently across your codebase. For new projects without legacy compatibility requirements, `#pragma once` is reasonable. For projects targeting embedded systems or unusual platforms, stick with `#ifndef`.

## Minimize Header Dependencies

Only include headers in .c files. Headers should almost never include other headers except when a type definition is genuinely necessary for your public interface.

**Bad:**

``` c
// config.h
#include "database.h"  // unnecessary

struct AppState {
    Database *db;
};
```

**Better:**

``` c
// config.h
struct Database;  // forward declaration

struct AppState {
    struct Database *db;
};

// config.c
#include "config.h"
#include "database.h"  // include here
```

Forward declarations eliminate circular dependencies and keep header dependency chains shallow. This reduces compilation time and makes the dependency graph easier to reason about.

## Declarations Only in Headers

Headers contain declarations: function prototypes, type definitions (structs, enums, unions), and extern variable declarations. Never define functions or allocate storage in headers.

``` c
// math_utils.h
int add(int a, int b);  // declaration only

// math_utils.c
#include "math_utils.h"

int add(int a, int b) {  // definition
    return a + b;
}
```

**Exception:** `static inline` functions can live in headers since each translation unit gets its own copy. Use them for performance-critical code only:

``` c
// math_utils.h
static inline int square(int x) {
    return x * x;
}
```

Mark them `static inline` to avoid ODR (One Definition Rule) violations and to signal intent that this is an optimization.

## Global Variables: Minimize and Document

If a module must export a variable, declare it as `extern` in the header:

``` c
// config.h
extern int max_connections;

// config.c
#include "config.h"

int max_connections = 100;
```

Global variables are a code smell — they complicate testing, threading, and reasoning about program state. Prefer passing data through function parameters or returning values. When globals are unavoidable (configuration constants, logging state), keep them limited, document their purpose clearly, and consider wrapping them in accessor functions for thread safety.

## Include Order Convention

In .c files, follow this include order to catch missing dependencies early:

``` c
// network.c
#include "network.h"      // validate module completeness first
#include <stdio.h>        // standard library headers next
#include <stdlib.h>
#include "config.h"       // project-local headers last
#include "logging.h"
```

This order ensures your module’s header is self-contained and catches missing includes before compilation spreads to other files.

## Const Correctness

Use `const` for immutable parameters and return values:

``` c
// string_utils.h
int string_length(const char *str);
const char* get_error_message(void);

void process_config(const struct Config *cfg);
```

Const annotations document intent, prevent accidental modifications, and let the compiler catch bugs.

## Document Public Interfaces

Add brief comments to public declarations, especially non-obvious behavior:

``` c
// Returns non-zero if file exists, zero otherwise.
// Sets errno on I/O errors.
int file_exists(const char *path);

// Caller must free returned memory.
char* read_file_contents(const char *path);
```

Clear documentation reduces confusion during code review and helps new developers understand module contracts.

## Practical Example: Module Template

Here’s a complete minimal module:

``` c
// vector.h
#pragma once

typedef struct {
    int *data;
    size_t capacity;
    size_t size;
} IntVector;

IntVector* vector_create(size_t initial_capacity);
void vector_destroy(IntVector *v);
void vector_push(IntVector *v, int value);
int vector_get(const IntVector *v, size_t index);
size_t vector_size(const IntVector *v);
```

``` c
// vector.c
#include "vector.h"
#include <stdlib.h>
#include <string.h>

IntVector* vector_create(size_t initial_capacity) {
    IntVector *v = malloc(sizeof(IntVector));
    if (!v) return NULL;

    v->data = malloc(initial_capacity * sizeof(int));
    if (!v->data) {
        free(v);
        return NULL;
    }

    v->capacity = initial_capacity;
    v->size = 0;
    return v;
}

void vector_destroy(IntVector *v) {
    if (v) {
        free(v->data);
        free(v);
    }
}

void vector_push(IntVector *v, int value) {
    if (v->size >= v->capacity) {
        v->capacity *= 2;
        v->data = realloc(v->data, v->capacity * sizeof(int));
    }
    v->data[v->size++] = value;
}

int vector_get(const IntVector *v, size_t index) {
    return v->data[index];
}

size_t vector_size(const IntVector *v) {
    return v->size;
}
```

This discipline scales across projects. Consistent structure makes code reviews faster, reduces build times through minimal dependencies, and makes onboarding new developers straightforward.
