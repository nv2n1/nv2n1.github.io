---
title: "curlopt_maxfilesize(3)"
name: "curlopt_maxfilesize"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_maxfilesize/"
description: "CURLOPT_MAXFILESIZE – maximum file size allowed to download"
---

<p>CURLOPT_MAXFILESIZE &#8211; maximum file size allowed to download</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_MAXFILESIZE, long size);</p>
<h2>Description</h2>
<p>Pass a long as parameter. This allows you to specify the maximum <i>size</i> (in bytes) of a file to download. If the file requested is found larger than this value, the transfer will not start and <i>CURLE_FILESIZE_EXCEEDED</i> will be returned. </p>
<p> The file size is not always known prior to download, and for such files this option has no effect even if the file transfer ends up being larger than this given limit. This concerns both FTP and HTTP transfers. </p>
<p> If you want a limit above 2GB, use <i><a href="/docs/linux/man/3-curlopt_maxfilesize_large/">CURLOPT_MAXFILESIZE_LARGE</a>(3)</i>.</p>
<h2>Default</h2>
<p>None</p>
<h2>Protocols</h2>
<p>FTP and HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_maxfilesize_large/">CURLOPT_MAXFILESIZE_LARGE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_max_recv_speed_large/">CURLOPT_MAX_RECV_SPEED_LARGE</a></code>(3),</p>
