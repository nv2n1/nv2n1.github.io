---
title: "sasl_setpass(3)"
name: "sasl_setpass"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_setpass/"
description: "sasl_setpass – Check a plaintext password"
---

<p>sasl_setpass &#8211; Check a plaintext password</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_setpass(sasl_conn_t *conn,
const char *user,
const char *pass, unsigned passlen,
const char *oldpass, unsigned oldpasslen,
unsigned flags)</code></pre>
<h2>Description</h2>
<p><code>sasl_setpass</code> will set passwords in the sasldb, and trigger the setpass callbacks for all available mechanisms. <i>user</i> is the username to set the password for. <i>pass</i> and <i>passlen</i> are the password to set and its length <i>oldpass</i> and <i>oldpasslen</i> are the old password &amp; its length (and are optional) <i>flags</i> Are flags including SASL_SET_CREATE and SASL_SET_DISABLE (to cause the creating of nonexistent accounts and the disabling of an account, respectively) </p>
<h2>Notes</h2>
<p><i>oldpass</i> and <i>oldpasslen</i> are unused in the Cyrus SASL implementation, though are passed on to any mechanisms that may require them. </p>
<h2>Return Value</h2>
<p>Returns SASL_OK on success. SASL error code on failure. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_checkpass/">sasl_checkpass</a>(3) </p>
