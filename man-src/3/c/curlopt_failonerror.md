---
title: "curlopt_failonerror(3)"
name: "curlopt_failonerror"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_failonerror/"
description: "CURLOPT_FAILONERROR – request failure on HTTP response >= 400"
---

<p>CURLOPT_FAILONERROR &#8211; request failure on HTTP response &gt;= 400</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FAILONERROR, long fail);</p>
<h2>Description</h2>
<p>A long parameter set to 1 tells the library to fail the request if the HTTP code returned is equal to or larger than 400. The default action would be to return the page normally, ignoring that code. </p>
<p> This method is not fail-safe and there are occasions where non-successful response codes will slip through, especially when authentication is involved (response codes 401 and 407). </p>
<p> You might get some amounts of headers transferred before this situation is detected, like when a &quot;100-continue&quot; is received as a response to a POST/PUT and a 401 or 407 is received immediately afterwards.</p>
<h2>Default</h2>
<p>0, do not fail on error</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is enabled, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_http200aliases/">CURLOPT_HTTP200ALIASES</a></code>(3),</p>
