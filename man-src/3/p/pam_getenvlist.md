---
title: "pam_getenvlist(3)"
name: "pam_getenvlist"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_getenvlist/"
description: "pam_getenvlist – getting the PAM environment"
---

<p>pam_getenvlist &#8211; getting the PAM environment</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

char **pam_getenvlist(pam_handle_t *pamh);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_getenvlist</code> function returns a complete copy of the PAM environment as associated with the handle <i>pamh</i>. The PAM environment variables represent the contents of the regular environment variables of the authenticated user when service is granted. </p>
<p> The format of the memory is a malloc()&#8217;d array of char pointers, the last element of which is set to NULL. Each of the non-NULL entries in this array point to a NUL terminated and malloc()&#8217;d char string of the form: &quot;<i>name=value</i>&quot;. </p>
<p> It should be noted that this memory will never be free()&#8217;d by libpam. Once obtained by a call to <code>pam_getenvlist</code>, it is the responsibility of the calling application to free() this memory. </p>
<p> It is by design, and not a coincidence, that the format and contents of the returned array matches that required for the third argument of the <code><a href="/docs/linux/man/3-execle/">execle</a></code>(3) function call.</p>
<h2>Return Values</h2>
<p>The <code>pam_getenvlist</code> function returns NULL on failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3), <code><a href="/docs/linux/man/3-pam_getenv/">pam_getenv</a></code>(3), <code><a href="/docs/linux/man/3-pam_putenv/">pam_putenv</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) </p>
