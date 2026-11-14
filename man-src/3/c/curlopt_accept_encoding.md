---
title: "curlopt_accept_encoding(3)"
name: "curlopt_accept_encoding"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_accept_encoding/"
description: "CURLOPT_ACCEPT_ENCODING – enables automatic decompression of HTTP downloads"
---

<p>CURLOPT_ACCEPT_ENCODING &#8211; enables automatic decompression of HTTP downloads</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_ACCEPT_ENCODING, char *enc);</p>
<h2>Description</h2>
<p>Pass a char * argument specifying what encoding you&#8217;d like. </p>
<p> Sets the contents of the Accept-Encoding: header sent in a HTTP request, and enables decoding of a response when a Content-Encoding: header is received. Three encodings are supported: <i>identity</i>, which does nothing, <i>deflate</i> which requests the server to compress its response using the zlib algorithm, and <i>gzip</i> which requests the gzip algorithm. </p>
<p> If a zero-length string is set like &quot;&quot;, then an Accept-Encoding: header containing all built-in supported encodings is sent. </p>
<p> You can also opt to just include the Accept-Encoding: header in your request with <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i> but then there will be no automatic decompressing when receiving data. </p>
<p> This is a request, not an order; the server may or may not do it. This option must be set (to any non-NULL value) or else any unsolicited encoding done by the server is ignored. See the special file lib/README.encoding for further details.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>This option was called CURLOPT_ENCODING before 7.21.6</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_transfer_encoding/">CURLOPT_TRANSFER_ENCODING</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_http_content_decoding/">CURLOPT_HTTP_CONTENT_DECODING</a></code>(3),</p>
