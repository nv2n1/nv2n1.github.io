---
title: "curlopt_append(3)"
name: "curlopt_append"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_append/"
description: "CURLOPT_APPEND – enable appending to the remote file"
---

<p>CURLOPT_APPEND &#8211; enable appending to the remote file</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_APPEND, long append);</p>
<h2>Description</h2>
<p>A parameter set to 1 tells the library to append to the remote file instead of overwrite it. This is only useful when uploading to an FTP site.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>This option was known as CURLOPT_FTPAPPEND up to 7.16.4</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_dirlistonly/">CURLOPT_DIRLISTONLY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_resume_from/">CURLOPT_RESUME_FROM</a></code>(3),</p>
