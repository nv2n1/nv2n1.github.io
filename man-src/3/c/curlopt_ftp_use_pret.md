---
title: "curlopt_ftp_use_pret(3)"
name: "curlopt_ftp_use_pret"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftp_use_pret/"
description: "CURLOPT_FTP_USE_PRET – enable the PRET command"
---

<p>CURLOPT_FTP_USE_PRET &#8211; enable the PRET command</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTP_USE_PRET, long enable);</p>
<h2>Description</h2>
<p>Pass a long. If the value is 1, it tells curl to send a PRET command before PASV (and EPSV). Certain FTP servers, mainly drftpd, require this non-standard command for directory listings as well as up and downloads in PASV mode. Has no effect when using the active FTP transfers mode.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.20.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ftp_use_eprt/">CURLOPT_FTP_USE_EPRT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ftp_use_epsv/">CURLOPT_FTP_USE_EPSV</a></code>(3),</p>
