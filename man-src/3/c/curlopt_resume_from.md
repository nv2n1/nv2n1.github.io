---
title: "curlopt_resume_from(3)"
name: "curlopt_resume_from"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_resume_from/"
description: "CURLOPT_RESUME_FROM – set a point to resume transfer from"
---

<p>CURLOPT_RESUME_FROM &#8211; set a point to resume transfer from</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_RESUME_FROM, long from);</p>
<h2>Description</h2>
<p>Pass a long as parameter. It contains the offset in number of bytes that you want the transfer to start from. Set this option to 0 to make the transfer start from the beginning (effectively disabling resume). For FTP, set this option to -1 to make the transfer start from the end of the target file (useful to continue an interrupted upload). </p>
<p> When doing uploads with FTP, the resume position is where in the local/source file libcurl should try to resume the upload from and it will then append the source file to the remote target file. </p>
<p> If you need to resume a transfer beyond the 2GB limit, use <i><a href="/docs/linux/man/3-curlopt_resume_from_large/">CURLOPT_RESUME_FROM_LARGE</a>(3)</i> instead.</p>
<h2>Default</h2>
<p>0, not used</p>
<h2>Protocols</h2>
<p>HTTP, FTP, SFTP, FILE</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a href="ftp://example.com">ftp://example.com</a>&quot;);
 /* resume upload at byte index 200 */
 curl_easy_setopt(curl, CURLOPT_RESUME_FROM, 200L);
 /* ask for upload */
 curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);
 /* set total data amount to expect */
 curl_easy_setopt(curl, CURLOPT_INFILESIZE, size_of_file);
 /* Perform the request */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_resume_from_large/">CURLOPT_RESUME_FROM_LARGE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_range/">CURLOPT_RANGE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_infilesize/">CURLOPT_INFILESIZE</a></code>(3),</p>
