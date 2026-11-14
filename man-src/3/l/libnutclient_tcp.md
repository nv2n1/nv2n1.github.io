---
title: "libnutclient_tcp(3)"
name: "libnutclient_tcp"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libnutclient_tcp/"
description: "libnutclient_tcp, nutclient_tcp_create_client, nutclient_tcp_is_connected, nutclient_tcp_disconnect, nutclient_tcp_reconnect, nutclient_tcp_set_timeout, nutclient_tcp_get_timeout – TCP protocol rel..."
---

<h2 class="name">NAME</h2>
<p> libnutclient_tcp, nutclient_tcp_create_client, nutclient_tcp_is_connected, nutclient_tcp_disconnect, nutclient_tcp_reconnect, nutclient_tcp_set_timeout, nutclient_tcp_get_timeout &#8211; TCP protocol related function for Network UPS Tools high-level client access library </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;nutclient.h&gt;
</code></pre>
<pre>
typedef NUTCLIENT_t NUTCLIENT_TCP_t;
</pre>
<pre><code>
NUTCLIENT_TCP_t nutclient_tcp_create_client(const char *host, unsigned short port);
int nutclient_tcp_is_connected(NUTCLIENT_TCP_t client);
void nutclient_tcp_disconnect(NUTCLIENT_TCP_t client);
int nutclient_tcp_reconnect(NUTCLIENT_TCP_t client);
void nutclient_tcp_set_timeout(NUTCLIENT_TCP_t client, long timeout);
long nutclient_tcp_get_timeout(NUTCLIENT_TCP_t client);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions allow to manage connections to <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) using NUT TCP protocol. </p>
<p> The <code>nutclient_tcp_create_client()</code> function create the <i>NUTCLIENT_TCP_t</i> context and intend to connect to upsd at <i>host</i> and <i>port</i>. The context must be freed by <i>nutclient_destroy()</i> </p>
<p> <i>host</i> can be a sever name or a valid IPv4 or IPv6 adress like &quot;localhost&quot;, &quot;127.0.0.1&quot; or &quot;::1&quot;. </p>
<p> <i>port</i> is a valid TCP port, genrally 3493. </p>
<p> The <code>nutclient_tcp_is_connected()</code> function test if the connection is valid. </p>
<p> The <code>nutclient_tcp_disconnect()</code> function force to disconnect the specified connection. </p>
<p> The <code>nutclient_tcp_reconnect()</code> function force to reconnect a connection, disconnecting it if needed. </p>
<p> The <code>nutclient_tcp_set_timeout()</code> function set the timeout duration for I/O operations. </p>
<p> The <code>nutclient_tcp_get_timeout()</code> function retrieve the timeout duration for I/O operations. </p>
<p> <i>timeout</i> values are specified in seconds, negatives values for blocking.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libnutclient/">libnutclient</a></code>(3) <code><a href="/docs/linux/man/3-libnutclient_general/">libnutclient_general</a></code>(3) </p>
<h2>Index</h2>
