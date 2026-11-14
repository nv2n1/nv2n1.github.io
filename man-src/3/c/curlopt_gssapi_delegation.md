---
title: "curlopt_gssapi_delegation(3)"
name: "curlopt_gssapi_delegation"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_gssapi_delegation/"
description: "CURLOPT_GSSAPI_DELEGATION – set allowed GSS-API delegation"
---

<p>CURLOPT_GSSAPI_DELEGATION &#8211; set allowed GSS-API delegation</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_GSSAPI_DELEGATION, long level);</p>
<h2>Description</h2>
<p>Set the long parameter <i>level</i> to CURLGSSAPI_DELEGATION_FLAG to allow unconditional GSSAPI credential delegation. The delegation is disabled by default since 7.21.7. Set the parameter to CURLGSSAPI_DELEGATION_POLICY_FLAG to delegate only if the OK-AS-DELEGATE flag is set in the service ticket in case this feature is supported by the GSS-API implementation and the definition of GSS_C_DELEG_POLICY_FLAG was available at compile-time.</p>
<h2>Default</h2>
<p>CURLGSSAPI_DELEGATION_NONE</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.22.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_httpauth/">CURLOPT_HTTPAUTH</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxyauth/">CURLOPT_PROXYAUTH</a></code>(3),</p>
