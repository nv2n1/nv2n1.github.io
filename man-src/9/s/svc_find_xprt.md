---
title: "svc_find_xprt(9)"
name: "svc_find_xprt"
section: "9"
letter: "s"
url: "/docs/linux/man/9-svc_find_xprt/"
---

svc_find_xprt - find an RPC transport instance

<h2>Synopsis</h2>

<pre><code>struct svc_xprt *svc_find_xprt(struct svc_serv *serv, const char *xcl_name, struct net *net, const sa_family_t af, const unsigned short port);</code></pre>

<h2>Arguments</h2>

<i>serv</i>
<dl><dd><dd>pointer to svc_serv to search</dl>
 

 <i>xcl_name</i>
<dl><dd>C string containing transport's class name</dl>
 

 <i>net</i>
<dl><dd>owner net pointer</dl>
 

 <i>af</i>
<dl><dd>Address family of transport's local address</dl>
 

 <i>port</i>
<dl><dd>transport's IP port number</dl>

<h2>Description</h2>

Return the transport instance pointer for the endpoint accepting connections/peer traffic from the specified transport class, address family and port. 

 Specifying 0 for the address family or port is effectively a wild-card, and will result in matching the first transport in the service's list that has a matching class name.

<h2>Copyright</h2>


