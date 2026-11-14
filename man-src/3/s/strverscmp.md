---
title: "strverscmp(3)"
name: "strverscmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strverscmp/"
description: "strverscmp – compare two version strings"
---

<p>strverscmp &#8211; compare two version strings</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;string.h&gt;

int strverscmp(const char *s1, const char *s2);</code></pre>
<h2>Description</h2>
<p>Often one has files <i>jan1</i>, <i>jan2</i>, &#8230;, <i>jan9</i>, <i>jan10</i>, &#8230; and it feels wrong when <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) orders them <i>jan1</i>, <i>jan10</i>, &#8230;, <i>jan2</i>, &#8230;, <i>jan9</i>. In order to rectify this, GNU introduced the <i>-v</i> option to <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1), which is implemented using <code><a href="/docs/linux/man/3-versionsort/">versionsort</a></code>(3), which again uses <code>strverscmp</code>(). </p>
<p> Thus, the task of <code>strverscmp</code>() is to compare two strings and find the &quot;right&quot; order, while <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3) finds only the lexicographic order. This function does not use the locale category <code>LC_COLLATE</code>, so is meant mostly for situations where the strings are expected to be in ASCII. </p>
<p> What this function does is the following. If both strings are equal, return 0. Otherwise, find the position between two bytes with the property that before it both strings are equal, while directly after it there is a difference. Find the largest consecutive digit strings containing (or starting at, or ending at) this position. If one or both of these is empty, then return what <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3) would have returned (numerical ordering of byte values). Otherwise, compare both digit strings numerically, where digit strings with one or more leading zeros are interpreted as if they have a decimal point in front (so that in particular digit strings with more leading zeros come before digit strings with fewer leading zeros). Thus, the ordering is <i>000</i>, <i>00</i>, <i>01</i>, <i>010</i>, <i>09</i>, <i>0</i>, <i>1</i>, <i>9</i>, <i>10</i>.</p>
<h2>Return Value</h2>
<p>The <code>strverscmp</code>() function returns an integer less than, equal to, or greater than zero if <i>s1</i> is found, respectively, to be earlier than, equal to, or later than <i>s2</i>.</p>
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
<td> <code>strverscmp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>This function is a GNU extension.</p>
<h2>Examples</h2>
<p>The program below can be used to demonstrate the behavior of <code>strverscmp</code>(). It uses <code>strverscmp</code>() to compare the two strings given as its command-line arguments. An example of its use is the following: </p>
<pre><code>$ ./a.out jan1 jan10
jan1 &lt; jan10



Program source



#define _GNU_SOURCE
#include &lt;string.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
int
main(int argc, char *argv[])
{
    int res;
    if (argc != 3) {
        fprintf(stderr, &quot;Usage: %s &lt;string1&gt; &lt;string2&gt;
&quot;, argv[0]);
        exit(EXIT_FAILURE);
    }
    res = strverscmp(argv[1], argv[2]);
    printf(&quot;%s %s %s
&quot;, argv[1],
    (res &lt; 0) ? &quot;&lt;&quot; : (res == 0) ? &quot;==&quot; : &quot;&gt;&quot;, argv[2]);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rename/">rename</a></code>(1), <code><a href="/docs/linux/man/3-strcasecmp/">strcasecmp</a></code>(3), <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3), <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
