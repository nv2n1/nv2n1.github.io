---
title: "globus_gsi_callback-h(3)"
name: "globus_gsi_callback-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_callback-h/"
description: "globus_gsi_callback.h – Globus GSI Callback."
---

<p>globus_gsi_callback.h &#8211; Globus GSI Callback.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217;<br />
 #include &#8216;globus_gsi_cert_utils.h&#8217;<br />
 #include &#8216;openssl/x509.h&#8217; </p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_GSI_CALLBACK_MODULE</code> </p>
<h3>Typedefs</h3>
<p>typedef struct<br />
 globus_l_gsi_callback_data_s * <code>globus_gsi_callback_data_t</code>&quot; </p>
<p> typedef int(* <code>globus_gsi_extension_callback_t</code> )(<code>globus_gsi_callback_data_t</code> callback_data, X509_EXTENSION *extension) </p>
<h2>Detailed Description</h2>
<p>Globus GSI Callback. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Sam Lang </p>
<p> Sam Meder</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_gsi_callback from the source code.</p>
