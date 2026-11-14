---
title: "pano_modify(1)"
name: "pano_modify"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pano_modify/"
description: "pano_modify – Change output parameters of project file"
---

<h2 class="name">NAME</h2>
<p> pano_modify &#8211; Change output parameters of project file </p>
<h2>SYNOPSIS</h2>
<p> <code>pano_modify</code> [options] <i>input.pto</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pano_modify</code> modifies a single Hugin .pto project.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code>, <code>&#8211;output=file.pto</code></p>
<dd> Output Hugin <font SIZE="-1">PTO</font> file. Default: &lt;filename&gt;_mod.pto</p>
<dt><code>-p</code>, <code>&#8211;projection=NUMBER</code></p>
<dd> Sets the output projection to number x</p>
<dt><code>&#8211;fov=AUTO|HFOV|HFOVxVFOV</code></p>
<dd> Sets field of view. </p>
<p> <font SIZE="-1">AUTO:</font> calculates optimal fov </p>
<p> HFOV|HFOVxVFOV: set to given fov</p>
<dt><code>-s</code>, <code>&#8211;straighten</code></p>
<dd> Straightens the panorama</p>
<dt><code>-c</code>, <code>&#8211;center</code></p>
<dd> Centers the panorama</p>
<dt><code>&#8211;canvas=AUTO|WIDTHxHEIGHT</code></p>
<dd> Sets the output canvas size </p>
<p> <font SIZE="-1">AUTO:</font> calculate optimal canvas size </p>
<p> WIDTHxHEIGHT: set to given size</p>
<dt><code>&#8211;crop=AUTO|left,right,top,bottom</code></p>
<dd> Sets the crop rectangle </p>
<p> <font SIZE="-1">AUTO:</font> autocrop panorama </p>
<p> left,right,top,bottom: to given size</p>
<dt><code>&#8211;rotate=yaw,pitch,roll</code></p>
<dd> Rotates the whole panorama with the given angles</p>
<dt><code>&#8211;translate=x,y,z</code></p>
<dd> Translates the whole panorama with the given values</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Shows help</dl>
<h2>AUTHORS</h2>
<p> Thomas Modes </p>
<h2>Index</h2>
