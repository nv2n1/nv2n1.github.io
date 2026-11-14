---
title: "ares_getsock(3)"
name: "ares_getsock"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_getsock/"
description: "ares_getsock – get socket descriptors to wait on"
---

<h2>NAME</h2>
<p> ares_getsock &#8211; get socket descriptors to wait on</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_getsock(ares_channel channel, ares_socket_t *socks,
                 int numsocks);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_getsock</code> function retrieves the set of socket descriptors which the calling application should wait on for reading and/or writing for the processing of name service queries pending on the name service channel identified by <i>channel</i>. Socket descriptors will be set in the socket descriptor array pointed to by <i>socks</i>. <i>numsocks</i> is the size of the given array in number of ints. </p>
<p> This function can only return information about up to 16 sockets. If more are in use (however unlikely that is), they are simply not reported back.</p>
<h2>RETURN VALUES</h2>
<p> <code>ares_getsock</code> returns a bitmask for what actions to wait for on the different sockets. The ares.h header file provides these convenience macros to extract the information appropriately: </p>
<pre><code>
#define ARES_GETSOCK_MAXNUM 16 /* ares_getsock() can return info about \
                                  this many sockets */
#define ARES_GETSOCK_READABLE(bits, num) (bits &amp; (1 &lt;&lt; (num)))
#define ARES_GETSOCK_WRITABLE(bits, num) (bits &amp; (1 &lt;&lt; ((num) + ARES_GETSOCK_MAXNUM)))
</code></pre>
<h2>NOTES</h2>
<p> This function was added in c-ares 1.3.1</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_timeout/">ares_timeout</a></code>(3), <code><a href="/docs/linux/man/3-ares_fds/">ares_fds</a></code>(3), <code><a href="/docs/linux/man/3-ares_process/">ares_process</a></code>(3) </p>
<h2>Index</h2>
