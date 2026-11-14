---
title: "setdomainname(2)"
name: "setdomainname"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setdomainname/"
description: "getdomainname, setdomainname – get/set NIS domain name"
---

<h2 class="name">NAME</h2>
<p> getdomainname, setdomainname &#8211; get/set NIS domain name </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int getdomainname(char *</code><i>name</i><code>, size_t </code><i>len</i><code>);</code><br />
 <code>int setdomainname(const char *</code><i>name</i><code>, size_t </code><i>len</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getdomainname</code>(), <code>setdomainname</code>(): </p>
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
<p> These functions are used to access or to change the NIS domain name of the host system. More precisely, they operate on the NIS domain name associated with the calling process&#8217;s UTS namespace. </p>
<p> <code>setdomainname</code>() sets the domain name to the value given in the character array <i>name</i>. The <i>len</i> argument specifies the number of bytes in <i>name</i>. (Thus, <i>name</i> does not require a terminating null byte.) </p>
<p> <code>getdomainname</code>() returns the null-terminated domain name in the character array <i>name</i>, which has a length of <i>len</i> bytes. If the null-terminated domain name requires more than <i>len</i> bytes, <code>getdomainname</code>() returns the first <i>len</i> bytes (glibc) or gives an error (libc).</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> <code>setdomainname</code>() can fail with the following errors:</p>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>name</i> pointed outside of user address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>len</i> was negative or too large.</p>
<dt><code>EPERM</code></p>
<dd> The caller did not have the <code>CAP_SYS_ADMIN</code> capability in the user namespace associated with its UTS namespace (see <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7)).</dl>
<p> <code>getdomainname</code>() can fail with the following errors:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> For <code>getdomainname</code>() under libc: <i>name</i> is NULL or <i>name</i> is longer than <i>len</i> bytes.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX does not specify these calls.</p>
<h2>NOTES</h2>
<p> Since Linux 1.0, the limit on the length of a domain name, including the terminating null byte, is 64 bytes. In older kernels, it was 8 bytes. </p>
<p> On most Linux architectures (including x86), there is no <code>getdomainname</code>() system call; instead, glibc implements <code>getdomainname</code>() as a library function that returns a copy of the <i>domainname</i> field returned from a call to <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2), <code><a href="/docs/linux/man/2-sethostname/">sethostname</a></code>(2), <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2), <code><a href="/docs/linux/man/7-uts_namespaces/">uts_namespaces</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
