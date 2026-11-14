---
title: "getpeereid(3)"
name: "getpeereid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getpeereid/"
description: "getpeereid – get the effective credentials of a UNIX-domain peer"
---

<h2 class="name">NAME</h2>
<p> <code>getpeereid</code> &#8211; get the effective credentials of a UNIX-domain peer </p>
<h2>LIBRARY</h2>
<p> Lb libbsd</p>
<h2>SYNOPSIS</h2>
<p> In sys/types.h In bsd/unistd.h Ft int Fn getpeereid int s uid_t *euid gid_t *egid</p>
<h2>DESCRIPTION</h2>
<p> The Fn getpeereid function returns the effective user and group IDs of the peer connected to a UNIX socket. The argument Fa s must be a UNIX socket (<a href="/docs/linux/man/4-unix/">unix</a>(4) ) of type <code>SOCK_STREAM</code> on which either <a href="/docs/linux/man/2-connect/">connect</a>(2) or <a href="/docs/linux/man/2-listen/">listen</a>(2) have been called. The effective used ID is placed in Fa euid , and the effective group ID in Fa egid . </p>
<p> The credentials returned to the <a href="/docs/linux/man/2-listen/">listen</a>(2) caller are those of its peer at the time it called <a href="/docs/linux/man/2-connect/">connect</a>(2); the credentials returned to the <a href="/docs/linux/man/2-connect/">connect</a>(2) caller are those of its peer at the time it called <a href="/docs/linux/man/2-listen/">listen</a>(2). This mechanism is reliable; there is no way for either side to influence the credentials returned to its peer except by calling the appropriate system call (i.e., either <a href="/docs/linux/man/2-connect/">connect</a>(2) or <a href="/docs/linux/man/2-listen/">listen</a>(2)) under different effective credentials. </p>
<p> One common use of this routine is for a UNIX server to verify the credentials of its client. Likewise, the client can verify the credentials of the server.</p>
<h2>IMPLEMENTATION NOTES</h2>
<p> On Fx , Fn getpeereid is implemented in terms of the <code>LOCAL_PEERCRED</code> <a href="/docs/linux/man/4-unix/">unix</a>(4) socket option.</p>
<h2>RETURN VALUES</h2>
<p> Rv -std getpeereid</p>
<h2>ERRORS</h2>
<p> The Fn getpeereid function fails if:</p>
<dl>
<dt><code>Bq </code>Er EBADF</p>
<dd> The argument Fa s is not a valid descriptor.</p>
<dt><code>Bq </code>Er ENOTSOCK</p>
<dd> The argument Fa s is a file, not a socket.</p>
<dt><code>Bq </code>Er ENOTCONN</p>
<dd> The argument Fa s does not refer to a socket on which <a href="/docs/linux/man/2-connect/">connect</a>(2) or <a href="/docs/linux/man/2-listen/">listen</a>(2) have been called.</p>
<dt><code>Bq </code>Er EINVAL</p>
<dd> The argument Fa s does not refer to a socket of type <code>SOCK_STREAM</code> or the kernel returned invalid data.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-connect/">connect</a>(2), <a href="/docs/linux/man/2-getpeername/">getpeername</a>(2), <a href="/docs/linux/man/2-getsockname/">getsockname</a>(2), <a href="/docs/linux/man/2-getsockopt/">getsockopt</a>(2), <a href="/docs/linux/man/2-listen/">listen</a>(2), <a href="/docs/linux/man/4-unix/">unix</a>(4)</p>
<h2>HISTORY</h2>
<p> The Fn getpeereid function appeared in Fx 4.6 . </p>
<h2>Index</h2>
