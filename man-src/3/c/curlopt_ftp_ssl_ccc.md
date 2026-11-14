---
title: "curlopt_ftp_ssl_ccc(3)"
name: "curlopt_ftp_ssl_ccc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftp_ssl_ccc/"
description: "CURLOPT_FTP_SSL_CCC – switch off SSL again with FTP after auth"
---

<p>CURLOPT_FTP_SSL_CCC &#8211; switch off SSL again with FTP after auth</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTP_SSL_CCC,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>long how);</p>
<h2>Description</h2>
<p>If enabled, this option makes libcurl use CCC (Clear Command Channel). It shuts down the SSL/TLS layer after authenticating. The rest of the control channel communication will be unencrypted. This allows NAT routers to follow the FTP transaction. Pass a long using one of the values below</p>
<dl COMPACT>
<dt>CURLFTPSSL_CCC_NONE</p>
<dd>Don&#8217;t attempt to use CCC.</p>
<dt>CURLFTPSSL_CCC_PASSIVE</p>
<dd>Do not initiate the shutdown, but wait for the server to do it. Do not send a reply.</p>
<dt>CURLFTPSSL_CCC_ACTIVE</p>
<dd>Initiate the shutdown and wait for a reply.</dl>
<h2>Default</h2>
<p>CURLFTPSSL_CCC_NONE</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.16.1</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_use_ssl/">CURLOPT_USE_SSL</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ftpsslauth/">CURLOPT_FTPSSLAUTH</a></code>(3),</p>
