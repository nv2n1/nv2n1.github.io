---
title: "sasl_client_step(3)"
name: "sasl_client_step"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_client_step/"
description: "sasl_client_step – Perform a step in the authentication negotiation"
---

<p>sasl_client_step &#8211; Perform a step in the authentication negotiation </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_client_step(sasl_conn_t *conn,
                     const char *serverin,
                     unsigned serverinlen,
                     sasl_interact_t **prompt_need,
                     const char **clientout,
                     unsigned *clientoutlen);</code></pre>
<h2>Description</h2>
<p><code>sasl_client_step()</code> performs a step in the authentication negotiation. It returns SASL_OK if the whole negotiation is successful and SASL_CONTINUE if this step is ok but at least one more step is needed. A client should not assume an authentication negotiation is successful just because the server signaled success via protocol (i.e. if the server said &quot;. OK Authentication succeeded&quot; in IMAP sasl_client_step should still be called one more time with a serverinlen of zero. If SASL_INTERACT is returned the library needs some values to be filled in before it can proceed. The prompt_need structure will be filled in with requests. The application should fulfill these requests and call sasl_client_start again with identical parameters (the prompt_need parameter will be the same pointer as before but filled in by the application). <i>conn</i> is the SASL connection context <i>serverin</i> is the data given by the server (decoded if the protocol encodes requests sent over the wire) <i>serverinlen</i> is the length of serverin <i>clientout</i> and <i>clientoutlen</i> is created. It is the initial client response to send to the server. It is the job of the client to send it over the network to the server. Any protocol specific encoding (such as base64 encoding) necessary needs to be done by the client. </p>
<h2>Return Value</h2>
<p>sasl_client_step returns an integer which corresponds to one of the following codes. SASL_CONTINUE indicates success and that there are more steps needed in the authentication. SASL_OK indicates that the authentication is complete. All other return codes indicate errors and should either be handled or the authentication session should be quit. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_client_init/">sasl_client_init</a>(3), <a href="/docs/linux/man/3-sasl_client_new/">sasl_client_new</a>(3), <a href="/docs/linux/man/3-sasl_client_start/">sasl_client_start</a>(3) </p>
