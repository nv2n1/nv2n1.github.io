---
title: "globus_xio_file_driver_instance(3)"
name: "globus_xio_file_driver_instance"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_xio_file_driver_instance/"
description: "Opening/Closing – An XIO handle with the file driver can be created with globus_xio_handle_create()"
---

<h2 class="name">NAME</h2>
<p> Opening/Closing &#8211; An XIO handle with the file driver can be created with <code>globus_xio_handle_create()</code> </p>
<p> If there is no handle set on the attr passed to the <code>globus_xio_open()</code> call, it performs the equivalent of an open() call. In this case, the contact string must contain either a pathname or one of </p>
<p><a href="stdin://,">stdin://,</a> <a href="stdout://,">stdout://,</a> or <a href="stderr://.">stderr://.</a> If a pathname is used, that path is opened. If one of the schemes are used the corresponding stdio handle is used (retrieved with fileno()). </p>
<p> In either of the above cases, it is most efficient to call the blocking version of <code>globus_xio_open()</code>. It is also safe to call within a locked critical section. </p>
<p> When the XIO handle is closed, the file driver will destroy its internal resources and close the fd (unless this fd was set on an attr or converted from one of the stdio handles).</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_xio from the source code. </p>
<h2>Index</h2>
