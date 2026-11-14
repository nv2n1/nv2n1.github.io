---
title: "curlopt_capath(3)"
name: "curlopt_capath"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_capath/"
description: "CURLOPT_CAPATH – specify directory holding CA certificates"
---

<p>CURLOPT_CAPATH &#8211; specify directory holding CA certificates</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CAPATH, char *capath);</p>
<h2>Description</h2>
<p>Pass a char * to a zero terminated string naming a directory holding multiple CA certificates to verify the peer with. If libcurl is built against OpenSSL, the certificate directory must be prepared using the openssl c_rehash utility. This makes sense only when used in combination with the <i><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a>(3)</i> option. </p>
<p> The <i><a href="/docs/linux/man/3-curlopt_capath/">CURLOPT_CAPATH</a>(3)</i> function apparently does not work in Windows due to some limitation in openssl.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>This option is OpenSSL-specific and does nothing if libcurl is built to use GnuTLS. NSS-powered libcurl provides the option only for backward compatibility.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if TLS enabled, and CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_cainfo/">CURLOPT_CAINFO</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_stderr/">CURLOPT_STDERR</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a></code>(3),</p>
