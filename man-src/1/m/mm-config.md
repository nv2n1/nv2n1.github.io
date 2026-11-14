---
title: "mm-config(1)"
name: "mm-config"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mm-config/"
description: "mm-config – OSSP mm library configuration/build utility"
---

<h2>NAME</h2>
<p> <code>mm-config</code> &#8211; OSSP mm library configuration/build utility</p>
<h2>VERSION</h2>
<p> <font SIZE="-1">OSSP</font> mm <font SIZE="-1">1.4.1 (10-Aug-2006)</font></p>
<h2>SYNOPSIS</h2>
<p> <code>mm-config</code> [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<code>&#8211;cflags</code>] [<code>&#8211;ldflags</code>] [<code>&#8211;libs</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>mm-config</code> program is a little helper utility for easy configuring and building applications based on the <i><a href="/docs/linux/man/3-mm/">mm</a></i>(3) library. It can be used to query the C compiler and linker flags which are required to correctly compile and link the application against the <i><a href="/docs/linux/man/3-mm/">mm</a></i>(3) library.</p>
<h2>OPTIONS</h2>
<p> <code>mm-config</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Prints the short usage information.</p>
<dt><code>&#8211;version</code></p>
<dd> Prints the version number and date of the installed <i><a href="/docs/linux/man/3-mm/">mm</a></i>(3) library.</p>
<dt><code>&#8211;cflags</code></p>
<dd> Prints the C compiler flags which are needed to compile the <i><a href="/docs/linux/man/3-mm/">mm</a></i>(3)-based application. The output is usually added to the <tt>&quot;CFLAGS&quot;</tt> variable of the applications <tt>&quot;Makefile&quot;</tt>.</p>
<dt><code>&#8211;ldflags</code></p>
<dd> Prints the linker flags (<tt>&quot;-L&quot;</tt>) which are needed to link the application with the <i><a href="/docs/linux/man/3-mm/">mm</a></i>(3) library. The output is usually added to the <tt>&quot;LDFLAGS&quot;</tt> variable of the applications <tt>&quot;Makefile&quot;</tt>.</p>
<dt><code>&#8211;libs</code></p>
<dd> Prints the library flags (<tt>&quot;-l&quot;</tt>) which are needed to link the application with the <i><a href="/docs/linux/man/3-mm/">mm</a></i>(3) library. The output is usually added to the <tt>&quot;LIBS&quot;</tt> variable of the applications <tt>&quot;Makefile&quot;</tt>.</dl>
<h2>EXAMPLE</h2>
<pre>
 CC=cc
 CFLAGS=-O `mm-config --cflags`
 LDFLAGS=`mm-config --ldflags`
 LIBS=-lm `mm-config --libs`
</pre>
<pre>
 all: foo
 foo: foo.o
     $(CC) $(LDFLAGS) -o foo foo.o $(LIBS)
 foo.o: foo.c
     $(CC) $(CFLAGS) -c foo.c
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-mm/">mm</a></i>(3).</p>
<h2>AUTHOR</h2>
<pre>
 Ralf S. Engelschall
 rse [at] engelschall.com
 <a rel="nofollow" href="http://www.engelschall.com">www.engelschall.com</a>
</pre>
<h2>Index</h2>
