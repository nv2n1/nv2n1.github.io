---
title: "sbrk(2)"
name: "sbrk"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sbrk/"
description: "brk, sbrk – change data segment size"
---

<h2 class="name">NAME</h2>
<p> brk, sbrk &#8211; change data segment size </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int brk(void *</code><i>addr</i><code>);</code> </p>
<p> <code>void *sbrk(intptr_t </code><i>increment</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>brk</code>(), <code>sbrk</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.19:</p>
<dd>
<pre><code>
_DEFAULT_SOURCE ||
    (_XOPEN_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 500) &amp;&amp;
        !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200112L)
</code></pre>
<dt>From glibc 2.12 to 2.19:</p>
<dd>
<pre><code>
_BSD_SOURCE || _SVID_SOURCE ||
    (_XOPEN_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 500) &amp;&amp;
        !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200112L)
</code></pre>
<dt>Before glibc 2.12:</p>
<dd> _BSD_SOURCE || _SVID_SOURCE || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>brk</code>() and <code>sbrk</code>() change the location of the <i>program break</i>, which defines the end of the process&#8217;s data segment (i.e., the program break is the first location after the end of the uninitialized data segment). Increasing the program break has the effect of allocating memory to the process; decreasing the break deallocates memory. </p>
<p> <code>brk</code>() sets the end of the data segment to the value specified by <i>addr</i>, when that value is reasonable, the system has enough memory, and the process does not exceed its maximum data size (see <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2)). </p>
<p> <code>sbrk</code>() increments the program&#8217;s data space by <i>increment</i> bytes. Calling <code>sbrk</code>() with an <i>increment</i> of 0 can be used to find the current location of the program break.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>brk</code>() returns zero. On error, -1 is returned, and <i>errno</i> is set to <code>ENOMEM</code>. </p>
<p> On success, <code>sbrk</code>() returns the previous program break. (If the break was increased, then this value is a pointer to the start of the newly allocated memory). On error, <i>(void&nbsp;*)&nbsp;-1</i> is returned, and <i>errno</i> is set to <code>ENOMEM</code>.</p>
<h2>CONFORMING TO</h2>
<p> 4.3BSD; SUSv1, marked LEGACY in SUSv2, removed in POSIX.1-2001.</p>
<h2>NOTES</h2>
<p> Avoid using <code>brk</code>() and <code>sbrk</code>(): the <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) memory allocation package is the portable and comfortable way of allocating memory. </p>
<p> Various systems use various types for the argument of <code>sbrk</code>(). Common are <i>int</i>, <i>ssize_t</i>, <i>ptrdiff_t</i>, <i>intptr_t</i>.</p>
<h3>C library/kernel differences</h3>
<p> The return value described above for <code>brk</code>() is the behavior provided by the glibc wrapper function for the Linux <code>brk</code>() system call. (On most other implementations, the return value from <code>brk</code>() is the same; this return value was also specified in SUSv2.) However, the actual Linux system call returns the new program break on success. On failure, the system call returns the current break. The glibc wrapper function does some work (i.e., checks whether the new break is less than <i>addr</i>) to provide the 0 and -1 return values described above. </p>
<p> On Linux, <code>sbrk</code>() is implemented as a library function that uses the <code>brk</code>() system call, and does some internal bookkeeping so that it can return the old break value.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/3-end/">end</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
