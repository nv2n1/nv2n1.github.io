---
title: "curlopt_ssl_verifypeer(3)"
name: "curlopt_ssl_verifypeer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssl_verifypeer/"
description: "CURLOPT_SSL_VERIFYPEER – verify the peer’s SSL certificate"
---

<p>CURLOPT_SSL_VERIFYPEER &#8211; verify the peer&#8217;s SSL certificate</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSL_VERIFYPEER, long verify);</p>
<h2>Description</h2>
<p>Pass a long as parameter to enable or disable. </p>
<p> This option determines whether curl verifies the authenticity of the peer&#8217;s certificate. A value of 1 means curl verifies; 0 (zero) means it doesn&#8217;t. </p>
<p> When negotiating a TLS or SSL connection, the server sends a certificate indicating its identity. Curl verifies whether the certificate is authentic, i.e. that you can trust that the server is who the certificate says it is. This trust is based on a chain of digital signatures, rooted in certification authority (CA) certificates you supply. curl uses a default bundle of CA certificates (the path for that is determined at build time) and you can specify alternate certificates with the <i><a href="/docs/linux/man/3-curlopt_cainfo/">CURLOPT_CAINFO</a>(3)</i> option or the <i><a href="/docs/linux/man/3-curlopt_capath/">CURLOPT_CAPATH</a>(3)</i> option. </p>
<p> When <i><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a>(3)</i> is enabled, and the verification fails to prove that the certificate is authentic, the connection fails. When the option is zero, the peer certificate verification succeeds regardless. </p>
<p> Authenticating the certificate is not enough to be sure about the server. You typically also want to ensure that the server is the server you mean to be talking to. Use <i><a href="/docs/linux/man/3-curlopt_ssl_verifyhost/">CURLOPT_SSL_VERIFYHOST</a>(3)</i> for that. The check that the host name in the certificate is valid for the host name you&#8217;re connecting to is done independently of the <i><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a>(3)</i> option. </p>
<p> WARNING: disabling verification of the certificate allows bad guys to man-in-the-middle the communication without you knowing it. Disabling verification makes the communication insecure. Just having encryption on a transfer is not enough as you cannot be sure that you are communicating with the correct end-point.</p>
<h2>Default</h2>
<p>By default, curl assumes a value of 1.</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If built TLS enabled.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssl_verifyhost/">CURLOPT_SSL_VERIFYHOST</a></code>(3),</p>
