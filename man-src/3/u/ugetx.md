---
title: "ugetx(3)"
name: "ugetx"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ugetx/"
description: "ugetx, ugetxc – Low level helper function for reading Unicode text data. Allegro game programming library."
---

<p>ugetx, ugetxc &#8211; Low level helper function for reading Unicode text data. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int ugetx(char **s);
int ugetxc(const char **s);</code></pre>
<h2>Description</h2>
<p>Low level helper function for reading Unicode text data. ugetxc is provided for working with pointer-to-pointer-to-const char data. Example: </p>
<pre><code>char *p = string;
int first_letter, second_letter, third_letter;
first_letter = ugetx(&amp;p);
second_letter = ugetx(&amp;p);
third_letter = ugetx(&amp;p);</code></pre>
<h2>Return Value</h2>
<p>Returns the character pointed to by `s&#8217; in the current encoding format, and advances the pointer to the next character after the one just returned. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ugetc/">ugetc</a></code>(3), <code><a href="/docs/linux/man/3-usetc/">usetc</a></code>(3), <code><a href="/docs/linux/man/3-uwidth/">uwidth</a></code>(3), <code><a href="/docs/linux/man/3-ucwidth/">ucwidth</a></code>(3), <code><a href="/docs/linux/man/3-uisok/">uisok</a></code>(3) </p>
