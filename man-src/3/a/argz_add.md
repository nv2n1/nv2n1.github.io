---
title: "argz_add(3)"
name: "argz_add"
section: "3"
letter: "a"
url: "/docs/linux/man/3-argz_add/"
description: "argz_add, argz_add_sep, argz_append, argz_count, argz_create, argz_create_sep, argz_delete, argz_extract, argz_insert, argz_next, argz_replace, argz_stringify – functions to handle an argz list"
---

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
<p> An argz vector is a pointer to a character buffer together with a length. The intended interpretation of the character buffer is an array of strings, where the strings are separated by null bytes (&#8216;\0&#8217;). If the length is nonzero, the last byte of the buffer must be a null byte. </p>
<p> These functions are for handling argz vectors. The pair (NULL,0) is an argz vector, and, conversely, argz vectors of length 0 must have null pointer. Allocation of nonempty argz vectors is done using <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), so that <code><a href="/docs/linux/man/3-free/">free</a></code>(3) can be used to dispose of them again. </p>
<p> <code>argz_add</code>() adds the string <i>str</i> at the end of the array <i>*argz</i>, and updates <i>*argz</i> and <i>*argz_len</i>. </p>
<p> <code>argz_add_sep</code>() is similar, but splits the string <i>str</i> into substrings separated by the delimiter <i>delim</i>. For example, one might use this on a UNIX search path with delimiter &#8216;:&#8216;. </p>
<p> <code>argz_append</code>() appends the argz vector (<i>buf</i>,&nbsp;<i>buf_len</i>) after (<i>*argz</i>,&nbsp;<i>*argz_len</i>) and updates <i>*argz</i> and <i>*argz_len</i>. (Thus, <i>*argz_len</i> will be increased by <i>buf_len</i>.) </p>
<p> <code>argz_count</code>() counts the number of strings, that is, the number of null bytes (&#8216;\0&#8217;), in (<i>argz</i>,&nbsp;<i>argz_len</i>). </p>
<p> <code>argz_create</code>() converts a UNIX-style argument vector <i>argv</i>, terminated by <i>(char&nbsp;*)&nbsp;0</i>, into an argz vector (<i>*argz</i>,&nbsp;<i>*argz_len</i>). </p>
<p> <code>argz_create_sep</code>() converts the null-terminated string <i>str</i> into an argz vector (<i>*argz</i>,&nbsp;<i>*argz_len</i>) by breaking it up at every occurrence of the separator <i>sep</i>. </p>
<p> <code>argz_delete</code>() removes the substring pointed to by <i>entry</i> from the argz vector (<i>*argz</i>,&nbsp;<i>*argz_len</i>) and updates <i>*argz</i> and <i>*argz_len</i>. </p>
<p> <code>argz_extract</code>() is the opposite of <code>argz_create</code>(). It takes the argz vector (<i>argz</i>,&nbsp;<i>argz_len</i>) and fills the array starting at <i>argv</i> with pointers to the substrings, and a final NULL, making a UNIX-style argv vector. The array <i>argv</i> must have room for <i>argz_count</i>(<i>argz</i>, <i>argz_len</i>) + 1 pointers. </p>
<p> <code>argz_insert</code>() is the opposite of <code>argz_delete</code>(). It inserts the argument <i>entry</i> at position <i>before</i> into the argz vector (<i>*argz</i>,&nbsp;<i>*argz_len</i>) and updates <i>*argz</i> and <i>*argz_len</i>. If <i>before</i> is NULL, then <i>entry</i> will inserted at the end. </p>
<p> <code>argz_next</code>() is a function to step through the argz vector. If <i>entry</i> is NULL, the first entry is returned. Otherwise, the entry following is returned. It returns NULL if there is no following entry. </p>
<p> <code>argz_replace</code>() replaces each occurrence of <i>str</i> with <i>with</i>, reallocating argz as necessary. If <i>replace_count</i> is non-NULL, <i>*replace_count</i> will be incremented by the number of replacements. </p>
<p> <code>argz_stringify</code>() is the opposite of <code>argz_create_sep</code>(). It transforms the argz vector into a normal string by replacing all null bytes (&#8216;\0&#8217;) except the last by <i>sep</i>.  </p>
<h2>RETURN VALUE</h2>
<p> All argz functions that do memory allocation have a return type of <i>error_t</i> (an integer type), and return 0 for success, and <code>ENOMEM</code> if an allocation error occurs.  </p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>argz_add</code>(), <code>argz_add_sep</code>(),  <code>argz_append</code>(), <code>argz_count</code>(),  <code>argz_create</code>(), <code>argz_create_sep</code>(),  <code>argz_delete</code>(), <code>argz_extract</code>(),  <code>argz_insert</code>(), <code>argz_next</code>(),  <code>argz_replace</code>(), <code>argz_stringify</code>() 
</td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are a GNU extension.  </p>
<h2>BUGS</h2>
<p> Argz vectors without a terminating null byte may lead to Segmentation Faults.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-envz_add/">envz_add</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
