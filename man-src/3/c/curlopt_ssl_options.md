---
title: "curlopt_ssl_options(3)"
name: "curlopt_ssl_options"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssl_options/"
description: "CURLOPT_SSL_OPTIONS – set SSL behavior options"
---

<p>CURLOPT_SSL_OPTIONS &#8211; set SSL behavior options</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSL_OPTIONS, long bitmask);</p>
<h2>Description</h2>
<p>Pass a long with a bitmask to tell libcurl about specific SSL behaviors. </p>
<p> <i>CURLSSLOPT_ALLOW_BEAST</i> is the only supported bit and by setting this the user will tell libcurl to not attempt to use any workarounds for a security flaw in the SSL3 and TLS1.0 protocols. If this option isn&#8217;t used or this bit is set to 0, the SSL layer libcurl uses may use a work-around for this flaw although it might cause interoperability problems with some (older) SSL implementations. WARNING: avoiding this work-around lessens the security, and by setting this option to 1 you ask for exactly that.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>All TLS-based protocols</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.25.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sslversion/">CURLOPT_SSLVERSION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssl_cipher_list/">CURLOPT_SSL_CIPHER_LIST</a></code>(3),</p>
