---
title: "argz_insert(3)"
name: "argz_insert"
section: "3"
letter: "a"
url: "/docs/linux/man/3-argz_insert/"
description: "argz_add, argz_add_sep, argz_append, argz_count, argz_create, argz_create_sep, argz_delete, argz_extract, argz_insert, argz_next, argz_replace, argz_stringify – functions to handle an argz list"
---

<h2 class="name">NAME</h2>
<p> argz_add, argz_add_sep, argz_append, argz_count, argz_create, argz_create_sep, argz_delete, argz_extract, argz_insert, argz_next, argz_replace, argz_stringify &#8211; functions to handle an argz list </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;argz.h&gt;
error_t argz_add(char **argz, size_t *argz_len, const char *str);
error_t argz_add_sep(char **argz, size_t *argz_len,
                     const char *str, int delim);
error_t argz_append(char **argz, size_t *argz_len,
                    const char *buf, size_t buf_len);
size_t argz_count(const char *argz, size_t argz_len);
error_t argz_create(char *const argv[], char **argz,
                    size_t *argz_len);
error_t argz_create_sep(const char *str, int sep, char **argz,
                        size_t *argz_len);
void argz_delete(char **argz, size_t *argz_len, char *entry);
void argz_extract(const char *argz, size_t argz_len, char **argv);
error_t argz_insert(char **argz, size_t *argz_len, char *before,
                    const char *entry);
char *argz_next(const char *argz, size_t argz_len, const char *entry);
error_t argz_replace(char **argz, size_t *argz_len, const char *str,
                     const char *with, unsigned int *replace_count);
void argz_stringify(char *argz, size_t len, int sep);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions are glibc-specific. </p>
<p> An argz vector is a pointer to a character buffer together with a length. The intended interpretation of the character buffer is an array of strings, where the strings are separated by null bytes (&#8216;
