---
title: "curl_escape(3)"
name: "curl_escape"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_escape/"
description: "curl_escape – URL encodes the given string"
---

<h2>NAME</h2>
<p> curl_escape &#8211; URL encodes the given string</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>char *curl_escape( char *</code><i>url</i><code>, int length</code><i> );</i></p>
<h2>DESCRIPTION</h2>
<p> Obsolete function. Use <i><a href="/docs/linux/man/3-curl_easy_escape/">curl_easy_escape</a>(3)</i> instead! </p>
<p> This function will convert the given input string to an URL encoded string and return that as a new allocated string. All input characters that are not a-z, A-Z or 0-9 will be converted to their &quot;URL escaped&quot; version (%NN where NN is a two-digit hexadecimal number). </p>
<p> If the &#8216;length&#8217; argument is set to 0, curl_escape() will use strlen() on the input &#8216;url&#8217; string to find out the size. </p>
<p> You must curl_free() the returned string when you&#8217;re done with it.</p>
<h2>AVAILABILITY</h2>
<p> Since 7.15.4, <i><a href="/docs/linux/man/3-curl_easy_escape/">curl_easy_escape</a>(3)</i> should be used. This function will be removed in a future release.</p>
<h2>RETURN VALUE</h2>
<p> A pointer to a zero terminated string or NULL if it failed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_unescape/">curl_unescape</a></code>(3), <code><a href="/docs/linux/man/3-curl_free/">curl_free</a></code>(3), <code>RFC</code>2396 </p>
<h2>Index</h2>
