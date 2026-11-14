---
title: "curlopt_ioctldata(3)"
name: "curlopt_ioctldata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ioctldata/"
description: "CURLOPT_IOCTLDATA – custom pointer passed to I/O callback"
---

<p>CURLOPT_IOCTLDATA &#8211; custom pointer passed to I/O callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_IOCTLDATA, void *pointer);</p>
<h2>Description</h2>
<p>Pass the <i>pointer</i> that will be untouched by libcurl and passed as the 3rd argument in the ioctl callback set with <i><a href="/docs/linux/man/3-curlopt_ioctlfunction/">CURLOPT_IOCTLFUNCTION</a>(3)</i>.</p>
<h2>Default</h2>
<p>By default, the value of this parameter is NULL.</p>
<h2>Protocols</h2>
<p>Used with HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.12.3</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ioctlfunction/">CURLOPT_IOCTLFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_seekfunction/">CURLOPT_SEEKFUNCTION</a></code>(3),</p>
