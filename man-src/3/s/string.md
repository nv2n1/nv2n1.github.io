---
title: "string(3)"
name: "string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-string/"
description: "stpcpy, strcasecmp, strcat, strchr, strcmp, strcoll, strcpy, strcspn, strdup, strfry, strlen, strncat, strncmp, strncpy, strncasecmp, strpbrk, strrchr, strsep, strspn, strstr, strtok, strxfrm, inde..."
---

<p>stpcpy, strcasecmp, strcat, strchr, strcmp, strcoll, strcpy, strcspn, strdup, strfry, strlen, strncat, strncmp, strncpy, strncasecmp, strpbrk, strrchr, strsep, strspn, strstr, strtok, strxfrm, index, rindex &#8211; string operations</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;strings.h&gt;

int strcasecmp(const char *s1, const char *s2);

Compare the strings
    s1

        and
            s2

                ignoring case.int
                strncasecmp(const char *s1, const char *s2, size_t n);

Compare the first
    n

        bytes of the strings
            s1

                and
                    s2

                        ignoring case.char *
                        index(const char *s, int c);

Return a pointer to the first occurrence of the character
    c

        in the string
            s.

    char *
    rindex(const char *s, int c);

Return a pointer to the last occurrence of the character
    c

        in the string
            s.

#include &lt;string.h&gt;

    char *
    stpcpy(char *dest, const char *src);

Copy a string from
    src

        to
            dest,

    returning a pointer to the end of the resulting string at
        dest.

    char *
    strcat(char *dest, const char *src);

Append the string
    src

        to the string
            dest,

    returning a pointer
        dest.

    char *
    strchr(const char *s, int c);

Return a pointer to the first occurrence of the character
    c

        in the string
            s.

    int
    strcmp(const char *s1, const char *s2);

Compare the strings
    s1

        with
            s2.

    int
    strcoll(const char *s1, const char *s2);

Compare the strings
    s1

        with
            s2

    using the current locale.char *
    strcpy(char *dest, const char *src);

Copy the string
    src

        to
            dest,

    returning a pointer to the start of
        dest.

    size_t
    strcspn(const char *s, const char *reject);

Calculate the length of the initial segment of the string
    s

        which does not contain any of bytes in the string
            reject,

    char *strdup(const char *s);

Return a duplicate of the string
    s

        in memory allocated using malloc(3)
            .

    char *strfry(char *string);

Randomly swap the characters in
    string.

    size_t
    strlen(const char *s);

Return the length of the string
    s.

    char *
    strncat(char *dest, const char *src, size_t n);

Append at most
    n

        bytes from the string
            src

                to the string
                    dest,

    returning a pointer to
        dest.

    int
    strncmp(const char *s1, const char *s2, size_t n);

Compare at most
    n

        bytes of the strings
            s1

                and
                    s2.

    char *
    strncpy(char *dest, const char *src, size_t n);

Copy at most
    n

        bytes from string
            src

                to
                    dest,

    returning a pointer to the start of
        dest.

    char *
    strpbrk(const char *s, const char *accept);

Return a pointer to the first occurrence in the string
    s

        of one of the bytes in the string
            accept.

    char *
    strrchr(const char *s, int c);

Return a pointer to the last occurrence of the character
    c

        in the string
            s.

    char *
    strsep(char **stringp, const char *delim);

Extract the initial token in
    stringp

        that is delimited by one of the bytes in
            delim.

    size_t
    strspn(const char *s, const char *accept);

Calculate the length of the starting segment in the string
    s

        that consists entirely of bytes in
            accept.

    char *
    strstr(const char *haystack, const char *needle);

Find the first occurrence of the substring
    needle

        in the string
            haystack,

    returning a pointer to the found substring.char *strtok(char *s, const char *delim);

Extract tokens from the string
    s

        that are delimited by one of the bytes in
            delim.

    size_t
    strxfrm(char *dest, const char *src, size_t n);

Transforms
    src

        to the current locale and copies the first
            n

                bytes to
                    dest.</code></pre>
<h2>Description</h2>
<p>The string functions perform operations on null-terminated strings. See the individual man pages for descriptions of each function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-index/">index</a></code>(3), <code><a href="/docs/linux/man/3-rindex/">rindex</a></code>(3), <code><a href="/docs/linux/man/3-stpcpy/">stpcpy</a></code>(3), <code><a href="/docs/linux/man/3-strcasecmp/">strcasecmp</a></code>(3), <code><a href="/docs/linux/man/3-strcat/">strcat</a></code>(3), <code><a href="/docs/linux/man/3-strchr/">strchr</a></code>(3), <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3), <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3), <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3), <code><a href="/docs/linux/man/3-strcspn/">strcspn</a></code>(3), <code><a href="/docs/linux/man/3-strdup/">strdup</a></code>(3), <code><a href="/docs/linux/man/3-strfry/">strfry</a></code>(3), <code><a href="/docs/linux/man/3-strlen/">strlen</a></code>(3), <code><a href="/docs/linux/man/3-strncasecmp/">strncasecmp</a></code>(3), <code><a href="/docs/linux/man/3-strncat/">strncat</a></code>(3), <code><a href="/docs/linux/man/3-strncmp/">strncmp</a></code>(3), <code><a href="/docs/linux/man/3-strncpy/">strncpy</a></code>(3), <code><a href="/docs/linux/man/3-strpbrk/">strpbrk</a></code>(3), <code><a href="/docs/linux/man/3-strrchr/">strrchr</a></code>(3), <code><a href="/docs/linux/man/3-strsep/">strsep</a></code>(3), <code><a href="/docs/linux/man/3-strspn/">strspn</a></code>(3), <code><a href="/docs/linux/man/3-strstr/">strstr</a></code>(3), <code><a href="/docs/linux/man/3-strtok/">strtok</a></code>(3), <code><a href="/docs/linux/man/3-strxfrm/">strxfrm</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
