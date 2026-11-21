---

title: "pto2mk(1)"
name: "pto2mk"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pto2mk/"
description: "pto2mk – Generate hugin stitching Makefiles"
---

<p> <code>pto2mk</code> <code>-o</code> <i>&lt;output_makefile</i>&gt; <code>-p</code> <i>&lt;output_prefix</i>&gt; <i>project_file</i></p>
<p> Hugin doesn&#8217;t stitch panoramas, it creates a Makefile containing all the rules to render, then blend the output image and processes this Makefile with &#8216;make&#8217;. </p>
<p> <code>pto2mk</code> will generate a platform specific Makefile from an existing hugin .pto project.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> file</dt>
<dd> Output Makefile</dd>
<dt><code>-p</code> output_prefix</dt>
<dd> Prefix of output panorama</dd></dl>
<h2>AUTHORS</h2>
<p> Written by Pablo d&#8217;Angelo and others. </p>
