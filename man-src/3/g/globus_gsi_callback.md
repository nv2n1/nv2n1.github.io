---
title: "globus_gsi_callback(3)"
name: "globus_gsi_callback"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_callback/"
description: "Globus GSI Callback –"
---

<h2 class="name">NAME</h2>
<p> Globus GSI Callback &#8211; </p>
<h3>Modules</h3>
<p> <code>Activation</code> </p>
<p> <code>Callback Functions</code> </p>
<p> <code>Callback Data Functions</code> </p>
<h3>Typedefs</h3>
<p> typedef int(* <code>globus_gsi_extension_callback_t</code> )(<code>globus_gsi_callback_data_t</code> callback_data, X509_EXTENSION *extension) </p>
<h2>Detailed Description</h2>
<p> The Globus GSI Callback library. This library contains functions that extend OpenSSL path validation. </p>
<dl>
<dt>&bull;</p>
<dd> <code>Activation</code></p>
<dt>&bull;</p>
<dd> <code>Callback Functions</code></p>
<dt>&bull;</p>
<dd> <code>Callback Data Functions</code></dl>
<h2>Typedef Documentation</h2>
<h3>typedef int(* globus_gsi_extension_callback_t)(<code>globus_gsi_callback_data_t</code> callback_data, X509_EXTENSION *extension)</h3>
<p> Typedef for a callback that may be registered for dealing with unhandled X.509 extension</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_callback from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Author</a></p>
<dd></dl>
