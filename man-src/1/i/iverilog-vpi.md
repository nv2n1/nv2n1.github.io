---
title: "iverilog-vpi(1)"
name: "iverilog-vpi"
section: "1"
letter: "i"
url: "/docs/linux/man/1-iverilog-vpi/"
description: "iverilog-vpi – Compile front end for VPI modules"
---

<h2>NAME</h2>
<p> iverilog-vpi &#8211; Compile front end for VPI modules </p>
<h2>SYNOPSIS</h2>
<p> <code>iverilog-vpi</code> [&#8211;name=<i>name</i>] <i>sourcefile</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <i>iverilog-vpi</i> is a tool to simplify the compilation of VPI modules for use with Icarus Verilog. It takes on the command line a list of C or C++ source files, and generates as output a linked VPI module. See the <code><a href="/docs/linux/man/1-vvp/">vvp</a></code>(1) man page for a description of how the linked module is loaded by a simulation. </p>
<p> The output is named after the first source file. For example, if the first source file is named <i>foo.c</i>, the output becomes <i>foo.vpi</i>. </p>
<h2>OPTIONS</h2>
<p> <i>iverilog-vpi</i> accepts the following options:</p>
<dl>
<dt><code>-l</code><i>library</i></p>
<dd> Include the named library in the link of the VPI module. This allows VPI modules to further reference external libraries. </p>
<dt><code>-I</code><i>directory</i></p>
<dd> Add <i>directory</i> to the list of directories that will be search for header files. </p>
<dt><code>-D</code><i>define</i></p>
<dd> Define a macro named <i>define</i>. </p>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> Normally, the output VPI module will be named after the first source file passed to the command. This flag sets the name (without the .vpi suffix) of the output vpi module. </p>
<dt><code>&#8211;install-dir</code></p>
<dd> This flag causes the program to print the install directory for VPI modules, then exit. It is a convenience for makefiles or automated plug-in installers. </p>
<dt><code>&#8211;cflags, &#8211;ldflags and -ldlibs</code></p>
<dd> These flags provide compile time information. </p>
</dl>
<h2>PC-ONLY OPTIONS</h2>
<p> The PC port of <i>iverilog-vpi</i> includes two special flags needed to support the more intractable development environment. These flags help the program locate parts that it needs. </p>
<dl>
<dt><code>-mingw=</code><i>path</i></p>
<dd> Tell the program the root of the Mingw compiler tool suite. The <code>vvp</code> runtime is compiled with this compiler, and this is the compiler that <i>iverilog-vpi</i> expects to use to compile your source code. This is normally not needed, and if you do use it, it is only needed once. The compiler will save the <i>path</i> in the registry for use later. </p>
<dt><code>-ivl=</code><i>path</i></p>
<dd> Set for the use during compilation the root if the Icarus Verilog install. This is the place where you installed Icarus Verilog when you ran the installer. This flag is also only needed once, and the path is stored in the registry for future use. </p>
</dl>
<h2>UNIX-ONLY OPTIONS</h2>
<p> The UNIX version of <i>iverilog-vpi</i> includes additional flags to let Makefile gurus peek at the configuration of the <i>iverilog</i> installation. This way, Makefiles can be written that handle complex VPI builds natively, and without hard-coding values that depend on the system and installation. If used at all, these options must be used one at a time, and without any other options or directives. </p>
<dl>
<dt><code>&#8211;cflags</code></p>
<dd> Print the compiler flags (CFLAGS or CXXFLAGS) needed to compile source code destined for a VPI module. </p>
<dt><code>&#8211;ldflags</code></p>
<dd> Print the linker flags (LDFLAGS) needed to link a VPI module. </p>
<dt><code>&#8211;ldlibs</code></p>
<dd> Print the libraries (LDLIBS) needed to link a VPI module. </p>
<dt><code>-m32</code></p>
<dd> On 64bit systems that support it (and support vvp32) this flag requests a 32bit vpi binary instead of the default 64bit binary. </p>
<p> Example GNU makefile that takes advantage of these flags:</p>
<dt>
<dd> CFLAGS = -Wall -O $(CFLAGS_$@)<br />
 VPI_CFLAGS := $(shell iverilog-vpi &#8211;cflags)<br />
 CFLAGS_messagev.o = $(VPI_CFLAGS)<br />
 CFLAGS_fifo.o = $(VPI_CFLAGS)<br />
 messagev.o fifo.o: transport.h<br />
 messagev.vpi: messagev.o fifo.o<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>iverilog-vpi $^</p>
</dl>
<h2>AUTHOR</h2>
<pre>
Steve Williams (steve [at] icarus.com)
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-iverilog/">iverilog</a>(1), <a href="/docs/linux/man/1-vvp/">vvp</a>(1), <code>&lt;<a rel="nofollow" href="http://www.icarus.com/eda/verilog/">http://www.icarus.com/eda/verilog/</a>&gt;,</code> <code>&lt;<a rel="nofollow" href="http://www.mingw.org">http://www.mingw.org</a>&gt;,</code> </p>
<h2>COPYRIGHT</h2>
<pre>
Copyright &#169;  2002-2009 Stephen Williams
This document can be freely redistributed according to the terms of the
GNU General Public License version 2.0
</pre>
<h2>Index</h2>
