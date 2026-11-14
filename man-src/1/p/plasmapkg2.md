---
title: "plasmapkg2(1)"
name: "plasmapkg2"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plasmapkg2/"
description: "plasmapkg2 – Install, list, remove Plasma packages"
---

<h2 class="name">NAME</h2>
<p> plasmapkg2 &#8211; Install, list, remove Plasma packages </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>plasmapkg2</code> [<code>&#8211;hash</code><i> path</i>] [<code>-g, &#8211;global</code>] [<code>-t, &#8211;type</code><i> type</i>] [<code>-i, &#8211;install</code><i> path</i>] [<code>-s, &#8211;show</code><i> name</i>] [<code>-u, &#8211;upgrade</code><i> path</i>] [<code>-l, &#8211;list</code>] [<code>&#8211;list-types</code>] [<code>-r, &#8211;remove</code><i> name</i>] [<code>-p, &#8211;packageroot</code><i> path</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>plasmapkg2</code></p>
<dd>is a command line tool to install, list, remove Plasma packages.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;hash</code> <i> path</i></p>
<dl>
<dt>
<dd> Generate a SHA1 hash for the package at &#8220;path&#8221;.</dl>
<p> <code>-g, &#8211;global</code></p>
<dl>
<dt>
<dd> For install or remove, operates on packages installed for all users.</dl>
<p> <code>-t, &#8211;type</code> <i> type</i></p>
<dl>
<dt>
<dd> The type of package, e.g. theme, wallpaper, plasmoid, dataengine, runner, layout-template, etc. [plasmoid].</dl>
<p> <code>-i, &#8211;install</code> <i> path</i></p>
<dl>
<dt>
<dd> Install the package at &#8220;path&#8221;.</dl>
<p> <code>-s, &#8211;show</code> <i> name</i></p>
<dl>
<dt>
<dd> Show information of package &#8220;name&#8221;.</dl>
<p> <code>-u, &#8211;upgrade</code> <i> path</i></p>
<dl>
<dt>
<dd> Upgrade the package at &#8220;path&#8221;.</dl>
<p> <code>-l, &#8211;list</code></p>
<dl>
<dt>
<dd> List installed packages.</dl>
<p> <code>&#8211;list-types</code></p>
<dl>
<dt>
<dd> Lists all known Package types that can be installed.</dl>
<p> <code>-r, &#8211;remove</code> <i> name</i></p>
<dl>
<dt>
<dd> Remove the package named &#8220;name&#8221;.</dl>
<p> <code>-p, &#8211;packageroot</code> <i> path</i></p>
<dl>
<dt>
<dd> Absolute path to the package root. If not supplied, then the standard data directories for this Plasma session will be searched instead.</dl>
<h2>SEE ALSO</h2>
<p> More detailed user documentation is available from m[blue]<code>help:/plasma-desktop</code>m[] (either enter this URL into Konqueror, or run <code>khelpcenter</code><i>help:/plasma-desktop</i>).</p>
<h2>AUTHORS</h2>
<p> <code>plasmapkg2</code> was written by Aaron Seigo&lt;aseigo [at] kde.org&gt;. </p>
<h2>Index</h2>
