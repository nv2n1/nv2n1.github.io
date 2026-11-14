---
title: "git-relink(1)"
name: "git-relink"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-relink/"
description: "git-relink – Hardlink common objects in local repositories"
---

<h2 class="name">NAME</h2>
<p> git-relink &#8211; Hardlink common objects in local repositories </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git relink</i> [--safe] &lt;dir&gt;... &lt;master_dir&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> This will scan 1 or more object repositories and look for objects in common with a master repository. Objects not already hardlinked to the master repository will be replaced with a hardlink to the master repository.</p>
<h2>OPTIONS</h2>
<p> &#8211;safe</p>
<dl>
<dt>
<dd> Stops if two objects with the same hash exist but have different sizes. Default is to warn and continue.</dl>
<p> &lt;dir&gt;</p>
<dl>
<dt>
<dd> Directories containing a .git/objects/ subdirectory.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
