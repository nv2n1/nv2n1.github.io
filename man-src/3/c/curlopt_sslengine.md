---
title: "curlopt_sslengine(3)"
name: "curlopt_sslengine"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_sslengine/"
description: "CURLOPT_SSLENGINE – set SSL engine identifier"
---

<p>CURLOPT_SSLENGINE &#8211; set SSL engine identifier</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSLENGINE, char *id);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. It will be used as the identifier for the crypto engine you want to use for your private key. </p>
<p> If the crypto device cannot be loaded, <i>CURLE_SSL_ENGINE_NOTFOUND</i> is returned.</p>
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
<p><code><a href="/docs/linux/man/3-curlopt_sslengine_default/">CURLOPT_SSLENGINE_DEFAULT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_sslkey/">CURLOPT_SSLKEY</a></code>(3),</p>
