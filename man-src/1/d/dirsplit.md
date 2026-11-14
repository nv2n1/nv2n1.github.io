---
title: "dirsplit(1)"
name: "dirsplit"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dirsplit/"
description: "dirsplit – splits directory into multiple with equal size"
---

<h2 class="name">NAME</h2>
<p> dirsplit &#8211; splits directory into multiple with equal size </p>
<h2>SYNOPSIS</h2>
<p> dirsplit <code>[options]</code> &lt; directory | content-list-file &gt;</p>
<h2>DESCRIPTION</h2>
<p> displit is designed to for a simple purpose: convert a directory with many multiple files (which are all smaller than a certain medium, eg. DVD) and &quot;splits&quot; it into &quot;volumes&quot;, looking for the optimal order to get the best space/medium-number efficiency. </p>
<p> The actual action is either adding the files to mkisofs catalogs or real moving of files into new directories (or creating links/symlinks). The method is not limited to files, whole directories can also be handled this way (see various filesystem exploration modes).</p>
<h2>OPTIONS</h2>
<dl>
<dt>Run dirsplit <code>-h</code> to get the basic usage info.</p>
<dd>
<dt>Run dirsplit <code>-H</code> to get the whole option overview and description.</p>
<dd></dl>
<h2>EXAMPLES</h2>
<p> Run dirsplit <code>-H</code> to see the commented examples.</p>
<h2>AUTHOR</h2>
<p> <code>dirsplit</code> is created by Eduard Bloch (blade [at] debian.org) and is licensed under the GPLv2. </p>
<h2>Index</h2>
