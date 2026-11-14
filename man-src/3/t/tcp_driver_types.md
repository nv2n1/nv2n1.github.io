---
title: "tcp_driver_types(3)"
name: "tcp_driver_types"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcp_driver_types/"
description: "Types –"
---

<p>Types &#8211;</p>
<h3>Defines</h3>
<pre><code>#define GLOBUS_XIO_TCP_INVALID_HANDLE



Enumerations
enum globus_xio_tcp_send_flags_t { GLOBUS_XIO_TCP_SEND_OOB =  MSG_OOB }</code></pre>
<h2>Define Documentation</h2>
<h3>#define GLOBUS_XIO_TCP_INVALID_HANDLE</h3>
<p>Invalid handle type. <code>See also:</code></p>
<dl>
<dd><code>GLOBUS_XIO_TCP_SET_HANDLE</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_tcp_send_flags_t</code></h3>
<p>TCP driver specific types. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>GLOBUS_XIO_TCP_SEND_OOB </i></p>
<dd>Use this with <code>GLOBUS_XIO_TCP_SET_SEND_FLAGS</code> to send a TCP message out of band (Urgent data flag set).</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus xio from the source code.</p>
