---
title: "globus_xio_tcp_send_oob(3)"
name: "globus_xio_tcp_send_oob"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_tcp_send_oob/"
description: "Types –"
---

<p>Types &#8211; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_XIO_TCP_INVALID_HANDLE</code> </p>
<h3>Enumerations</h3>
<p>enum <code>globus_xio_tcp_send_flags_t</code> { <code>GLOBUS_XIO_TCP_SEND_OOB</code> = MSG_OOB } </p>
<h2>Detailed Description</h2>
<h2>Macro Definition Documentation</h2>
<h3>#define GLOBUS_XIO_TCP_INVALID_HANDLE</h3>
<p>Invalid handle type </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>GLOBUS_XIO_TCP_SET_HANDLE</code></dl>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_xio_tcp_send_flags_t</code></h3>
<p>TCP driver specific types </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_XIO_TCP_SEND_OOB </i></p>
<dd>Use this with <code>GLOBUS_XIO_TCP_SET_SEND_FLAGS</code> to send a TCP message out of band (Urgent data flag set)</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_xio from the source code.</p>
