---
title: "sethostname(2)"
name: "sethostname"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sethostname/"
description: "gethostname, sethostname – get/set hostname"
---

<h2 class="name">NAME</h2>
<p> gethostname, sethostname &#8211; get/set hostname </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int gethostname(char *</code><i>name</i><code>, size_t </code><i>len</i><code>);</code><br />
 <code>int sethostname(const char *</code><i>name</i><code>, size_t </code><i>len</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>gethostname</code>():</p>
<dl>
<dt>
<dd> Since glibc 2.12: _BSD_SOURCE || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
 || /* Since glibc 2.12: */ _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<p> <code>sethostname</code>(): </p>
<pre><code>
Since glibc 2.21 : _DEFAULT_SOURCE
                       In glibc 2.19 and
                   2.20 : _DEFAULT_SOURCE ||
    (_XOPEN_SOURCE &amp;&amp; _XOPEN_SOURCE &amp; nbsp; &lt; &amp;nbsp; 500)
        Up to and including glibc 2.19 : _BSD_SOURCE
                                         ||
                                         (_XOPEN_SOURCE &amp;&amp; _XOPEN_SOURCE &amp; nbsp; &lt; &amp;nbsp; 500)
</code></pre>
<h2>DESCRIPTION</h2>
<p> These system calls are used to access or to change the system hostname. More precisely, they operate on the hostname associated with the calling process&#8217;s UTS namespace. </p>
<p> <code>sethostname</code>() sets the hostname to the value given in the character array <i>name</i>. The <i>len</i> argument specifies the number of bytes in <i>name</i>. (Thus, <i>name</i> does not require a terminating null byte.) </p>
<p> <code>gethostname</code>() returns the null-terminated hostname in the character array <i>name</i>, which has a length of <i>len</i> bytes. If the null-terminated hostname is too large to fit, then the name is truncated, and no error is returned (but see NOTES below). POSIX.1 says that if such truncation occurs, then it is unspecified whether the returned buffer includes a terminating null byte.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>name</i> is an invalid address.</p>
<dt><code>EINVAL</code></p>
<dd> <i>len</i> is negative or, for <code>sethostname</code>(), <i>len</i> is larger than the maximum allowed size.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> (glibc <code>gethostname</code>()) <i>len</i> is smaller than the actual size. (Before version 2.1, glibc uses <code>EINVAL</code> for this case.)</p>
<dt><code>EPERM</code></p>
<dd> For <code>sethostname</code>(), the caller did not have the <code>CAP_SYS_ADMIN</code> capability in the user namespace associated with its UTS namespace (see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7)).</dl>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.4BSD (these interfaces first appeared in 4.2BSD). POSIX.1-2001 and POSIX.1-2008 specify <code>gethostname</code>() but not <code>sethostname</code>().</p>
<h2>NOTES</h2>
<p> SUSv2 guarantees that &quot;Host names are limited to 255 bytes&quot;. POSIX.1 guarantees that &quot;Host names (not including the terminating null byte) are limited to <code>HOST_NAME_MAX</code> bytes&quot;. On Linux, <code>HOST_NAME_MAX</code> is defined with the value 64, which has been the limit since Linux 1.0 (earlier kernels imposed a limit of 8 bytes).</p>
<h3>C library/kernel differences</h3>
<p> The GNU C library does not employ the <code>gethostname</code>() system call; instead, it implements <code>gethostname</code>() as a library function that calls <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2) and copies up to <i>len</i> bytes from the returned <i>nodename</i> field into <i>name</i>. Having performed the copy, the function then checks if the length of the <i>nodename</i> was greater than or equal to <i>len</i>, and if it is, then the function returns -1 with <i>errno</i> set to <code>ENAMETOOLONG</code>; in this case, a terminating null byte is not included in the returned <i>name</i>. </p>
<p> Versions of glibc before 2.2 handle the case where the length of the <i>nodename</i> was greater than or equal to <i>len</i> differently: nothing is copied into <i>name</i> and the function returns -1 with <i>errno</i> set to <code>ENAMETOOLONG</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-hostname/">hostname</a></code>(1), <code><a href="/docs/linux/man/2-getdomainname/">getdomainname</a></code>(2), <code><a href="/docs/linux/man/2-setdomainname/">setdomainname</a></code>(2), <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2), <code><a href="/docs/linux/man/7-uts_namespaces/">uts_namespaces</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
