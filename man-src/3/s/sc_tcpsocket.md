---
title: "sc_tcpsocket(3)"
name: "sc_tcpsocket"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_tcpsocket/"
description: "TCPSocket –"
---

<p>TCPSocket &#8211;</p>
<h2>Synopsis</h2>
<p> Inherited by <code>TCPIOSocket</code>, and <code>TCPServerSocket</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>void create ()



void bind (u_int16_t port_begin, u_int16_t port_fence)



int port ()



u_int32_t addr ()



bool initialized ()



bool bound ()



virtual void close ()



Protected Attributes
int socket_



int port_



bool initialized_



bool bound_
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
