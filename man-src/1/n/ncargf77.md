---
title: "ncargf77(1)"
name: "ncargf77"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncargf77/"
description: "ncargf77 – Command for compiling Fortran code that uses the NCAR Graphics low-level utilities"
---

<h2>NAME</h2>
<p> ncargf77 &#8211; Command for compiling Fortran code that uses the NCAR Graphics low-level utilities</p>
<h2>SYNOPSIS</h2>
<p> <code>ncargf77</code> [<code>-ngmath</code>] [<code>-smooth</code>] [<code>-quick</code>] [<code>-super</code>] [<code>-agupwrtx</code>] [<code>-ncarbd</code>] [<code>-ngmathbd</code>] [<code>-ictrans</code>] [<code>-noX11</code>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>ncargf77</i> is a script that invokes the FORTRAN 77 compiler/linker with the proper NCAR Graphics LLU (low-level utility) libraries. Arguments presented above are associated with NCAR Graphics. All other arguments and options are identical to the f77 command on your particular machine; arguments that include quoted strings may have to be enclosed in single quotes. </p>
<p> NOTE: <i>ncargf77</i> cannot be used to compile NCAR Graphics Fortran programs that call the HLUs (high-level utilities). You must use <i>nhlf77</i> instead. See the <i>nhlf77</i> man page for more information. </p>
<p> In order to run <i>ncargf77</i>, you must have your NCARG_ROOT environment variable set to the directory pathname where the NCAR Graphics libraries, binaries, and include files were installed. If you are not sure what NCARG_ROOT should be set to, please check with your system administrator or the site representative for NCAR Graphics. If the NCAR Graphics libraries, binaries, and include files were not installed under one root directory, then you will need to set the environment variables NCARG_LIB, NCARG_BIN, and NCARG_INCLUDE instead. Please see &quot;man ncargintro&quot; for more information. </p>
<p> Note that, on some systems, if you supply your own binary libraries in addition to the ones automatically referenced by <i>ncargf77</i>, all the libraries must have been created in a similar fashion. </p>
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
<dd> Link in the &quot;agupwrtx&quot; library.</p>
<dt>-ictrans</p>
<dd> When <i>ncargf77</i> is invoked with the this option, the resulting executable will, upon invocation, send its metafile output to the translator <code>ictrans</code>. The environment variable GRAPHCAP must be set to a valid graphics output device whenever the executable is executed. </p>
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
<p> Online: <code>ictrans(1NCARG),</code> <code>gcaps(1NCARG),</code> <code>ncargcc(1NCARG),</code> <code>nhlcc(1NCARG),</code> <code>nhlf77(1NCARG),</code> <code>ncargintro(5NCARG)</code> </p>
<p> Hardcopy: NCAR Graphics Fundamentals, UNIX Version</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2002<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
