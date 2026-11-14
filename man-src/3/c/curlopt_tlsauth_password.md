---
title: "curlopt_tlsauth_password(3)"
name: "curlopt_tlsauth_password"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_tlsauth_password/"
description: "CURLOPT_TLSAUTH_PASSWORD – password to use for TLS authentication"
---

<p>CURLOPT_TLSAUTH_PASSWORD &#8211; password to use for TLS authentication</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TLSAUTH_PASSWORD, char *pwd);</p>
<h2>Description</h2>
<p>Pass a char * as parameter, which should point to the zero terminated password to use for the TLS authentication method specified with the <i><a href="/docs/linux/man/3-curlopt_tlsauth_type/">CURLOPT_TLSAUTH_TYPE</a>(3)</i> option. Requires that the <i><a href="/docs/linux/man/3-curlopt_tlsauth_username/">CURLOPT_TLSAUTH_USERNAME</a>(3)</i> option also be set.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All TLS-based protocols</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.21.4</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_tlsauth_type/">CURLOPT_TLSAUTH_TYPE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_tlsauth_username/">CURLOPT_TLSAUTH_USERNAME</a></code>(3),</p>
