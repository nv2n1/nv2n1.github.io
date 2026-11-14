---
title: "curlopt_ftp_skip_pasv_ip(3)"
name: "curlopt_ftp_skip_pasv_ip"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftp_skip_pasv_ip/"
description: "CURLOPT_FTP_SKIP_PASV_IP – ignore the IP address in the PASV response"
---

<p>CURLOPT_FTP_SKIP_PASV_IP &#8211; ignore the IP address in the PASV response</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTP_SKIP_PASV_IP, long skip);</p>
<h2>Description</h2>
<p>Pass a long. If <i>skip</i> is set to 1, it instructs libcurl to not use the IP address the server suggests in its 227-response to libcurl&#8217;s PASV command when libcurl connects the data connection. Instead libcurl will re-use the same IP address it already uses for the control connection. But it will use the port number from the 227-response. </p>
<p> This option thus allows libcurl to work around broken server installations that due to NATs, firewalls or incompetence report the wrong IP address back. </p>
<p> This option has no effect if PORT, EPRT or EPSV is used instead of PASV.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.14.2</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ftpport/">CURLOPT_FTPPORT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ftp_use_eprt/">CURLOPT_FTP_USE_EPRT</a></code>(3),</p>
