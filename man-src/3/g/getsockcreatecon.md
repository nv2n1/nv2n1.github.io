---
title: "getsockcreatecon(3)"
name: "getsockcreatecon"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getsockcreatecon/"
description: "getsockcreatecon, setsockcreatecon – get or set the SELinux security context used for creating a new labeled sockets"
---

<h2 class="name">NAME</h2>
<p> getsockcreatecon, setsockcreatecon &#8211; get or set the SELinux security context used for creating a new labeled sockets </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>int getsockcreatecon(char **</code><i>con</i><code>);</code> </p>
<p> <code>int getsockcreatecon_raw(char **</code><i>con</i><code>);</code> </p>
<p> <code>int setsockcreatecon(char *</code><i>context</i><code>);</code> </p>
<p> <code>int setsockcreatecon_raw(char *</code><i>context</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>getsockcreatecon</code>() retrieves the context used for creating a new labeled network socket. This returned context should be freed with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3) if non-NULL. <code>getsockcreatecon</code>() sets *con to NULL if no sockcreate context has been explicitly set by the program (i.e. using the default policy behavior). </p>
<p> <code>setsockcreatecon</code>() sets the context used for creating a new labeled network sockets NULL can be passed to <code>setsockcreatecon</code>() to reset to the default policy behavior. The sockcreate context is automatically reset after the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), so a program doesn&#8217;t need to explicitly sanitize it upon startup. </p>
<p> <code>setsockcreatecon</code>() can be applied prior to library functions that internally perform an file creation, in order to set an file context on the objects. </p>
<p> <code>getsockcreatecon_raw</code>() and <code>setsockcreatecon_raw</code>() behave identically to their non-raw counterparts but do not perform context translation. </p>
<p> <code>Note:</code> Signal handlers that perform a <code>setsockcreatecon</code>() must take care to save, reset, and restore the sockcreate context to avoid unexpected behavior. </p>
<p> <code>Note:</code> Contexts are thread specific. </p>
<h2>RETURN VALUE</h2>
<p> On error -1 is returned. On success 0 is returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-getcon/">getcon</a></code>(3) </p>
<h2>Index</h2>
