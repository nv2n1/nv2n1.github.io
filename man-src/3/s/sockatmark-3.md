---
title: "sockatmark-3(3)"
name: "sockatmark-3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sockatmark-3/"
description: "sockatmark – determine whether socket is at out-of-band mark"
---

<p>sockatmark &#8211; determine whether socket is at out-of-band mark</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;
int sockatmark(int sockfd);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>sockatmark</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</p>
<h2>Description</h2>
<p><code>sockatmark</code>() returns a value indicating whether or not the socket referred to by the file descriptor <i>sockfd</i> is at the out-of-band mark. If the socket is at the mark, then 1 is returned; if the socket is not at the mark, 0 is returned. This function does not remove the out-of-band mark.</p>
<h2>Return Value</h2>
<p>A successful call to <code>sockatmark</code>() returns 1 if the socket is at the out-of-band mark, or 0 if it is not. On error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EBADF</code></p>
<dd><i>sockfd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd><i>sockfd</i> is not a file descriptor to which <code>sockatmark</code>() can be applied.</dl>
<h2>Versions</h2>
<p><code>sockatmark</code>() was added to glibc in version 2.2.4.</p>
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
<td> <code>sockatmark</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>If <code>sockatmark</code>() returns 1, then the out-of-band data can be read using the <code>MSG_OOB</code> flag of <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2). </p>
<p> Out-of-band data is supported only on some stream socket protocols. </p>
<p> <code>sockatmark</code>() can safely be called from a handler for the <code>SIGURG</code> signal. </p>
<p> <code>sockatmark</code>() is implemented using the <code>SIOCATMARK</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation.</p>
<h2>Bugs</h2>
<p>Prior to glibc 2.4, <code>sockatmark</code>() did not work.</p>
<h2>Examples</h2>
<p>The following code can be used after receipt of a <code>SIGURG</code> signal to read (and discard) all data up to the mark, and then read the byte of data at the mark: </p>
<pre><code>char buf[BUF_LEN];
char oobdata;
int atmark, s;
for (;;) {
    atmark = sockatmark(sockfd);
    if (atmark == -1) {
        perror(&quot;sockatmark&quot;);
        break;
    }
    if (atmark)
        break;
    s = read(sockfd, buf, BUF_LEN);
    if (s == -1)
        perror(&quot;read&quot;);
    if (s &lt;= 0)
        break;
}
if (atmark == 1) {
    if (recv(sockfd, &amp;oobdata, 1, MSG_OOB) == -1) {
        perror(&quot;recv&quot;);
        ...
    }
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), <code><a href="/docs/linux/man/2-send/">send</a></code>(2), <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
