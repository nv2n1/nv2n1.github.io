---
title: "curlopt_sslcert(3)"
name: "curlopt_sslcert"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_sslcert/"
description: "CURLOPT_SSLCERT – set SSL client certificate"
---

<p>CURLOPT_SSLCERT &#8211; set SSL client certificate</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSLCERT, char *cert);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. The string should be the file name of your client certificate. The default format is &quot;P12&quot; on Secure Transport and &quot;PEM&quot; on other engines, and can be changed with <i><a href="/docs/linux/man/3-curlopt_sslcerttype/">CURLOPT_SSLCERTTYPE</a>(3)</i>. </p>
<p> With NSS or Secure Transport, this can also be the nickname of the certificate you wish to authenticate with as it is named in the security database. If you want to use a file from the current directory, please precede it with &quot;./&quot; prefix, in order to avoid confusion with a nickname. </p>
<p> When using a client certificate, you most likely also need to provide a private key with <i><a href="/docs/linux/man/3-curlopt_sslkey/">CURLOPT_SSLKEY</a>(3)</i>.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If built TLS enabled.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if TLS enabled, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sslcerttype/">CURLOPT_SSLCERTTYPE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_sslkey/">CURLOPT_SSLKEY</a></code>(3),</p>
