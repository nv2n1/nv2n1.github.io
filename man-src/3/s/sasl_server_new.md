---
title: "sasl_server_new(3)"
name: "sasl_server_new"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_server_new/"
description: "sasl_server_new – Create a new server authentication object"
---

<p>sasl_server_new &#8211; Create a new server authentication object </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_server_new(const char *service,
                    const char *serverFQDN,
                    const char *user_realm,
                    const char *iplocalport,
                    const char *ipremoteport,
                    const sasl_callback_t *callbacks,
                    unsigned flags,
                    sasl_conn_t **pconn);</code></pre>
<h2>Description</h2>
<p><code>sasl_server_new()</code> creates a new SASL context. This context will be used for all SASL calls for one connection. It handles both authentication and integrity/encryption layers after authentication. <i>service</i> is the registered name of the service (usually the protocol name) using SASL (e.g. &quot;imap&quot;). <i>serverFQDN</i> is the fully qualified server domain name. NULL means use gethostname(). This is useful for multi-homed servers. <i>user_realm</i> is the domain of the user agent. This is usually not necessary (NULL is default) <i>iplocalport</i> is the IP and port of the local side of the connection, or NULL. If iplocalport is NULL it will disable mechanisms that require IP address information. This strings must be in one of the following formats: &quot;a.b.c.d;port&quot; (IPv4), &quot;e:f:g:h:i:j:k:l;port&quot; (IPv6), or &quot;e:f:g:h:i:j:a.b.c.d;port&quot; (IPv6) <i>ipremoteport</i> is the IP and port of the remote side of the connection, or NULL (see iplocalport) <i>flags</i> are connection flags (see below) <i>pconn</i> is a pointer to the connection context allocated by the library. This structure will be used for all future SASL calls for this connection. <code>Connection Flags</code></p>
<dl>
<dt><code>SASL_SUCCESS_DATA</code></p>
<dd>The protocol supports a server-last send</p>
<dt><code>SASL_NEED_PROXY</code></p>
<dd>Force the use of a mechanism that supports an authorization id that is not the authentication id. </p>
<h2>Return Value</h2>
<p><code>sasl_server_new()</code> returns an integer which corresponds to one of the SASL error codes. SASL_OK is the only one that indicates success. All others indicate errors and should either be handled or the authentication session should be quit. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_server_init/">sasl_server_init</a>(3), <a href="/docs/linux/man/3-sasl_server_start/">sasl_server_start</a>(3), <a href="/docs/linux/man/3-sasl_server_step/">sasl_server_step</a>(3), <a href="/docs/linux/man/3-sasl_setprop/">sasl_setprop</a>(3) </p>
