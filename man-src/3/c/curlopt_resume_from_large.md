---
title: "curlopt_resume_from_large(3)"
name: "curlopt_resume_from_large"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_resume_from_large/"
description: "CURLOPT_RESUME_FROM_LARGE – set a point to resume transfer from"
---

<p>CURLOPT_RESUME_FROM_LARGE &#8211; set a point to resume transfer from</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_RESUME_FROM_LARGE,
 curl_off_t from);</pre>
<h2>Description</h2>
<p>Pass a curl_off_t as parameter. It contains the offset in number of bytes that you want the transfer to start from. Set this option to 0 to make the transfer start from the beginning (effectively disabling resume). For FTP, set this option to -1 to make the transfer start from the end of the target file (useful to continue an interrupted upload). </p>
<p> When doing uploads with FTP, the resume position is where in the local/source file libcurl should try to resume the upload from and it will then append the source file to the remote target file.</p>
<h2>Default</h2>
<p>0, not used</p>
<h2>Protocols</h2>
<p>HTTP, FTP, SFTP, FILE</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 curl_off_t resume_position = GET_IT_SOMEHOW;
 curl_off_t file_size = GET_IT_SOMEHOW_AS_WELL;
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a href="ftp://example.com">ftp://example.com</a>&quot;);
 /* resuming upload at this position, possibly beyond 2GB */
 curl_easy_setopt(curl, CURLOPT_RESUME_FROM_LARGE, resume_position);
 /* ask for upload */
 curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);
 /* set total data amount to expect */
 curl_easy_setopt(curl, CURLOPT_INFILESIZE_LARGE, file_size);
 /* Perform the request */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Added in 7.11.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_resume_from/">CURLOPT_RESUME_FROM</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_range/">CURLOPT_RANGE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_infilesize_large/">CURLOPT_INFILESIZE_LARGE</a></code>(3),</p>
