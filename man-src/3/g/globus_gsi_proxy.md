---
title: "globus_gsi_proxy(3)"
name: "globus_gsi_proxy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_proxy/"
description: "Globus GSI Proxy API –"
---

<h2 class="name">NAME</h2>
<p> Globus GSI Proxy API &#8211; </p>
<h3>Modules</h3>
<p> <code>Activation</code> </p>
<p> <code>Handle Management</code><br />
 <i>Create/Destroy/Modify a GSI Proxy Handle. </i><br />
 <code>Handle Attributes</code> </p>
<p> <code>Proxy Operations</code><br />
 <i>Initiate a proxy operation. </i><br />
 <code>Proxy Constants</code> </p>
<h2>Detailed Description</h2>
<p> The globus_gsi_proxy library is motivated by the desire to provide a abstraction layer for the proxy creation and delegation process. For background on this process please refer to the proxy certificate profile draft. </p>
<p> Any program that uses Globus GSI Proxy functions must include &#8216;globus_gsi_proxy.h&#8217;. </p>
<p> We envision the API being used in the following manner: </p>
<p> Delegator Delegatee set desired cert info extension in the handle by using the handle set functions. <code>globus_gsi_proxy_create_req()</code> <code>globus_gsi_proxy_inquire_req()</code> modify cert info extension by using <code>handle set/get/clear functions.</code> <code>globus_gsi_proxy_sign_req()</code> <code>globus_gsi_proxy_assemble_cred()</code> The API documentation is divided into the following sections</p>
<dl>
<dt>&bull;</p>
<dd> <code>Activation</code></p>
<dt>&bull;</p>
<dd> <code>Handle Management</code></p>
<dt>&bull;</p>
<dd> <code>Handle Attributes</code></p>
<dt>&bull;</p>
<dd> <code>Proxy Operations</code></p>
<dt>&bull;</p>
<dd> <code>Proxy Constants</code></dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gsi_proxy_core from the source code. </p>
<h2>Index</h2>
