---
title: "tilestache-render(1)"
name: "tilestache-render"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tilestache-render/"
description: "tilestache-render – render tiles from tilestache"
---

<h2>NAME</h2>
<p> tilestache-render &#8211; render tiles from tilestache</p>
<h2>SYNOPSIS</h2>
<p> <code>tilestache-render</code> [<i>options</i>]<i> coordinates</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>tilestache-render</code> command. </p>
<p> <code>tilestache-render</code> is used to render tiles from <code>TileStache</code>.<br />
 Each coordinate in the argument list should look like &quot;12/656/1582.png&quot;, similar to URL paths in web server usage. Coordinates are processed in order, each one rendered to an image file in a temporary location and output to stdout.</p>
<h2>REQUIRED OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;config</code> <i>file</i></p>
<dd> Path to configuration file.</p>
<dt><code>-l</code>, <code>&#8211;layer</code> <i>layer</i></p>
<dd> Layer name from configuration.</dl>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code> Show summary of options.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tilestache-seed/">tilestache-seed</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>TileStache</code> was written by Michal Migurski &lt;mike [at] stamen.com&gt;. </p>
<p> This manual page was written by David Paleino &lt;dapal [at] debian.org&gt;, for the Debian project (and may be used by others). </p>
<h2>Index</h2>
