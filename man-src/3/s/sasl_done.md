---
title: "sasl_done(3)"
name: "sasl_done"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_done/"
description: "sasl_done – Dispose of a SASL connection object"
---

<p>sasl_done &#8211; Dispose of a SASL connection object </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

void sasl_done(void);</code></pre>
<h2>Description</h2>
<p><code>sasl_done</code> is called when the application is completely done with the SASL library. </p>
<h2>Return Value</h2>
<p>No return values </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_server_init/">sasl_server_init</a>(3), <a href="/docs/linux/man/3-sasl_client_init/">sasl_client_init</a>(3) </p>
