---
title: "curlopt_krblevel(3)"
name: "curlopt_krblevel"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_krblevel/"
description: "CURLOPT_KRBLEVEL – set FTP kerberos security level"
---

<p>CURLOPT_KRBLEVEL &#8211; set FTP kerberos security level</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_KRBLEVEL, char *level);</p>
<h2>Description</h2>
<p>Pass a char * as parameter. Set the kerberos security level for FTP; this also enables kerberos awareness. This is a string that should match one of the following: &#8216;clear&#8217;, &#8216;safe&#8217;, &#8216;confidential&#8217; or &#8216;private&#8217;. If the string is set but doesn&#8217;t match one of these, &#8216;private&#8217; will be used. Set the string to NULL to disable kerberos support for FTP.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>This option was known as CURLOPT_KRB4LEVEL up to 7.16.3</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_krblevel/">CURLOPT_KRBLEVEL</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ftp_ssl/">CURLOPT_FTP_SSL</a></code>(3),</p>
