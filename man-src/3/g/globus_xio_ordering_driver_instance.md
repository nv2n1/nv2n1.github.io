---
title: "globus_xio_ordering_driver_instance(3)"
name: "globus_xio_ordering_driver_instance"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_ordering_driver_instance/"
description: "Opening/Closing – Ordering driver is a transform driver and thus has to be used on top of a transport driver. An XIO handle with the ordering driver can be created with either globus_xio_handle_cre..."
---

<h2 class="name">NAME</h2>
<p> Opening/Closing &#8211; Ordering driver is a transform driver and thus has to be used on top of a transport driver. An XIO handle with the ordering driver can be created with either <code>globus_xio_handle_create()</code> or <code>globus_xio_server_register_accept()</code>. </p>
<p> When the XIO handle is closed, the ordering driver will destroy its internal resources. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
