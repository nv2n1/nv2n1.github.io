---
title: "sasl_user_exists(3)"
name: "sasl_user_exists"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_user_exists/"
description: "sasl_user_exists – Check if a user exists on server"
---

<p>sasl_user_exists &#8211; Check if a user exists on server </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;


int sasl_user_exists( sasl_conn_t *conn,
const char *service, const char *user_realm,
const char *user)</code></pre>
<h2>Description</h2>
<p><code>sasl_user_exists</code> will check if a user exists on the server. <i>conn</i> a connection context <i>service</i> Service name or NULL (for service name of connection context) <i>user_realm</i> Realm to check in or NULL (for default realm) <i>user</i> User name to check for existence of. </p>
<h2>Return Value</h2>
<p>Returns SASL_OK on success. SASL error code on failure. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) </p>
