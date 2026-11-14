---
title: "curl_easy_unescape(3)"
name: "curl_easy_unescape"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_unescape/"
description: "curl_easy_unescape – URL decodes the given string"
---

<h2>NAME</h2>
<p> curl_easy_unescape &#8211; URL decodes the given string</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>char *curl_easy_unescape( CURL *</code><i>curl</i><code>, char *</code><i>url</i><code>, int inlength</code> <code>, int *</code><i>outlength</i><code> );</code></p>
<h2>DESCRIPTION</h2>
<p> This function converts the given URL encoded input string to a &quot;plain string&quot; and returns that in an allocated memory area. All input characters that are URL encoded (%XX where XX is a two-digit hexadecimal number) are converted to their binary versions. </p>
<p> If the <code>length</code> argument is set to 0 (zero), <i><a href="/docs/linux/man/3-curl_easy_unescape/">curl_easy_unescape</a>(3)</i> will use strlen() on the input <i>url</i> string to find out the size. </p>
<p> If <code>outlength</code> is non-NULL, the function will write the length of the returned string in the integer it points to. This allows an escaped string containing %00 to still get used properly after unescaping. </p>
<p> You must <i><a href="/docs/linux/man/3-curl_free/">curl_free</a>(3)</i> the returned string when you&#8217;re done with it.</p>
<h2>AVAILABILITY</h2>
<p> Added in 7.15.4 and replaces the old <i><a href="/docs/linux/man/3-curl_unescape/">curl_unescape</a>(3)</i> function.</p>
<h2>RETURN VALUE</h2>
<p> A pointer to a zero terminated string or NULL if it failed.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-curl_easy_escape/">curl_easy_escape</a>(3), <a href="/docs/linux/man/3-curl_free/">curl_free</a>(3), RFC 2396</i> </p>
<h2>Index</h2>
