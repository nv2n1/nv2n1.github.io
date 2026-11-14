---
title: "gnu_get_libc_release(3)"
name: "gnu_get_libc_release"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnu_get_libc_release/"
description: "gnu_get_libc_version, gnu_get_libc_release – get glibc version and release"
---

<h2 class="name">NAME</h2>
<p> gnu_get_libc_version, gnu_get_libc_release &#8211; get glibc version and release </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;gnu/libc-version.h&gt;
const char *gnu_get_libc_version(void);
const char *gnu_get_libc_release(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The function <code>gnu_get_libc_version</code>() returns a string that identifies the glibc version available on the system. </p>
<p> The function <code>gnu_get_libc_release</code>() returns a string indicates the release status of the glibc version available on the system. This will be a string such as <i>stable</i>.</p>
<h2>VERSIONS</h2>
<p> These functions first appeared in glibc in version 2.1.</p>
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
<td> <code>gnu_get_libc_version</code>(), <code>gnu_get_libc_release</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are glibc-specific.</p>
<h2>EXAMPLES</h2>
<p> When run, the program below will produce output such as the following: </p>
<p> $<code> ./a.out</code> GNU libc version: 2.8 GNU libc release: stable</p>
<h3>Program source</h3>
<p> #include &lt;gnu/libc-version.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;GNU libc version:&nbsp;%s
&quot;, gnu_get_libc_version());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;GNU libc release:&nbsp;%s
&quot;, gnu_get_libc_release());<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-confstr/">confstr</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
