---
title: "sasl_canon_user_t(3)"
name: "sasl_canon_user_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_canon_user_t/"
description: "sasl_server_userdb_checkpass_t – Plaintext Password Verification Callback"
---

<p>sasl_server_userdb_checkpass_t &#8211; Plaintext Password Verification Callback </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


int sasl_canon_user_t(sasl_conn_t *conn,
void *context,
const char *user, unsigned ulen,
unsigned flags,
const char *user_realm,
char *out_user, unsigned out_umax,
unsigned *out_ulen)</code></pre>
<h2>Description</h2>
<p><code>sasl_canon_user_t</code> Is the callback for an application-supplied user canonicalization function. This function is subject to the requirements that all user canonicalization functions are: It must copy the result into the output buffers, but the output buffers and the input buffers may be the same. <i>context</i> context from the callback record <i>user</i> and <i>ulen</i> Un-canonicalized username (and length) <i>flags</i> Either SASL_CU_AUTHID (indicating the authentication ID is being canonicalized) or SASL_CU_AUTHZID (indicating the authorization ID is to be canonicalized) or a bitwise OR of the the two. <i>user_realm</i> Realm of authentication. <i>out_user</i> and <i>out_umax</i> and <i>out_ulen</i> The output buffer, max length, and actual length for the username. </p>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) </p>
