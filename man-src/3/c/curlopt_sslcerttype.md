---
title: "curlopt_sslcerttype(3)"
name: "curlopt_sslcerttype"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_sslcerttype/"
description: "CURLOPT_SSLCERTTYPE – specify type of the client SSL certificate"
---

<p>CURLOPT_SSLCERTTYPE &#8211; specify type of the client SSL certificate</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSLCERTTYPE, char *type);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. The string should be the format of your certificate. Supported formats are &quot;PEM&quot; and &quot;DER&quot;, except with Secure Transport. OpenSSL (versions 0.9.3 and later) and Secure Transport (on iOS 5 or later, or OS X 10.7 or later) also support &quot;P12&quot; for PKCS#12-encoded files.</p>
<h2>Default</h2>
<p>&quot;PEM&quot;</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If built TLS enabled. Added in 7.9.3</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if TLS is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sslcert/">CURLOPT_SSLCERT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_sslkey/">CURLOPT_SSLKEY</a></code>(3),</p>
