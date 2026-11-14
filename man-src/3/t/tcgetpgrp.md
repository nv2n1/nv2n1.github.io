---
title: "tcgetpgrp(3)"
name: "tcgetpgrp"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcgetpgrp/"
description: "tcgetpgrp, tcsetpgrp – get and set terminal foreground process group"
---

<p>tcgetpgrp, tcsetpgrp &#8211; get and set terminal foreground process group</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;unistd.h&gt;</code></pre>
<p> <code>pid_t tcgetpgrp(int </code><i>fd</i><code>);</code> </p>
<pre><code>int tcsetpgrp(int fd, pid_t pgrp);</code></pre>
<h2>Description</h2>
<p>The function <code>tcgetpgrp</code>() returns the process group ID of the foreground process group on the terminal associated to <i>fd</i>, which must be the controlling terminal of the calling process. </p>
<p> The function <code>tcsetpgrp</code>() makes the process group with process group ID <i>pgrp</i> the foreground process group on the terminal associated to <i>fd</i>, which must be the controlling terminal of the calling process, and still be associated with its session. Moreover, <i>pgrp</i> must be a (nonempty) process group belonging to the same session as the calling process. </p>
<p> If <code>tcsetpgrp</code>() is called by a member of a background process group in its session, and the calling process is not blocking or ignoring <code>SIGTTOU</code>, a <code>SIGTTOU</code> signal is sent to all members of this background process group.</p>
<h2>Return Value</h2>
<p>When <i>fd</i> refers to the controlling terminal of the calling process, the function <code>tcgetpgrp</code>() will return the foreground process group ID of that terminal if there is one, and some value larger than 1 that is not presently a process group ID otherwise. When <i>fd</i> does not refer to the controlling terminal of the calling process, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> When successful, <code>tcsetpgrp</code>() returns 0. Otherwise, it returns -1, and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>EBADF</code></p>
<dd><i>fd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd><i>pgrp</i> has an unsupported value.</p>
<dt><code>ENOTTY</code></p>
<dd>The calling process does not have a controlling terminal, or it has one but it is not described by <i>fd</i>, or, for <code>tcsetpgrp</code>(), this controlling terminal is no longer associated with the session of the calling process.</p>
<dt><code>EPERM</code></p>
<dd><i>pgrp</i> has a supported value, but is not the process group ID of a process in the same session as the calling process.</dl>
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
<td> <code>tcgetpgrp</code>(), <code>tcsetpgrp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>These functions are implemented via the <code>TIOCGPGRP</code> and <code>TIOCSPGRP</code> ioctls.</p>
<h3>History</h3>
<p>The ioctls appeared in 4.2BSD. The functions are POSIX inventions.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-setpgid/">setpgid</a></code>(2), <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
