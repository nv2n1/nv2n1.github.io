---
title: "bindresvport(3)"
name: "bindresvport"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bindresvport/"
description: "bindresvport – bind a socket to a privileged IP port"
---

<h2 class="name">NAME</h2>
<p> bindresvport &#8211; bind a socket to a privileged IP port </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netinet/in.h&gt;
#include &lt;sys/types.h&gt;
int bindresvport(int sockfd, struct sockaddr_in *sin);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>bindresvport</code>() is used to bind the socket referred to by the file descriptor <i>sockfd</i> to a privileged anonymous IP port, that is, a port number arbitrarily selected from the range 512 to 1023. </p>
<p> If the <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2) performed by <code>bindresvport</code>() is successful, and <i>sin</i> is not NULL, then <i>sin-&gt;sin_port</i> returns the port number actually allocated. </p>
<p> <i>sin</i> can be NULL, in which case <i>sin-&gt;sin_family</i> is implicitly taken to be <code>AF_INET</code>. However, in this case, <code>bindresvport</code>() has no way to return the port number actually allocated. (This information can later be obtained using <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2).)</p>
<h2>RETURN VALUE</h2>
<p> <code>bindresvport</code>() returns 0 on success; otherwise -1 is returned and <i>errno</i> set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<p> <code>bindresvport</code>() can fail for any of the same reasons as <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2). In addition, the following errors may occur:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The calling process was not privileged (on Linux: the calling process did not have the <code>CAP_NET_BIND_SERVICE</code> capability in the user namespace governing its network namespace).</p>
<dt><code>EADDRINUSE</code></p>
<dd> All privileged ports are in use.</p>
<dt><code>EAFNOSUPPORT</code> (<code>EPFNOSUPPORT</code> in glibc 2.7 and earlier)</p>
<dd> <i>sin</i> is not NULL and <i>sin-&gt;sin_family</i> is not <code>AF_INET</code>.</dl>
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
<td> <code>bindresvport</code>() </td>
<td>Thread safety</td>
<td> glibc &gt;= 2.17: MT-Safe<br />
 glibc &lt; 2.17: MT-Unsafe
</td>
</tr>
</table>
<p> The <code>bindresvport</code>() function uses a static variable that was not protected by a lock before glibc 2.17, rendering the function MT-Unsafe.</p>
<h2>CONFORMING TO</h2>
<p> Not in POSIX.1. Present on the BSDs, Solaris, and many other systems.</p>
<h2>NOTES</h2>
<p> Unlike some <code>bindresvport</code>() implementations, the glibc implementation ignores any value that the caller supplies in <i>sin-&gt;sin_port</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
