---
title: "curl_easy_escape(3)"
name: "curl_easy_escape"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_escape/"
description: "curl_easy_escape – URL encodes the given string"
---

<h2>NAME</h2>
<p> curl_easy_escape &#8211; URL encodes the given string</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>char *curl_easy_escape( CURL *</code><i>curl</i><code>, char *</code><i>url</i><code>, int length</code><i> );</i></p>
<h2>DESCRIPTION</h2>
<p> This function converts the given input string to an URL encoded string and returns that as a new allocated string. All input characters that are not a-z, A-Z, 0-9, &#8216;-&#8216;, &#8216;.&#8217;, &#8216;_&#8217; or &#8216;~&#8217; are converted to their &quot;URL escaped&quot; version (%NN where NN is a two-digit hexadecimal number). </p>
<p> If the <code>length</code> argument is set to 0 (zero), <i><a href="/docs/linux/man/3-curl_easy_escape/">curl_easy_escape</a>(3)</i> uses strlen() on the input <code>url</code> to find out the size. </p>
<p> You must <i><a href="/docs/linux/man/3-curl_free/">curl_free</a>(3)</i> the returned string when you&#8217;re done with it.</p>
<h2>AVAILABILITY</h2>
<p> Added in 7.15.4 and replaces the old <i><a href="/docs/linux/man/3-curl_escape/">curl_escape</a>(3)</i> function.</p>
<h2>RETURN VALUE</h2>
<p> A pointer to a zero terminated string or NULL if it failed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_easy_unescape/">curl_easy_unescape</a></code>(3), <code><a href="/docs/linux/man/3-curl_free/">curl_free</a></code>(3), <code>RFC</code>2396 </p>
<h2>Index</h2>
