---
title: "curlopt_nobody(3)"
name: "curlopt_nobody"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_nobody/"
description: "CURLOPT_NOBODY – do the download request without getting the body"
---

<p>CURLOPT_NOBODY &#8211; do the download request without getting the body</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_NOBODY, long opt);</p>
<h2>Description</h2>
<p>A long parameter set to 1 tells libcurl to not include the body-part in the output when doing what would otherwise be a download. For HTTP(S), this makes libcurl do a HEAD request. For most other protocols it means just not asking to transfer the body data. </p>
<p> Enabling this option means asking for a download but without a body.</p>
<h2>Default</h2>
<p>0, the body is transferred</p>
<h2>Protocols</h2>
<p>Most</p>
<h2>Example</h2>
<pre>curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 /* get us the resource without a body! */ 
 curl_easy_setopt(curl, CURLOPT_NOBODY, 1L);
 /* Perform the request */ 
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_httpget/">CURLOPT_HTTPGET</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_post/">CURLOPT_POST</a></code>(3),</p>
