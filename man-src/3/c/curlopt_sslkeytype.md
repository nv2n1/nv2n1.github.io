---
title: "curlopt_sslkeytype(3)"
name: "curlopt_sslkeytype"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_sslkeytype/"
description: "CURLOPT_SSLKEYTYPE – set type of the private key file"
---

<p>CURLOPT_SSLKEYTYPE &#8211; set type of the private key file</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSLKEYTYPE, char *type);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. The string should be the format of your private key. Supported formats are &quot;PEM&quot;, &quot;DER&quot; and &quot;ENG&quot;. </p>
<p> The format &quot;ENG&quot; enables you to load the private key from a crypto engine. In this case <i><a href="/docs/linux/man/3-curlopt_sslkey/">CURLOPT_SSLKEY</a>(3)</i> is used as an identifier passed to the engine. You have to set the crypto engine with <i><a href="/docs/linux/man/3-curlopt_sslengine/">CURLOPT_SSLENGINE</a>(3)</i>. &quot;DER&quot; format key file currently does not work because of a bug in OpenSSL.</p>
<h2>Default</h2>
<p>&quot;PEM&quot;</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If built TLS enabled.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if TLS is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sslkey/">CURLOPT_SSLKEY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_sslcert/">CURLOPT_SSLCERT</a></code>(3),</p>
