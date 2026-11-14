---
title: "strcasestr(3)"
name: "strcasestr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strcasestr/"
description: "strstr, strcasestr – locate a substring"
---

<p>strstr, strcasestr &#8211; locate a substring</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;string.h&gt;

char *strstr(const char *haystack, const char *needle);

#define _GNU_SOURCE /* See feature_test_macros(7) */

#include &lt;string.h&gt;

char *strcasestr(const char *haystack, const char *needle);</code></pre>
<h2>Description</h2>
<p>The <code>strstr</code>() function finds the first occurrence of the substring <i>needle</i> in the string <i>haystack</i>. The terminating null bytes (&#8216;
