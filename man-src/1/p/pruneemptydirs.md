---
title: "pruneemptydirs(1)"
name: "pruneemptydirs"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pruneemptydirs/"
description: "pruneemptydirs – Detects stale source directories in a CVS tree"
---

<h2 class="name">NAME</h2>
<p> pruneemptydirs &#8211; Detects stale source directories in a CVS tree </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>pruneemptydirs</code> [<code>-f</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>pruneemptydirs</code></p>
<dd>is used to clean up a local CVS tree. It detects directories containing remnants of old stuff which has been removed from the CVS. Such stale directories often break compilation. The current directory and all directories beneath it will be examined. </p>
<p> Note that this tool does not remove anything; it simply prints what to do as a series of remove commands. You can copy and paste these commands, or use them with eval in a script. </p>
<p> This tool works better if the source directory is not the same as the build directory, since it will not print directories containing old executables. </p>
<p> This utility is part of the KDE Software Development Kit.</p>
<h2>OPTIONS</h2>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> Actually perform the deletions instead of just printing them out. Use this option with care.</dl>
<h2>AUTHORS</h2>
<p> <code>pruneemptydirs</code> was written by David Faure&lt;faure [at] kde.org&gt; </p>
<p> This manual page was prepared by Ben Burton&lt;bab [at] debian.org&gt;</p>
<h2>AUTHOR</h2>
<p> <code>Ben Burton</code> &lt;bab [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
