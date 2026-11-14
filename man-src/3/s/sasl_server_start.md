---
title: "sasl_server_start(3)"
name: "sasl_server_start"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_server_start/"
description: "sasl_server_start – Begin an authentication negotiation"
---

<p>sasl_server_start &#8211; Begin an authentication negotiation </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_server_start(sasl_conn_t *conn,
                      const char *mech,
                      const char *clientin,
                      unsigned *clientinlen,
                      const char **serverout,
                      unsigned *serveroutlen);</code></pre>
<h2>Description</h2>
<p><code>sasl_server_start()</code> begins the authentication with the mechanism specified with mech. This fails if the mechanism is not supported. SASL_OK is returned if the authentication is complete and the user is authenticated. SASL_CONTINUE is returned if one or more steps are still required in the authentication. All other return values indicate failure. <i>conn</i> is the SASL context for this connection <i>mech</i> is the mechanism name that the client requested <i>clientin</i> is the client initial response, NULL if the protocol lacks support for client-send-first or if the other end did not have an initial send. Note that no initial client send is distinct from an initial send of a null string, and the protocol MUST account for this difference. <i>clientinlen</i> is the length of initial response <i>serverout</i> is created by the plugin library. It is the initial server response to send to the client. This is allocated/freed by the library and it is the job of the client to send it over the network to the server. Also protocol specific encoding (such as base64 encoding) must needs to be done by the server. <i>serveroutlen</i> is set to the length of initial server challenge </p>
<h2>Return Value</h2>
<p>sasl_server_start returns an integer which corresponds to one of the SASL errorcodes. SASL_OK indicates that authentication is completed successfully. SASL_CONTINUE indicates success and that there are more steps needed in the authentication. All other return codes indicate errors and should either be handled or the authentication session should be quit. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_server_init/">sasl_server_init</a>(3), <a href="/docs/linux/man/3-sasl_server_new/">sasl_server_new</a>(3), <a href="/docs/linux/man/3-sasl_server_step/">sasl_server_step</a>(3) </p>
