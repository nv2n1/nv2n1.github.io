---
title: "sasl_dispose(3)"
name: "sasl_dispose"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_dispose/"
description: "sasl_dispose – Dispose of a SASL connection object"
---

<p>sasl_dispose &#8211; Dispose of a SASL connection object </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

void sasl_dispose(sasl_conn_t **pconn);</code></pre>
<h2>Description</h2>
<p><code>sasl_dispose</code> is called when a SASL connection object is no longer needed. Note that this is usually when the protocol session is done NOT when the authentication is done since a security layer may have been negotiated. </p>
<h2>Return Value</h2>
<p>No return values </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_server_new/">sasl_server_new</a>(3), <a href="/docs/linux/man/3-sasl_client_new/">sasl_client_new</a>(3) </p>
