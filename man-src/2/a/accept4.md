---
title: "accept4(2)"
name: "accept4"
section: "2"
letter: "a"
url: "/docs/linux/man/2-accept4/"
description: "accept, accept4 – accept a connection on a socket"
---

<h2 class="name">NAME</h2>
<p> accept, accept4 &#8211; accept a connection on a socket </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt; /* See NOTES */
int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;sys/socket.h&gt;
int accept4(int sockfd, struct sockaddr *addr,
            socklen_t *addrlen, int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>accept</code>() system call is used with connection-based socket types (<code>SOCK_STREAM</code>, <code>SOCK_SEQPACKET</code>). It extracts the first connection request on the queue of pending connections for the listening socket, <i>sockfd</i>, creates a new connected socket, and returns a new file descriptor referring to that socket. The newly created socket is not in the listening state. The original socket <i>sockfd</i> is unaffected by this call. </p>
<p> The argument <i>sockfd</i> is a socket that has been created with <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), bound to a local address with <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), and is listening for connections after a <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2). </p>
<p> The argument <i>addr</i> is a pointer to a <i>sockaddr</i> structure. This structure is filled in with the address of the peer socket, as known to the communications layer. The exact format of the address returned <i>addr</i> is determined by the socket&#8217;s address family (see <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) and the respective protocol man pages). When <i>addr</i> is NULL, nothing is filled in; in this case, <i>addrlen</i> is not used, and should also be NULL. </p>
<p> The <i>addrlen</i> argument is a value-result argument: the caller must initialize it to contain the size (in bytes) of the structure pointed to by <i>addr</i>; on return it will contain the actual size of the peer address. </p>
<p> The returned address is truncated if the buffer provided is too small; in this case, <i>addrlen</i> will return a value greater than was supplied to the call. </p>
<p> If no pending connections are present on the queue, and the socket is not marked as nonblocking, <code>accept</code>() blocks the caller until a connection is present. If the socket is marked nonblocking and no pending connections are present on the queue, <code>accept</code>() fails with the error <code>EAGAIN</code> or <code>EWOULDBLOCK</code>. </p>
<p> In order to be notified of incoming connections on a socket, you can use <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), or <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). A readable event will be delivered when a new connection is attempted and you may then call <code>accept</code>() to get a socket for that connection. Alternatively, you can set the socket to deliver <code>SIGIO</code> when activity occurs on a socket; see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) for details. </p>
<p> If <i>flags</i> is 0, then <code>accept4</code>() is the same as <code>accept</code>(). The following values can be bitwise ORed in <i>flags</i> to obtain different behavior:</p>
<dl>
<dt><code>SOCK_NONBLOCK</code></p>
<dd> Set the <code>O_NONBLOCK</code> file status flag on the open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) referred to by the new file descriptor. Using this flag saves extra calls to <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) to achieve the same result.</p>
<dt><code>SOCK_CLOEXEC</code></p>
<dd> Set the close-on-exec (<code>FD_CLOEXEC</code>) flag on the new file descriptor. See the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful.</dl>
<h2>RETURN VALUE</h2>
<p> On success, these system calls return a file descriptor for the accepted socket (a nonnegative integer). On error, -1 is returned, <i>errno</i> is set appropriately, and <i>addrlen</i> is left unchanged.</p>
<h3>Error handling</h3>
<p> Linux <code>accept</code>() (and <code>accept4</code>()) passes already-pending network errors on the new socket as an error code from <code>accept</code>(). This behavior differs from other BSD socket implementations. For reliable operation the application should detect the network errors defined for the protocol after <code>accept</code>() and treat them like <code>EAGAIN</code> by retrying. In the case of TCP/IP, these are <code>ENETDOWN</code>, <code>EPROTO</code>, <code>ENOPROTOOPT</code>, <code>EHOSTDOWN</code>, <code>ENONET</code>, <code>EHOSTUNREACH</code>, <code>EOPNOTSUPP</code>, and <code>ENETUNREACH</code>.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EAGAIN</code> or <code>EWOULDBLOCK</code></p>
<dd> The socket is marked nonblocking and no connections are present to be accepted. POSIX.1-2001 and POSIX.1-2008 allow either error to be returned for this case, and do not require these constants to have the same value, so a portable application should check for both possibilities.</p>
<dt><code>EBADF</code></p>
<dd> <i>sockfd</i> is not an open file descriptor.</p>
<dt><code>ECONNABORTED</code></p>
<dd> A connection has been aborted.</p>
<dt><code>EFAULT</code></p>
<dd> The <i>addr</i> argument is not in a writable part of the user address space.</p>
<dt><code>EINTR</code></p>
<dd> The system call was interrupted by a signal that was caught before a valid connection arrived; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> Socket is not listening for connections, or <i>addrlen</i> is invalid (e.g., is negative).</p>
<dt><code>EINVAL</code></p>
<dd> (<code>accept4</code>()) invalid value in <i>flags</i>.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOBUFS</code>, <code>ENOMEM</code></p>
<dd> Not enough free memory. This often means that the memory allocation is limited by the socket buffer limits, not by the system memory.</p>
<dt><code>ENOTSOCK</code></p>
<dd> The file descriptor <i>sockfd</i> does not refer to a socket.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> The referenced socket is not of type <code>SOCK_STREAM</code>.</p>
<dt><code>EPROTO</code></p>
<dd> Protocol error.</dl>
<p> In addition, Linux <code>accept</code>() may fail if:</p>
<dl>
<dt><code>EPERM</code></p>
<dd> Firewall rules forbid connection.</dl>
<p> In addition, network errors for the new socket and as defined for the protocol may be returned. Various Linux kernels can return other errors such as <code>ENOSR</code>, <code>ESOCKTNOSUPPORT</code>, <code>EPROTONOSUPPORT</code>, <code>ETIMEDOUT</code>. The value <code>ERESTARTSYS</code> may be seen during a trace.</p>
<h2>VERSIONS</h2>
<p> The <code>accept4</code>() system call is available starting with Linux 2.6.28; support in glibc is available starting with version 2.10.</p>
<h2>CONFORMING TO</h2>
<p> <code>accept</code>(): POSIX.1-2001, POSIX.1-2008, SVr4, 4.4BSD (<code>accept</code>() first appeared in 4.2BSD). </p>
<p> <code>accept4</code>() is a nonstandard Linux extension. </p>
<p> On Linux, the new socket returned by <code>accept</code>() does <i>not</i> inherit file status flags such as <code>O_NONBLOCK</code> and <code>O_ASYNC</code> from the listening socket. This behavior differs from the canonical BSD sockets implementation. Portable programs should not rely on inheritance or noninheritance of file status flags and always explicitly set all required flags on the socket returned from <code>accept</code>().</p>
<h2>NOTES</h2>
<p> POSIX.1-2001 does not require the inclusion of <i>&lt;sys/types.h&gt;</i>, and this header file is not required on Linux. However, some historical (BSD) implementations required this header file, and portable applications are probably wise to include it. </p>
<p> There may not always be a connection waiting after a <code>SIGIO</code> is delivered or <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), or <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) return a readability event because the connection might have been removed by an asynchronous network error or another thread before <code>accept</code>() is called. If this happens, then the call will block waiting for the next connection to arrive. To ensure that <code>accept</code>() never blocks, the passed socket <i>sockfd</i> needs to have the <code>O_NONBLOCK</code> flag set (see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7)). </p>
<p> For certain protocols which require an explicit confirmation, such as DECnet, <code>accept</code>() can be thought of as merely dequeuing the next connection request and not implying confirmation. Confirmation can be implied by a normal read or write on the new file descriptor, and rejection can be implied by closing the new socket. Currently, only DECnet has these semantics on Linux.</p>
<h3>The socklen_t type</h3>
<p> In the original BSD sockets implementation (and on other older systems) the third argument of <code>accept</code>() was declared as an <i>int&nbsp;*</i>. A POSIX.1g draft standard wanted to change it into a <i>size_t&nbsp;*</i>C; later POSIX standards and glibc 2.x have <i>socklen_t&nbsp;* .</i></p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
