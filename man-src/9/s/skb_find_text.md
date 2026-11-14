---
title: "skb_find_text(9)"
name: "skb_find_text"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_find_text/"
description: "skb_find_text – Find a text pattern in skb data"
---

<p>skb_find_text &#8211; Find a text pattern in skb data</p>
<h2>Synopsis</h2>
<pre><code>unsigned int skb_find_text(struct sk_buff *skb, unsigned int from, unsigned int to, struct ts_config *config);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>the buffer to look in</dl>
<p> <i>from</i></p>
<dl>
<dd>search offset</dl>
<p> <i>to</i></p>
<dl>
<dd>search limit</dl>
<p> <i>config</i></p>
<dl>
<dd>textsearch configuration</dl>
<h2>Description</h2>
<p>Finds a pattern in the skb data according to the specified textsearch configuration. Use <code>textsearch_next</code> to retrieve subsequent occurrences of the pattern. Returns the offset to the first occurrence or UINT_MAX if no match was found.</p>
<h2>Copyright</h2>
