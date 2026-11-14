---
title: "curl_strequal(3)"
name: "curl_strequal"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_strequal/"
description: "curl_strequal, curl_strnequal – case insensitive string comparisons"
---

<h2>NAME</h2>
<p> curl_strequal, curl_strnequal &#8211; case insensitive string comparisons</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>int curl_strequal(char *</code><i>str1</i><code>, char *</code><i>str2</i><code>);</code> </p>
<p> <code>int curl_strenqual(char *</code><i>str1</i><code>, char *</code><i>str2</i><code>, size_t </code><i>len</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>curl_strequal()</code> function compares the two strings <i>str1</i> and <i>str2</i>, ignoring the case of the characters. It returns a non-zero (TRUE) integer if the strings are identical. </p>
<p> The <code>curl_strnequal()</code> function is similar, except it only compares the first <i>len</i> characters of <i>str1</i>. </p>
<p> These functions are provided by libcurl to enable applications to compare strings in a truly portable manner. There are no standard portable case insensitive string comparison functions. These two work on all platforms.</p>
<h2>AVAILABILITY</h2>
<p> These functions will be removed from the public libcurl API in a near future. They will instead be made &quot;available&quot; by source code access only, and then as curlx_strequal() and curlx_strenqual().</p>
<h2>RETURN VALUE</h2>
<p> Non-zero if the strings are identical. Zero if they&#8217;re not.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-strcmp/">strcmp</a></code>(3), <code><a href="/docs/linux/man/3-strcasecmp/">strcasecmp</a></code>(3) </p>
<h2>Index</h2>
