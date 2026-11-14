---
title: "curlopt_accepttimeout_ms(3)"
name: "curlopt_accepttimeout_ms"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_accepttimeout_ms/"
description: "CURLOPT_ACCEPTTIMEOUT_MS – timeout waiting for FTP server to connect back"
---

<p>CURLOPT_ACCEPTTIMEOUT_MS &#8211; timeout waiting for FTP server to connect back</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_ACCEPTTIMEOUT_MS, long ms);</p>
<h2>Description</h2>
<p>Pass a long telling libcurl the maximum number of milliseconds to wait for a server to connect back to libcurl when an active FTP connection is used.</p>
<h2>Default</h2>
<p>If no timeout is set, the internal default of 60000 (one minute) will be used.</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.24.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_stderr/">CURLOPT_STDERR</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a></code>(3),</p>
