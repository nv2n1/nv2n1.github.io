---
title: "qsort_r(3)"
name: "qsort_r"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qsort_r/"
description: "qsort, qsort_r – sort an array"
---

<p>qsort, qsort_r &#8211; sort an array</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;

void qsort(void *base, size_t nmemb, size_t size,
           int (*compar)(const void *, const void *));

void qsort_r(void *base, size_t nmemb, size_t size,
             int (*compar)(const void *, const void *, void *),
             void *arg);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>qsort_r</code>(): _GNU_SOURCE</p>
<h2>Description</h2>
<p>The <code>qsort</code>() function sorts an array with <i>nmemb</i> elements of size <i>size</i>. The <i>base</i> argument points to the start of the array. </p>
<p> The contents of the array are sorted in ascending order according to a comparison function pointed to by <i>compar</i>, which is called with two arguments that point to the objects being compared. </p>
<p> The comparison function must return an integer less than, equal to, or greater than zero if the first argument is considered to be respectively less than, equal to, or greater than the second. If two members compare as equal, their order in the sorted array is undefined. </p>
<p> The <code>qsort_r</code>() function is identical to <code>qsort</code>() except that the comparison function <i>compar</i> takes a third argument. A pointer is passed to the comparison function via <i>arg</i>. In this way, the comparison function does not need to use global variables to pass through arbitrary arguments, and is therefore reentrant and safe to use in threads.</p>
<h2>Return Value</h2>
<p>The <code>qsort</code>() and <code>qsort_r</code>() functions return no value.</p>
<h2>Versions</h2>
<p><code>qsort_r</code>() was added to glibc in version 2.8.</p>
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
<td> <code>qsort</code>(), <code>qsort_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p><code>qsort</code>(): POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>Notes</h2>
<p>To compare C strings, the comparison function can call <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3), as shown in the example below.</p>
<h2>Examples</h2>
<p>For one example of use, see the example under <code><a href="/docs/linux/man/3-bsearch/">bsearch</a></code>(3). Another example is the following program, which sorts the strings given in its command-line arguments: #include &lt;stdio.h&gt;<br />
#include &lt;stdlib.h&gt;<br />
#include &lt;string.h&gt; static int cmpstringp(const void *p1, const void *p2) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;The actual arguments to this function are&nbsp;&quot;pointers to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointers to char&quot;, but&nbsp;<a href="/docs/linux/man/3-strcmp/">strcmp</a>(3)&nbsp;arguments are&nbsp;&quot;pointers<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to char&quot;, hence the following cast plus dereference&nbsp;*/ </p>
<pre><code>return strcmp(*(const char **)p1, *(const char **)p2);
}
int main(int argc, char *argv[])
{
    if (argc &lt; 2) {
        fprintf(stderr, &quot;Usage: %s &lt;string&gt;...
&quot;, argv[0]);
        exit(EXIT_FAILURE);
    }
    qsort(&amp;argv[1], argc - 1, sizeof(char *), cmpstringp);
    for (int j = 1; j &lt; argc; j++)
        puts(argv[j]);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sort/">sort</a></code>(1), <code><a href="/docs/linux/man/3-alphasort/">alphasort</a></code>(3), <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3), <code><a href="/docs/linux/man/3-versionsort/">versionsort</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
