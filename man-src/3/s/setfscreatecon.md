---
title: "setfscreatecon(3)"
name: "setfscreatecon"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setfscreatecon/"
description: "getfscreatecon, setfscreatecon – get or set the SELinux security context used for creating a new file system object"
---

<p>getfscreatecon, setfscreatecon &#8211; get or set the SELinux security context used for creating a new file system object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int getfscreatecon(char **con);
int getfscreatecon_raw(char **con);
int setfscreatecon(char *context);
int setfscreatecon_raw(char *context);</code></pre>
<h2>Description</h2>
<p><code>getfscreatecon</code>() retrieves the context used for creating a new file system object. This returned context should be freed with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3) if non-NULL. <code>getfscreatecon</code>() sets *con to NULL if no fscreate context has been explicitly set by the program (i.e. using the default policy behavior). <code>setfscreatecon</code>() sets the context used for creating a new file system object. NULL can be passed to <code>setfscreatecon</code>() to reset to the default policy behavior. The fscreate context is automatically reset after the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), so a program doesn&#8217;t need to explicitly sanitize it upon startup. <code>setfscreatecon</code>() can be applied prior to library functions that internally perform an file creation, in order to set an file context on the objects. <code>getfscreatecon_raw</code>() and <code>setfscreatecon_raw</code>() behave identically to their non-raw counterparts but do not perform context translation. <code>Note:</code> Signal handlers that perform a <code>setfscreatecon</code>() must take care to save, reset, and restore the fscreate context to avoid unexpected behavior.<br />
 <code>Note:</code> Contexts are thread specific. </p>
<h2>Return Value</h2>
<p>On error -1 is returned. On success 0 is returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-getcon/">getcon</a></code>(3), <code><a href="/docs/linux/man/3-getexeccon/">getexeccon</a></code>(3) </p>
