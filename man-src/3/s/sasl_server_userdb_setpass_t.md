---
title: "sasl_server_userdb_setpass_t(3)"
name: "sasl_server_userdb_setpass_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_server_userdb_setpass_t/"
description: "sasl_server_userdb_setpass_t – UserDB Plaintext Password Setting Callback"
---

<p>sasl_server_userdb_setpass_t &#8211; UserDB Plaintext Password Setting Callback </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


int sasl_server_userdb_setpass_t(sasl_conn_t *conn,
void *context,
const char *user,
const char *pass,
unsigned passlen,
struct propctx *propctx,
unsigned flags)</code></pre>
<h2>Description</h2>
<p><code>sasl_server_userdb_setpass_t</code> is used to store or change a plaintext password in the callback-supplier&#8217;s user database. <i>context</i> context from the callback record <i>user</i> NUL terminated user name with user [at] realm syntax <i>pass</i> password to check (may not be NUL terminated) <i>passlen</i> length of the password <i>propctx</i> Auxilliary Properties (not stored) <i>flags</i> These are the same flags that are passed to <a href="/docs/linux/man/3-sasl_setpass/">sasl_setpass</a>(3), and are documented on that man page. </p>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_server_userdb_checkpass_t/">sasl_server_userdb_checkpass_t</a>(3), <a href="/docs/linux/man/3-sasl_setpass/">sasl_setpass</a>(3) </p>
