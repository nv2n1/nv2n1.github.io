---
title: "match_string(9)"
name: "match_string"
section: "9"
letter: "m"
url: "/docs/linux/man/9-match_string/"
description: "match_string – matches given string in an array"
---

<p>match_string &#8211; matches given string in an array</p>
<h2>Synopsis</h2>
<pre><code>int match_string(const char *const *array, size_t n, const char *string);</code></pre>
<h2>Arguments</h2>
<p><i>array</i></p>
<dl>
<dd>
<dd>array of strings</dl>
<p> <i>n</i></p>
<dl>
<dd>number of strings in the array or -1 for NULL terminated arrays</dl>
<p> <i>string</i></p>
<dl>
<dd>string to match with</dl>
<h2>Return</h2>
<p>index of a <i>string</i> in the <i>array</i> if matches, or <code>-EINVAL</code> otherwise.</p>
<h2>Copyright</h2>
