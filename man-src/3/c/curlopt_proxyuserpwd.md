---
title: "curlopt_proxyuserpwd(3)"
name: "curlopt_proxyuserpwd"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_proxyuserpwd/"
description: "CURLOPT_PROXYUSERPWD – user name and password to use for proxy authentication"
---

<p>CURLOPT_PROXYUSERPWD &#8211; user name and password to use for proxy authentication</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PROXYUSERPWD, char *userpwd);</p>
<h2>Description</h2>
<p>Pass a char * as parameter, which should be [user name]:[password] to use for the connection to the HTTP proxy. Both the name and the password will be URL decoded before use, so to include for example a colon in the user name you should encode it as %3A. (This is different to how <i><a href="/docs/linux/man/3-curlopt_userpwd/">CURLOPT_USERPWD</a>(3)</i> is used &#8211; beware.) </p>
<p> Use <i><a href="/docs/linux/man/3-curlopt_proxyauth/">CURLOPT_PROXYAUTH</a>(3)</i> to specify the authentication method.</p>
<h2>Default</h2>
<p>This is NULL by default.</p>
<h2>Protocols</h2>
<p>Used with all protocols that can use a proxy</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if proxies are supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxytype/">CURLOPT_PROXYTYPE</a></code>(3),</p>
