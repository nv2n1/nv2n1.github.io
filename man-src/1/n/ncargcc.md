---
title: "ncargcc(1)"
name: "ncargcc"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncargcc/"
description: "ncargcc – Command for compiling C code that uses the NCAR Graphics low-level utilities"
---

<h2>NAME</h2>
<p> ncargcc &#8211; Command for compiling C code that uses the NCAR Graphics low-level utilities</p>
<h2>SYNOPSIS</h2>
<p> <code>ncargcc</code> [<code>-ngmath</code>] [<code>-smooth</code>] [<code>-quick</code>] [<code>-super</code>] [<code>-agupwrtx</code>] [<code>-ncarbd</code>] &#8230; [<code>-ngmathbd</code>] &#8230; [<code>-noX11</code>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>ncargcc</i> is a script that invokes the C compiler/linker with the proper NCAR Graphics LLU (low-level utility) libraries. Arguments presented above are associated with NCAR Graphics. All other arguments and options are identical to the cc command on your particular machine; arguments that include quoted strings may have to be enclosed in single quotes. </p>
<p> NOTE: <i>ncargcc</i> cannot be used to compile NCAR Graphics C programs that call the HLUs (high-level utilities). You must use <i>nhlcc</i> instead. See the <i>nhlcc</i> man page for more information. </p>
<p> If you don&#8217;t want to use <i>ncargcc</i>, you can just type it on the command line to see what gets included in the link line, and then you can add this information to your own Makefile or script. It is important to note that you must define the macro <i>NeedFuncProto</i> in order for function prototyping to work correctly. </p>
<p> In order to run <i>ncargcc</i>, you must have your NCARG_ROOT environment variable set to the directory pathname where the NCAR Graphics libraries, binaries, and include files were installed. If you are not sure what NCARG_ROOT should be set to, please check with your system administrator or the site representative for NCAR Graphics. If the NCAR Graphics libraries, binaries, and include files were not installed under one root directory, then you will need to set the environment variables NCARG_LIB, NCARG_BIN, and NCARG_INCLUDE instead. Please see &quot;man ncargintro&quot; for more information. </p>
<p> When <code>ncargcc</code> is invoked with the <code>-ictrans</code> option the resulting executable will, upon invocation, send its metafile output to the translator <code>ictrans</code>. The environment variable GRAPHCAP must be set to a valid graphics output device whenever the executable is executed. </p>
<p> By default, <i>ncargcc</i> will load the X11 library when linking your C program. If you try running <i>ncargcc</i> and the compiler complains that it cannot find the library for X11, then try running <i>ncargcc -L/xxx/yyy/zzz program.c</i> where <i>/xxx/yyy/zzz</i> is the path leading to your X11 library. If you do not have the X11 library, or else you just don&#8217;t want to link it in, you can use the <code>-noX11</code> option. </p>
<p> <i>OPTIONS</i></p>
<dl>
<dt>-ngmath</p>
<dd> Links in the NCAR Graphics ngmath library. </p>
<dt>-smooth</p>
<dd> Link in the &quot;smooth&quot; objects. </p>
<dt>-quick</p>
<dd> Link in the &quot;quick&quot; objects. </p>
<dt>-super</p>
<dd> Link in the &quot;super&quot; objects. </p>
<dt>-agupwrtx</p>
<dd> Link in the &quot;agupwrtx&quot; library. </p>
<dt>-ncarbd</p>
<dd> Use this option for compilers that appear to be having trouble initializing blockdata variables. It will cause a small subroutine to be linked in that helps force the loading of blockdata initialization routines. </p>
<dt>-ngmathbd</p>
<dd> Just like with the <code>-ncarbd</code> option, use this option for compilers that appear to be having trouble initializing Ngmath-related blockdata variables. It will cause a small subroutine to be linked in that helps force the loading of Ngmath blockdata initialization routines. </p>
<p> Note: this option doesn&#8217;t need to be specified separately if you are already including the <code>-ncarbd</code> and <code>-ngmath</code> options. </p>
<dt>-noX11</p>
<dd> Do not link in the X library when linking the code. </p>
<p> By default, <i>ncargf77</i> will load the X11 library when linking your Fortran program. This is because the GKS library now has an X11 driver. If you try running <i>ncargf77</i> and the compiler complains that it cannot find the library for X11, then try running <i>ncargf77 -L/xxx/yyy/zzz program.f</i> where <i>/xxx/yyy/zzz</i> is the path leading to your X11 library. If you do not have the X11 library, or else you just don&#8217;t want it to be loaded, you can use the <code>-noX11</code> option. </p>
</dl>
<h2>SEE ALSO</h2>
<p> Online: ictrans(1NCARG), <code>gcaps(1NCARG),</code> <code>ncargf77(1NCARG),</code> <code>nhlcc(1NCARG),</code> <code>nhlf77(1NCARG),</code> <code>ncargintro(5NCARG)</code> </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2002<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
