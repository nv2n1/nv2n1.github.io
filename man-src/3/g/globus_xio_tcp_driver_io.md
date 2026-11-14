---
title: "globus_xio_tcp_driver_io(3)"
name: "globus_xio_tcp_driver_io"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_tcp_driver_io/"
description: "Reading/Writing – Both the globus_xio_register_read() and globus_xio_register_write() calls follow similar semantics as described below."
---

<h2 class="name">NAME</h2>
<p> Reading/Writing &#8211; Both the <code>globus_xio_register_read()</code> and <code>globus_xio_register_write()</code> calls follow similar semantics as described below. </p>
<p> If the waitforbytes parameter is greater than zero, the io will happen asynchronously and be completed when at least waitforbytes has been read/written. </p>
<p> If the waitforbytes parameter is equal to zero, one of the following alternative behaviors occur: </p>
<p> If the length of the buffer is &gt; 0 the read or write happens synchronously. If the user is using one of the blocking xio calls, no internal callback will occur. </p>
<p> If the length of the buffer is also 0, the call behaves like an asynchronous notification of data ready to be either read or written. ie, an asynchronous select(). </p>
<p> In any case, when an error or EOF occurs before the waitforbytes request has been met, the outgoing nbytes is set to the amount of data actually read/written before the error or EOF occurred. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
