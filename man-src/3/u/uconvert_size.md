---
title: "uconvert_size(3)"
name: "uconvert_size"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uconvert_size/"
description: "uconvert_size – Number of bytes needed to store a string after conversion. Allegro game programming library."
---

<p>uconvert_size &#8211; Number of bytes needed to store a string after conversion. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int uconvert_size(const char *s, int type, int newtype);</code></pre>
<h2>Description</h2>
<p>Finds out how many bytes are required to store the specified string `s&#8217; after a conversion from `type&#8217; to `newtype&#8217;, including the mandatory zero terminator of the string. You can use U_CURRENT for either `type&#8217; or `newtype&#8217; as a shortcut to represent whatever text encoding format is currently selected. Example: </p>
<pre><code>length = uconvert_size(old_string, U_CURRENT, U_UNICODE);
new_string = malloc(length);
ustrcpy(new_string, old_string);</code></pre>
<h2>Return Value</h2>
<p>Returns the number of bytes required to store the string after conversion. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-need_uconvert/">need_uconvert</a></code>(3), <code><a href="/docs/linux/man/3-do_uconvert/">do_uconvert</a></code>(3) </p>
