---
title: "curlopt_redir_protocols(3)"
name: "curlopt_redir_protocols"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_redir_protocols/"
description: "CURLOPT_REDIR_PROTOCOLS – set protocols allowed to redirect to"
---

<p>CURLOPT_REDIR_PROTOCOLS &#8211; set protocols allowed to redirect to</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_REDIR_PROTOCOLS, long bitmask);</p>
<h2>Description</h2>
<p>Pass a long that holds a bitmask of CURLPROTO_* defines. If used, this bitmask limits what protocols libcurl may use in a transfer that it follows to in a redirect when <i><a href="/docs/linux/man/3-curlopt_followlocation/">CURLOPT_FOLLOWLOCATION</a>(3)</i> is enabled. This allows you to limit specific transfers to only be allowed to use a subset of protocols in redirections. By default libcurl will allow all protocols except for FILE and SCP. </p>
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
<p>All protocols except for FILE, SCP and SMB.</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<pre>curl = curl_easy_init();
if(curl) {
 /* pass in the URL from an external source */
 curl_easy_setopt(curl, CURLOPT_URL, argv[1]);
 /* only allow redirects to HTTP and HTTPS URLs */
 curl_easy_setopt(curl, CURLOPT_REDIR_PROTOCOLS,
 CURLPROTO_HTTP | CURLPROTO_HTTPS);
 /* Perform the request */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Added in 7.19.4, before then it would follow all protocols.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_protocols/">CURLOPT_PROTOCOLS</a></code>(3),</p>
