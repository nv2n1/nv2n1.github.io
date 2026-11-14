---
title: "prj2make(1)"
name: "prj2make"
section: "1"
letter: "p"
url: "/docs/linux/man/1-prj2make/"
description: "prj2make – Makefile generator from Visual Studio and Sharp Develop solution files."
---

<h2>NAME</h2>
<p> prj2make &#8211; Makefile generator from Visual Studio and Sharp Develop solution files.</p>
<h2>SYNOPSIS</h2>
<p> <code>prj2make options file</code></p>
<h2>DESCRIPTIOn</h2>
<p> The <i>prj2make</i> tool will produce Makefiles or NMakefiles from Visual Studio solution files (files ending in .sln or .csproj) or SharpDevelop combine files (files ending in .cmbx or .prjx). </p>
<p> This tool is commonly used to compile on Unix source code which has been originally developed with Visual Studio or SharpDevelop. </p>
<p> This tool can also be used to convert Visual Studio project files (.sln or .csproj) into Sharp Develop .prjx/.cmbx files, use the `-csproj2prjx&#8217; for this. </p>
<p> By default <i>prj2make</i> will produce Makefiles suitable to be consumed by Unix Make. If your application needs to target nmake, you can use the option `-isNmake&#8217;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-c, -isCsc</i></p>
<dd> Use csc instead of mcs on the generated files.</p>
<dt><i>-csproj2prjx</i></p>
<dd> Runs in conversion mode, and turns a csproj/sln into a set of prjx/cmbx files.</p>
<dt><i>-n, -isNmake</i></p>
<dd> Produce makefiles suitable to be used by Nmake.</dl>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-list">http://lists.ximian.com/mailman/listinfo/mono-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit: <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mcs/">mcs</a>(1),</code><a href="/docs/linux/man/1-mono/">mono</a>(1),<code><a href="/docs/linux/man/1-make/">make</a>(1),</code><a href="/docs/linux/man/5-mono-config/">mono-config</a>(5) </p>
<h2>Index</h2>
