---
title: "pto2mk(1)"
name: "pto2mk"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pto2mk/"
description: "pto2mk – Generate hugin stitching Makefiles"
---

<h2 class="name">NAME</h2>
<p> pto2mk &#8211; Generate hugin stitching Makefiles </p>
<h2>SYNOPSIS</h2>
<p> <code>pto2mk</code> <code>-o</code> <i>&lt;output_makefile</i>&gt; <code>-p</code> <i>&lt;output_prefix</i>&gt; <i>project_file</i></p>
<h2>DESCRIPTION</h2>
<p> Hugin doesn&#8217;t stitch panoramas, it creates a Makefile containing all the rules to render, then blend the output image and processes this Makefile with &#8216;make&#8217;. </p>
<p> <code>pto2mk</code> will generate a platform specific Makefile from an existing hugin .pto project.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> file</p>
<dd> Output Makefile</p>
<dt><code>-p</code> output_prefix</p>
<dd> Prefix of output panorama</dl>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo and others. </p>
<h2>Index</h2>
