---
title: "chcp(8)"
name: "chcp"
section: "8"
letter: "c"
url: "/docs/linux/man/8-chcp/"
description: "chcp – change mode of NILFS2 checkpoints"
---

<p>chcp &#8211; change mode of NILFS2 checkpoints</p>
<h2>Synopsis</h2>
<p><code>chcp</code> [<i>options</i>] <code>cp</code> | <code>ss</code> [<i>device</i>] <i>checkpoint-number</i> &#8230;</p>
<h2>Description</h2>
<p><code>chcp</code> is a utility to change the mode of the given checkpoints for the NILFS2 file system found in <i>device</i>. <code>chcp</code> changes checkpoints to snapshots, or vice versa. The target checkpoints are specified with one or more checkpoint numbers. When <i>device</i> is omitted, it tries to find a NILFS2 file system from <i>/proc/mounts</i>. </p>
<p> This command is valid only for mounted NILFS2 file systems, and will fail if the <i>device</i> has no active mounts.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Display help message and exit.</dl>
<h2>Author</h2>
<p>Koji Sato &lt;koji [at] osrg.net&gt;</p>
<h2>Availability</h2>
<p><code>chcp</code> is part of the nilfs-utils package and is available from <a rel="nofollow" href="http://www.nilfs.org.">http://www.nilfs.org.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nilfs/">nilfs</a></code>(8), <code><a href="/docs/linux/man/1-lscp/">lscp</a></code>(1), <code><a href="/docs/linux/man/8-mkcp/">mkcp</a></code>(8), <code><a href="/docs/linux/man/8-rmcp/">rmcp</a></code>(8). </p>
