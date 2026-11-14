---
title: "strtok_r(3)"
name: "strtok_r"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strtok_r/"
description: "strtok, strtok_r – extract tokens from strings"
---

<p>strtok, strtok_r &#8211; extract tokens from strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

char *strtok(char *str, const char *delim);

char *strtok_r(char *str, const char *delim, char **saveptr);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strtok_r</code>(): _POSIX_C_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p>The <code>strtok</code>() function breaks a string into a sequence of zero or more nonempty tokens. On the first call to <code>strtok</code>(), the string to be parsed should be specified in <i>str</i>. In each subsequent call that should parse the same string, <i>str</i> must be NULL. </p>
<p> The <i>delim</i> argument specifies a set of bytes that delimit the tokens in the parsed string. The caller may specify different strings in <i>delim</i> in successive calls that parse the same string. </p>
<p> Each call to <code>strtok</code>() returns a pointer to a null-terminated string containing the next token. This string does not include the delimiting byte. If no more tokens are found, <code>strtok</code>() returns NULL. </p>
<p> A sequence of calls to <code>strtok</code>() that operate on the same string maintains a pointer that determines the point from which to start searching for the next token. The first call to <code>strtok</code>() sets this pointer to point to the first byte of the string. The start of the next token is determined by scanning forward for the next nondelimiter byte in <i>str</i>. If such a byte is found, it is taken as the start of the next token. If no such byte is found, then there are no more tokens, and <code>strtok</code>() returns NULL. (A string that is empty or that contains only delimiters will thus cause <code>strtok</code>() to return NULL on the first call.) </p>
<p> The end of each token is found by scanning forward until either the next delimiter byte is found or until the terminating null byte (&#8216;
