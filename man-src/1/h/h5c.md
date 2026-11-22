---
title: "h5c(1)"
name: "h5c"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5c/"
description: "h5c++ – Helper script to compile HDF5 C++ applications."
---

<p>h5c++ &#8211; Helper script to compile HDF5 C++ applications.</p>
<h2>Synopsis</h2>
<p>h5c++ [OPTIONS] &lt;compile line&gt;</p>
<h2>Description</h2>
<p>h5c++ can be used in much the same way MPIch is used to compile an HDF5 program. It takes care of specifying where the HDF5 header files and libraries are on the command line. </p>
<p> h5c++ supercedes all other compiler scripts in that if you&#8217;ve used one set of compiler scripts to compile the HDF5 C++ library, then h5c++ uses those same scripts. For example, when compiling an MPIch program, you use the mpiCC script. </p>
<p> Some programs use HDF5 in only a few modules. It isn&#8217;t necessary to use h5c++ to compile those modules which don&#8217;t use HDF5. In fact, since h5c++ is only a convenience script, you are still able to compile HDF5 C++ modules in the normal way. In that case, you will have to specify the HDF5 libraries and include paths yourself. </p>
<p> An example of how to use h5c++ to compile the program hdf_prog, which consists of modules prog1.cpp and prog2.cpp and uses the HDF5 C++ library, would be as follows:<br/>
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>h5c++&nbsp;<wbr>-c prog1.cpp<br/>
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>h5c++&nbsp;<wbr>-c prog2.cpp<br/>
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>h5c++&nbsp;<wbr>-o hdf_prog prog1.o prog2.o</p>
<dl>
<dt><code>-help</code></dt>
<dd>Prints a help message.</dd>
<dt><code>-echo</code></dt>
<dd>Show all the shell commands executed.</dd>
<dt><code>-prefix=DIR</code></dt>
<dd>Use the directory DIR to find the HDF5 lib/ and include/ subdirectories. Default: prefix specified when configuring HDF5.</dd>
<dt><code>-show</code></dt>
<dd>Show the commands without executing them.</dd>
<dt>&lt;compile line&gt;</dt>
<dd>The normal compile line options for your compiler. h5c++ uses the same compiler you used to compile HDF5. Check your compiler&#8217;s manual for more information on which options are needed.</dd></dl>
<h2>Environment</h2>
<dl>
<dt><code>HDF5_CXX</code></dt>
<dd>Use a different C++ compiler.</dd>
<dt><code>HDF5_CXXLINKER</code></dt>
<dd>Use a different linker.</dd></dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-h5cc/">h5cc</a></i>(1), <i><a href="/docs/linux/man/1-h5fc/">h5fc</a></i>(1)</p>
