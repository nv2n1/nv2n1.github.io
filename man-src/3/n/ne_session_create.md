---
title: "ne_session_create(3)"
name: "ne_session_create"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_session_create/"
description: "ne_session_create, ne_close_connection, ne_session_destroy – set up HTTP sessions"
---

<p>ne_session_create, ne_close_connection, ne_session_destroy &#8211; set up HTTP sessions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_session.h&gt;

ne_session *ne_session_create(const char *scheme, const char *hostname, unsigned int port);

void ne_close_connection(ne_session *session);

void ne_session_destroy(ne_session *session);</code></pre>
<h2>Description</h2>
<dd>An <code>ne_session</code> object represents an HTTP session &#8211; a logical grouping of a sequence of HTTP requests made to a certain server. Any requests made using the session can use a persistent connection, share cached authentication credentials and any other common attributes. </p>
<p> A new HTTP session is created using the <code>ne_session_create</code> function; the <i>hostname</i> and <i>port</i> parameters specify the origin server to use, along with the <i>scheme</i> (usually &quot;http&quot;). Before the first use of <code>ne_session_create</code> in a process, ne_sock_init must have been called to perform any global initialization needed by any libraries used by neon. </p>
<p> To enable SSL/TLS for the session, pass the string &quot;https&quot; as the <i>scheme</i> parameter, and either register a certificate verification function (see ne_ssl_set_verify) or trust the appropriate certificate (see ne_ssl_trust_cert, ne_ssl_trust_default_ca). </p>
<p> To use a proxy server for the session, it must be configured (see ne_session_proxy) before any requests are created from session object. </p>
<p> Further per-session options may be changed using the ne_set_session_flag interface. </p>
<p> If it is known that the session will not be used for a significant period of time, <code>ne_close_connection</code> can be called to close the connection, if one remains open. Use of this function is entirely optional, but it must not be called if there is a request active using the session. </p>
<p> Once a session has been completed, <code>ne_session_destroy</code> must be called to destroy the resources associated with the session. Any subsequent use of the session pointer produces undefined behaviour. The session object must not be destroyed until after all associated request objects have been destroyed.</p>
<h2>Notes</h2>
<p>The hostname passed to <code>ne_session_create</code> is resolved when the first request using the session is dispatched; a DNS resolution failure can only be detected at that time (using the NE_LOOKUP error code); see ne_request_dispatch for details.</p>
<h2>Return Values</h2>
<p><code>ne_session_create</code> will return a pointer to a new session object (and never NULL).</p>
<h2>Examples</h2>
<p>Create and destroy a session: </p>
<pre><code>ne_session *sess;
sess = ne_session_create(&quot;http&quot;, &quot;host.example.com&quot;, 80);
/* ... use sess ... */
ne_session_destroy(sess);</code></pre>
<h2>See Also</h2>
<p>ne_ssl_set_verify, ne_ssl_trust_cert, ne_sock_init, ne_set_session_flag</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
