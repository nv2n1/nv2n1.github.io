---
title: "do_uconvert(3)"
name: "do_uconvert"
section: "3"
letter: "d"
url: "/docs/linux/man/3-do_uconvert/"
description: "do_uconvert – Converts a string to another encoding format. Allegro game programming library."
---

<h2>NAME</h2>
<p> do_uconvert &#8211; Converts a string to another encoding format. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void do_uconvert(const char *s, int type,</code> <code>char *buf, int newtype, int size);</code></p>
<h2>DESCRIPTION</h2>
<p> Converts the specified string `s&#8217; from `type&#8217; to `newtype&#8217;, storing at most `size&#8217; bytes into the output `buf&#8217;. The type parameters can use the value U_CURRENT as a shortcut to represent the currently selected encoding format. Example: </p>
<pre><code>
char temp_string[256];
do_uconvert(input_string, U_CURRENT, temp_string, U_ASCII, 256);
</code></pre>
<p> Note that, even for empty strings, your destination string must have at least enough bytes to store the terminating null character of the string, and your parameter size must reflect this. Otherwise, the debug version of Allegro will abort at an assertion, and the release version of Allegro will overrun the destination buffer. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3) </p>
<h2>Index</h2>
