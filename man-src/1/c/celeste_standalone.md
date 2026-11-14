---
title: "celeste_standalone(1)"
name: "celeste_standalone"
section: "1"
letter: "c"
url: "/docs/linux/man/1-celeste_standalone/"
description: "celeste_standalone – Cloud identification"
---

<h2 class="name">NAME</h2>
<p> celeste_standalone &#8211; Cloud identification </p>
<h2>SYNOPSIS</h2>
<p> <code>celeste_standalone</code> [options] <i>image1</i> <i>image2</i> <i>[..]</i></p>
<h2>DESCRIPTION</h2>
<p> Celeste has been trained using Support vector machine techniques to identify clouds in photos and remove control points from these areas. celeste_standalone is a command-line tool with all the same functionality as Celeste in hugin. </p>
<p> Simple usage is to just &#8216;clean&#8217; an existing project file: </p>
<pre>
 celeste_standalone -i project.pto -o project.pto
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code> &lt;filename&gt;</p>
<dd> Input Hugin <font SIZE="-1">PTO</font> file. Control points over <font SIZE="-1">SVM</font> threshold will be removed before being written to the output file. If -m is set to 1, images in the file will be also be masked.</p>
<dt><code>-o</code> &lt;filename&gt;</p>
<dd> Output Hugin <font SIZE="-1">PTO</font> file. Default: &#8216;&lt;filename&gt;_celeste.pto&#8217;</p>
<dt><code>-d</code> &lt;filename&gt;</p>
<dd> <font SIZE="-1">SVM</font> model file. Default: &#8216;data/celeste.model&#8217;</p>
<dt><code>-s</code> &lt;int&gt;</p>
<dd> Maximum dimension for re-sized image prior to processing. A higher value will increase the resolution of the mask but is significantly slower. Default: 800</p>
<dt><code>-t</code> &lt;float&gt;</p>
<dd> <font SIZE="-1">SVM</font> threshold. Raise this value to remove fewer control points, lower it to remove more. Range 0 to 1. Default: 0.5</p>
<dt><code>-m</code> &lt;1|0&gt;</p>
<dd> Create masks when processing Hugin <font SIZE="-1">PTO</font> file. Default: 0</p>
<dt><code>-f</code> &lt;string&gt;</p>
<dd> Mask file format. Options are <font SIZE="-1">PNG, JPEG, BMP, GIF</font> and <font SIZE="-1">TIFF. </font> Default: <font SIZE="-1">PNG</font></p>
<dt><code>-r</code> &lt;1|0&gt;</p>
<dd> Filter radius. 0 = large (more accurate), 1 = small (higher resolution mask, slower, less accurate). Default: 0</p>
<dt><code>-h</code></p>
<dd> Print usage.</dl>
<h2>AUTHORS</h2>
<p> Written by Tim Nugent. </p>
<h2>Index</h2>
