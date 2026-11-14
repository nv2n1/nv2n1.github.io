---
title: "globus_gsi_sysconfig_shared(3)"
name: "globus_gsi_sysconfig_shared"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_sysconfig_shared/"
description: "Functions for all platforms –"
---

<h2 class="name">NAME</h2>
<p> Functions for all platforms &#8211; </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_gsi_sysconfig_get_unique_proxy_filename</code> (char **unique_filename)<br />
 <i>Get Unique Proxy Filename. </i></p>
<h2>Detailed Description</h2>
<p> These functions are platform independent members of the Globus GSI System Configuration API.</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_gsi_sysconfig_get_unique_proxy_filename (char **unique_filename)</h3>
<p> Get Unique Proxy Filename. Get a unique proxy cert filename. This is mostly used for delegated proxy credentials. Each filename returned is going to be unique for each time the function is called. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>unique_filename</i> the unique filename for a delegated proxy cert</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> GLOBUS_SUCCESS or an error object identifier</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_sysconfig from the source code. </p>
<h2>Index</h2>
