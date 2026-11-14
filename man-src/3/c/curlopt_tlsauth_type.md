---
title: "curlopt_tlsauth_type(3)"
name: "curlopt_tlsauth_type"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_tlsauth_type/"
description: "CURLOPT_TLSAUTH_TYPE – set TLS authentication methods"
---

<p>CURLOPT_TLSAUTH_TYPE &#8211; set TLS authentication methods</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TLSAUTH_TYPE, long bitmask);</p>
<h2>Description</h2>
<p>Pass a long as parameter, which is set to a bitmask, to tell libcurl which authentication method(s) you want it to use for TLS authentication. </p>
<dl COMPACT>
<dt>CURL_TLSAUTH_SRP</p>
<dd>TLS-SRP authentication. Secure Remote Password authentication for TLS is defined in RFC5054 and provides mutual authentication if both sides have a shared secret. To use TLS-SRP, you must also set the <i><a href="/docs/linux/man/3-curlopt_tlsauth_username/">CURLOPT_TLSAUTH_USERNAME</a>(3)</i> and <i><a href="/docs/linux/man/3-curlopt_tlsauth_password/">CURLOPT_TLSAUTH_PASSWORD</a>(3)</i> options.</dl>
<h2>Default</h2>
<p>CURL_TLSAUTH_NONE (0)</p>
<h2>Protocols</h2>
<p>All TLS-based protocols</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>You need to build libcurl with GnuTLS or OpenSSL with TLS-SRP support for this to work. Added in 7.21.4</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_tlsauth_username/">CURLOPT_TLSAUTH_USERNAME</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_tlsauth_password/">CURLOPT_TLSAUTH_PASSWORD</a></code>(3),</p>
