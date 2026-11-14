---
title: "globus_gsi_gss_requested_context_flags(3)"
name: "globus_gsi_gss_requested_context_flags"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_gsi_gss_requested_context_flags/"
description: "Request Flags –"
---

<h2 class="name">NAME</h2>
<p> Request Flags &#8211; </p>
<p> Request Flags.</p>
<h3>Macros</h3>
<p> #define <code>GSS_C_GLOBUS_DONT_ACCEPT_LIMITED_PROXY_FLAG</code><br />
 <i>No limited proxy flag. </i><br />
 #define <code>GSS_C_GLOBUS_DELEGATE_LIMITED_PROXY_FLAG</code><br />
 <i>Delegate Limited Proxy Flag. </i><br />
 #define <code>GSS_C_GLOBUS_ACCEPT_PROXY_SIGNED_BY_LIMITED_PROXY_FLAG</code><br />
 <i>Accept Proxy Signed By Limited Proxy Flag. </i><br />
 #define <code>GSS_C_GLOBUS_ALLOW_MISSING_SIGNING_POLICY</code><br />
 <i>Allow Missing Signing Policy Flag. </i><br />
 #define <code>GSS_C_GLOBUS_FORCE_SSL3</code><br />
 <i>Force SSLv3 Flag. </i></p>
<h2>Detailed Description</h2>
<p> Request Flags. </p>
<p> These macros set the REQUESTED type of context &#8211; these should be set (or not) in the context&#8217;s req_flags (or in the context&#8217;s ret_flags if accept_sec_context is being called)</p>
<h2>Macro Definition Documentation</h2>
<h3>#define GSS_C_GLOBUS_ACCEPT_PROXY_SIGNED_BY_LIMITED_PROXY_FLAG</h3>
<p> Accept Proxy Signed By Limited Proxy Flag. Set if you want to accept proxies signed by limited proxies</p>
<h3>#define GSS_C_GLOBUS_ALLOW_MISSING_SIGNING_POLICY</h3>
<p> Allow Missing Signing Policy Flag. Set if you want to allow CA certs without a signing policy to verify.</p>
<h3>#define GSS_C_GLOBUS_DELEGATE_LIMITED_PROXY_FLAG</h3>
<p> Delegate Limited Proxy Flag. Set if you want the delegated proxy to be a limited proxy</p>
<h3>#define GSS_C_GLOBUS_DONT_ACCEPT_LIMITED_PROXY_FLAG</h3>
<p> No limited proxy flag. Set if you don&#8217;t want a context to accept a limited proxy. If this flag is set, and a limited proxy is received, the call will not be successful and the context will not be set up</p>
<h3>#define GSS_C_GLOBUS_FORCE_SSL3</h3>
<p> Force SSLv3 Flag. Set if you want to force SSLv3 instead of negotiating TLSv1 or SSLv3</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_gssapi_gsi from the source code. </p>
<h2>Index</h2>
