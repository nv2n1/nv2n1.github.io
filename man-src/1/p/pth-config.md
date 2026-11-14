---
title: "pth-config(1)"
name: "pth-config"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pth-config/"
description: "pth-config – Pth library build utility"
---

<h2>NAME</h2>
<p> <code>pth-config</code> &#8211; Pth library build utility</p>
<h2>VERSION</h2>
<p> <font SIZE="-1">GNU</font> Pth <font SIZE="-1">2.0.7 (08-Jun-2006)</font></p>
<h2>SYNOPSIS</h2>
<p> <code>pth-config</code> [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<code>&#8211;all</code>] [<code>&#8211;prefix</code>] [<code>&#8211;exec-prefix</code>] [<code>&#8211;bindir</code>] [<code>&#8211;libdir</code>] [<code>&#8211;includedir</code>] [<code>&#8211;mandir</code>] [<code>&#8211;datadir</code>] [<code>&#8211;acdir</code>] [<code>&#8211;cflags</code>] [<code>&#8211;ldflags</code>] [<code>&#8211;libs</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>pth-config</code> program is a little helper utility for easy configuring and building applications based on the <i><a href="/docs/linux/man/3-pth/">pth</a></i>(3) library. It can be used to query the C compiler and linker flags which are required to correctly compile and link the application against the <i><a href="/docs/linux/man/3-pth/">pth</a></i>(3) library.</p>
<h2>OPTIONS</h2>
<p> <code>pth-config</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Prints the short usage information.</p>
<dt><code>&#8211;version</code></p>
<dd> Prints the version number and date of the installed <i><a href="/docs/linux/man/3-pth/">pth</a></i>(3) library.</p>
<dt><code>&#8211;all</code></p>
<dd> Forces the output of all flags, that is, including extra flags which are not <code>Pth</code> specific.</p>
<dt><code>&#8211;prefix</code></p>
<dd> Prints the installation prefix of architecture independent files</p>
<dt><code>&#8211;exec-prefix</code></p>
<dd> Prints the installation prefix of architecture dependent files.</p>
<dt><code>&#8211;bindir</code></p>
<dd> Prints the installation directory of binaries.</p>
<dt><code>&#8211;libdir</code></p>
<dd> Prints the installation directory of libraries.</p>
<dt><code>&#8211;includedir</code></p>
<dd> Prints the installation directory of include headers.</p>
<dt><code>&#8211;mandir</code></p>
<dd> Prints the installation directory of manual pages.</p>
<dt><code>&#8211;datadir</code></p>
<dd> Prints the installation directory of shared data.</p>
<dt><code>&#8211;acdir</code></p>
<dd> Prints the installation directory of <code>autoconf</code> data.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Prints the C compiler flags which are needed to compile the <i><a href="/docs/linux/man/3-pth/">pth</a></i>(3)-based application. The output is usually added to the <tt>&quot;CFLAGS&quot;</tt> variable of the applications <tt>&quot;Makefile&quot;</tt>.</p>
<dt><code>&#8211;ldflags</code></p>
<dd> Prints the linker flags (<tt>&quot;-L&quot;</tt>) which are needed to link the application with the <i><a href="/docs/linux/man/3-pth/">pth</a></i>(3) library. The output is usually added to the <tt>&quot;LDFLAGS&quot;</tt> variable of the applications <tt>&quot;Makefile&quot;</tt>.</p>
<dt><code>&#8211;libs</code></p>
<dd> Prints the library flags (<tt>&quot;-l&quot;</tt>) which are needed to link the application with the <i><a href="/docs/linux/man/3-pth/">pth</a></i>(3) library. The output is usually added to the <tt>&quot;LIBS&quot;</tt> variable of the applications <tt>&quot;Makefile&quot;</tt>.</dl>
<h2>EXAMPLE</h2>
<pre>
 CC      = cc
 CFLAGS  = -O `pth-config --cflags`
 LDFLAGS = `pth-config --ldflags`
 LIBS    = -lm `pth-config --libs`
</pre>
<pre>
 all: foo
 foo: foo.o
     $(CC) $(LDFLAGS) -o foo foo.o $(LIBS)
 foo.o: foo.c
     $(CC) $(CFLAGS) -c foo.c
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-pth/">pth</a></i>(3), <i><a href="/docs/linux/man/1-cc/">cc</a></i>(1).</p>
<h2>AUTHOR</h2>
<pre>
 Ralf S. Engelschall
 rse [at] engelschall.com
 <a rel="nofollow" href="http://www.engelschall.com">www.engelschall.com</a>
</pre>
<h2>Index</h2>
