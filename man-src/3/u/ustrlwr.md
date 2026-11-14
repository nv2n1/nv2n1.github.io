---
title: "ustrlwr(3)"
name: "ustrlwr"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrlwr/"
description: "ustrlwr – Replaces all letters with lower case. Allegro game programming library."
---

<p>ustrlwr &#8211; Replaces all letters with lower case. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrlwr(char *s);</code></pre>
<h2>Description</h2>
<p>This function replaces all upper case letters in `s&#8217; with lower case letters. Example: </p>
<pre><code>char buffer[] = &quot;UPPER CASE STRING&quot;;
allegro_message(ustrlwr(buffer));</code></pre>
<h2>Return Value</h2>
<p>The return value is the value of `s&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-utolower/">utolower</a></code>(3), <code><a href="/docs/linux/man/3-ustrupr/">ustrupr</a></code>(3) </p>
