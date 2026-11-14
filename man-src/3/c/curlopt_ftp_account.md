---
title: "curlopt_ftp_account(3)"
name: "curlopt_ftp_account"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftp_account/"
description: "CURLOPT_FTP_ACCOUNT – set account info for FTP"
---

<p>CURLOPT_FTP_ACCOUNT &#8211; set account info for FTP</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTP_ACCOUNT, char *account);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string (or NULL to disable). When an FTP server asks for &quot;account data&quot; after user name and password has been provided, this data is sent off using the ACCT command.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.13.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_password/">CURLOPT_PASSWORD</a></code>(3),</p>
