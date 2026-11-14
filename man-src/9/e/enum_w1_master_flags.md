---
title: "enum_w1_master_flags(9)"
name: "enum_w1_master_flags"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enum_w1_master_flags/"
description: "enum_w1_master_flags – bitfields used in w1_master.flags"
---

<p>enum_w1_master_flags &#8211; bitfields used in w1_master.flags</p>
<h2>Synopsis</h2>
<pre>enum w1_master_flags {
 W1_ABORT_SEARCH,
 W1_WARN_MAX_COUNT
}; </pre>
<h2>Constants</h2>
<p>W1_ABORT_SEARCH</p>
<dl>
<dd>abort searching early on shutdown</dl>
<p> W1_WARN_MAX_COUNT</p>
<dl>
<dd>limit warning when the maximum count is reached</dl>
<h2>Author</h2>
<p><code>David Fries</code> &lt;David [at] Fries.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
