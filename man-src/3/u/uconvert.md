---
title: "uconvert(3)"
name: "uconvert"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uconvert/"
description: "uconvert – High level string encoding conversion wrapper. Allegro game programming library."
---

<p>uconvert &#8211; High level string encoding conversion wrapper. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *uconvert(const char *s, int type,

               char *buf, int newtype, int size);</code></pre>
<h2>Description</h2>
<p>Higher level function running on top of do_uconvert(). This function converts the specified string `s&#8217; from `type&#8217; to `newtype&#8217;, storing at most `size&#8217; bytes into the output `buf&#8217; (including the terminating null character), but it checks before doing the conversion, and doesn&#8217;t bother if the string formats are already the same (either both types are equal, or one is ASCII, the other is UTF-8, and the string contains only 7-bit ASCII characters). As a convenience, if `buf&#8217; is NULL it will convert the string into an internal static buffer and the `size&#8217; parameter will be ignored. You should be wary of using this feature, though, because that buffer will be overwritten the next time this routine is called, so don&#8217;t expect the data to persist across any other library calls. The static buffer may hold less than 1024 characters, so you won&#8217;t be able to convert large chunks of text. Example: </p>
<pre><code>char *p = uconvert(input_string, U_CURRENT, buffer, U_ASCII, 256);</code></pre>
<h2>Return Value</h2>
<p>Returns a pointer to `buf&#8217; (or the static buffer if you used NULL) if a conversion was performed. Otherwise returns a copy of `s&#8217;. In any cases, you should use the return value rather than assuming that the string will always be moved to `buf&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_uformat/">set_uformat</a></code>(3), <code><a href="/docs/linux/man/3-need_uconvert/">need_uconvert</a></code>(3), <code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-uconvert_ascii/">uconvert_ascii</a></code>(3), <code><a href="/docs/linux/man/3-uconvert_toascii/">uconvert_toascii</a></code>(3), <code><a href="/docs/linux/man/3-do_uconvert/">do_uconvert</a></code>(3) </p>
