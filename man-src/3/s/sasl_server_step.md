---
title: "sasl_server_step(3)"
name: "sasl_server_step"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_server_step/"
description: "sasl_server_step – Perform a step in the authentication negotiation"
---

<p>sasl_server_step &#8211; Perform a step in the authentication negotiation </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_server_step(sasl_conn_t *conn,
                     const char *clientin,
                     unsigned clientinlen,
                     const char **serverout,
                     unsigned *serveroutlen);</code></pre>
<h2>Description</h2>
<p><code>sasl_server_step()</code> performs a step in the authentication negotiation. It returns SASL_OK if the whole negotiation is successful and SASL_CONTINUE if this step is ok but at least one more step is needed. <i>conn</i> is the SASL connection context <i>clientin</i> is the data given by the client (decoded if the protocol encodes requests sent over the wire) <i>clientinlen</i> is the length of <i>clientin</i> <i>serverout</i> and <i>serveroutlen</i> are set by the library and should be sent to the client. </p>
<h2>Return Value</h2>
<p>sasl_server_step returns an integer which corresponds to one of the SASL error codes. SASL_CONTINUE indicates success and that there are more steps needed in the authentication. SASL_OK indicates that the authentication is complete. All other return codes indicate errors and should either be handled or the authentication session should be quit. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_server_init/">sasl_server_init</a>(3), <a href="/docs/linux/man/3-sasl_server_new/">sasl_server_new</a>(3), <a href="/docs/linux/man/3-sasl_server_start/">sasl_server_start</a>(3) </p>
