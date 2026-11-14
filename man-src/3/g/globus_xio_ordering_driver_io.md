---
title: "globus_xio_ordering_driver_io(3)"
name: "globus_xio_ordering_driver_io"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_ordering_driver_io/"
description: "Reading/Writing – Ordering driver does not allow multiple globus_xio_register_read() to be outstanding. This limitation is there to enforce that the users get the read callback in order. There is a..."
---

<h2 class="name">NAME</h2>
<p> Reading/Writing &#8211; Ordering driver does not allow multiple <code>globus_xio_register_read()</code> to be outstanding. This limitation is there to enforce that the users get the read callback in order. There is a known issue in enforcing the order in which read callbacks are delivered with multiple outstanding reads. This limitation does not restrict the use of parallel reads feature provided by the underlying transport driver. <code>GLOBUS_XIO_ORDERING_SET_MAX_READ_COUNT</code> on the attr can be used to specify the number of parallel reads. Ordering will have a maximum of this many number of reads outstanding to the driver below it on the stack. It buffers the data read and delivers it to the user in order. </p>
<p> <code>globus_xio_register_write()</code> does not enforce any restriction. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
