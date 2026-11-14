---
title: "curlopt_certinfo(3)"
name: "curlopt_certinfo"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_certinfo/"
description: "CURLOPT_CERTINFO – request SSL certificate information"
---

<p>CURLOPT_CERTINFO &#8211; request SSL certificate information</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CERTINFO, long certinfo);</p>
<h2>Description</h2>
<p>Pass a long set to 1 to enable libcurl&#8217;s certificate chain info gatherer. With this enabled, libcurl (if built with OpenSSL, NSS or GSKit) will extract lots of information and data about the certificates in the certificate chain used in the SSL connection. This data may then be retrieved after a transfer using <i><a href="/docs/linux/man/3-curl_easy_getinfo/">curl_easy_getinfo</a>(3)</i> and its option <i>CURLINFO_CERTINFO</i>.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>All TLS-based</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.19.1</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_cainfo/">CURLOPT_CAINFO</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a></code>(3),</p>
