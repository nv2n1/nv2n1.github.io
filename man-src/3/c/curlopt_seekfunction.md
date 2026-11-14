---
title: "curlopt_seekfunction(3)"
name: "curlopt_seekfunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_seekfunction/"
description: "CURLOPT_SEEKFUNCTION – user callback for seeking in input stream"
---

<p>CURLOPT_SEEKFUNCTION &#8211; user callback for seeking in input stream</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
/* These are the return codes for the seek callbacks */
#define CURL_SEEKFUNC_OK 0
#define CURL_SEEKFUNC_FAIL 1 /* fail the entire transfer */
#define CURL_SEEKFUNC_CANTSEEK 2 /* tell libcurl seeking can't be done, so
 libcurl might try other means instead */
int seek_callback(void *userp, curl_off_t offset, int origin);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SEEKFUNCTION, seek_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This function gets called by libcurl to seek to a certain position in the input stream and can be used to fast forward a file in a resumed upload (instead of reading all uploaded bytes with the normal read function/callback). It is also called to rewind a stream when doing a HTTP PUT or POST with a multi-pass authentication method. The function shall work like <a href="/docs/linux/man/3-fseek/">fseek</a>(3) or <a href="/docs/linux/man/3-lseek/">lseek</a>(3) and it gets SEEK_SET, SEEK_CUR or SEEK_END as argument for <i>origin</i>, although libcurl currently only passes SEEK_SET. </p>
<p> <i>userp</i> is the pointer you set with <i><a href="/docs/linux/man/3-curlopt_seekdata/">CURLOPT_SEEKDATA</a>(3)</i>. </p>
<p> The callback function must return <i>CURL_SEEKFUNC_OK</i> on success, <i>CURL_SEEKFUNC_FAIL</i> to cause the upload operation to fail or <i>CURL_SEEKFUNC_CANTSEEK</i> to indicate that while the seek failed, libcurl is free to work around the problem if possible. The latter can sometimes be done by instead reading from the input or similar. </p>
<p> If you forward the input arguments directly to <a href="/docs/linux/man/3-fseek/">fseek</a>(3) or <a href="/docs/linux/man/3-lseek/">lseek</a>(3), note that the data type for <i>offset</i> is not the same as defined for curl_off_t on many systems!</p>
<h2>Default</h2>
<p>By default, this is NULL and unused.</p>
<h2>Protocols</h2>
<p>HTTP, FTP, SFTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.18.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_seekdata/">CURLOPT_SEEKDATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ioctlfunction/">CURLOPT_IOCTLFUNCTION</a></code>(3),</p>
