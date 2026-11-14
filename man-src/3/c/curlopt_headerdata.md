---
title: "curlopt_headerdata(3)"
name: "curlopt_headerdata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_headerdata/"
description: "CURLOPT_HEADERDATA – pointer to pass to header callback"
---

<p>CURLOPT_HEADERDATA &#8211; pointer to pass to header callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HEADERDATA, void *pointer);</p>
<h2>Description</h2>
<p>Pass a <i>pointer</i> to be used to write the header part of the received data to. </p>
<p> If <i><a href="/docs/linux/man/3-curlopt_writefunction/">CURLOPT_WRITEFUNCTION</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_headerfunction/">CURLOPT_HEADERFUNCTION</a>(3)</i> is used, <i>pointer</i> will be passed in to the respective callback. </p>
<p> If neither of those options are set, <i>pointer</i> must be a valid FILE * and it will be used by a plain fwrite() to write headers to.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_headerfunction/">CURLOPT_HEADERFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_writefunction/">CURLOPT_WRITEFUNCTION</a></code>(3),</p>
