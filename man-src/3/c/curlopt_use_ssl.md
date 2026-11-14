---
title: "curlopt_use_ssl(3)"
name: "curlopt_use_ssl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_use_ssl/"
description: "CURLOPT_USE_SSL – request using SSL / TLS for the transfer"
---

<p>CURLOPT_USE_SSL &#8211; request using SSL / TLS for the transfer</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_USE_SSL, long level);</p>
<h2>Description</h2>
<p>Pass a long using one of the values from below, to make libcurl use your desired <i>level</i> of SSL for the transfer. </p>
<p> These are all protocols that start out plain text and get &quot;upgraded&quot; to SSL using the STARTTLS command. </p>
<p> This is for enabling SSL/TLS when you use FTP, SMTP, POP3, IMAP etc.</p>
<dl COMPACT>
<dt>CURLUSESSL_NONE</p>
<dd>Don&#8217;t attempt to use SSL.</p>
<dt>CURLUSESSL_TRY</p>
<dd>Try using SSL, proceed as normal otherwise.</p>
<dt>CURLUSESSL_CONTROL</p>
<dd>Require SSL for the control connection or fail with <i>CURLE_USE_SSL_FAILED</i>.</p>
<dt>CURLUSESSL_ALL</p>
<dd>Require SSL for all communication or fail with <i>CURLE_USE_SSL_FAILED</i>.</dl>
<h2>Default</h2>
<p>CURLUSESSL_NONE</p>
<h2>Protocols</h2>
<p>FTP, SMTP, POP3, IMAP</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a href="ftp://example.com/dir/file.ext">ftp://example.com/dir/file.ext</a>&quot;);
 /* require use of SSL for this, or fail */
 curl_easy_setopt(curl, CURLOPT_USE_SSL, CURLUSESSL_ALL);
 /* Perform the request */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Added in 7.11.0. This option was known as CURLOPT_FTP_SSL up to 7.16.4, and the constants were known as CURLFTPSSL_*</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sslversion/">CURLOPT_SSLVERSION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssl_options/">CURLOPT_SSL_OPTIONS</a></code>(3),</p>
