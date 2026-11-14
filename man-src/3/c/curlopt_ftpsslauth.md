---
title: "curlopt_ftpsslauth(3)"
name: "curlopt_ftpsslauth"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftpsslauth/"
description: "CURLOPT_FTPSSLAUTH – set order in which to attempt TLS vs SSL when using FTP"
---

<p>CURLOPT_FTPSSLAUTH &#8211; set order in which to attempt TLS vs SSL when using FTP</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTPSSLAUTH, long order);</p>
<h2>Description</h2>
<p>Pass a long using one of the values from below, to alter how libcurl issues &quot;AUTH TLS&quot; or &quot;AUTH SSL&quot; when FTP over SSL is activated. This is only interesting if <i><a href="/docs/linux/man/3-curlopt_use_ssl/">CURLOPT_USE_SSL</a>(3)</i> is also set. </p>
<p> Possible <i>order</i> values:</p>
<dl COMPACT>
<dt>CURLFTPAUTH_DEFAULT</p>
<dd>Allow libcurl to decide.</p>
<dt>CURLFTPAUTH_SSL</p>
<dd>Try &quot;AUTH SSL&quot; first, and only if that fails try &quot;AUTH TLS&quot;.</p>
<dt>CURLFTPAUTH_TLS</p>
<dd>Try &quot;AUTH TLS&quot; first, and only if that fails try &quot;AUTH SSL&quot;.</dl>
<h2>Default</h2>
<p>CURLFTPAUTH_DEFAULT</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.12.2</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_use_ssl/">CURLOPT_USE_SSL</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ftp_ssl_ccc/">CURLOPT_FTP_SSL_CCC</a></code>(3),</p>
