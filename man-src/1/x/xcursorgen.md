---
title: "xcursorgen(1)"
name: "xcursorgen"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xcursorgen/"
description: "xcursorgen – create an X cursor file from a collection of PNG images"
---

<h2 class="name">NAME</h2>
<p> xcursorgen &#8211; create an X cursor file from a collection of PNG images </p>
<h2>SYNOPSIS</h2>
<p> <code>xcursorgen</code> [ <code>-V</code> ] [ <code>&#8211;version</code> ] [ <code>-?</code> ] [ <code>&#8211;help</code> ] [ <code>-p</code> <i>dir</i> ] [ <code>&#8211;prefix</code> <i>dir</i> ] [ <i>config-file</i> [ <i>output-file</i> ] ]</p>
<h2>DESCRIPTION</h2>
<p> Xcursorgen reads the <i>config-file</i> to find the list of cursor images along with their hotspot and nominal size information. Xcursorgen converts all of the images to Xcursor format and writes them to the <i>output-file</i>. </p>
<p> Each line in the config file is of the form:<br />
 &lt;size&gt; &lt;xhot&gt; &lt;yhot&gt; &lt;filename&gt; &lt;ms-delay&gt; </p>
<p> Multiple images with the same &lt;size&gt; are used to create animated cursors, the &lt;ms-delay&gt; value on each line indicates how long each image should be displayed before switching to the next. &lt;ms-delay&gt; can be elided for static cursors. </p>
<p> If <i>config-file</i> is not specified, or is specified as &quot;-&quot;, standard input is used for the configuration file. If <i>output-file</i> is not specified, or is specified as &quot;-&quot;, standard output is used for the output file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display the version number and exit.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Display the usage message and exit.</p>
<dt><code>-p </code><i>dir</i>, <code>&#8211;prefix </code><i>dir</i></p>
<dd> Find cursor images in the directory specified by <i>dir</i>. If not specified, the current directory is used.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-xcursor/">Xcursor</a>(3) </p>
<h2>Index</h2>
