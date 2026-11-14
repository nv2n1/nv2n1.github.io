---
title: "curlopt_unrestricted_auth(3)"
name: "curlopt_unrestricted_auth"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_unrestricted_auth/"
description: "CURLOPT_UNRESTRICTED_AUTH – send credentials to other hosts too"
---

<p>CURLOPT_UNRESTRICTED_AUTH &#8211; send credentials to other hosts too</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_UNRESTRICTED_AUTH,
 long goahead);</pre>
<h2>Description</h2>
<p>A long parameter set to 1 tells libcurl it can continue to send authentication (user+password) credentials when following locations, even when hostname changed. This option is meaningful only when setting <i><a href="/docs/linux/man/3-curlopt_followlocation/">CURLOPT_FOLLOWLOCATION</a>(3)</i>.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Along with HTTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_followlocation/">CURLOPT_FOLLOWLOCATION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_userpwd/">CURLOPT_USERPWD</a></code>(3),</p>
