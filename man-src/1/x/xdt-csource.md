---
title: "xdt-csource(1)"
name: "xdt-csource"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdt-csource/"
---

<h2 class="name">NAME</h2>
 

 xdt-csource - C code generation utility for arbitrary data 

<h2>SYNOPSIS</h2>

 

 <b>xdt-csource</b> [<i>options</i>] [<i>file</i>] 

 <b>xdt-csource</b> [<i>options</i>] <b>--build-list</b> [[<i>name file</i>]...]

<h2>DESCRIPTION</h2>

 

 <b>xdt-csource</b> is a small utility that generates C code containing arbitrary data, useful for compiling texts or other data directly into programs.

<h2>INVOCATION</h2>

 

 <b>xdt-csource</b> either takes as input one file name to generate code for, or, using the <b>--build-list</b> option, a list of (<i>name</i>, <i>file</i>) pairs to generate code for a list of images into named variables.
<dl>
<dt><b>-h</b>, <b>--help</b>
<dd> Print this help message and exit
<dt><b>-V</b>, <b>--version</b>
<dd> Print version information and exit
<dt><b>--extern</b>
<dd> Generate extern symbols
<dt><b>--static</b>
<dd> Generate static symbols
<dt><b>--name</b>=<i>identifier</i>
<dd> C macro/variable name
<dt><b>--build-list</b>
<dd> Parse (name, file) pairs
<dt><b>--strip-comments</b>
<dd> Remove comments from XML files
<dt><b>--strip-content</b>
<dd> Remove node contents from XML files</dl>

<h2>COPYRIGHT</h2>

 Copyright &#169; 2005-2011
<dl>
<dt>
<dd> The Xfce development team. All rights reserved.</dl>
 

 Please report bugs to &lt;<a rel="nofollow" HREF="http://bugzilla.xfce.org/enter_bug.cgi?product=Xfce4-dev-tools">http://bugzilla.xfce.org/enter_bug.cgi?product=Xfce4-dev-tools</a>&gt;. 

<h2>Index</h2>


