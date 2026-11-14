---
title: "ne_shave(3)"
name: "ne_shave"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_shave/"
description: "ne_shave – trim whitespace from a string"
---

<p>ne_shave &#8211; trim whitespace from a string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_string.h&gt;

char *ne_shave(char *str, const char *whitespace);</code></pre>
<h2>Description</h2>
<p><code>ne_shave</code></p>
<dd>returns a portion of <i>str</i> with any leading or trailing characters in the <i>whitespace</i> array removed. <i>str</i> may be modified. Note that the return value may not be equal to <i>str</i>.</p>
<h2>Examples</h2>
<p>The following code segment will output &quot;fish&quot;: </p>
<pre><code>char s[] = &quot;.!.fish!.!&quot;;
puts(ne_shave(s, &quot;.!&quot;));</code></pre>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
