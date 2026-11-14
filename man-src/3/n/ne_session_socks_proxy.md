---
title: "ne_session_socks_proxy(3)"
name: "ne_session_socks_proxy"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_session_socks_proxy/"
description: "ne_session_proxy, ne_session_socks_proxy, ne_session_system_proxy, ne_set_addrlist – configure proxy servers"
---

<p>ne_session_proxy, ne_session_socks_proxy, ne_session_system_proxy, ne_set_addrlist &#8211; configure proxy servers</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_session.h&gt;

void ne_session_proxy(ne_session *session, const char *hostname, unsigned int port);

void ne_session_system_proxy(ne_session *session, unsigned int flags);

void ne_session_socks_proxy(ne_session *session, enum ne_sock_sversion version, const char *hostname, unsigned int port, const char *username, const char *password);

void ne_set_addrlist(ne_session *session, const ne_inet_addr **addrlist, size_t count);</code></pre>
<h2>Description</h2>
<dd>One (and no more than one) of the functions <code>ne_session_proxy</code>, <code>ne_session_system_proxy</code>, <code>ne_session_socks_proxy</code>, <code>ne_set_addrlist</code> can be used to configure a proxy server for a given session object. If more than one function is invoked for any given session object, only the last call has effect. If one of the functions is to be used, it must be used before the creation of any request object for the session.</p>
<h3>HTTP proxy specification</h3>
<p>The <code>ne_session_proxy</code> function configures use of an HTTP proxy server for the session, the location of which is given by the <i>hostname</i> and <i>port</i> paramters. If the proxy requires authentication, ne_set_proxy_auth should be used.</p>
<h3>System proxy configuration</h3>
<p>The <code>ne_session_system_proxy</code> function configures the session to use any proxy servers specified by the system configuration. Support for this function is platform-specific; if unsupported, the function has no effect.</p>
<h3>SOCKS proxy configuration</h3>
<p>The <code>ne_session_socks_proxy</code> function configures the session to use a SOCKS proxy. The <i>version</i> indicates which version of the SOCKS protocol should be used. The <i>hostname</i> and <i>port</i> parameters specify the SOCKS proxy location. Note that a server with only an IPv6 address cannot be used with SOCKS v4 or v4A. The interpretation of the other arguments depends on the version specified: </p>
<p> <code>NE_SOCK_SOCKSV4</code> (version 4)</p>
<dl>
<dd>The <i>username</i> parameter must be non-NULL; the <i>password</i> parameter is ignored.</dl>
<p> <code>NE_SOCK_SOCKSV4A</code> (version 4A)</p>
<dl>
<dd>The <i>username</i> parameter must be non-NULL; the <i>password</i> parameter is ignored.</dl>
<p> <code>NE_SOCK_SOCKSV5</code> (version 5)</p>
<dl>
<dd>The <i>username</i> parameter may be NULL; if it is non-NULL, the <i>password</i> parameter must also be non-NULL; otherwise, it is ignored..</dl>
<h3>Origin server address override</h3>
<p>The <code>ne_set_addrlist</code> function forces use of an address and port the a specified list when establishing a TCP connection, ignoring the &quot;real&quot; hostname and port identifying the origin server for the session (as passed to <code>ne_session_create</code>). The origin server&#8217;s &quot;real&quot; hostname and port will still be used in the Host header in HTTP requests. When a connection is required, the library will iterate through the <i>addrlist</i> list, attempting to connect to the address <i>addrlist[0]</i> through to <i>addrlist[count-1]</i> in turn, until a connection can be established.</p>
<h2>Return Values</h2>
<p>None of the functions described here has a return value.</p>
<h2>Examples</h2>
<p>Create and destroy a session: </p>
<pre><code>ne_session *sess;
sess = ne_session_create(&quot;http&quot;, &quot;host.example.com&quot;, 80);
ne_session_proxy(sess, &quot;proxy.example.com&quot;, 3128);
/* ... use sess ... */
ne_session_destroy(sess);</code></pre>
<h2>See Also</h2>
<p>ne_ssl_set_verify, ne_ssl_trust_cert, ne_sock_init, ne_set_session_flag</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
