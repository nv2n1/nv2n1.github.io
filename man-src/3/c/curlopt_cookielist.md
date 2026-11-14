---
title: "curlopt_cookielist(3)"
name: "curlopt_cookielist"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_cookielist/"
description: "CURLOPT_COOKIELIST – add to or manipulate cookies held in memory"
---

<p>CURLOPT_COOKIELIST &#8211; add to or manipulate cookies held in memory</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_COOKIELIST,
 char *cookie);</pre>
<h2>Description</h2>
<p>Pass a char * to a <i>cookie</i> string. </p>
<p> Such a cookie can be either a single line in Netscape / Mozilla format or just regular HTTP-style header (Set-Cookie: &#8230;) format. This will also enable the cookie engine. This adds that single cookie to the internal cookie store. </p>
<p> Additionally, there are commands available that perform actions if you pass in these exact strings:</p>
<dl COMPACT>
<dt>ALL</p>
<dd>erases all cookies held in memory </p>
<dt>SESS</p>
<dd>erases all session cookies held in memory </p>
<dt>FLUSH</p>
<dd>writes all known cookies to the file specified by <i><a href="/docs/linux/man/3-curlopt_cookiejar/">CURLOPT_COOKIEJAR</a>(3)</i> </p>
<dt>RELOAD</p>
<dd>loads all cookies from the files specified by <i><a href="/docs/linux/man/3-curlopt_cookiefile/">CURLOPT_COOKIEFILE</a>(3)</i> </p>
</dl>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>ALL was added in 7.14.1 </p>
<p> SESS was added in 7.15.4 </p>
<p> FLUSH was added in 7.17.1 </p>
<p> RELOAD was added in 7.39.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_cookiefile/">CURLOPT_COOKIEFILE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_cookiejar/">CURLOPT_COOKIEJAR</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_cookie/">CURLOPT_COOKIE</a></code>(3),</p>
