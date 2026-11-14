---
title: "strsep(9)"
name: "strsep"
section: "9"
letter: "s"
url: "/docs/linux/man/9-strsep/"
description: "strsep – Split a string into tokens"
---

<p>strsep &#8211; Split a string into tokens</p>
<h2>Synopsis</h2>
<pre><code>char *strsep(char **s, const char *ct);</code></pre>
<h2>Arguments</h2>
<p><i>s</i></p>
<dl>
<dd>
<dd>The string to be searched</dl>
<p> <i>ct</i></p>
<dl>
<dd>The characters to search for</dl>
<h2>Description</h2>
<p><code>strsep</code> updates <i>s</i> to point after the token, ready for the next call. </p>
<p> It returns empty tokens, too, behaving exactly like the libc function of that name. In fact, it was stolen from glibc2 and de-fancy-fied. Same semantics, slimmer shape. ;)</p>
<h2>Copyright</h2>
