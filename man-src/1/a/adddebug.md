---
title: "adddebug(1)"
name: "adddebug"
section: "1"
letter: "a"
url: "/docs/linux/man/1-adddebug/"
description: "adddebug – Modifies Makefile(s) to add debug info"
---

<h2 class="name">NAME</h2>
<p> adddebug &#8211; Modifies Makefile(s) to add debug info </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>adddebug</code> [<code>-k</code>] [<code>-r</code>] [<code>-n</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>adddebug</code></p>
<dd>modifies the Makefile in the current directory (and optionally in its subdirectories) to add debug info (<code>-g3</code>). It will also remove optimisations (<code>-O[1-9]</code>). </p>
<p> This utility is part of the KDE Software Development Kit.</p>
<h2>OPTIONS</h2>
<p> <code>-k</code></p>
<dl>
<dt>
<dd> Keep optimisations (do not remove <code>-O[1-9]?</code> flags which are removed by default).</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> Recursively search through all subdirectories of the current directory and operate on every Makefile that is found.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> compile without NDEBUG and NO_DEBUG being defined (makes <code>kDebug</code> calls work)</dl>
<h2>AUTHOR</h2>
<p> <code>Ben Burton</code> &lt;bab [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
