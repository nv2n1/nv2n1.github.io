---
title: "sasl_client_start(3)"
name: "sasl_client_start"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_client_start/"
description: "sasl_client_start – Begin an authentication negotiation"
---

<p>sasl_client_start &#8211; Begin an authentication negotiation</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_client_start(sasl_conn_t *conn,
                      const char *mechlist,
                      sasl_interact_t **prompt_need,
                      const char **clientout,
                      unsigned *clientoutlen,
                      const char **mech);</code></pre>
<h2>Description</h2>
<p><code>sasl_client_start()</code> selects a mechanism for authentication and starts the authentication session. The mechlist is the list of mechanisms the client might like to use. The mechanisms in the list are not necessarily supported by the client or even valid. SASL determines which of these to use based upon the security preferences specified earlier. The list of mechanisms is typically a list of mechanisms the server supports acquired from a capability request. If SASL_INTERACT is returned the library needs some values to be filled in before it can proceed. The prompt_need structure will be filled in with requests. The application should fulfill these requests and call sasl_client_start again with identical parameters (the prompt_need parameter will be the same pointer as before but filled in by the application). <i>mechlist</i> is a list of mechanisms the server has available. Punctuation is ignored. <i>prompt_need</i> is filled in with a list of prompts needed to continue (if necessary). <i>clientout</i> and <i>clientoutlen</i> is created. It is the initial client response to send to the server. It is the job of the client to send it over the network to the server. Any protocol specific encoding (such as base64 encoding) necessary needs to be done by the client. If the protocol lacks client-send-first capability, then set <i>clientout</i> to NULL. If there is no initial client-send, then <i>*clientout</i> will be set to NULL on return. <i>mech</i> contains the name of the chosen SASL mechanism (on success) </p>
<h2>Return Value</h2>
<p>sasl_client_start returns an integer which corresponds to one of the following codes. SASL_CONTINUE indicates success and that there are more steps needed in the authentication. All other return codes indicate errors and should either be handled or the authentication session should be quit. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_callbacks/">sasl_callbacks</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_client_init/">sasl_client_init</a>(3), <a href="/docs/linux/man/3-sasl_client_new/">sasl_client_new</a>(3), <a href="/docs/linux/man/3-sasl_client_step/">sasl_client_step</a>(3) </p>
