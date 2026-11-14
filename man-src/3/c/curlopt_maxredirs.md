---
title: "curlopt_maxredirs(3)"
name: "curlopt_maxredirs"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_maxredirs/"
description: "CURLOPT_MAXREDIRS – maximum number of redirects allowed"
---

<p>CURLOPT_MAXREDIRS &#8211; maximum number of redirects allowed</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_MAXREDIRS, long amount);</p>
<h2>Description</h2>
<p>Pass a long. The set number will be the redirection limit <i>amount</i>. If that many redirections have been followed, the next redirect will cause an error (<i>CURLE_TOO_MANY_REDIRECTS</i>). This option only makes sense if the <i><a href="/docs/linux/man/3-curlopt_followlocation/">CURLOPT_FOLLOWLOCATION</a>(3)</i> is used at the same time. </p>
<p> Setting the limit to 0 will make libcurl refuse any redirect. </p>
<p> Set it to -1 for an infinite number of redirects.</p>
<h2>Default</h2>
<p>-1, unlimited</p>
<h2>Protocols</h2>
<p>HTTP(S)</p>
<h2>Example</h2>
<pre>curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com/">http://example.com/</a>&quot;);
 /* enable redirect following */
 curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
 /* allow three redirects */
 curl_easy_setopt(curl, CURLOPT_MAXREDIRS, 3L);
 /* Perform the request */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_followlocation/">CURLOPT_FOLLOWLOCATION</a></code>(3),</p>
