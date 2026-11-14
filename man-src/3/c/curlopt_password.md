---
title: "curlopt_password(3)"
name: "curlopt_password"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_password/"
description: "CURLOPT_PASSWORD – password to use in authentication"
---

<p>CURLOPT_PASSWORD &#8211; password to use in authentication</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PASSWORD, char *pwd);</p>
<h2>Description</h2>
<p>Pass a char * as parameter, which should be pointing to the zero terminated password to use for the transfer. </p>
<p> The <i><a href="/docs/linux/man/3-curlopt_password/">CURLOPT_PASSWORD</a>(3)</i> option should be used in conjunction with the <i><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a>(3)</i> option.</p>
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
<p><code><a href="/docs/linux/man/3-curlopt_userpwd/">CURLOPT_USERPWD</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpauth/">CURLOPT_HTTPAUTH</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxyauth/">CURLOPT_PROXYAUTH</a></code>(3)</p>
