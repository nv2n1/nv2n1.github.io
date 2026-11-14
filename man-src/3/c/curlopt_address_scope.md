---
title: "curlopt_address_scope(3)"
name: "curlopt_address_scope"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_address_scope/"
description: "CURLOPT_ADDRESS_SCOPE – set scope for local IPv6 addresses"
---

<p>CURLOPT_ADDRESS_SCOPE &#8211; set scope for local IPv6 addresses</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_ADDRESS_SCOPE, long scope);</p>
<h2>Description</h2>
<p>Pass a long specifying the scope_id value to use when connecting to IPv6 link-local or site-local addresses.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>All, when using IPv6</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.19.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_stderr/">CURLOPT_STDERR</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a></code>(3),</p>
