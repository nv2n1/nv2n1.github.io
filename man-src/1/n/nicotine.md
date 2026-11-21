---

title: "nicotine(1)"
name: "nicotine"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nicotine/"
description: "nicotine is a graphical client for the SoulSeek peer-to-peer network."
---

<p> <code>nicotine</code> is a graphical client for the SoulSeek peer-to-peer network.</p>
<h2>SYNOPSIS</h2>
<p> <code>nicotine</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>nicotine</code> is a GTK-based client for the SoulSeek peer-to-peer network written in Python.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code><i> &lt;file&gt;</i>, &#8211;config=<i>&lt;file&gt;</i></dt>
<dd> Use &lt;file&gt; as configuration file. If &lt;file&gt; does not exists a new empty configuration file will be created.</dd>
<dt><code>-d, &#8211;disable-trayicon</code></dt>
<dd>
</dd><dt><code>-t, &#8211;enable-trayicon</code></dt>
<dd> Enable/disable the tray icon.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show help and exit.</dd>
<dt><code>-r, &#8211;enable-rgba</code></dt>
<dd>
</dd><dt><code>-x, &#8211;disable-rgba</code></dt>
<dd> Enable/disable RGBA mode, for full program transparency. Default is not to use RGBA.</dd>
<dt><code>-s, &#8211;hidden</code></dt>
<dd> Start the program hidden so only the tray icon is shown.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Show version number and exit.</dd></dl>
<h2>EXIT STATUS</h2>
<p> Normally the exit status of the program will be 0. In case required dependencies are not present it returns 1, if the given list of arguments cannot be parsed it returns 2.</p>
<h2>FILES</h2>
<p> All personal files are stored in the folder ~/.nicotine/</p>
<h2>AUTHOR</h2>
<p> This manual page was initially written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Nicotine+ project.<br />
 Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nicotine-import-winconfig/">nicotine-import-winconfig</a>(1)</code> </p>
