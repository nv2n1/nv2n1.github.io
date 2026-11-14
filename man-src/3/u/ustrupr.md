---
title: "ustrupr(3)"
name: "ustrupr"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrupr/"
description: "ustrupr – Replaces all letters with upper case. Allegro game programming library."
---

<p>ustrupr &#8211; Replaces all letters with upper case. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrupr(char *s);</code></pre>
<h2>Description</h2>
<p>This function replaces all lower case letters in `s&#8217; with upper case letters. Example: </p>
<pre><code>char buffer[] = &quot;lower case string&quot;;
allegro_message(ustrupr(buffer));</code></pre>
<h2>Return Value</h2>
<p>The return value is the value of `s&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-utolower/">utolower</a></code>(3), <code><a href="/docs/linux/man/3-ustrlwr/">ustrlwr</a></code>(3) </p>
