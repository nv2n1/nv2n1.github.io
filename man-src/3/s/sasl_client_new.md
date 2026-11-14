---
title: "sasl_client_new(3)"
name: "sasl_client_new"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_client_new/"
description: "sasl_client_new – Create a new client authentication object"
---

<p>sasl_client_new &#8211; Create a new client authentication object </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_client_new(const char *service,
                    const char *serverFQDN,
                    const char *iplocalport,
                    const char *ipremoteport,
                    const sasl_callback_t *prompt_supp,
                    unsigned flags,
                    sasl_conn_t **pconn);</code></pre>
<h2>Description</h2>
<p><code>sasl_client_new()</code> creates a new SASL context. This context will be used for all SASL calls for one connection. It handles both authentication and integrity/encryption layers after authentication. <i>service</i> is the registered name of the service (usually the protocol name) using SASL (e.g. &quot;imap&quot;). <i>serverFQDN</i> is the fully qualified domain name of the server (e.g. &quot;serverhost.cmu.edu&quot;). <i>iplocalport</i> is the IP and port of the local side of the connection, or NULL. If iplocalport is NULL it will disable mechanisms that require IP address information. This strings must be in one of the following formats: &quot;a.b.c.d;port&quot; (IPv4), &quot;e:f:g:h:i:j:k:l;port&quot; (IPv6), or &quot;e:f:g:h:i:j:a.b.c.d;port&quot; (IPv6) <i>ipremoteport</i> is the IP and port of the remote side of the connection, or NULL (see iplocalport) <i>prompt_supp</i> is a list of client interactions supported that is unique to this connection. If this parameter is NULL the global callbacks (specified in sasl_client_init) will be used. See sasl_callback for more information. <i>flags</i> are connection flags (see below) <i>pconn</i> is the connection context allocated by the library. This structure will be used for all future SASL calls for this connection. <code>Connection Flags</code> Flags that may be passed to <code>sasl_server_new()</code> include</p>
<dl>
<dt><code>SASL_SUCCESS_DATA</code></p>
<dd>The protocol supports a server-last send</p>
<dt><code>SASL_NEED_PROXY</code></p>
<dd>Force the use of a mechanism that supports an authorization id that is not the authentication id. </p>
<h2>Return Value</h2>
<p>sasl_client_new returns an integer which corresponds to one of the following codes. SASL_OK is the only one that indicates success. All others indicate errors and should either be handled or the authentication session should be quit. </p>
<h2>Errors</h2>
<dl>
<dt><code>SASL_OK</code></p>
<dd>Success</p>
<dt><code>SASL_BADPARAM</code></p>
<dd>Error in config file or passed parameters</p>
<dt><code>SASL_NOMECH</code></p>
<dd>No mechanism meets requested properties</p>
<dt><code>SASL_NOMEM</code></p>
<dd>Not enough memory to complete operation </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_client_init/">sasl_client_init</a>(3), <a href="/docs/linux/man/3-sasl_client_start/">sasl_client_start</a>(3), <a href="/docs/linux/man/3-sasl_client_step/">sasl_client_step</a>(3), <a href="/docs/linux/man/3-sasl_setprop/">sasl_setprop</a>(3) </p>
