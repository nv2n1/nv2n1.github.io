---
title: "curlopt_range(3)"
name: "curlopt_range"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_range/"
description: "CURLOPT_RANGE – set byte range to request"
---

<p>CURLOPT_RANGE &#8211; set byte range to request</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_RANGE, char *range);</p>
<h2>Description</h2>
<p>Pass a char * as parameter, which should contain the specified range you want to retrieve. It should be in the format &quot;X-Y&quot;, where either X or Y may be left out and X and Y are byte indexes. </p>
<p> HTTP transfers also support several intervals, separated with commas as in <i>&quot;X-Y,N-M&quot;</i>. Using this kind of multiple intervals will cause the HTTP server to send the response document in pieces (using standard MIME separation techniques). For RTSP, the formatting of a range should follow RFC2326 Section 12.29. For RTSP, byte ranges are <code>not</code> permitted. Instead, ranges should be given in npt, utc, or smpte formats. </p>
<p> Pass a NULL to this option to disable the use of ranges.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP, FTP, FILE, RTSP and SFTP.</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 /* get the first 200 bytes */
 curl_easy_setopt(curl, CURLOPT_RANGE, &quot;0-199&quot;);
 /* Perform the request */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>FILE since 7.18.0, RTSP since 7.20.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK on success or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_resume_from/">CURLOPT_RESUME_FROM</a></code>(3),</p>
