---
title: "curlopt_ignore_content_length(3)"
name: "curlopt_ignore_content_length"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ignore_content_length/"
description: "CURLOPT_IGNORE_CONTENT_LENGTH – ignore Content-Length in HTTP response"
---

<p>CURLOPT_IGNORE_CONTENT_LENGTH &#8211; ignore Content-Length in HTTP response</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_IGNORE_CONTENT_LENGTH,
 long ignore);</pre>
<h2>Description</h2>
<p>If <i>ignore</i> is set to 1, ignore the Content-Length header in the HTTP response. This is useful for Apache 1.x (and similar servers) which will report incorrect content length for files over 2 gigabytes. If this option is used, curl will not be able to accurately report progress, and will simply stop the download when the server ends the connection. </p>
<p> Only use this option if strictly necessary.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.14.1</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_http_version/">CURLOPT_HTTP_VERSION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_maxfilesize_large/">CURLOPT_MAXFILESIZE_LARGE</a></code>(3),</p>
