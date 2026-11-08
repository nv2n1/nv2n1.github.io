---
title: "Hash Tables in C: Building and Using Them Effectively"
date: 2013-07-12 16:47:47 +0000
modified: 2026-04-11 17:16:26 +0000
author: "Eric Ma"
layout: post
categories: [algorithms-data-structures]
canonical: /hashing-library-for-c/
---

When building applications requiring fast key-value lookups, hash tables are fundamental. C offers several options—from POSIX standard library functions to specialized third-party libraries. The right choice depends on your dataset characteristics, memory constraints, and whether you need dynamic resizing.

## Standard Library: hsearch()

The simplest option is `hsearch()` from `<search.h>` in POSIX-compliant systems. It provides basic hash table functionality for small to medium datasets.

``` c
#include <search.h>
#include <string.h>
#include <stdio.h>

int main() {
    hcreate(100);  // Initialize table with approximate capacity

    ENTRY item = {"key1", (void *)"value1"};
    hsearch(item, ENTER);

    item.key = "key1";
    ENTRY *result = hsearch(item, FIND);

    if (result != NULL) {
        printf("Found: %s\n", (char *)result->data);
    }

    hdestroy();
    return 0;
}
```

Limitations are significant: fixed maximum size set at `hcreate()`, poor collision handling in some implementations, and minimal API. Use `hsearch()` only for simple tools or embedded scenarios where external dependencies aren’t acceptable.

## Modern Header-Only Libraries: uthash and khash

For new projects, uthash and khash are the de facto standards. Both are header-only or single-file, requiring no build system integration.

### uthash: Type-Safe Macro-Based Hashing

uthash generates type-safe operations via preprocessor macros. Your data structures gain hash capabilities by including a `UT_hash_handle` field.

``` c
#include "uthash.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

struct user {
    int id;
    char name[64];
    UT_hash_handle hh;
};

int main() {
    struct user *users = NULL;

    // Insert
    struct user *u = malloc(sizeof(struct user));
    u->id = 1;
    strcpy(u->name, "alice");
    HASH_ADD_INT(users, id, u);

    // Lookup
    struct user *found = NULL;
    HASH_FIND_INT(users, &(int){1}, found);
    if (found) {
        printf("Found: %s\n", found->name);
    }

    // Iterate and cleanup
    struct user *tmp;
    HASH_ITER(hh, users, u, tmp) {
        HASH_DEL(users, u);
        free(u);
    }

    return 0;
}
```

uthash supports multiple key types: integers, strings, or custom structures. Macro-based generation means compilation overhead but excellent runtime performance and type safety.

### khash: Minimal Overhead Performance

khash prioritizes minimal code footprint and speed with straightforward C semantics.

``` c
#include "khash.h"
#include <stdio.h>

KHASH_MAP_INIT_STR(str, int)

int main() {
    khash_t(str) *h = kh_init(str);
    int ret;
    khiter_t k;

    // Insert
    k = kh_put(str, h, "key1", &ret);
    kh_val(h, k) = 42;

    // Lookup
    k = kh_get(str, h, "key1");
    if (k != kh_end(h)) {
        printf("Value: %d\n", kh_val(h, k));
    }

    // Delete
    kh_del(str, h, k);

    // Cleanup
    kh_destroy(str, h);
    return 0;
}
```

khash generates specialized code for each key-value type pair, resulting in tight, predictable memory usage. Return codes from `kh_put()` distinguish insertions from updates, enabling conditional logic without extra lookups.

## CMPH: Perfect Hashing for Static Data

For deterministic, space-efficient lookups on static datasets, CMPH (C Minimal Perfect Hashing Library) is unmatched. A perfect hash function maps n keys to n hash values with zero collisions.

CMPH excels with massive, immutable datasets (100+ million keys) that fit in memory. It generates minimal perfect hash functions serializable to disk for reuse across processes.

``` bash
# Build a perfect hash function from a wordlist
cmph -g czech -c 10 -k wordlist.txt -m chd -o wordlist.cmph
```

Use CMPH when:

- Your dataset is static or changes rarely
- Memory efficiency is critical
- You need reproducible hash functions across processes or applications
- Zero hash collisions matter for guaranteed O(1) lookups

## libghthash: Dynamic Hash Tables with Complex Types

libghthash provides a more flexible, production-ready hash table supporting arbitrary data types and custom comparisons. Unlike `hsearch()`, it handles dynamic resizing and heterogeneous objects cleanly.

``` c
#include <ghthash.h>
#include <string.h>
#include <stdio.h>

int main() {
    GHashTable *table = ghthash_create_table(NULL, NULL);

    ghthash_insert(table, "username", 8, "alice", 5);

    char *value = (char *)ghthash_lookup(table, "username", 8);
    if (value) {
        printf("User: %s\n", value);
    }

    ghthash_remove(table, "username", 8);
    ghthash_destroy_table(table);

    return 0;
}
```

Key advantages:

- Custom hash and comparison functions
- Automatic resizing as load factor increases
- Handles binary data and non-string keys
- Portable across Linux, BSD, and Windows

## Choosing the Right Library

| Use Case                                  | Best Choice     |
|-------------------------------------------|-----------------|
| Toy projects, minimal dependencies        | `hsearch()`     |
| Enormous static datasets, memory-critical | CMPH            |
| Dynamic data, complex heterogeneous types | libghthash      |
| New production code, embedded systems     | uthash or khash |

For most modern C projects, **uthash** or **khash** are the pragmatic default: they require no external build dependencies, compile quickly, and provide excellent performance with clean APIs. Choose uthash for type safety via macros; choose khash for minimal overhead and explicit control.

If you’re integrating with large ecosystems, check whether your project already uses GLib (which includes its own hash table) before adding another dependency.
