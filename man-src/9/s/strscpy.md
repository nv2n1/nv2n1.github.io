---
title: "strscpy(9)"
name: "strscpy"
section: "9"
letter: "s"
url: "/docs/linux/man/9-strscpy/"
description: "strscpy – Copy a C-string into a sized buffer"
---

<p>strscpy &#8211; Copy a C-string into a sized buffer</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t strscpy(char&nbsp;<wbr>*&nbsp;<wbr></code><i>dest</i><code>, const char&nbsp;<wbr>*&nbsp;<wbr></code><i>src</i><code>, size_t&nbsp;<wbr></code><i>count</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dest</i></p>
<dl>
<dd>
<dd>Where to copy the string to</dl>
<p> <i>src</i></p>
<dl>
<dd>Where to copy the string from</dl>
<p> <i>count</i></p>
<dl>
<dd>Size of destination buffer</dl>
<h2>Description</h2>
<p>Copy the string, or as much of it as fits, into the dest buffer. The routine returns the number of characters copied (not including the trailing NUL) or -E2BIG if the destination buffer wasn&#8217;t big enough. The behavior is undefined if the string buffers overlap. The destination buffer is always NUL terminated, unless it&#8217;s zero-sized. </p>
<p> Preferred to <code>strlcpy</code> since the API doesn&#8217;t require reading memory from the src string beyond the specified &#8220;count&#8221; bytes, and since the return value is easier to error-check than <code>strlcpy</code>&#8216;s. In addition, the implementation is robust to the string changing out from underneath it, unlike the current <code>strlcpy</code> implementation. </p>
<p> Preferred to <code>strncpy</code> since it always returns a valid string, and doesn&#8217;t unnecessarily force the tail of the destination buffer to be zeroed. If the zeroing is desired, it&#8217;s likely cleaner to use <code>strscpy</code> with an overflow test, then just <code>memset</code> the tail of the dest buffer.</p>
<h2>Copyright</h2>
