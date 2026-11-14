---
title: "bind(2)"
name: "bind"
section: "2"
letter: "b"
url: "/docs/linux/man/2-bind/"
description: "bind – bind a name to a socket"
---

<h2 class="name">NAME</h2>
<p> bind &#8211; bind a name to a socket </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt; /* See NOTES */
int bind(int sockfd, const struct sockaddr *addr,
         socklen_t addrlen);
</code></pre>
<h2>DESCRIPTION</h2>
<p> When a socket is created with <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), it exists in a name space (address family) but has no address assigned to it. <code>bind</code>() assigns the address specified by <i>addr</i> to the socket referred to by the file descriptor <i>sockfd</i>. <i>addrlen</i> specifies the size, in bytes, of the address structure pointed to by <i>addr</i>. Traditionally, this operation is called &#8220;assigning a name to a socket&#8221;. </p>
<p> It is normally necessary to assign a local address using <code>bind</code>() before a <code>SOCK_STREAM</code> socket may receive connections (see <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2)). </p>
<p> The rules used in name binding vary between address families. Consult the manual entries in Section 7 for detailed information. For <code>AF_INET</code>, see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7); for <code>AF_INET6</code>, see <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7); for <code>AF_UNIX</code>, see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7); for <code>AF_APPLETALK</code>, see <code><a href="/docs/linux/man/7-ddp/">ddp</a></code>(7); for <code>AF_PACKET</code>, see <code><a href="/docs/linux/man/7-packet/">packet</a></code>(7); for <code>AF_X25</code>, see <code><a href="/docs/linux/man/7-x25/">x25</a></code>(7); and for <code>AF_NETLINK</code>, see <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7). </p>
<p> The actual structure passed for the <i>addr</i> argument will depend on the address family. The <i>sockaddr</i> structure is defined as something like: </p>
<p> struct sockaddr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sa_family_t sa_family;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sa_data[14]; } </p>
<p> The only purpose of this structure is to cast the structure pointer passed in <i>addr</i> in order to avoid compiler warnings. See EXAMPLES below.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> The address is protected, and the user is not the superuser.</p>
<dt><code>EADDRINUSE</code></p>
<dd> The given address is already in use.</p>
<dt><code>EADDRINUSE</code></p>
<dd> (Internet domain sockets) The port number was specified as zero in the socket address structure, but, upon attempting to bind to an ephemeral port, it was determined that all port numbers in the ephemeral port range are currently in use. See the discussion of <i>/proc/sys/net/ipv4/ip_local_port_range</i> <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7).</p>
<dt><code>EBADF</code></p>
<dd> <i>sockfd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> The socket is already bound to an address.</p>
<dt><code>EINVAL</code></p>
<dd> <i>addrlen</i> is wrong, or <i>addr</i> is not a valid address for this socket&#8217;s domain.</p>
<dt><code>ENOTSOCK</code></p>
<dd> The file descriptor <i>sockfd</i> does not refer to a socket.</dl>
<p> The following errors are specific to UNIX domain (<code>AF_UNIX</code>) sockets:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> Search permission is denied on a component of the path prefix. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EADDRNOTAVAIL</code></p>
<dd> A nonexistent interface was requested or the requested address was not local.</p>
<dt><code>EFAULT</code></p>
<dd> <i>addr</i> points outside the user&#8217;s accessible address space.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>addr</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>addr</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd> A component in the directory prefix of the socket pathname does not exist.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component of the path prefix is not a directory.</p>
<dt><code>EROFS</code></p>
<dd> The socket inode would reside on a read-only filesystem.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.4BSD (<code>bind</code>() first appeared in 4.2BSD).</p>
<h2>NOTES</h2>
<p> POSIX.1 does not require the inclusion of <i>&lt;sys/types.h&gt;</i>, and this header file is not required on Linux. However, some historical (BSD) implementations required this header file, and portable applications are probably wise to include it. </p>
<p> For background on the <i>socklen_t</i> type, see <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2).</p>
<h2>BUGS</h2>
<p> The transparent proxy options are not described.</p>
<h2>EXAMPLES</h2>
<p> An example of the use of <code>bind</code>() with Internet domain sockets can be found in <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3). </p>
<p> The following example shows how to bind a stream socket in the UNIX (<code>AF_UNIX</code>) domain, and accept connections: </p>
<p> #include &lt;sys/socket.h&gt; #include &lt;sys/un.h&gt; #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;string.h&gt; </p>
<p> #define MY_SOCK_PATH &quot;/somepath&quot; #define LISTEN_BACKLOG 50 </p>
<p> #define handle_error(msg) \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;perror(msg);&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int sfd, cfd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sockaddr_un my_addr, peer_addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;socklen_t peer_addr_size; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sfd&nbsp;=&nbsp;socket(AF_UNIX, SOCK_STREAM, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sfd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;socket&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(&amp;my_addr, 0, sizeof(my_addr));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Clear structure&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;my_addr.sun_family&nbsp;=&nbsp;AF_UNIX;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strncpy(my_addr.sun_path, MY_SOCK_PATH,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(my_addr.sun_path)&nbsp;&#8211; 1); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(bind(sfd,&nbsp;(struct sockaddr&nbsp;*)&nbsp;&amp;my_addr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sizeof(my_addr))&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;bind&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(listen(sfd, LISTEN_BACKLOG)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;listen&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Now we can accept incoming connections one<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;at a time using&nbsp;<a href="/docs/linux/man/2-accept/">accept</a>(2)&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;peer_addr_size&nbsp;=&nbsp;sizeof(peer_addr);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cfd&nbsp;=&nbsp;accept(sfd,&nbsp;(struct sockaddr&nbsp;*)&nbsp;&amp;peer_addr,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&amp;peer_addr_size);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(cfd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;accept&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Code to deal with incoming connection(s)&#8230;&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;When no longer required, the socket pathname, MY_SOCK_PATH<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;should be deleted using&nbsp;<a href="/docs/linux/man/2-unlink/">unlink</a>(2)&nbsp;or&nbsp;<a href="/docs/linux/man/3-remove/">remove</a>(3)&nbsp;*/ }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-getsockname/">getsockname</a></code>(2), <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3), <code><a href="/docs/linux/man/3-getifaddrs/">getifaddrs</a></code>(3), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
