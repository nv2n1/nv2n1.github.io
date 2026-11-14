---
title: "icc2ps(1)"
name: "icc2ps"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icc2ps/"
description: "icc2ps – little cms PostScript converter."
---

<h2>NAME</h2>
<p> icc2ps &#8211; little cms PostScript converter.</p>
<h2>SYNOPSIS</h2>
<p> <code>icc2ps</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> lcms is a standalone CMM engine, which deals with the color management. It implements a fast transformation between ICC profiles. <code>icc2ps </code> is little cms PostScript converter.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b </code></p>
<dd> Black point compensation (CRD only).</p>
<dt><code>-i&nbsp;<wbr></code><i>profile</i></p>
<dd> Input profile: Generates Color Space Array (CSA).</p>
<dt><code>-o&nbsp;<wbr></code><i>profile</i></p>
<dd> Output profile: Generates Color Rendering Dictionary(CRD).</p>
<dt><code>-t &lt;0,1,2,3&gt;</code></p>
<dd> Intent (0=Perceptual, 1=Colorimetric, 2=Saturation, 3=Absolute).</p>
<dt><code>-u </code></p>
<dd> Do NOT generate resource name on CRD.</dl>
<h2>NOTES</h2>
<p> For suggestions, comments, bug reports etc. send mail to info [at] littlecms.com.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-jpegicc/">jpegicc</a></code>(1), <code><a href="/docs/linux/man/1-tifficc/">tifficc</a></code>(1), <code><a href="/docs/linux/man/1-icclink/">icclink</a></code>(1), <code><a href="/docs/linux/man/1-icctrans/">icctrans</a></code>(1), <code><a href="/docs/linux/man/1-wtpt/">wtpt</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Shiju p. Nair &lt;shiju.p [at] gmail.com&gt;, for the Debian project. </p>
<h2>Index</h2>
