---

title: "pano_modify(1)"
name: "pano_modify"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pano_modify/"
description: "pano_modify – Change output parameters of project file"
---

<p> pano_modify &#8211; Change output parameters of project file </p>
<h2>SYNOPSIS</h2>
<p> <code>pano_modify</code> [options] <i>input.pto</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pano_modify</code> modifies a single Hugin .pto project.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code>, <code>&#8211;output=file.pto</code></dt>
<dd> Output Hugin PTO file. Default: &lt;filename&gt;_mod.pto</dd>
<dt><code>-p</code>, <code>&#8211;projection=NUMBER</code></dt>
<dd> Sets the output projection to number x</dd>
<dt><code>&#8211;fov=AUTO|HFOV|HFOVxVFOV</code></dt>
<dd> Sets field of view. </dd>
<p> AUTO: calculates optimal fov </p>
<p> HFOV|HFOVxVFOV: set to given fov</p>
<dt><code>-s</code>, <code>&#8211;straighten</code></dt>
<dd> Straightens the panorama</dd>
<dt><code>-c</code>, <code>&#8211;center</code></dt>
<dd> Centers the panorama</dd>
<dt><code>&#8211;canvas=AUTO|WIDTHxHEIGHT</code></dt>
<dd> Sets the output canvas size </dd>
<p> AUTO: calculate optimal canvas size </p>
<p> WIDTHxHEIGHT: set to given size</p>
<dt><code>&#8211;crop=AUTO|left,right,top,bottom</code></dt>
<dd> Sets the crop rectangle </dd>
<p> AUTO: autocrop panorama </p>
<p> left,right,top,bottom: to given size</p>
<dt><code>&#8211;rotate=yaw,pitch,roll</code></dt>
<dd> Rotates the whole panorama with the given angles</dd>
<dt><code>&#8211;translate=x,y,z</code></dt>
<dd> Translates the whole panorama with the given values</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Shows help</dd></dl>
<h2>AUTHORS</h2>
<p> Thomas Modes </p>
