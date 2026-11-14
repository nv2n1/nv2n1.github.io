---
title: "curlopt_protocols(3)"
name: "curlopt_protocols"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_protocols/"
description: "CURLOPT_PROTOCOLS – set allowed protocols"
---

<p>CURLOPT_PROTOCOLS &#8211; set allowed protocols</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PROTOCOLS, long bitmask);</p>
<h2>Description</h2>
<p>Pass a long that holds a bitmask of CURLPROTO_* defines. If used, this bitmask limits what protocols libcurl may use in the transfer. This allows you to have a libcurl built to support a wide range of protocols but still limit specific transfers to only be allowed to use a subset of them. By default libcurl will accept all protocols it supports (<i>CURLPROTO_ALL</i>). See also <i><a href="/docs/linux/man/3-curlopt_redir_protocols/">CURLOPT_REDIR_PROTOCOLS</a>(3)</i>. </p>
<p> These are the available protocol defines: </p>
<pre>CURLPROTO_DICT
CURLPROTO_FILE
CURLPROTO_FTP
CURLPROTO_FTPS
CURLPROTO_GOPHER
CURLPROTO_HTTP
CURLPROTO_HTTPS
CURLPROTO_IMAP
CURLPROTO_IMAPS
CURLPROTO_LDAP
CURLPROTO_LDAPS
CURLPROTO_POP3
CURLPROTO_POP3S
CURLPROTO_RTMP
CURLPROTO_RTMPE
CURLPROTO_RTMPS
CURLPROTO_RTMPT
CURLPROTO_RTMPTE
CURLPROTO_RTMPTS
CURLPROTO_RTSP
CURLPROTO_SCP
CURLPROTO_SFTP
CURLPROTO_SMB
CURLPROTO_SMTP
CURLPROTO_SMTPS
CURLPROTO_TELNET
CURLPROTO_TFTP</pre>
<h2>Default</h2>
<p>All protocols built-in</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<pre>curl = curl_easy_init();
if(curl) {
 /* pass in the URL from an external source */
 curl_easy_setopt(curl, CURLOPT_URL, argv[1]);
 /* only allow HTTP, TFTP and SFTP */
 curl_easy_setopt(curl, CURLOPT_PROTOCOLS,
 CURLPROTO_HTTP | CURLPROTO_TFTP | CURLPROTO_SFTP);
 /* Perform the request */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Added in 7.19.4</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_redir_protocols/">CURLOPT_REDIR_PROTOCOLS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_url/">CURLOPT_URL</a></code>(3),</p>
