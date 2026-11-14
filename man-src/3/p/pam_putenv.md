---
title: "pam_putenv(3)"
name: "pam_putenv"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_putenv/"
description: "pam_putenv – set or change PAM environment variable"
---

<p>pam_putenv &#8211; set or change PAM environment variable</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

int pam_putenv(pam_handle_t *pamh, const char *name_value);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_putenv</code> function is used to add or change the value of PAM environment variables as associated with the <i>pamh</i> handle. </p>
<p> The <i>pamh</i> argument is an authentication handle obtained by a prior call to pam_start(). The <i>name_value</i> argument is a single NUL terminated string of one of the following forms: </p>
<p> NAME=value of variable</p>
<dl>
<dd>In this case the environment variable of the given NAME is set to the indicated value: <i>value of variable</i>. If this variable is already known, it is overwritten. Otherwise it is added to the PAM environment.</dl>
<p> NAME=</p>
<dl>
<dd>This function sets the variable to an empty value. It is listed separately to indicate that this is the correct way to achieve such a setting.</dl>
<p> NAME</p>
<dl>
<dd>Without an &#8216;=&#8217; the <code>pam_putenv</code>() function will delete the corresponding variable from the PAM environment.</dl>
<p> <code>pam_putenv</code>() operates on a copy of <i>name_value</i>, which means in contrast to <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), the application is responsible to free the data.</p>
<h2>Return Values</h2>
<p>PAM_PERM_DENIED</p>
<dl>
<dd>Argument <i>name_value</i> given is a NULL pointer.</dl>
<p> PAM_BAD_ITEM</p>
<dl>
<dd>Variable requested (for deletion) is not currently set.</dl>
<p> PAM_ABORT</p>
<dl>
<dd>The <i>pamh</i> handle is corrupt.</dl>
<p> PAM_BUF_ERR</p>
<dl>
<dd>Memory buffer error.</dl>
<p> PAM_SUCCESS</p>
<dl>
<dd>The environment variable was successfully updated.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pam_start/">pam_start</a></code>(3), <code><a href="/docs/linux/man/3-pam_getenv/">pam_getenv</a></code>(3), <code><a href="/docs/linux/man/3-pam_getenvlist/">pam_getenvlist</a></code>(3), <code><a href="/docs/linux/man/3-pam_strerror/">pam_strerror</a></code>(3), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) </p>
