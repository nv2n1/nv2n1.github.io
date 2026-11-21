---
title: "stpcpy(3)"
name: "stpcpy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stpcpy/"
description: "stpcpy – copy a string returning a pointer to its end"
---

<p>stpcpy &#8211; copy a string returning a pointer to its end</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;
char *stpcpy(char *dest, const char *src);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>stpcpy</code>():</p>
<dl>
<dd>
</dd><dl>
<dt>Since glibc 2.10:</dt>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dd>
<dt>Before glibc 2.10:</dt>
<dd>_GNU_SOURCE</dd></dl>
</dl>
<h2>Description</h2>
<p>The <code>stpcpy</code>() function copies the string pointed to by <i>src</i> (including the terminating null byte (&#8216;\0&#8217;)) to the array pointed to by <i>dest</i>. The strings may not overlap, and the destination string <i>dest</i> must be large enough to receive the copy.  </p>
<h2>RETURN VALUE</h2>
<p> <code>stpcpy</code>() returns a pointer to the <code>end</code> of the string <i>dest</i> (that is, the address of the terminating null byte) rather than the beginning.  </p>
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
<td> <code>stpcpy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function was added to POSIX.1-2008. Before that, it was not part of the C or POSIX.1 standards, nor customary on UNIX systems. It first appeared at least as early as 1986, in the Lattice C AmigaDOS compiler, then in the GNU fileutils and GNU textutils in 1989, and in the GNU C library by 1992. It is also present on the BSDs.  </p>
<h2>BUGS</h2>
<p> This function may overrun the buffer <i>dest</i>.  </p>
<h2>EXAMPLES</h2>
<p> For example, this program uses <code>stpcpy</code>() to concatenate <code>foo</code> and <code>bar</code> to produce <code>foobar</code>, which it then prints. </p>
<p> #define _GNU_SOURCE #include &lt;string.h&gt; #include &lt;stdio.h&gt; </p>
<p> int main(void) { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buffer[20]; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*to&nbsp;=&nbsp;buffer; </p>
<p> <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to&nbsp;=&nbsp;stpcpy(to,&nbsp;&quot;foo&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;to&nbsp;=&nbsp;stpcpy(to,&nbsp;&quot;bar&quot;); <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%s\n&quot;, buffer); }  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-bcopy/">bcopy</a></code>(3), <code><a href="/docs/linux/man/3-memccpy/">memccpy</a></code>(3), <code><a href="/docs/linux/man/3-memcpy/">memcpy</a></code>(3), <code><a href="/docs/linux/man/3-memmove/">memmove</a></code>(3), <code><a href="/docs/linux/man/3-stpncpy/">stpncpy</a></code>(3), <code><a href="/docs/linux/man/3-strcpy/">strcpy</a></code>(3), <code><a href="/docs/linux/man/3-string/">string</a></code>(3), <code><a href="/docs/linux/man/3-wcpcpy/">wcpcpy</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
