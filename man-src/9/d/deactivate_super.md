---
title: "deactivate_super(9)"
name: "deactivate_super"
section: "9"
letter: "d"
url: "/docs/linux/man/9-deactivate_super/"
description: "deactivate_super – drop an active reference to superblock"
---

<p>deactivate_super &#8211; drop an active reference to superblock</p>
<h2>Synopsis</h2>
<pre><code>void deactivate_super(struct super_block *s);</code></pre>
<h2>Arguments</h2>
<p><i>s</i></p>
<dl>
<dd>
<dd>superblock to deactivate</dl>
<h2>Description</h2>
<p>Variant of <code>deactivate_locked_super</code>, except that superblock is *not* locked by caller. If we are going to drop the final active reference, lock will be acquired prior to that.</p>
<h2>Copyright</h2>
