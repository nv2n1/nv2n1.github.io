---
title: "inkview(1)"
name: "inkview"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inkview/"
description: "Inkview – an SVG viewer and slideshow program."
---

<h2 class="name">NAME</h2>
<p> Inkview &#8211; an SVG viewer and slideshow program. </p>
<h2>SYNOPSIS</h2>
<p> <tt>&quot;inkview [options] [filename ...]&quot;</tt> </p>
<p> options: </p>
<pre><code>
- h, --help - V, --version - f, --fullscreen - r, --recursive - t, --timer = NUMBER - s, --scale = NUMBER - p, --preload
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>Inkview</code> is an <code>Scalable Vector Graphics (</code><font SIZE="-1"><code>SVG</code></font><code>)</code> viewer that can also be used for slideshows or presentations. One or more <font SIZE="-1"><code>FILES</code></font> or <font SIZE="-1"><code>FOLDERS</code></font> can be specified on the command-line for opening. Inkview will display all <font SIZE="-1">SVG</font> files in the given order. Folders will be expanded to a list of contained <font SIZE="-1">SVG</font> files. </p>
<p> You can also launch Inkview without any command-line arguments, which will bring up a file chooser that allows to select files and folders via a graphical user interface.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print Inkview version and build date (this is usually matches the Inkscape version).</p>
<dt><code>-f</code>, <code>&#8211;fullscreen</code></p>
<dd> Launch Inkview in fullscreen mode.</p>
<dt><code>-r</code>, <code>&#8211;recursive</code></p>
<dd> Search folders specified on the command line recursively for <font SIZE="-1">SVG</font> files. This means all <font SIZE="-1">SVG</font> files in all subfolders of the specified folder will be opened.</p>
<dt><code>-t</code>, <code>&#8211;timer=NUMBER</code></p>
<dd> Change to the next image every <font SIZE="-1">NUMBER</font> seconds</p>
<dt><code>-s</code>, <code>&#8211;scale=NUMBER</code></p>
<dd> Show image scaled by a factor of <font SIZE="-1">NUMBER</font> instead of using the file&#8217;s native size.</p>
<dt><code>-p</code>, <code>&#8211;preload</code></p>
<dd> Preloads all <font SIZE="-1">SVG</font> files. Inkview still needs to render images upon showing, however this option ensures all <font SIZE="-1">SVG</font> files are already parsed and loaded into memory. This option can also be used to verify if all files can be opened properly, without having to cycle through all files manually.</dl>
<h2>KEYBINDINGS</h2>
<dl>
<dt>&bull;</p>
<dd> Left, Page Up, or Backspace: show previous image</p>
<dt>&bull;</p>
<dd> Right, Page Down, or Space: show next image</p>
<dt>&bull;</p>
<dd> Up, or Home: go to first image</p>
<dt>&bull;</p>
<dd> Down, or End: go to last image</p>
<dt>&bull;</p>
<dd> Return: show control window</p>
<dt>&bull;</p>
<dd> F11: toggle fullscreen mode</p>
<dt>&bull;</p>
<dd> Escape or Q: quit</dl>
<h2>EXAMPLES</h2>
<p> Open two <font SIZE="-1">SVG</font> files for viewing: </p>
<pre>
    inkview file1.svg file2.svg
</pre>
<p> Open all <font SIZE="-1">SVG</font> files in the examples folder shipped with Inkscape: </p>
<pre>
    inkview B&lt;/usr/share&gt;/inkscape/examples
</pre>
<p> Launch a fullscreen slideshow that automatically changes to the next image every 5 seconds: </p>
<pre><code>
inkview-- fullscreen-- timer = 5 [files / folders...]
</code></pre>
<h2>SEE ALSO</h2>
<p> inkscape </p>
<p> &lt;<a rel="nofollow" href="http://www.inkscape.org/">http://www.inkscape.org/</a>&gt;</p>
<h2>AUTHORS</h2>
<p> See <code><a href="/docs/linux/man/1-inkscape/">inkscape</a></code>(1)</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> <code>Copyright (C)</code> 1999-2020 by Authors. </p>
<p> <code>Inkscape</code> is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GPL</font> version 3 or later. </p>
<h2>Index</h2>
