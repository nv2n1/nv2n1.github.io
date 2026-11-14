---
title: "sd_is_special(3)"
name: "sd_is_special"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sd_is_special/"
description: "sd_is_fifo, sd_is_socket, sd_is_socket_inet, sd_is_socket_unix, sd_is_mq, sd_is_special – Check the type of a file descriptor"
---

<p>sd_is_fifo, sd_is_socket, sd_is_socket_inet, sd_is_socket_unix, sd_is_mq, sd_is_special &#8211; Check the type of a file descriptor</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;systemd/sd-daemon.h&gt;

int sd_is_fifo(int fd, const char *path);

int sd_is_socket(int fd, int family, int type, int listening);

int sd_is_socket_inet(int fd, int family, int type, int listening, uint16_t port);

int sd_is_socket_unix(int fd, int type, int listening, const char *path, size_t length);

int sd_is_mq(int fd, const char *path);

int sd_is_special(int fd, const char *path);</code></pre>
<h2>Description</h2>
<p><code>sd_is_fifo()</code></p>
<dd>may be called to check whether the specified file descriptor refers to a FIFO or pipe. If the <i>path</i> parameter is not <code>NULL</code>, it is checked whether the FIFO is bound to the specified file system path. </p>
<p> <code>sd_is_socket()</code> may be called to check whether the specified file descriptor refers to a socket. If the <i>family</i> parameter is not <code>AF_UNSPEC</code>, it is checked whether the socket is of the specified family (AF_UNIX, <code>AF_INET</code>, &#8230;). If the <i>type</i> parameter is not 0, it is checked whether the socket is of the specified type (<code>SOCK_STREAM</code>, <code>SOCK_DGRAM</code>, &#8230;). If the <i>listening</i> parameter is positive, it is checked whether the socket is in accepting mode, i.e. <code>listen()</code> has been called for it. If <i>listening</i> is 0, it is checked whether the socket is not in this mode. If the parameter is negative, no such check is made. The <i>listening</i> parameter should only be used for stream sockets and should be set to a negative value otherwise. </p>
<p> <code>sd_is_socket_inet()</code> is similar to <code>sd_is_socket()</code>, but optionally checks the IPv4 or IPv6 port number the socket is bound to, unless <i>port</i> is zero. For this call <i>family</i> must be passed as either <code>AF_UNSPEC</code>, <code>AF_INET</code>, or <code>AF_INET6</code>. </p>
<p> <code>sd_is_socket_unix()</code> is similar to <code>sd_is_socket()</code> but optionally checks the <code>AF_UNIX</code> path the socket is bound to, unless the <i>path</i> parameter is <code>NULL</code>. For normal file system <code>AF_UNIX</code> sockets, set the <i>length</i> parameter to 0. For Linux abstract namespace sockets, set the <i>length</i> to the size of the address, including the initial 0 byte, and set the <i>path</i> to the initial 0 byte of the socket address. </p>
<p> <code>sd_is_mq()</code> may be called to check whether the specified file descriptor refers to a POSIX message queue. If the <i>path</i> parameter is not <code>NULL</code>, it is checked whether the message queue is bound to the specified name. </p>
<p> <code>sd_is_special()</code> may be called to check whether the specified file descriptor refers to a special file. If the <i>path</i> parameter is not <code>NULL</code>, it is checked whether the file descriptor is bound to the specified file name. Special files in this context are character device nodes and files in /proc or /sys.</p>
<h2>Return Value</h2>
<p>On failure, these calls return a negative errno-style error code. If the file descriptor is of the specified type and bound to the specified address, a positive return value is returned, otherwise zero.</p>
<h2>Notes</h2>
<p>These APIs are implemented as a shared library, which can be compiled and linked to with the <code>libsystemd</code>&nbsp;<wbr><code><a href="/docs/linux/man/1-pkg-config/">pkg-config</a></code>(1) file. </p>
<p> Internally, these function use a combination of fstat() and getsockname() to check the file descriptor type and where it is bound to.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/3-sd-daemon/">sd-daemon</a></code>(3), <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5) </p>
