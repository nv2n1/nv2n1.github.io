---
title: "generic_shutdown_super(9)"
name: "generic_shutdown_super"
section: "9"
letter: "g"
url: "/docs/linux/man/9-generic_shutdown_super/"
description: "generic_shutdown_super – common helper for ->kill_sb"
---

<p>generic_shutdown_super &#8211; common helper for -&gt;<code>kill_sb</code></p>
<h2>Synopsis</h2>
<pre><code>void generic_shutdown_super(struct super_block *sb);</code></pre>
<h2>Arguments</h2>
<p><i>sb</i></p>
<dl>
<dd>
<dd>superblock to kill</dl>
<h2>Description</h2>
<p><code>generic_shutdown_super</code> does all fs-independent work on superblock shutdown. Typical -&gt;<code>kill_sb</code> should pick all fs-specific objects that need destruction out of superblock, call <code>generic_shutdown_super</code> and release aforementioned objects. Note: dentries and inodes _are_ taken care of and do not need specific handling. </p>
<p> Upon calling this function, the filesystem may no longer alter or rearrange the set of dentries belonging to this super_block, nor may it change the attachments of dentries to inodes.</p>
<h2>Copyright</h2>
