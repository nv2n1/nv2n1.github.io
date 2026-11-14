---
title: "nicotine(1)"
name: "nicotine"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nicotine/"
description: "nicotine is a graphical client for the SoulSeek peer-to-peer network."
---

<h2>NAME</h2>
<p> <code>nicotine</code> is a graphical client for the SoulSeek peer-to-peer network.</p>
<h2>SYNOPSIS</h2>
<p> <code>nicotine</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>nicotine</code> is a GTK-based client for the SoulSeek peer-to-peer network written in Python.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code><i> &lt;file&gt;</i>, &#8211;config=<i>&lt;file&gt;</i></p>
<dd> Use &lt;file&gt; as configuration file. If &lt;file&gt; does not exists a new empty configuration file will be created.</p>
<dt><code>-d, &#8211;disable-trayicon</code></p>
<dd>
<dt><code>-t, &#8211;enable-trayicon</code></p>
<dd> Enable/disable the tray icon.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show help and exit.</p>
<dt><code>-r, &#8211;enable-rgba</code></p>
<dd>
<dt><code>-x, &#8211;disable-rgba</code></p>
<dd> Enable/disable RGBA mode, for full program transparency. Default is not to use RGBA.</p>
<dt><code>-s, &#8211;hidden</code></p>
<dd> Start the program hidden so only the tray icon is shown.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show version number and exit.</dl>
<h2>EXIT STATUS</h2>
<p> Normally the exit status of the program will be 0. In case required dependencies are not present it returns 1, if the given list of arguments cannot be parsed it returns 2.</p>
<h2>FILES</h2>
<p> All personal files are stored in the folder ~/.nicotine/</p>
<h2>AUTHOR</h2>
<p> This manual page was initially written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Nicotine+ project.<br />
 Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nicotine-import-winconfig/">nicotine-import-winconfig</a>(1)</code> </p>
<h2>Index</h2>
