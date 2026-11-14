---
title: "thaw_super(9)"
name: "thaw_super"
section: "9"
letter: "t"
url: "/docs/linux/man/9-thaw_super/"
description: "thaw_super – – unlock filesystem"
---

<p>thaw_super &#8211; &#8211; unlock filesystem</p>
<h2>Synopsis</h2>
<pre><code>int thaw_super(struct super_block *sb);</code></pre>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>the super to thaw</dl>
<h2>Description</h2>
<p>Unlocks the filesystem and marks it writeable again after <code>freeze_super</code>.</p>
<h2>Copyright</h2>
