---
title: "pto_gen(1)"
name: "pto_gen"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pto_gen/"
description: "pto_gen – Generate a Hugin project file from a list of images."
---

<h2 class="name">NAME</h2>
<p> pto_gen &#8211; Generate a Hugin project file from a list of images. </p>
<h2>SYNOPSIS</h2>
<p> <code>pto_gen</code> [options] <i>image</i> [&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pto_gen</code> assembles a Hugin .pto project file that is suitable as input for further tools such as the <code>cpfind</code> control-point generator, or for opening with the Hugin panorama <font SIZE="-1">GUI</font> itself. Functionality is similar to <code>match-n-shift</code>.</p>
<h2>USAGE</h2>
<pre>
   pto_gen *.jpg
</pre>
<p> This creates a project file from all jpg images, in the same folder as the first photo. The project file is named first_file-last_file.pto using the same convention as the Hugin <font SIZE="-1">GUI. </font></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o|&#8211;output</code> <i>file</i></p>
<dd> Output Hugin <font SIZE="-1">PTO</font> file.</p>
<dt><code>-p|&#8211;projection</code> <i>num</i></p>
<dd> Projection type (default: 0)</p>
<dt><code>-f|&#8211;fov</code> <i>float</i></p>
<dd> Horizontal field of view of images (default: 50)</p>
<dt><code>-s|&#8211;stacklength</code> <i>num</i></p>
<dd> Number of images in stack (default: 1, no stacks)</p>
<dt><code>-l|&#8211;linkstacks</code></p>
<dd> Link image positions in stacks</p>
<dt><code>-h|&#8211;help</code></p>
<dd> shows help</dl>
<h2>AUTHORS</h2>
<p> Thomas Modes </p>
<h2>Index</h2>
