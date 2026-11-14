---
title: "curlopt_seekdata(3)"
name: "curlopt_seekdata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_seekdata/"
description: "CURLOPT_SEEKDATA – custom pointer passed to the seek callback"
---

<p>CURLOPT_SEEKDATA &#8211; custom pointer passed to the seek callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SEEKDATA, void *pointer);</p>
<h2>Description</h2>
<p>Data <i>pointer</i> to pass to the seek callback function. If you use the <i><a href="/docs/linux/man/3-curlopt_seekfunction/">CURLOPT_SEEKFUNCTION</a>(3)</i> option, this is the pointer you&#8217;ll get as input.</p>
<h2>Default</h2>
<p>If you don&#8217;t set this, NULL is passed to the callback.</p>
<h2>Protocols</h2>
<p>HTTP, FTP, SFTP</p>
<h2>Example</h2>
<h2>Availability</h2>
<p>Added in 7.18.0</p>
<h2>Return Value</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_stderr/">CURLOPT_STDERR</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a></code>(3),</p>
