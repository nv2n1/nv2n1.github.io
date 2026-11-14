---
title: "rmcp(8)"
name: "rmcp"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rmcp/"
description: "rmcp – remove NILFS2 checkpoints"
---

<p>rmcp &#8211; remove NILFS2 checkpoints</p>
<h2>Synopsis</h2>
<p><code>rmcp</code> [<i>options</i>] [<i>device</i>] <i>checkpoint-range</i> &#8230;</p>
<h2>Description</h2>
<p><code>rmcp</code> is a utility for removing checkpoints from the NILFS2 file system found in <i>device</i>. The checkpoints which user wants to remove are specified with one or more <i>checkpoint-ranges</i>. When <i>device</i> is omitted, rmcp tries to find a NILFS2 file system from <i>/proc/mounts</i>. </p>
<p> The <i>checkpoint-range</i> must be provided with one or two integers in one of the following way:</p>
<dl>
<dt><code>cno</code></p>
<dd>single checkpoint number</p>
<dt><code>start..end</code></p>
<dd>every checkpoint number between <code>start</code> and <code>end</code></p>
<dt><code>..end</code></p>
<dd>every checkpoint number equal or younger than <code>end</code></p>
<dt><code>start..</code></p>
<dd>every checkpoint number equal or greater than <code>start</code></dl>
<p> This command is valid only for mounted NILFS2 file systems, and will fail if the <i>device</i> has no active mounts.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Ignore snapshots or nonexistent checkpoints.</p>
<dt><code>-i</code></p>
<dd>Prompt before any removal.</p>
<dt><code>-h</code></p>
<dd>Display help message and exit.</dl>
<h2>Author</h2>
<p>Koji Sato &lt;koji [at] osrg.net&gt;, Ryusuke Konishi &lt;ryusuke [at] osrg.net&gt;.</p>
<h2>Availability</h2>
<p><code>rmcp</code> is part of the nilfs-utils package and is available from <a rel="nofollow" href="http://www.nilfs.org.">http://www.nilfs.org.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nilfs/">nilfs</a></code>(8), <code><a href="/docs/linux/man/1-lscp/">lscp</a></code>(1), <code><a href="/docs/linux/man/8-mkcp/">mkcp</a></code>(8), <code><a href="/docs/linux/man/8-chcp/">chcp</a></code>(8). </p>
