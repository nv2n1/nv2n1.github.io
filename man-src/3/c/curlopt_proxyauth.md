---
title: "curlopt_proxyauth(3)"
name: "curlopt_proxyauth"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_proxyauth/"
description: "CURLOPT_PROXYAUTH – set HTTP proxy authentication methods to try"
---

<p>CURLOPT_PROXYAUTH &#8211; set HTTP proxy authentication methods to try</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PROXYAUTH, long bitmask);</p>
<h2>Description</h2>
<p>Pass a long as parameter, which is set to a bitmask, to tell libcurl which HTTP authentication method(s) you want it to use for your proxy authentication. If more than one bit is set, libcurl will first query the site to see what authentication methods it supports and then pick the best one you allow it to use. For some methods, this will induce an extra network round-trip. Set the actual name and password with the <i><a href="/docs/linux/man/3-curlopt_proxyuserpwd/">CURLOPT_PROXYUSERPWD</a>(3)</i> option. </p>
<p> The bitmask can be constructed by or&#8217;ing together the bits fully listed and described in the <i><a href="/docs/linux/man/3-curlopt_httpauth/">CURLOPT_HTTPAUTH</a>(3)</i> man page.</p>
<h2>Default</h2>
<p>CURLAUTH_BASIC</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.10.7</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_NOT_BUILT_IN if the bitmask specified no supported authentication methods.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxytype/">CURLOPT_PROXYTYPE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxyuserpwd/">CURLOPT_PROXYUSERPWD</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxyport/">CURLOPT_PROXYPORT</a></code>(3),</p>
