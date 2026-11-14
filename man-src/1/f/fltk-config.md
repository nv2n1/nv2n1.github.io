---
title: "fltk-config(1)"
name: "fltk-config"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fltk-config/"
---

<h2>NAME</h2>

 fltk-config - script to get information about the installed version of fltk. 

<h2>SYNOPSIS</h2>

 fltk-config [ --prefix <i>[=DIR]</i> ] [ --exec-prefix <i>[=DIR]</i> ] [ --version ] [ --api-version ] [ --use-gl ] [ --use-images ] [ --use-glut ] [ --cc ] [ --cxx ] [ --cflags ] [ --cxxflags ] [ --ldflags ] [ --ldstaticflags ] [ --libs ] [ -D<i>name[=value]</i> ] [ -g ] [ --compile <i>program.cxx</i> ]

<h2>DESCRIPTION</h2>

 <i>fltk-config</i> is a utility script that can be used to get information about the current version of FLTK that is installed on the system, what compiler and linker options to use when building FLTK-based applications, and to build simple FLTK applications. 

 The following options are supported:
<dl>
<dt>--api-version
<dd> 
 Displays the current FLTK API version number, e.g. &quot;1.1&quot;.
<dt>--cc
<dd>
<dt>--cxx
<dd> 
 Displays the C/C++ compiler that was used to compile FLTK.
<dt>--cflags
<dd>
<dt>--cxxflags
<dd> 
 Displays the C/C++ compiler options to use when compiling source files that use FLTK.
<dt>--compile <i>program.cxx</i>
<dd> 
 Compiles the source file <i>program.cxx</i> into <i>program</i>. This option implies &quot;--post <i>program</i>&quot;.
<dt>-g
<dd> 
 Enables debugging information when compiling with the <i>--compile</i> option.
<dt>--ldflags
<dd> 
 Displays the linker options to use when linking a FLTK application.
<dt>--ldstaticflags
<dd> 
 Displays the linker options to use when linking a FLTK application to the static FLTK libraries.
<dt>--libs
<dd> 
 Displays the full path to the FLTK library files, to be used for dependency checking.
<dt>--use-gl
<dd> 
 Enables OpenGL support.
<dt>--use-glut
<dd> 
 Enables GLUT support.
<dt>--use-images
<dd> 
 Enables image file support.
<dt>--version
<dd> 
 Displays the current FLTK version number, e.g. &quot;1.1.0&quot;.</dl>

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-fluid/">fluid</a>(1), <a HREF="/docs/linux/man/3-fltk/">fltk</a>(3) 
 FLTK Programming Manual 
 FLTK Web Site, <a rel="nofollow" HREF="http://www.fltk.org/">http://www.fltk.org/</a>

<h2>AUTHORS</h2>

 Bill Spitzak and others. 

<h2>Index</h2>


