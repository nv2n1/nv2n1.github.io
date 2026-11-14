---
title: "curlopt_upload(3)"
name: "curlopt_upload"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_upload/"
description: "CURLOPT_UPLOAD – enable data upload"
---

<p>CURLOPT_UPLOAD &#8211; enable data upload</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_UPLOAD, long upload);</p>
<h2>Description</h2>
<p>The long parameter <i>upload</i> set to 1 tells the library to prepare for and perform an upload. The <i><a href="/docs/linux/man/3-curlopt_readdata/">CURLOPT_READDATA</a>(3)</i> and <i><a href="/docs/linux/man/3-curlopt_infilesize/">CURLOPT_INFILESIZE</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_infilesize_large/">CURLOPT_INFILESIZE_LARGE</a>(3)</i> options are also interesting for uploads. If the protocol is HTTP, uploading means using the PUT request unless you tell libcurl otherwise. </p>
<p> Using PUT with HTTP 1.1 implies the use of a &quot;Expect: 100-continue&quot; header. You can disable this header with <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i> as usual. </p>
<p> If you use PUT to a HTTP 1.1 server, you can upload data without knowing the size before starting the transfer if you use chunked encoding. You enable this by adding a header like &quot;Transfer-Encoding: chunked&quot; with <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i>. With HTTP 1.0 or without chunked transfer, you must specify the size.</p>
<h2>Default</h2>
<p>0, default is download</p>
<h2>Protocols</h2>
<p>Most</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 /* we want to use our own read function */
 curl_easy_setopt(curl, CURLOPT_READFUNCTION, read_callback);
 /* enable uploading */
 curl_easy_setopt(curl, CURLOPT_UPLOAD, 1L);
 /* specify target */
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a href="ftp://example.com/dir/to/newfile">ftp://example.com/dir/to/newfile</a>&quot;);
 /* now specify which pointer to pass to our callback */
 curl_easy_setopt(curl, CURLOPT_READDATA, hd_src);
 /* Set the size of the file to upload */
 curl_easy_setopt(curl, CURLOPT_INFILESIZE_LARGE, (curl_off_t)fsize);
 /* Now run off and do what you've been told! */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_put/">CURLOPT_PUT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_readfunction/">CURLOPT_READFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_infilesize_large/">CURLOPT_INFILESIZE_LARGE</a></code>(3),</p>
