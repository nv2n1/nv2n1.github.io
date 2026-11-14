---
title: "need_uconvert(3)"
name: "need_uconvert"
section: "3"
letter: "n"
url: "/docs/linux/man/3-need_uconvert/"
description: "need_uconvert – Tells if a string requires encoding conversion. Allegro game programming library."
---

<p>need_uconvert &#8211; Tells if a string requires encoding conversion. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int need_uconvert(const char *s, int type, int newtype);</code></pre>
<h2>Description</h2>
<p>Given a pointer to a string (`s&#8217;), a description of the type of the string (`type&#8217;), and the type that you would like this string to be converted into (`newtype&#8217;), this function tells you whether any conversion is required. No conversion will be needed if `type&#8217; and `newtype&#8217; are the same, or if one type is ASCII, the other is UTF-8, and the string contains only character values less than 128. As a convenience shortcut, you can pass the value U_CURRENT as either of the type parameters, to represent whatever text encoding format is currently selected. Example: </p>
<pre><code>if (need_uconvert(text, U_UTF8, U_CURRENT)) {
    /* conversion is required */
}</code></pre>
<h2>Return Value</h2>
<p>Returns non-zero if any conversion is required or zero otherwise. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_uformat/">set_uformat</a></code>(3), <code><a href="/docs/linux/man/3-get_uformat/">get_uformat</a></code>(3), <code><a href="/docs/linux/man/3-do_uconvert/">do_uconvert</a></code>(3), <code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3) </p>
