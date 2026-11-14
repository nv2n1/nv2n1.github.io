---
title: "setkeycreatecon_raw(3)"
name: "setkeycreatecon_raw"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setkeycreatecon_raw/"
description: "getkeycreatecon, setkeycreatecon – get or set the SELinux security context used for creating a new kernel keyrings"
---

<p>getkeycreatecon, setkeycreatecon &#8211; get or set the SELinux security context used for creating a new kernel keyrings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int getkeycreatecon(char **con);
int getkeycreatecon_raw(char **con);
int setkeycreatecon(char *context);
int setkeycreatecon_raw(char *context);</code></pre>
<h2>Description</h2>
<p><code>getkeycreatecon</code>() retrieves the context used for creating a new kernel keyring. This returned context should be freed with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3) if non-NULL. <code>getkeycreatecon</code>() sets *con to NULL if no keycreate context has been explicitly set by the program (i.e. using the default policy behavior). </p>
<p> <code>setkeycreatecon</code>() sets the context used for creating a new kernel keyring. NULL can be passed to <code>setkeycreatecon</code>() to reset to the default policy behavior. The keycreate context is automatically reset after the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), so a program doesn&#8217;t need to explicitly sanitize it upon startup. </p>
<p> <code>setkeycreatecon</code>() can be applied prior to library functions that internally perform an file creation, in order to set an file context on the objects. </p>
<p> <code>getkeycreatecon_raw</code>() and <code>setkeycreatecon_raw</code>() behave identically to their non-raw counterparts but do not perform context translation. </p>
<p> <code>Note:</code> Signal handlers that perform a <code>setkeycreatecon</code>() must take care to save, reset, and restore the keycreate context to avoid unexpected behavior. </p>
<p> <code>Note:</code> Contexts are thread specific.</p>
<h2>Return Value</h2>
<p>On error -1 is returned. On success 0 is returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-getcon/">getcon</a></code>(3), <code><a href="/docs/linux/man/3-getexeccon/">getexeccon</a></code>(3) </p>
