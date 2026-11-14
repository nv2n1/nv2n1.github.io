---
title: "pam_misc_setenv(3)"
name: "pam_misc_setenv"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_misc_setenv/"
description: "pam_misc_setenv – BSD like PAM environment variable setting"
---

<p>pam_misc_setenv &#8211; BSD like PAM environment variable setting</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_misc.h&gt;

int pam_misc_setenv(pam_handle_t *pamh, const char *name, const char *value, intreadonly);</code></pre>
<h2>Description</h2>
<dd>This function performs a task equivalent to <code><a href="/docs/linux/man/3-pam_putenv/">pam_putenv</a></code>(3), its syntax is, however, more like the BSD style function; <code>setenv()</code>. The <i>name</i> and <i>value</i> are concatenated with an &#8216;=&#8217; to form a name=value and passed to <code>pam_putenv()</code>. If, however, the PAM variable is already set, the replacement will only be applied if the last argument, <i>readonly</i>, is zero.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_putenv/">pam_putenv</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Standards</h2>
<p>The <code>pam_misc_setenv</code> function is part of the <code>libpam_misc</code> Library and not defined in any standard.</p>
