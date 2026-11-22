---

title: "inkview(1)"
name: "inkview"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inkview/"
description: "Inkview – an SVG viewer and slideshow program."
---

<p> Inkview &#8211; an SVG viewer and slideshow program. </p>
<h2>SYNOPSIS</h2>
<p> <tt>&quot;inkview [options] [filename ...]&quot;</tt> </p>
<p> options: </p>
<pre><code>
- h, --help - V, --version - f, --fullscreen - r, --recursive - t, --timer = NUMBER - s, --scale = NUMBER - p, --preload
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>Inkview</code> is an <code>Scalable Vector Graphics (</code><code>SVG</code><code>)</code> viewer that can also be used for slideshows or presentations. One or more <code>FILES</code> or <code>FOLDERS</code> can be specified on the command-line for opening. Inkview will display all SVG files in the given order. Folders will be expanded to a list of contained SVG files. </p>
<p> You can also launch Inkview without any command-line arguments, which will bring up a file chooser that allows to select files and folders via a graphical user interface.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print Inkview version and build date (this is usually matches the Inkscape version).</dd>
<dt><code>-f</code>, <code>&#8211;fullscreen</code></dt>
<dd> Launch Inkview in fullscreen mode.</dd>
<dt><code>-r</code>, <code>&#8211;recursive</code></dt>
<dd> Search folders specified on the command line recursively for SVG files. This means all SVG files in all subfolders of the specified folder will be opened.</dd>
<dt><code>-t</code>, <code>&#8211;timer=NUMBER</code></dt>
<dd> Change to the next image every NUMBER seconds</dd>
<dt><code>-s</code>, <code>&#8211;scale=NUMBER</code></dt>
<dd> Show image scaled by a factor of NUMBER instead of using the file&#8217;s native size.</dd>
<dt><code>-p</code>, <code>&#8211;preload</code></dt>
<dd> Preloads all SVG files. Inkview still needs to render images upon showing, however this option ensures all SVG files are already parsed and loaded into memory. This option can also be used to verify if all files can be opened properly, without having to cycle through all files manually.</dd></dl>
<h2>KEYBINDINGS</h2>
<dl>
<dt>&bull;</dt>
<dd> Left, Page Up, or Backspace: show previous image</dd>
<dt>&bull;</dt>
<dd> Right, Page Down, or Space: show next image</dd>
<dt>&bull;</dt>
<dd> Up, or Home: go to first image</dd>
<dt>&bull;</dt>
<dd> Down, or End: go to last image</dd>
<dt>&bull;</dt>
<dd> Return: show control window</dd>
<dt>&bull;</dt>
<dd> F11: toggle fullscreen mode</dd>
<dt>&bull;</dt>
<dd> Escape or Q: quit</dd></dl>
<h2>EXAMPLES</h2>
<p> Open two SVG files for viewing: </p>
<pre>
    inkview file1.svg file2.svg
</pre>
<p> Open all SVG files in the examples folder shipped with Inkscape: </p>
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
<p> <code>Inkscape</code> is free software; you can redistribute it and/or modify it under the terms of the GPL version 3 or later. </p>
