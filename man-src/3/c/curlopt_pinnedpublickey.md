---
title: "curlopt_pinnedpublickey(3)"
name: "curlopt_pinnedpublickey"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_pinnedpublickey/"
description: "CURLOPT_PINNEDPUBLICKEY – set pinned public key"
---

<p>CURLOPT_PINNEDPUBLICKEY &#8211; set pinned public key</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PINNEDPUBLICKEY, char *pinnedpubkey);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. The string should be the file name of your pinned public key. The format expected is &quot;PEM&quot; or &quot;DER&quot;. </p>
<p> When negotiating a TLS or SSL connection, the server sends a certificate indicating its identity. A public key is extracted from this certificate and if it does not exactly match the public key provided to this option, curl will abort the connection before sending or receiving any data.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="https://example.com">https://example.com</a>&quot;);
 curl_easy_setopt(curl, CURLOPT_PINNEDPUBLICKEY, &quot;/etc/publickey.der&quot;);
 /* Perform the request */
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>If built TLS enabled. This is currently only implemented in the OpenSSL, GnuTLS, NSS and GSKit backends. </p>
<p> Added in libcurl 7.39.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if TLS enabled, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssl_verifyhost/">CURLOPT_SSL_VERIFYHOST</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_cainfo/">CURLOPT_CAINFO</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_capath/">CURLOPT_CAPATH</a></code>(3),</p>
