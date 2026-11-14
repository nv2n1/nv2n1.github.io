---
title: "curlopt_ftp_alternative_to_user(3)"
name: "curlopt_ftp_alternative_to_user"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftp_alternative_to_user/"
description: "CURLOPT_FTP_ALTERNATIVE_TO_USER – command to use instead of USER with FTP"
---

<p>CURLOPT_FTP_ALTERNATIVE_TO_USER &#8211; command to use instead of USER with FTP</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTP_ALTERNATIVE_TO_USER,
 char *cmd);</pre>
<h2>Description</h2>
<p>Pass a char * as parameter, pointing to a string which will be used to authenticate if the usual FTP &quot;USER user&quot; and &quot;PASS password&quot; negotiation fails. This is currently only known to be required when connecting to Tumbleweed&#8217;s Secure Transport FTPS server using client certificates for authentication.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.15.5</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ftp_skip_pasv_ip/">CURLOPT_FTP_SKIP_PASV_IP</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ftp_response_timeout/">CURLOPT_FTP_RESPONSE_TIMEOUT</a></code>(3),</p>
