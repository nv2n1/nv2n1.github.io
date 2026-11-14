---
title: "getexeccon_raw(3)"
name: "getexeccon_raw"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getexeccon_raw/"
description: "getexeccon, setexeccon – get or set the SELinux security context used for executing a new process"
---

<h2 class="name">NAME</h2>
<p> getexeccon, setexeccon &#8211; get or set the SELinux security context used for executing a new process </p>
<p> rpm_execcon &#8211; run a helper for rpm in an appropriate security context </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;selinux/selinux.h&gt;</code> </p>
<p> <code>int getexeccon(char **</code><i>context</i><code>);</code> </p>
<p> <code>int getexeccon_raw(char **</code><i>context</i><code>);</code> </p>
<p> <code>int setexeccon(char *</code><i>context</i><code>);</code> </p>
<p> <code>int setexeccon_raw(char *</code><i>context</i><code>);</code> </p>
<p> <code>int setexecfilecon(const char *</code><i>filename</i><code>, const char *</code><i>fallback_type</i><code>);</code> </p>
<p> <code>int rpm_execcon(unsigned int </code><i>verified</i><code>, const char *</code><i>filename</i><code>, char *const </code><i>argv</i><code>[] , char *const </code><i>envp</i><code>[]);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>getexeccon</code>() retrieves the context used for executing a new process. This returned context should be freed with <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3) if non-NULL. <code>getexeccon</code>() sets <code>*</code><i>context</i> to NULL if no exec context has been explicitly set by the program (i.e. using the default policy behavior). </p>
<p> <code>setexeccon</code>() sets the context used for the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) call. NULL can be passed to <code>setexeccon</code>() to reset to the default policy behavior. The exec context is automatically reset after the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), so a program doesn&#8217;t need to explicitly sanitize it upon startup. </p>
<p> <code>setexeccon</code>() can be applied prior to library functions that internally perform an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), e.g. <code>execl</code>*(3), <code>execv</code>*(3), <code><a href="/docs/linux/man/3-popen/">popen</a></code>(3), in order to set an exec context for that operation. </p>
<p> <code>getexeccon_raw</code>() and <code>setexeccon_raw</code>() behave identically to their non-raw counterparts but do not perform context translation. </p>
<p> <code>Note:</code> Signal handlers that perform an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) must take care to save, reset, and restore the exec context to avoid unexpected behavior. </p>
<p> <code>setexecfilecon</code>() sets the context used for the next <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) call, based on the policy for the <i>filename</i>, and falling back to a new context with a <i>fallback_type</i> in case there is no transition. </p>
<p> <code>rpm_execcon</code>() is deprecated; please use <code>setexecfilecon</code>() in conjunction with <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) in all new code. This function runs a helper for rpm in an appropriate security context. The verified parameter should contain the return code from the signature verification (0 == ok, 1 == notfound, 2 == verifyfail, 3 == nottrusted, 4 == nokey), although this information is not yet used by the function. The function determines the proper security context for the helper based on policy, sets the exec context accordingly, and then executes the specified filename with the provided argument and environment arrays.</p>
<h2>RETURN VALUE</h2>
<p> On error -1 is returned. </p>
<p> On success <code>getexeccon</code>(), <code>setexeccon</code>() and <code>setexecfilecon</code>() return 0. <code>rpm_execcon</code>() only returns upon errors, as it calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-getcon/">getcon</a></code>(3) </p>
<h2>Index</h2>
