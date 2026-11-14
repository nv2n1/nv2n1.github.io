---
title: "setexeccon_raw(3)"
name: "setexeccon_raw"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setexeccon_raw/"
description: "getexeccon, setexeccon – get or set the SELinux security context used for executing a new process"
---

<p>getexeccon, setexeccon &#8211; get or set the SELinux security context used for executing a new process </p>
<p> rpm_execcon &#8211; run a helper for rpm in an appropriate security context</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int getexeccon(char **context);
int getexeccon_raw(char **context);
int setexeccon(char *context);
int setexeccon_raw(char *context);
int setexecfilecon(const char *filename, const char *fallback_type);
int rpm_execcon(unsigned int verified, const char *filename, char *const argv[], char *const envp[]);</code></pre>
<h2>Description</h2>
<p><code>getexeccon</code>() retrieves the context used for executing a new process. This returned context should be freed with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3) if non-NULL. <code>getexeccon</code>() sets <code>*</code><i>context</i> to NULL if no exec context has been explicitly set by the program (i.e. using the default policy behavior). </p>
<p> <code>setexeccon</code>() sets the context used for the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) call. NULL can be passed to <code>setexeccon</code>() to reset to the default policy behavior. The exec context is automatically reset after the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), so a program doesn&#8217;t need to explicitly sanitize it upon startup. </p>
<p> <code>setexeccon</code>() can be applied prior to library functions that internally perform an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), e.g. <code>execl</code>*(3), <code>execv</code>*(3), <code><a href="/docs/linux/man/3-popen/">popen</a></code>(3), in order to set an exec context for that operation. </p>
<p> <code>getexeccon_raw</code>() and <code>setexeccon_raw</code>() behave identically to their non-raw counterparts but do not perform context translation. </p>
<p> <code>Note:</code> Signal handlers that perform an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) must take care to save, reset, and restore the exec context to avoid unexpected behavior. </p>
<p> <code>setexecfilecon</code>() sets the context used for the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) call, based on the policy for the <i>filename</i>, and falling back to a new context with a <i>fallback_type</i> in case there is no transition. </p>
<p> <code>rpm_execcon</code>() is deprecated; please use <code>setexecfilecon</code>() in conjunction with <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) in all new code. This function runs a helper for rpm in an appropriate security context. The verified parameter should contain the return code from the signature verification (0 == ok, 1 == notfound, 2 == verifyfail, 3 == nottrusted, 4 == nokey), although this information is not yet used by the function. The function determines the proper security context for the helper based on policy, sets the exec context accordingly, and then executes the specified filename with the provided argument and environment arrays.</p>
<h2>Return Value</h2>
<p>On error -1 is returned. </p>
<p> On success <code>getexeccon</code>(), <code>setexeccon</code>() and <code>setexecfilecon</code>() return 0. <code>rpm_execcon</code>() only returns upon errors, as it calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-getcon/">getcon</a></code>(3) </p>
