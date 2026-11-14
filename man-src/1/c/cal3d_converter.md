---
title: "cal3d_converter(1)"
name: "cal3d_converter"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cal3d_converter/"
description: "cal3d_converter – convert cal3d files from / to binary and XML (version 0.11.0)"
---

<h2>NAME</h2>
<p> cal3d_converter &#8211; convert cal3d files from / to binary and XML (version 0.11.0) </p>
<h2>SYNOPSIS</h2>
<p> cal3d_converter source destination </p>
<h2>DESCRIPTION</h2>
<p> A source or destination cal3d file is either a skeleton (.xsf or .csf), a mesh (.xmf or .cmf), an animation (.xaf or .caf) or a material (.xrf or .crf). The files with an extension starting with an <code>x</code> denote XML files (.xsf, .xmf, .xaf, xrf) and the files with an extension starting with a <code>c</code> denot binary files (.csf, .cmf, .caf, .crf). </p>
<p> If the <i>source</i> is a file of a given type, the <i>destination </i> is expected to be a file of the same type. </p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>cal3d_converter skeleton.csf skeleton.xsf</code></p>
<dd> Convert the skeleton.csf skeleton file from binary format to XML format. </p>
</dl>
<h2>AUTHORS</h2>
<p> Loic Dachary &lt;loic [at] gnu.org&gt; </p>
<h2>Index</h2>
