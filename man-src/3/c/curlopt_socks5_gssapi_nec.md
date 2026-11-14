---
title: "curlopt_socks5_gssapi_nec(3)"
name: "curlopt_socks5_gssapi_nec"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_socks5_gssapi_nec/"
description: "CURLOPT_SOCKS5_GSSAPI_NEC – set socks proxy gssapi negotiation protection"
---

<p>CURLOPT_SOCKS5_GSSAPI_NEC &#8211; set socks proxy gssapi negotiation protection</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SOCKS5_GSSAPI_NEC, long nec);</p>
<h2>Description</h2>
<p>Pass a long set to 1 to enable or 0 to disable. As part of the gssapi negotiation a protection mode is negotiated. The RFC1961 says in section 4.3/4.4 it should be protected, but the NEC reference implementation does not. If enabled, this option allows the unprotected exchange of the protection mode negotiation.</p>
<h2>Default</h2>
<p>?</p>
<h2>Protocols</h2>
<p>Most</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.19.4</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_socks5_gssapi_service/">CURLOPT_SOCKS5_GSSAPI_SERVICE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a></code>(3),</p>
