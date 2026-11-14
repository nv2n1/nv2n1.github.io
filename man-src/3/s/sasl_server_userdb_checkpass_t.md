---
title: "sasl_server_userdb_checkpass_t(3)"
name: "sasl_server_userdb_checkpass_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_server_userdb_checkpass_t/"
description: "sasl_server_userdb_checkpass_t – Plaintext Password Verification Callback"
---

<p>sasl_server_userdb_checkpass_t &#8211; Plaintext Password Verification Callback </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


int sasl_server_userdb_checkpass_t(sasl_conn_t *conn,
void *context,
const char *user,
const char *pass,
unsigned passlen,
struct propctx *propctx)</code></pre>
<h2>Description</h2>
<p><code>sasl_server_userdb_checkpass_t</code> is used to verify a plaintext password against the callback supplier&#8217;s user database. This is to allow additional ways to encode the userPassword property. <i>context</i> context from the callback record <i>user</i> NUL terminated user name with user [at] realm syntax <i>pass</i> password to check (may not be NUL terminated) <i>passlen</i> length of the password <i>propctx</i> property context to fill in with userPassword </p>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_server_userdb_setpass_t/">sasl_server_userdb_setpass_t</a>(3) </p>
