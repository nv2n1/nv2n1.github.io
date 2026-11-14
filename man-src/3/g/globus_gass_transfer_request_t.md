---
title: "globus_gass_transfer_request_t(3)"
name: "globus_gass_transfer_request_t"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gass_transfer_request_t/"
description: "globus_gass_transfer_request_t –"
---

<h2 class="name">NAME</h2>
<p> globus_gass_transfer_request_t &#8211; </p>
<p> Request handle.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;globus_gass_transfer.h&gt;</p>
<h2>Detailed Description</h2>
<p> Request handle. </p>
<p> A request handle is associated with each file transfer operation. The same structure is used for both client- and server- side requests. For client operations, the initial call to <code>globus_gass_transfer_get()</code>, <code>globus_gass_transfer_register_get()</code>, <code>globus_gass_transfer_get()</code>, <code>globus_gass_transfer_register_put()</code>, <code>globus_gass_transfer_append()</code>, <code>globus_gass_transfer_register_append()</code> initializes the request. For server operations, the request is initialized by calling globus_gass_transfer_accept(). </p>
<p> The functions in the <code>request section</code> of this manual describe the functions available for accessing information from a request handle. </p>
<p> Each request handle should be destroyed by calling <code>globus_gass_transfer_request_destroy()</code> once the user has completed processing the request. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gass_transfer from the source code. </p>
<h2>Index</h2>
