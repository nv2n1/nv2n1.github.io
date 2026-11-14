---
title: "curlopt_filetime(3)"
name: "curlopt_filetime"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_filetime/"
description: "CURLOPT_FILETIME – get the modification time of the remote resource"
---

<p>CURLOPT_FILETIME &#8211; get the modification time of the remote resource</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FILETIME, long gettime);</p>
<h2>Description</h2>
<p>Pass a long. If it is 1, libcurl will attempt to get the modification time of the remote document in this operation. This requires that the remote server sends the time or replies to a time querying command. The <i><a href="/docs/linux/man/3-curl_easy_getinfo/">curl_easy_getinfo</a>(3)</i> function with the <i>CURLINFO_FILETIME</i> argument can be used after a transfer to extract the received time (if any).</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>HTTP, FTP, SFTP, FILE</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curl_easy_getinfo/">curl_easy_getinfo</a></code>(3),</p>
