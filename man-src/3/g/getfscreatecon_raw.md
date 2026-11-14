---
title: "getfscreatecon_raw(3)"
name: "getfscreatecon_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getfscreatecon_raw/"
description: "getfscreatecon, setfscreatecon – get or set the SELinux security context used for creating a new file system object"
---

<h2 class="name">NAME</h2>
<p> getfscreatecon, setfscreatecon &#8211; get or set the SELinux security context used for creating a new file system object </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>int getfscreatecon(char **</code><i>con</i><code>);</code> </p>
<p> <code>int getfscreatecon_raw(char **</code><i>con</i><code>);</code> </p>
<p> <code>int setfscreatecon(char *</code><i>context</i><code>);</code> </p>
<p> <code>int setfscreatecon_raw(char *</code><i>context</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>getfscreatecon</code>() retrieves the context used for creating a new file system object. This returned context should be freed with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3) if non-NULL. <code>getfscreatecon</code>() sets *con to NULL if no fscreate context has been explicitly set by the program (i.e. using the default policy behavior). </p>
<p> <code>setfscreatecon</code>() sets the context used for creating a new file system object. NULL can be passed to <code>setfscreatecon</code>() to reset to the default policy behavior. The fscreate context is automatically reset after the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), so a program doesn&#8217;t need to explicitly sanitize it upon startup. </p>
<p> <code>setfscreatecon</code>() can be applied prior to library functions that internally perform an file creation, in order to set an file context on the objects. </p>
<p> <code>getfscreatecon_raw</code>() and <code>setfscreatecon_raw</code>() behave identically to their non-raw counterparts but do not perform context translation. </p>
<p> <code>Note:</code> Signal handlers that perform a <code>setfscreatecon</code>() must take care to save, reset, and restore the fscreate context to avoid unexpected behavior. </p>
<p> <code>Note:</code> Contexts are thread specific. </p>
<h2>RETURN VALUE</h2>
<p> On error -1 is returned. On success 0 is returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-getcon/">getcon</a></code>(3), <code><a href="/docs/linux/man/3-getexeccon/">getexeccon</a></code>(3) </p>
<h2>Index</h2>
