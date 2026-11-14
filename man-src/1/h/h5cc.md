---
title: "h5cc(1)"
name: "h5cc"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5cc/"
description: "h5cc – Helper script to compile HDF5 applications."
---

<h2>NAME</h2>
<p> h5cc &#8211; Helper script to compile HDF5 applications.</p>
<h2>SYNOPSIS</h2>
<p> h5cc [OPTIONS] &lt;compile line&gt;</p>
<h2>DESCRIPTION</h2>
<p> h5cc can be used in much the same way MPIch is used to compile an HDF5 program. It takes care of specifying where the HDF5 header files and libraries are on the command line. </p>
<p> h5cc supercedes all other compiler scripts in that if you&#8217;ve used them to compile the HDF5 library, then h5cc also uses those scripts. For example, when compiling an MPIch program, you use the mpicc script. If you&#8217;ve built HDF5 using MPIch, then h5cc uses the MPIch program for compilation. </p>
<p> Some programs use HDF5 in only a few modules. It isn&#8217;t necessary to use h5cc to compile those modules which don&#8217;t use HDF5. In fact, since h5cc is only a convenience script, you are still able to compile HDF5 modules in the normal way. In that case, you will have to specify the HDF5 libraries and include paths yourself. </p>
<p> An example of how to use h5cc to compile the program hdf_prog, which consists of modules prog1.c and prog2.c and uses the HDF5 shared library, would be as follows:</p>
<dl>
<dt>
<dd> # h5cc -c prog1.c # h5cc -c prog2.c # h5cc -shlib -o hdf_prog prog1.o prog2.o</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Prints a help message.</p>
<dt><code>-echo</code></p>
<dd> Show all the shell commands executed.</p>
<dt><code>-prefix=DIR</code></p>
<dd> Use the directory DIR to find the HDF5 lib/ and include/ subdirectories. Default: prefix specified when configuring HDF5.</p>
<dt><code>-show</code></p>
<dd> Show the commands without executing them.</p>
<dt><code>-shlib</code></p>
<dd> Compile using shared HDF5 libraries.</p>
<dt><code>-noshlib</code></p>
<dd> Compile using static HDF5 libraries [default].</p>
<dt>&lt;compile line&gt;</p>
<dd> The normal compile line options for your compiler. h5cc uses the same compiler you used to compile HDF5. Check your compiler&#8217;s manual for more information on which options are needed.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HDF5_CC</code></p>
<dd> Use a different C compiler.</p>
<dt><code>HDF5_CLINKER</code></p>
<dd> Use a different linker.</p>
<dt><code>HDF5_USE_SHLIB=[yes|no]</code></p>
<dd> Use shared version of the HDF5 library [default: no].</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-h5fc/">h5fc</a></i>(1), <i>h5c++</i>(1) </p>
<h2>Index</h2>
