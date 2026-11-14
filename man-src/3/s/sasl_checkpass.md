---
title: "sasl_checkpass(3)"
name: "sasl_checkpass"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_checkpass/"
description: "sasl_checkpass – Check a plaintext password"
---

<p>sasl_checkpass &#8211; Check a plaintext password</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_checkpass(sasl_conn_t *conn,
                   const char *user,
                   unsigned userlen,
                   const char *pass,
                   unsigned passlen);</code></pre>
<h2>Description</h2>
<p><code>sasl_checkpass()</code> will check a plaintext password. This is needed for protocols that had a login method before SASL (for example the LOGIN command in IMAP). The password is checked with the <i>pwcheck_method</i> See <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3) for information on how this parameter is set. </p>
<h2>Return Value</h2>
<p>sasl_checkpass returns an integer which corresponds to one of the following codes. SASL_OK indicates that the authentication is complete. All other return codes indicate errors and should either be handled or the authentication session should be quit. See <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) for meanings of return codes. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_setpass/">sasl_setpass</a>(3) </p>
