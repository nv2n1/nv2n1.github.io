---
title: "curlopt_proxypassword(3)"
name: "curlopt_proxypassword"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_proxypassword/"
description: "CURLOPT_PROXYPASSWORD – password to use with proxy authentication"
---

<p>CURLOPT_PROXYPASSWORD &#8211; password to use with proxy authentication</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PROXYPASSWORD, char *pwd);</p>
<h2>Description</h2>
<p>Pass a char * as parameter, which should be pointing to the zero terminated password to use for authentication with the proxy. </p>
<p> The <i><a href="/docs/linux/man/3-curlopt_proxypassword/">CURLOPT_PROXYPASSWORD</a>(3)</i> option should be used in conjunction with the <i><a href="/docs/linux/man/3-curlopt_proxyusername/">CURLOPT_PROXYUSERNAME</a>(3)</i> option.</p>
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
<p><code><a href="/docs/linux/man/3-curlopt_password/">CURLOPT_PASSWORD</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxyusername/">CURLOPT_PROXYUSERNAME</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpauth/">CURLOPT_HTTPAUTH</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxyauth/">CURLOPT_PROXYAUTH</a></code>(3)</p>
