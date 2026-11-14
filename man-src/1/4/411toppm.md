---
title: "411toppm(1)"
name: "411toppm"
section: "1"
letter: "4"
url: "/docs/linux/man/1-411toppm/"
description: "411toppm – convert Sony Mavica .411 image to ppm"
---

<h2 class="name">NAME</h2>
<p> 411toppm &#8211; convert Sony Mavica .411 image to ppm </p>
<h2>SYNOPSIS</h2>
<p> <code>411toppm</code> [<code>-width </code><i>width</i>] [<code>-height </code><i>height</i>] [<i>411file</i>] </p>
<p> All options may be abbreviated to the shortest unique prefix. </p>
<h2>DESCRIPTION</h2>
<p> Reads a .411 file, such as from a Sony Mavic camera, and converts it to a PPM image as output. </p>
<p> Output is to Standard Output. </p>
<p> The originator of this program and decipherer of the .411 format, Steve Allen &lt;sla [at] alumni.caltech.edu&gt;, has this to say about the utility of this program: &quot;There&#8217;s so little image in a 64&#215;48 thumbnail (especially when you have the full size JPG file) that the only point in doing this was to answer the implicit challenge posed by the manual stating that only the camera can use these files.&quot; </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-width</code></p>
<dd> The width (number of columns) of the input image. Default is 64.</p>
<dt><code>-height</code></p>
<dd> The height (number of rows) of the input image. Default is 48. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-ppm/">ppm</a></code>(5) </p>
<h2>Index</h2>
