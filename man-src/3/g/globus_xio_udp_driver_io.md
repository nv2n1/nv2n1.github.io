---
title: "globus_xio_udp_driver_io(3)"
name: "globus_xio_udp_driver_io"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_udp_driver_io/"
description: "Reading/Writing – globus_xio_register_read() semantics:"
---

<h2 class="name">NAME</h2>
<p> Reading/Writing &#8211; <code>globus_xio_register_read()</code> semantics: </p>
<p> If the waitforbytes parameter is greater than zero, the read will happen asynchronously and be completed when at least waitforbytes has been read/written. </p>
<p> If the waitforbytes parameter is equal to zero, one of the following alternative behaviors occur: </p>
<p> If the length of the buffer is &gt; 0 the read happens synchronously. If the user is using one of the blocking xio calls, no internal callback will occur. </p>
<p> If the length of the buffer is also 0, the call behaves like an asynchronous notification of data ready to be read. ie, an asynchronous select(). </p>
<p> In any case, when an error occurs before the waitforbytes request has been met, the outgoing nbytes is set to the amount of data actually read before the error occurred. </p>
<p> If the handle is not connected, the user should pass in a data descriptor. After the read, this data_descriptor will contain the contact string of the sender. The user can either get this contact string with <code>GLOBUS_XIO_UDP_GET_CONTACT</code> or pass the data descriptor directly to <code>globus_xio_register_write()</code> to send a message back to the sender. </p>
<p> Also, if the handle is not connected, the waitforbytes should probably be 1 to guarantee that only one packet is received and the sender contact isnt overwritten by multiple packets from different senders. </p>
<p> <code>globus_xio_register_write()</code> semantics: </p>
<p> When performing a write, exactly one UDP packet is sent of the entire buffer length. The waitforbytes parameter is ignored. If the entire buffer can not be written, a <code>GLOBUS_XIO_UDP_ERROR_SHORT_WRITE</code> error will be returned with nbytes set to the number of bytes actually sent. </p>
<p> If the handle is not &#8216;connected&#8217;, a contact string must be set in the data descriptor to <code>globus_xio_register_write()</code>. This can either be done explicitly with <code>GLOBUS_XIO_UDP_SET_CONTACT</code> or implicitly by passing in a data descriptor received from <code>globus_xio_register_read()</code>. </p>
<p> The udp write semantics are always synchronous. No blocking or internal callback will occur when using <code>globus_xio_write()</code>. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
