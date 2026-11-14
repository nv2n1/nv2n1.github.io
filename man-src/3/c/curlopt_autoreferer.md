---
title: "curlopt_autoreferer(3)"
name: "curlopt_autoreferer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_autoreferer/"
description: "CURLOPT_AUTOREFERER – automatically update the referer header"
---

<p>CURLOPT_AUTOREFERER &#8211; automatically update the referer header</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_AUTOREFERER, long autorefer);</p>
<h2>Description</h2>
<p>Pass a parameter set to 1 to enable this. When enabled, libcurl will automatically set the Referer: header field in HTTP requests where it follows a Location: redirect.</p>
<h2>Default</h2>
<p>0, disabled</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_referer/">CURLOPT_REFERER</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_followlocation/">CURLOPT_FOLLOWLOCATION</a></code>(3),</p>
