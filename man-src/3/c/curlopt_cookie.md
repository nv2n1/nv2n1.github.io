---
title: "curlopt_cookie(3)"
name: "curlopt_cookie"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_cookie/"
description: "CURLOPT_COOKIE – set contents of HTTP Cookie header"
---

<p>CURLOPT_COOKIE &#8211; set contents of HTTP Cookie header</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_COOKIE, char *cookie);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. It will be used to set a cookie in the HTTP request. The format of the string should be NAME=CONTENTS, where NAME is the cookie name and CONTENTS is what the cookie should contain. </p>
<p> If you need to set multiple cookies, set them all using a single option concatenated like this: &quot;name1=content1; name2=content2;&quot; etc. </p>
<p> This option sets the cookie header explicitly in the outgoing request(s). If multiple requests are done due to authentication, followed redirections or similar, they will all get this cookie passed on. </p>
<p> Using this option multiple times will only make the latest string override the previous ones. </p>
<p> This option will not enable the cookie engine. Use <i><a href="/docs/linux/man/3-curlopt_cookiefile/">CURLOPT_COOKIEFILE</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_cookiejar/">CURLOPT_COOKIEJAR</a>(3)</i> to enable parsing and sending cookies automatically.</p>
<h2>Default</h2>
<p>NULL, no cookies</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If HTTP is enabled</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is enabled, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_cookiefile/">CURLOPT_COOKIEFILE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_cookiejar/">CURLOPT_COOKIEJAR</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_cookielist/">CURLOPT_COOKIELIST</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a></code>(3),</p>
