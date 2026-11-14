---
title: "kde4-config(1)"
name: "kde4-config"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kde4-config/"
description: "kde4-config – Prints KDE installation paths"
---

<h2 class="name">NAME</h2>
<p> kde4-config &#8211; Prints KDE installation paths </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>kde4-config</code> [&#8211;expandvars] [&#8211;prefix] [&#8211;exec-prefix] [&#8211;libsuffix] [&#8211;localprefix] [&#8211;version] [&#8211;types] [&#8211;path&nbsp;<wbr><i>type</i>] [&#8211;userpath&nbsp;<wbr><i>type</i>] [&#8211;install&nbsp;<wbr><i>type</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>kde4-config is a command line program used to retrieve information about KDE installation or user paths. </p>
<p> Use this program to determine where the various aspects of the KDE installation reside on your system.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;expandvars</code></p>
<dl>
<dt>
<dd> expand ${prefix} and ${exec_prefix} in output</dl>
<p> <code>&#8211;prefix</code></p>
<dl>
<dt>
<dd> Compiled in prefix for KDE libraries</dl>
<p> <code>&#8211;exec-prefix</code></p>
<dl>
<dt>
<dd> Compiled in exec_prefix for KDE libraries</dl>
<p> <code>&#8211;libsuffix</code></p>
<dl>
<dt>
<dd> Compiled in library path suffix</dl>
<p> <code>&#8211;localprefix</code></p>
<dl>
<dt>
<dd> Prefix in $<code>HOME</code> used to write files</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Compiled in version string for KDE libraries</dl>
<p> <code>&#8211;types</code></p>
<dl>
<dt>
<dd> Print a list of all available KDE resource types</dl>
<p> <code>&#8211;path </code><i>type</i></p>
<dl>
<dt>
<dd> Search path for the specified <i>type</i></dl>
<p> <code>&#8211;userpath </code><i>type</i></p>
<dl>
<dt>
<dd> User paths for the types: desktop|autostart|trash|document</dl>
<p> <code>&#8211;install </code><i>type</i></p>
<dl>
<dt>
<dd> Prefix to install resource files to</dl>
<h2>EXAMPLES</h2>
<p> Print the top-level KDE installation directory: </p>
<p> %<code>kde4-config &#8211;prefix</code> </p>
<p> Print a list of all resource types: </p>
<p> %<code>kde4-config &#8211;types</code> </p>
<p> Print the installed wallpaper path: </p>
<p> %<code>kde4-config &#8211;path wallpaper</code></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-kdeoptions/">kdeoptions</a>(7)</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> <code>Stephan Kulow</code> &lt;coolo [at] kde.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
