---
title: "tilestache-clean(1)"
name: "tilestache-clean"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tilestache-clean/"
description: "tilestache-clean – clean tiles from a TileStache cache"
---

<h2>NAME</h2>
<p> tilestache-clean &#8211; clean tiles from a TileStache cache</p>
<h2>SYNOPSIS</h2>
<p> <code>tilestache-clean</code> [<i>options</i>]<i> zoom</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>tilestache-clean</code> command. </p>
<p> <code>tilestache-clean</code> is used to clean tiles from a TileStache cache. </p>
<p> Cleans a single layer in your TileStache configuration &#8211; no images are returned, and TileStache ends up with an empty in selected areas cache. Bounding box is given as a pair of lat/lon coordinates, e.g. &quot;37.788 -122.349 37.833 -122.246&quot;. Output is a list of tile paths as they are created. </p>
<p> The <i>zoom</i> option is a space separated list of zoom levels which will be cleaned. e.g. 12 13 14 15 will clean zooms 12 through 15. Many shells allow you to use {a..b} which will expand to a list of numbers a though to b. <code>Required.</code></p>
<h2>REQUIRED OPTIONS</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;config</code> <i>file</i></p>
<dd> Path to configuration file. <code>Required.</code></p>
<dt><code>-l</code>, <code>&#8211;layer</code> <i>layer</i></p>
<dd> Layer name from configuration. &quot;ALL&quot; is a special value that will clean all layers in turn. If you have an actual layer named &quot;ALL&quot;, use &quot;ALL LAYERS&quot; instead. <code>Required.</code></p>
<dt><code>-b</code>, <code>&#8211;bbox</code> <i>south west north east</i></p>
<dd> Bounding box in floating point geographic coordinates. <code>Required.</code></dl>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;help</code> Show summary of options.</p>
<dl>
<dt><code>-p</code>, <code>&#8211;padding</code> <i>padding</i></p>
<dd> Extra margin of tiles to add around bounded area. Default value is 0 (no extra tiles).</p>
<dt><code>-e</code>, <code>&#8211;extension</code> <i>extension</i></p>
<dd> Optional file type for rendered tiles. Default value is &#8216;png&#8217;.</p>
<dt><code>-f</code>, <code>&#8211;progress-file</code> <i>file</i></p>
<dd> Optional JSON progress file that gets written on each iteration, so you don&#8217;t have to pay close attention.</p>
<dt><code>-q</code></p>
<dd> Suppress chatty output, &#8211;progress-file works well with this.</p>
<dt><code>-i</code>, <code>&#8211;include-path</code> <i>path</i></p>
<dd> Add the following colon-separated list of paths to Python&#8217;s include path (aka sys.path)</p>
<dt><code>&#8211;tile-list</code> <i>file</i></p>
<dd> Optional file of tile coordinates, a simple text list of Z/X/Y coordinates. Overrides &#8211;bbox and &#8211;padding.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tilestache-seed/">tilestache-seed</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>TileStache</code> was written by Michal Migurski &lt;mike [at] stamen.com&gt;. </p>
<p> This manual page was written by Andrew Harvey &lt;andrew.harvey4 [at] gmail.com&gt;, for the Debian project (and may be used by others). </p>
<h2>Index</h2>
