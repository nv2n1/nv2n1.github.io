---
title: "setsockcreatecon(3)"
name: "setsockcreatecon"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setsockcreatecon/"
description: "getsockcreatecon, setsockcreatecon – get or set the SELinux security context used for creating a new labeled sockets"
---

<p>getsockcreatecon, setsockcreatecon &#8211; get or set the SELinux security context used for creating a new labeled sockets</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int getsockcreatecon(char **con);
int getsockcreatecon_raw(char **con);
int setsockcreatecon(char *context);
int setsockcreatecon_raw(char *context);</code></pre>
<h2>Description</h2>
<p><code>getsockcreatecon</code>() retrieves the context used for creating a new labeled network socket. This returned context should be freed with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3) if non-NULL. <code>getsockcreatecon</code>() sets *con to NULL if no sockcreate context has been explicitly set by the program (i.e. using the default policy behavior). <code>setsockcreatecon</code>() sets the context used for creating a new labeled network sockets NULL can be passed to <code>setsockcreatecon</code>() to reset to the default policy behavior. The sockcreate context is automatically reset after the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), so a program doesn&#8217;t need to explicitly sanitize it upon startup. <code>setsockcreatecon</code>() can be applied prior to library functions that internally perform an file creation, in order to set an file context on the objects. <code>getsockcreatecon_raw</code>() and <code>setsockcreatecon_raw</code>() behave identically to their non-raw counterparts but do not perform context translation. <code>Note:</code> Signal handlers that perform a <code>setsockcreatecon</code>() must take care to save, reset, and restore the sockcreate context to avoid unexpected behavior.<br />
 <code>Note:</code> Contexts are thread specific. </p>
<h2>Return Value</h2>
<p>On error -1 is returned. On success 0 is returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-getcon/">getcon</a></code>(3) </p>
