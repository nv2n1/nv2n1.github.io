---
title: "sc_tcpiosocket(3)"
name: "sc_tcpiosocket"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_tcpiosocket/"
description: "TCPIOSocket –"
---

<p>TCPIOSocket &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>TCPSocket</code>. Inherited by <code>TCPClientConnection</code>, and <code>TCPServerConnection</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>int read (void *d, int n)



int write (const void *d, int n)



int read_int (int *d, int n)



int write_int (const int *d, int n)



int read_string (std::string &amp;)



int write_string (const std::string &amp;)



int read_int (int &amp;)



int write_int (int)



int read_uint32 (u_int32_t &amp;)



int write_uint32 (u_int32_t)
</code></pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
