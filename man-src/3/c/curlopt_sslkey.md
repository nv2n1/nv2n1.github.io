---
title: "curlopt_sslkey(3)"
name: "curlopt_sslkey"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_sslkey/"
description: "CURLOPT_SSLKEY – specify private keyfile for TLS and SSL client cert"
---

<p>CURLOPT_SSLKEY &#8211; specify private keyfile for TLS and SSL client cert</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSLKEY, char *keyfile);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. The string should be the file name of your private key. The default format is &quot;PEM&quot; and can be changed with <i><a href="/docs/linux/man/3-curlopt_sslkeytype/">CURLOPT_SSLKEYTYPE</a>(3)</i>. </p>
<p> (iOS and Mac OS X only) This option is ignored if curl was built against Secure Transport. Secure Transport expects the private key to be already present in the keychain or PKCS#12 file containing the certificate.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If built TLS enabled.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if TLS is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sslkeytype/">CURLOPT_SSLKEYTYPE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_sslcert/">CURLOPT_SSLCERT</a></code>(3),</p>
