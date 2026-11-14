---
title: "pam_getenv(3)"
name: "pam_getenv"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_getenv/"
description: "pam_getenv – get a PAM environment variable"
---

<p>pam_getenv &#8211; get a PAM environment variable</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

const char *pam_getenv(pam_handle_t *pamh, const char *name);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_getenv</code> function searches the PAM environment list as associated with the handle <i>pamh</i> for an item that matches the string pointed to by <i>name</i> and returns a pointer to the value of the environment variable. The application is not allowed to free the data.</p>
<h2>Return Values</h2>
<p>The <code>pam_getenv</code> function returns NULL on failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3), <code><a href="/docs/linux/man/3-pam_getenvlist/">pam_getenvlist</a></code>(3), <code><a href="/docs/linux/man/3-pam_putenv/">pam_putenv</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) </p>
