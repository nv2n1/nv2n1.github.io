---
title: "curlopt_ftp_use_eprt(3)"
name: "curlopt_ftp_use_eprt"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftp_use_eprt/"
description: "CURLOPT_FTP_USE_EPRT – enable/disable use of EPRT with FTP"
---

<p>CURLOPT_FTP_USE_EPRT &#8211; enable/disable use of EPRT with FTP</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTP_USE_EPRT, long enabled);</p>
<h2>Description</h2>
<p>Pass a long. If the value is 1, it tells curl to use the EPRT command when doing active FTP downloads (which is enabled by <i><a href="/docs/linux/man/3-curlopt_ftpport/">CURLOPT_FTPPORT</a>(3)</i>). Using EPRT means that it will first attempt to use EPRT before using PORT, but if you pass zero to this option, it will not try using EPRT, only plain PORT. </p>
<p> If the server is an IPv6 host, this option will have no effect as EPRT is necessary then.</p>
<h2>Default</h2>
<h2>Protocols</h2>
<h2>Example</h2>
<h2>Availability</h2>
<p>Added in 7.10.5</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ftp_use_epsv/">CURLOPT_FTP_USE_EPSV</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ftpport/">CURLOPT_FTPPORT</a></code>(3),</p>
