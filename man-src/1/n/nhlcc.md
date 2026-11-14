---
title: "nhlcc(1)"
name: "nhlcc"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nhlcc/"
description: "nhlcc – Command for compiling C code that uses the NCAR Graphics high-level utilities."
---

<h2>NAME</h2>
<p> nhlcc &#8211; Command for compiling C code that uses the NCAR Graphics high-level utilities.</p>
<h2>SYNOPSIS</h2>
<p> <code>nhlcc</code> [<code>-ngmath</code>] [<code>-ncarbd</code>] [<code>-ngmathbd</code>] [<code>-netcdf</code>] [<code>-hdf</code>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>nhlcc</i> is a script that invokes the C compiler/linker with the proper NCAR Graphics LLU (low-level utility) and HLU (high-level utility) libraries. Arguments presented above are associated with NCAR Graphics. All other arguments and options are identical to the cc command on your particular machine; arguments that include quoted strings may have to be enclosed in single quotes. </p>
<p> If you don&#8217;t want to use <i>nhlcc</i>, you can just type it on the command line to see what gets included in the link line, and then you can add this information to your own Makefile or script. It is important to note that you must define the macro <i>NeedFuncProto</i> in order for function prototyping to work correctly. </p>
<p> In order to run <i>nhlcc</i>, you must have your NCARG_ROOT environment variable set to the directory pathname where the NCAR Graphics libraries, binaries, and include files were installed. If you are not sure what NCARG_ROOT should be set to, please check with your system administrator or the site representative for NCAR Graphics. If the NCAR Graphics libraries, binaries, and include files were not installed under one root directory, then you will need to set the environment variables NCARG_LIB, NCARG_BIN, and NCARG_INCLUDE instead. Please see &quot;man ncargintro&quot; for more information. </p>
<p> Note that, on some systems, if you supply your own binary libraries in addition to the ones automatically referenced by <i>nhlcc</i>, all the libraries must have been created in a similar fashion. </p>
<p> <i>OPTIONS</i></p>
<dl>
<dt>-ngmath</p>
<dd> Links in the NCAR Graphics ngmath library. </p>
<dt>-ncarbd</p>
<dd> Use this option for compilers that appear to be having trouble initializing blockdata variables. It will cause a small subroutine to be linked in that helps force the loading of blockdata initialization routines. </p>
<dt>-ngmathbd</p>
<dd> Just like with the <code>-ncarbd</code> option, use this option for compilers that appear to be having trouble initializing Ngmath-related blockdata variables. It will cause a small subroutine to be linked in that helps force the loading of Ngmath blockdata initialization routines. </p>
<p> Note: this option doesn&#8217;t need to be specified separately if you are already including the <code>-ncarbd</code> and <code>-ngmath</code> options. </p>
<dt>-netcdf</p>
<dd> Links in the netCDF library. This library is not part of NCAR Graphics, so check with your system administrator if you need it installed. You can obtain a copy of it by doing an anonymous ftp to unidata.ucar.edu. </p>
<dt>-hdf</p>
<dd> Links in the HDF library. This library is not part of NCAR Graphics, so check with your system administrator if you need it installed. You can obtain a copy of it by doing an anonymous ftp to <a href="ftp://ftp.ncsa.uiuc.edu">ftp.ncsa.uiuc.edu</a>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> Online: <code>nhlf77(1NCARG),</code> <code>ncargf77(1NCARG),</code> <code>ncargcc(1NCARG),</code> <code>ncargintro(5NCARG)</code> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1987-2000<br />
 University Corporation for Atmospheric Research<br />
 The use of this Software is governed by a License Agreement. </p>
<h2>Index</h2>
