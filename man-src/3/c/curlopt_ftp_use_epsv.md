---
title: "curlopt_ftp_use_epsv(3)"
name: "curlopt_ftp_use_epsv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftp_use_epsv/"
description: "CURLOPT_FTP_USE_EPSV – enable/disable use of EPSV"
---

<p>CURLOPT_FTP_USE_EPSV &#8211; enable/disable use of EPSV</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTP_USE_EPSV, long epsv);</p>
<h2>Description</h2>
<p>Pass <i>epsv</i> as a long. If the value is 1, it tells curl to use the EPSV command when doing passive FTP downloads (which it does by default). Using EPSV means that it will first attempt to use EPSV before using PASV, but if you pass zero to this option, it will not try using EPSV, only plain PASV. </p>
<p> If the server is an IPv6 host, this option will have no effect as of 7.12.3.</p>
<h2>Default</h2>
<p>1</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Along with FTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if FTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ftp_use_eprt/">CURLOPT_FTP_USE_EPRT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ftpport/">CURLOPT_FTPPORT</a></code>(3),</p>
