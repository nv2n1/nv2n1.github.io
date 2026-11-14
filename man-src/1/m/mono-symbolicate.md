---
title: "mono-symbolicate(1)"
name: "mono-symbolicate"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mono-symbolicate/"
description: "mono-symbolicate – Mono Symbolicate Tool"
---

<h2>NAME</h2>
<p> mono-symbolicate &#8211; Mono Symbolicate Tool</p>
<h2>SYNOPSIS</h2>
<p> <code>mono-symbolicate exefile stacktracesfile [directories&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> mono-symbolicate is a tool that converts a stack trace with &lt;filename unknown&gt;:0 into one with file names and line numbers. </p>
<p> The output of calling this tool will be the provided <i>stacktracesfile</i> where &lt;filename unknown&gt;:0 parts are replaced by a file name and a line number. </p>
<p> For the tool to work it needs to load referenced assemblies, it will first look in the same folder as <i>exefile</i> then from one of the provided <i>directories.</i> </p>
<p> The tool assumes that the folder with a referenced assembly called for example name.dll will also include name.dll.mdb, if the referenced assembly is AOT compiled then the tool is also expecting to find name.dll.msym.</p>
<h2>AUTHOR</h2>
<p> Written by Marcos Henrich</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2015 Xamarin.</p>
<h2>MAILING LISTS</h2>
<p> Visit <a rel="nofollow" href="http://lists.ximian.com/mailman/listinfo/mono-devel-list">http://lists.ximian.com/mailman/listinfo/mono-devel-list</a> for details.</p>
<h2>WEB SITE</h2>
<p> Visit <a rel="nofollow" href="http://www.mono-project.com">http://www.mono-project.com</a> for details </p>
<h2>Index</h2>
