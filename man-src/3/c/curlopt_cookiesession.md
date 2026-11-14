---
title: "curlopt_cookiesession(3)"
name: "curlopt_cookiesession"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_cookiesession/"
description: "CURLOPT_COOKIESESSION – start a new cookie session"
---

<p>CURLOPT_COOKIESESSION &#8211; start a new cookie session</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_COOKIESESSION, long init);</p>
<h2>Description</h2>
<p>Pass a long set to 1 to mark this as a new cookie &quot;session&quot;. It will force libcurl to ignore all cookies it is about to load that are &quot;session cookies&quot; from the previous session. By default, libcurl always stores and loads all cookies, independent if they are session cookies or not. Session cookies are cookies without expiry date and they are meant to be alive and existing for this &quot;session&quot; only. </p>
<p> A &quot;session&quot; is usually defined in browser land for as long as you have your browser up, more or less.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_cookiefile/">CURLOPT_COOKIEFILE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_cookie/">CURLOPT_COOKIE</a></code>(3),</p>
