---
title: "curlopt_sslengine_default(3)"
name: "curlopt_sslengine_default"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_sslengine_default/"
---

CURLOPT_SSLENGINE_DEFAULT - make SSL engine default
<h2>Synopsis</h2>#include &lt;curl/curl.h&gt; 

 CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSLENGINE_DEFAULT, long val);
<h2>Description</h2>Pass a long set to 1 as parameter. Sets the actual crypto engine as the default for (asymmetric) crypto operations. 

 If the crypto device cannot be set, <i>CURLE_SSL_ENGINE_SETFAILED</i> is returned.
<h2>Default</h2>None
<h2>Protocols</h2>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.
<h2>Example</h2>TODO
<h2>Availability</h2>If built TLS enabled.
<h2>Return Value</h2>Returns CURLE_OK if TLS is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.
<h2>See Also</h2><b><a HREF="/docs/linux/man/3-curlopt_sslengine/">CURLOPT_SSLENGINE</a></b>(3), <b><a HREF="/docs/linux/man/3-curlopt_sslcert/">CURLOPT_SSLCERT</a></b>(3),
