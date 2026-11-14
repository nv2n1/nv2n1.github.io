---
title: "memparse(9)"
name: "memparse"
section: "9"
letter: "m"
url: "/docs/linux/man/9-memparse/"
---

memparse - parse a string with mem suffixes into a number

<h2>Synopsis</h2>

<pre><code>unsigned long long memparse(const char *ptr, char **retptr);</code></pre>

<h2>Arguments</h2>

<i>ptr</i>
<dl><dd><dd>Where parse begins</dl>
 

 <i>retptr</i>
<dl><dd>(output) Optional pointer to next char after parse completes</dl>

<h2>Description</h2>

Parses a string into a number. The number stored at <i>ptr</i> is potentially suffixed with K, M, G, T, P, E.

<h2>Copyright</h2>


