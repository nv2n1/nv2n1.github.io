---
title: "strncmp(3)"
name: "strncmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strncmp/"
description: "strcmp, strncmp – compare two strings"
---

<p>strcmp, strncmp &#8211; compare two strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

int strcmp(const char *s1, const char *s2);

int strncmp(const char *s1, const char *s2, size_t n);</code></pre>
<h2>Description</h2>
<p>The <code>strcmp</code>() function compares the two strings <i>s1</i> and <i>s2</i>. The locale is not taken into account (for a locale-aware comparison, see <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3)). The comparison is done using unsigned characters. </p>
<p> <code>strcmp</code>() returns an integer indicating the result of the comparison, as follows:</p>
<dl>
<dt>&bull;</p>
<dd>0, if the <i>s1</i> and <i>s2</i> are equal;</p>
<dt>&bull;</p>
<dd>a negative value if <i>s1</i> is less than <i>s2</i>;</p>
<dt>&bull;</p>
<dd>a positive value if <i>s1</i> is greater than <i>s2</i>.</dl>
<p> The <code>strncmp</code>() function is similar, except it compares only the first (at most) <i>n</i> bytes of <i>s1</i> and <i>s2</i>.</p>
<h2>Return Value</h2>
<p>The <code>strcmp</code>() and <code>strncmp</code>() functions return an integer less than, equal to, or greater than zero if <i>s1</i> (or the first <i>n</i> bytes thereof) is found, respectively, to be less than, to match, or be greater than <i>s2</i>.</p>
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
<td> <code>strcmp</code>(), <code>strncmp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>Notes</h2>
<p>POSIX.1 specifies only that:</p>
<dl>
<dd>The sign of a nonzero return value shall be determined by the sign of the difference between the values of the first pair of bytes (both interpreted as type <i>unsigned char</i>) that differ in the strings being compared.</dl>
<p> In glibc, as in most other implementations, the return value is the arithmetic result of subtracting the last compared byte in <i>s2</i> from the last compared byte in <i>s1</i>. (If the two characters are equal, this difference is 0.)</p>
<h2>Examples</h2>
<p>The program below can be used to demonstrate the operation of <code>strcmp</code>() (when given two arguments) and <code>strncmp</code>() (when given three arguments). First, some examples using <code>strcmp</code>(): $ <code>./string_comp ABC ABC</code> &lt;str1&gt; and &lt;str2&gt; are equal $ <code>./string_comp ABC AB</code> # &#8216;C&#8217; is ASCII 67; &#8216;C&#8217; &#8211; &#8216;&nbsp;&#8216; = 67 &lt;str1&gt; is greater than &lt;str2&gt; (67) $ <code>./string_comp ABA ABZ</code> # &#8216;A&#8217; is ASCII 65; &#8216;Z&#8217; is ASCII 90 &lt;str1&gt; is less than &lt;str2&gt; (-25) $ <code>./string_comp ABJ ABC</code> &lt;str1&gt; is greater than &lt;str2&gt; (7) $ .<code>/string_comp $&#8217;\201&#8242; A</code> # 0201 &#8211; 0101 = 0100 (or 64 decimal) &lt;str1&gt; is greater than &lt;str2&gt; (64) The last example uses <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1)-specific syntax to produce a string containing an 8-bit ASCII code; the result demonstrates that the string comparison uses unsigned characters. And then some examples using <code>strncmp</code>(): $ <code>./string_comp ABC AB 3</code> &lt;str1&gt; is greater than &lt;str2&gt; (67) $ <code>./string_comp ABC AB 2</code> &lt;str1&gt; and &lt;str2&gt; are equal in the first 2 bytes</p>
<h3>Program source</h3>
<p>/* string_comp.c </p>
<pre><code>Licensed under GNU General Public License v2 or later.
                                                        * /
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
                                                    int
                                                    main(int argc, char *argv[])
{
    int res;
    if (argc &lt; 3) {
        fprintf(stderr, &quot;Usage: %s &lt;str1&gt; &lt;str2&gt; [&lt;len&gt;]
&quot;, argv[0]);
        exit(EXIT_FAILURE);
    }
    if (argc == 3)
        res = strcmp(argv[1], argv[2]);
    else
        res = strncmp(argv[1], argv[2], atoi(argv[3]));
    if (res == 0) {
        printf(&quot;&lt;str1&gt; and &lt;str2&gt; are equal&quot;);
        if (argc &gt; 3)
            printf(&quot; in the first %d bytes
&quot;, atoi(argv[3]));
        printf(&quot;
&quot;);
    } else if (res &lt; 0) {
        printf(&quot;&lt;str1&gt; is less than &lt;str2&gt; (%d)
&quot;, res);
    } else {
        printf(&quot;&lt;str1&gt; is greater than &lt;str2&gt; (%d)
&quot;, res);
    }
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-bcmp/">bcmp</a></code>(3), <code><a href="/docs/linux/man/3-memcmp/">memcmp</a></code>(3), <code><a href="/docs/linux/man/3-strcasecmp/">strcasecmp</a></code>(3), <code><a href="/docs/linux/man/3-strcoll/">strcoll</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-strncasecmp/">strncasecmp</a></code>(3), <code><a href="/docs/linux/man/3-strverscmp/">strverscmp</a></code>(3), <code><a href="/docs/linux/man/3-wcscmp/">wcscmp</a></code>(3), <code><a href="/docs/linux/man/3-wcsncmp/">wcsncmp</a></code>(3), <code><a href="/docs/linux/man/7-ascii/">ascii</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
