---
title: "curl_unescape(3)"
name: "curl_unescape"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_unescape/"
description: "curl_unescape – URL decodes the given string"
---

<h2>NAME</h2>
<p> curl_unescape &#8211; URL decodes the given string</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>char *curl_unescape( char *</code><i>url</i><code>, int length</code><i> );</i></p>
<h2>DESCRIPTION</h2>
<p> Obsolete function. Use <i><a href="/docs/linux/man/3-curl_easy_unescape/">curl_easy_unescape</a>(3)</i> instead! </p>
<p> This function will convert the given URL encoded input string to a &quot;plain string&quot; and return that as a new allocated string. All input characters that are URL encoded (%XX where XX is a two-digit hexadecimal number) will be converted to their plain text versions. </p>
<p> If the &#8216;length&#8217; argument is set to 0, curl_unescape() will use strlen() on the input &#8216;url&#8217; string to find out the size. </p>
<p> You must curl_free() the returned string when you&#8217;re done with it.</p>
<h2>AVAILABILITY</h2>
<p> Since 7.15.4, <i><a href="/docs/linux/man/3-curl_easy_unescape/">curl_easy_unescape</a>(3)</i> should be used. This function will be removed in a future release.</p>
<h2>RETURN VALUE</h2>
<p> A pointer to a zero terminated string or NULL if it failed.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-curl_easy_escape/">curl_easy_escape</a>(3), <a href="/docs/linux/man/3-curl_easy_unescape/">curl_easy_unescape</a>(3), <a href="/docs/linux/man/3-curl_free/">curl_free</a>(3), RFC 2396</i> </p>
<h2>Index</h2>
