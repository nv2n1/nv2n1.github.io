---
title: "mkcp(8)"
name: "mkcp"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mkcp/"
description: "mkcp – make a NILFS2 checkpoint"
---

<p>mkcp &#8211; make a NILFS2 checkpoint</p>
<h2>Synopsis</h2>
<p><code>mkcp</code> [<i>options</i>] [<i>device</i>]</p>
<h2>Description</h2>
<p><code>mkcp</code> is a utility for making a checkpoint or snapshot for the NILFS2 file system found in <i>device</i>. When <i>device</i> is omitted, it tries to find a NILFS2 file system from <i>/proc/mounts</i>. </p>
<p> This command is valid only for mounted NILFS2 file systems, and will fail if the <i>device</i> has no active mounts.</p>
<h2>Options</h2>
<dl>
<dt><code>-s</code></p>
<dd>Create a snapshot.</p>
<dt><code>-h</code></p>
<dd>Display help message and exit.</dl>
<h2>Author</h2>
<p>Koji Sato &lt;koji [at] osrg.net&gt;</p>
<h2>Availability</h2>
<p><code>mkcp</code> is part of the nilfs-utils package and is available from <a rel="nofollow" href="http://www.nilfs.org.">http://www.nilfs.org.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nilfs/">nilfs</a></code>(8), <code><a href="/docs/linux/man/1-lscp/">lscp</a></code>(1), <code><a href="/docs/linux/man/8-chcp/">chcp</a></code>(8), <code><a href="/docs/linux/man/8-rmcp/">rmcp</a></code>(8). </p>
