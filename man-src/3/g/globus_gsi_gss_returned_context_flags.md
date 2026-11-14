---
title: "globus_gsi_gss_returned_context_flags(3)"
name: "globus_gsi_gss_returned_context_flags"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_gss_returned_context_flags/"
description: "Return Flags –"
---

<h2 class="name">NAME</h2>
<p> Return Flags &#8211; </p>
<p> Return Flags.</p>
<h3>Macros</h3>
<p> #define <code>GSS_C_GLOBUS_RECEIVED_LIMITED_PROXY_FLAG</code><br />
 <i>Received Limited Proxy Flag. </i><br />
 #define <code>GSS_C_GLOBUS_RECEIVED_LIMITED_PROXY_DURING_DELEGATION_FLAG</code><br />
 <i>Received Limited Proxy During Delegation Flag. </i><br />
 #define <code>GSS_C_GLOBUS_LIMITED_PROXY_MANY_FLAG</code><br />
 <i>Limited Proxy Many Flag. </i></p>
<h2>Detailed Description</h2>
<p> Return Flags. </p>
<p> These macros set the RETURNED context type &#8211; these will be be set (or not) in the context&#8217;s ret_flags</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GSS_C_GLOBUS_LIMITED_PROXY_MANY_FLAG</h3>
<p> Limited Proxy Many Flag.</p>
<h3>#define GSS_C_GLOBUS_RECEIVED_LIMITED_PROXY_DURING_DELEGATION_FLAG</h3>
<p> Received Limited Proxy During Delegation Flag. If the proxy received is a limited proxy received during delegation, this flag is set in the returned flags</p>
<h3>#define GSS_C_GLOBUS_RECEIVED_LIMITED_PROXY_FLAG</h3>
<p> Received Limited Proxy Flag. If the proxy received is a limited proxy, this flag will be set in the returned context flags (ret_flags)</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gssapi_gsi from the source code. </p>
<h2>Index</h2>
