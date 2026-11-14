---
title: "curlopt_ssl_verifyhost(3)"
name: "curlopt_ssl_verifyhost"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssl_verifyhost/"
description: "CURLOPT_SSL_VERIFYHOST – verify the certificate’s name against host"
---

<p>CURLOPT_SSL_VERIFYHOST &#8211; verify the certificate&#8217;s name against host</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSL_VERIFYHOST, long verify);</p>
<h2>Description</h2>
<p>Pass a long as parameter specifying what to <i>verify</i>. </p>
<p> This option determines whether libcurl verifies that the server cert is for the server it is known as. </p>
<p> When negotiating TLS and SSL connections, the server sends a certificate indicating its identity. </p>
<p> When <i><a href="/docs/linux/man/3-curlopt_ssl_verifyhost/">CURLOPT_SSL_VERIFYHOST</a>(3)</i> is 2, that certificate must indicate that the server is the server to which you meant to connect, or the connection fails. Simply put, it means it has to have the same name in the certificate as is in the URL you operate against. </p>
<p> Curl considers the server the intended one when the Common Name field or a Subject Alternate Name field in the certificate matches the host name in the URL to which you told Curl to connect. </p>
<p> When the <i>verify</i> value is 1, <i>curl_easy_setopt</i> will return an error and the option value will not be changed. It was previously (in 7.28.0 and earlier) a debug option of some sorts, but it is no longer supported due to frequently leading to programmer mistakes. Future versions will stop returning an error for 1 and just treat 1 and 2 the same. </p>
<p> When the <i>verify</i> value is 0, the connection succeeds regardless of the names in the certificate. Use that ability with caution! </p>
<p> The default value for this option is 2. </p>
<p> This option controls checking the server&#8217;s certificate&#8217;s claimed identity. The server could be lying. To control lying, see <i><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a>(3)</i>. If libcurl is built against NSS and <i><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a>(3)</i> is zero, <i><a href="/docs/linux/man/3-curlopt_ssl_verifyhost/">CURLOPT_SSL_VERIFYHOST</a>(3)</i> is also set to zero and cannot be overridden.</p>
<h2>Default</h2>
<p>2</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If built TLS enabled.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if TLS is supported, and CURLE_UNKNOWN_OPTION if not. </p>
<p> If 1 is set as argument, <i>CURLE_BAD_FUNCTION_ARGUMENT</i> is returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_cainfo/">CURLOPT_CAINFO</a></code>(3),</p>
