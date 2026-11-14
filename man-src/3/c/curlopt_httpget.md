---
title: "curlopt_httpget(3)"
name: "curlopt_httpget"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_httpget/"
description: "CURLOPT_HTTPGET – ask for a HTTP GET request"
---

<p>CURLOPT_HTTPGET &#8211; ask for a HTTP GET request</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HTTPGET, long useget);</p>
<h2>Description</h2>
<p>Pass a long. If <i>useget</i> is 1, this forces the HTTP request to get back to using GET. Usable if a POST, HEAD, PUT, etc has been used previously using the same curl <i>handle</i>. </p>
<p> When setting <i><a href="/docs/linux/man/3-curlopt_httpget/">CURLOPT_HTTPGET</a>(3)</i> to 1, it will automatically set <i><a href="/docs/linux/man/3-curlopt_nobody/">CURLOPT_NOBODY</a>(3)</i> to 0 and <i><a href="/docs/linux/man/3-curlopt_upload/">CURLOPT_UPLOAD</a>(3)</i> to 0.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>HTTP(S)</p>
<h2>Example</h2>
<pre>curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 /* use a GET to fetch this */ 
 curl_easy_setopt(curl, CURLOPT_HTTPGET, 1L);
 /* Perform the request */ 
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_nobody/">CURLOPT_NOBODY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_upload/">CURLOPT_UPLOAD</a></code>(3),</p>
