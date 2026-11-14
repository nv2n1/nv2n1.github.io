---
title: "file_driver_io(3)"
name: "file_driver_io"
section: "3"
letter: "f"
url: "/docs/linux/man/3-file_driver_io/"
description: "Reading/Writing –"
---

<h2 class="name">NAME</h2>
<p> Reading/Writing &#8211; </p>
<p> Both the <code>globus_xio_register_read()</code> and <code>globus_xio_register_write()</code> calls follow similar semantics as described below. Both the <code>globus_xio_register_read()</code> and <code>globus_xio_register_write()</code> calls follow similar semantics as described below. </p>
<p> If the waitforbytes parameter is greater than zero, the io will happen asynchronously and be completed when at least waitforbytes has been read/written. </p>
<p> If the waitforbytes parameter is equal to zero, one of the following alternative behaviors occur: </p>
<p> If the length of the buffer is &gt; 0 the read or write happens synchronously. If the user is using one of the blocking xio calls, no internal callback will occur. </p>
<p> If the length of the buffer is also 0, the call behaves like an asynchronous notification of data ready to be either read or written. ie, an asynchronous select(). </p>
<p> In any case, when an error or EOF occurs before the waitforbytes request has been met, the outgoing nbytes is set to the amount of data actually read/written before the error or EOF occurred. </p>
<p> You may either use GLOBUS_XIO_FILE_SEEK or GLOBUS_XIO_SEEK to position the file pointer before each read or write or you can specify the desired offset on a data descriptor with the xio cmd, GLOBUS_XIO_DD_SET_OFFSET. simultaneous reading and writing is only predictable if the data descriptor method is used. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus xio from the source code. </p>
<h2>Index</h2>
