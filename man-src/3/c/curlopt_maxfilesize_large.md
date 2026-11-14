---
title: "curlopt_maxfilesize_large(3)"
name: "curlopt_maxfilesize_large"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_maxfilesize_large/"
description: "CURLOPT_MAXFILESIZE_LARGE – maximum file size allowed to download"
---

<p>CURLOPT_MAXFILESIZE_LARGE &#8211; maximum file size allowed to download</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_MAXFILESIZE_LARGE,
 curl_off_t size);</pre>
<h2>Description</h2>
<p>Pass a curl_off_t as parameter. This allows you to specify the maximum <i>size</i> (in bytes) of a file to download. If the file requested is found larger than this value, the transfer will not start and <i>CURLE_FILESIZE_EXCEEDED</i> will be returned. </p>
<p> The file size is not always known prior to download, and for such files this option has no effect even if the file transfer ends up being larger than this given limit. This concerns both FTP and HTTP transfers.</p>
<h2>Default</h2>
<p>None</p>
<h2>Protocols</h2>
<p>FTP and HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.11.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_maxfilesize/">CURLOPT_MAXFILESIZE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_max_recv_speed_large/">CURLOPT_MAX_RECV_SPEED_LARGE</a></code>(3),</p>
