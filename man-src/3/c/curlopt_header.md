---
title: "curlopt_header(3)"
name: "curlopt_header"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_header/"
description: "CURLOPT_HEADER – pass headers to the data stream"
---

<p>CURLOPT_HEADER &#8211; pass headers to the data stream</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HEADER, long onoff);</p>
<h2>Description</h2>
<p>Pass in <i>onoff</i> set to 1 to tell the library to include the header in the body output for requests with this <i>handle</i>. This option is relevant for protocols that actually have headers or other meta-data (like HTTP and FTP). </p>
<p> When asking to get the header info passed to the same callback as the body, it is not possible to accurately separate them again without detailed knowledge about the protocol in use. </p>
<p> It is often better to use <i><a href="/docs/linux/man/3-curlopt_headerfunction/">CURLOPT_HEADERFUNCTION</a>(3)</i> to get the header data separately.</p>
<h2>Default</h2>
<p>0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_headerfunction/">CURLOPT_HEADERFUNCTION</a></code>(3),</p>
