---
title: "curlopt_put(3)"
name: "curlopt_put"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_put/"
description: "CURLOPT_PUT – make a HTTP PUT request"
---

<p>CURLOPT_PUT &#8211; make a HTTP PUT request</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PUT, long put);</p>
<h2>Description</h2>
<p>A parameter set to 1 tells the library to use HTTP PUT to transfer data. The data should be set with <i><a href="/docs/linux/man/3-curlopt_readdata/">CURLOPT_READDATA</a>(3)</i> and <i><a href="/docs/linux/man/3-curlopt_infilesize/">CURLOPT_INFILESIZE</a>(3)</i>. </p>
<p> This option is <code>deprecated</code> since version 7.12.1. Use <i><a href="/docs/linux/man/3-curlopt_upload/">CURLOPT_UPLOAD</a>(3)</i>!</p>
<h2>Default</h2>
<p>0, disabled</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Deprecated since 7.12.1. Do not use.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_upload/">CURLOPT_UPLOAD</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpget/">CURLOPT_HTTPGET</a></code>(3),</p>
