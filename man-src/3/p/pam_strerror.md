---
title: "pam_strerror(3)"
name: "pam_strerror"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pam_strerror/"
description: "pam_strerror – return string describing PAM error code"
---

<p>pam_strerror &#8211; return string describing PAM error code</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;security/pam_appl.h&gt;

const char *pam_strerror(pam_handle_t *pamh, int errnum);</code></pre>
<h2>Description</h2>
<dd>The <code>pam_strerror</code> function returns a pointer to a string describing the error code passed in the argument <i>errnum</i>, possibly using the LC_MESSAGES part of the current locale to select the appropriate language. This string must not be modified by the application. No library function will modify this string.</p>
<h2>Return Values</h2>
<p>This function returns always a pointer to a string.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) </p>
