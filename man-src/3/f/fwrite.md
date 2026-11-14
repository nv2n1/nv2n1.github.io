---
title: "fwrite(3)"
name: "fwrite"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fwrite/"
description: "fread, fwrite – binary stream input/output"
---

<p>fread, fwrite &#8211; binary stream input/output </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;</code>
<code>size_t fread(void *</code><i>ptr</i><code>, size_t </code><i>size</i><code>, size_t </code><i>nmemb</i><code>, FILE *</code><i>stream</i><code>);</code>
<code>size_t fwrite(const void *</code><i>ptr</i><code>, size_t </code><i>size</i><code>, size_t </code><i>nmemb</i><code>,</code>
<code> FILE *</code><i>stream</i><code>);</code></pre>
<h2>Description</h2>
<p>The function <code>fread</code>() reads <i>nmemb</i> items of data, each <i>size</i> bytes long, from the stream pointed to by <i>stream</i>, storing them at the location given by <i>ptr</i>. </p>
<p> The function <code>fwrite</code>() writes <i>nmemb</i> items of data, each <i>size</i> bytes long, to the stream pointed to by <i>stream</i>, obtaining them from the location given by <i>ptr</i>. </p>
<p> For nonlocking counterparts, see <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3).</p>
<h2>Return Value</h2>
<p>On success, <code>fread</code>() and <code>fwrite</code>() return the number of items read or written. This number equals the number of bytes transferred only when <i>size</i> is 1. If an error occurs, or the end of the file is reached, the return value is a short item count (or zero). </p>
<p> The file position indicator for the stream is advanced by the number of bytes successfully read or written. </p>
<p> <code>fread</code>() does not distinguish between end-of-file and error, and callers must use <code><a href="/docs/linux/man/3-feof/">feof</a></code>(3) and <code><a href="/docs/linux/man/3-ferror/">ferror</a></code>(3) to determine which occurred.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>fread</code>(), <code>fwrite</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C89.</p>
<h2>Examples</h2>
<p>The program below demonstrates the use of <code>fread</code>() by parsing /bin/sh ELF executable in binary mode and printing its magic and class: </p>
<pre><code>$ ./a.out
ELF magic: 0x7f454c46
Class: 0x02



Program source



#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof((arr)[0]))
int
main(void)
{
    FILE *fp = fopen(&quot;/bin/sh&quot;, &quot;rb&quot;);
    if (!fp) {
        perror(&quot;fopen&quot;);
        return EXIT_FAILURE;
    }
    unsigned char buffer[4];
    size_t ret = fread(buffer, ARRAY_SIZE(buffer), sizeof(*buffer), fp);
    if (ret != sizeof(*buffer)) {
        fprintf(stderr, &quot;fread() failed: %zu
&quot;, ret);
        exit(EXIT_FAILURE);
    }
    printf(&quot;ELF magic: %#04x%02x%02x%02x
&quot;, buffer[0], buffer[1],
    buffer[2], buffer[3]);
    ret = fread(buffer, 1, 1, fp);
    if (ret != 1) {
        fprintf(stderr, &quot;fread() failed: %zu
&quot;, ret);
        exit(EXIT_FAILURE);
    }
    printf(&quot;Class: %#04x
&quot;, buffer[0]);
    fclose(fp);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/3-feof/">feof</a></code>(3), <code><a href="/docs/linux/man/3-ferror/">ferror</a></code>(3), <code><a href="/docs/linux/man/3-unlocked_stdio/">unlocked_stdio</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
