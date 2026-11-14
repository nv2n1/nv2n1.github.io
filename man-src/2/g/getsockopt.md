---
title: "getsockopt(2)"
name: "getsockopt"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getsockopt/"
description: "getsockopt, setsockopt – get and set options on sockets"
---

<h2 class="name">NAME</h2>
<p> getsockopt, setsockopt &#8211; get and set options on sockets </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt; /* See NOTES */
int getsockopt(int sockfd, int level, int optname,
               void *optval, socklen_t *optlen);
int setsockopt(int sockfd, int level, int optname,
               const void *optval, socklen_t optlen);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>getsockopt</code>() and <code>setsockopt</code>() manipulate options for the socket referred to by the file descriptor <i>sockfd</i>. Options may exist at multiple protocol levels; they are always present at the uppermost socket level. </p>
<p> When manipulating socket options, the level at which the option resides and the name of the option must be specified. To manipulate options at the sockets API level, <i>level</i> is specified as <code>SOL_SOCKET</code>. To manipulate options at any other level the protocol number of the appropriate protocol controlling the option is supplied. For example, to indicate that an option is to be interpreted by the <code>TCP</code> protocol, <i>level</i> should be set to the protocol number of <code>TCP</code>; see <code><a href="/docs/linux/man/3-getprotoent/">getprotoent</a></code>(3). </p>
<p> The arguments <i>optval</i> and <i>optlen</i> are used to access option values for <code>setsockopt</code>(). For <code>getsockopt</code>() they identify a buffer in which the value for the requested option(s) are to be returned. For <code>getsockopt</code>(), <i>optlen</i> is a value-result argument, initially containing the size of the buffer pointed to by <i>optval</i>, and modified on return to indicate the actual size of the value returned. If no option value is to be supplied or returned, <i>optval</i> may be NULL. </p>
<p> <i>Optname</i> and any specified options are passed uninterpreted to the appropriate protocol module for interpretation. The include file <i>&lt;sys/socket.h&gt;</i> contains definitions for socket level options, described below. Options at other protocol levels vary in format and name; consult the appropriate entries in section 4 of the manual. </p>
<p> Most socket-level options utilize an <i>int</i> argument for <i>optval</i>. For <code>setsockopt</code>(), the argument should be nonzero to enable a boolean option, or zero if the option is to be disabled. </p>
<p> For a description of the available socket options see <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7) and the appropriate protocol man pages.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned for the standard options. On error, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> Netfilter allows the programmer to define custom socket options with associated handlers; for such options, the return value on success is the value returned by the handler.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> The argument <i>sockfd</i> is not a valid file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> The address pointed to by <i>optval</i> is not in a valid part of the process address space. For <code>getsockopt</code>(), this error may also be returned if <i>optlen</i> is not in a valid part of the process address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>optlen</i> invalid in <code>setsockopt</code>(). In some cases this error can also occur for an invalid value in <i>optval</i> (e.g., for the <code>IP_ADD_MEMBERSHIP</code> option described in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7)).</p>
<dt><code>ENOPROTOOPT</code></p>
<dd> The option is unknown at the level indicated.</p>
<dt><code>ENOTSOCK</code></p>
<dd> The file descriptor <i>sockfd</i> does not refer to a socket.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.4BSD (these system calls first appeared in 4.2BSD).</p>
<h2>NOTES</h2>
<p> POSIX.1 does not require the inclusion of <i>&lt;sys/types.h&gt;</i>, and this header file is not required on Linux. However, some historical (BSD) implementations required this header file, and portable applications are probably wise to include it. </p>
<p> For background on the <i>socklen_t</i> type, see <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2).</p>
<h2>BUGS</h2>
<p> Several of the socket options should be handled at lower levels of the system.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/3-getprotoent/">getprotoent</a></code>(3), <code><a href="/docs/linux/man/5-protocols/">protocols</a></code>(5), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/7-packet/">packet</a></code>(7), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7), <code><a href="/docs/linux/man/7-udp/">udp</a></code>(7), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
