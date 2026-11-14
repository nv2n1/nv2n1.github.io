---
title: "sasl_getsecret_t(3)"
name: "sasl_getsecret_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_getsecret_t/"
description: "sasl_getsecret_t – The SASL callback for secrets (passwords)"
---

<p>sasl_getsecret_t &#8211; The SASL callback for secrets (passwords) </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_getsecret_t(sasl_conn_t *conn,
                     void *context,
                     int id,
                     sasl_secret_t **psecret);</code></pre>
<h2>Description</h2>
<p><code>sasl_getsecret_t</code> is used to retrieve the secret from the application. A sasl_secret_t should be allocated to length sizeof(sasl_secret_t)+&lt;length of secret&gt;. It has two fields <i>len</i> which is the length of the secret in bytes and <i>data</i> which contains the secret itself (does not need to be null terminated). </p>
<h2>Return Value</h2>
<p>SASL callback functions should return SASL return codes. See sasl.h for a complete list. SASL_OK indicates success. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3) </p>
