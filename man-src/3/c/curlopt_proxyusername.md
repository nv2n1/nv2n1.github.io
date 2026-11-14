---
title: "curlopt_proxyusername(3)"
name: "curlopt_proxyusername"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_proxyusername/"
description: "CURLOPT_PROXYUSERNAME – user name to use for proxy authentication"
---

<p>CURLOPT_PROXYUSERNAME &#8211; user name to use for proxy authentication</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PROXYUSERNAME,
 char *username);</pre>
<h2>Description</h2>
<p>Pass a char * as parameter, which should be pointing to the zero terminated user name to use for the transfer. </p>
<p> <code><a href="/docs/linux/man/3-curlopt_proxyusername/">CURLOPT_PROXYUSERNAME</a>(3)</code> sets the user name to be used in protocol authentication with the proxy. </p>
<p> To specify the proxy password use the <i><a href="/docs/linux/man/3-curlopt_proxypassword/">CURLOPT_PROXYPASSWORD</a>(3)</i>.</p>
<h2>Default</h2>
<p>blank</p>
<h2>Protocols</h2>
<p>Most</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.19.1</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_proxypassword/">CURLOPT_PROXYPASSWORD</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpauth/">CURLOPT_HTTPAUTH</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxyauth/">CURLOPT_PROXYAUTH</a></code>(3)</p>
