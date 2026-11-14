---
title: "curlopt_transfer_encoding(3)"
name: "curlopt_transfer_encoding"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_transfer_encoding/"
description: "CURLOPT_TRANSFER_ENCODING – ask for HTTP Transfer Encoding"
---

<p>CURLOPT_TRANSFER_ENCODING &#8211; ask for HTTP Transfer Encoding</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TRANSFER_ENCODING, long enable);</p>
<h2>Description</h2>
<p>Pass a long set to 1 to <i>enable</i> or 0 to disable. </p>
<p> Adds a request for compressed Transfer Encoding in the outgoing HTTP request. If the server supports this and so desires, it can respond with the HTTP response sent using a compressed Transfer-Encoding that will be automatically uncompressed by libcurl on reception. </p>
<p> Transfer-Encoding differs slightly from the Content-Encoding you ask for with <code><a href="/docs/linux/man/3-curlopt_accept_encoding/">CURLOPT_ACCEPT_ENCODING</a>(3)</code> in that a Transfer-Encoding is strictly meant to be for the transfer and thus MUST be decoded before the data arrives in the client. Traditionally, Transfer-Encoding has been much less used and supported by both HTTP clients and HTTP servers.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.21.6</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_accept_encoding/">CURLOPT_ACCEPT_ENCODING</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_http_transfer_decoding/">CURLOPT_HTTP_TRANSFER_DECODING</a></code>(3),</p>
