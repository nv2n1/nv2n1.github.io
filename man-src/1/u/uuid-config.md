---
title: "uuid-config(1)"
name: "uuid-config"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uuid-config/"
description: "uuid-config – OSSP uuid API build utility"
---

<h2 class="name">NAME</h2>
<p> <code>uuid-config</code> &#8211; <font SIZE="-1"><code>OSSP</code></font><code> uuid </code><font SIZE="-1"><code>API</code></font><code> build utility</code> </p>
<h2>VERSION</h2>
<p> <font SIZE="-1">OSSP</font> uuid <font SIZE="-1">1.6.2 (04-Jul-2008)</font></p>
<h2>SYNOPSIS</h2>
<p> <code>uuid-config</code> [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<code>&#8211;all</code>] [<code>&#8211;prefix</code>] [<code>&#8211;exec-prefix</code>] [<code>&#8211;bindir</code>] [<code>&#8211;libdir</code>] [<code>&#8211;includedir</code>] [<code>&#8211;mandir</code>] [<code>&#8211;datadir</code>] [<code>&#8211;acdir</code>] [<code>&#8211;cflags</code>] [<code>&#8211;ldflags</code>] [<code>&#8211;libs</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>uuid-config</code> program is a little helper utility for easy configuring and building applications based on the <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3) library. It can be used to query the C compiler and linker flags which are required to correctly compile and link the application against the <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3) library.</p>
<h2>OPTIONS</h2>
<p> <code>uuid-config</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Prints the short usage information.</p>
<dt><code>&#8211;version</code></p>
<dd> Prints the version number and date of the installed <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3) library.</p>
<dt><code>&#8211;all</code></p>
<dd> Forces the output of all flags, that is, including extra flags which are not <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> specific.</p>
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
<dd> Prints the C compiler flags which are needed to compile the <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3)-based application. The output is usually added to the <tt> CFLAGS<br />
 </tt> uuidiable of the applications <tt> Makefile<br />
 </tt>.</p>
<dt><code>&#8211;ldflags</code></p>
<dd> Prints the linker flags (<tt> -L<br />
 </tt>) which are needed to link the application with the <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3) library. The output is usually added to the <tt> LDFLAGS<br />
 </tt> uuidiable of the applications <tt> Makefile<br />
 </tt>.</p>
<dt><code>&#8211;libs</code></p>
<dd> Prints the library flags (<tt> -l<br />
 </tt>) which are needed to link the application with the C <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3) library. The output is usually added to the <tt> LIBS<br />
 </tt> uuidiable of the applications <tt> Makefile<br />
 </tt>.</dl>
<h2>EXAMPLE</h2>
<pre>
 CC      = cc
 CFLAGS  = -O `uuid-config --cflags`
 LDFLAGS = `uuid-config --ldflags`
 LIBS    = -lm `uuid-config --libs`
 all: foo
 foo: foo.o
     $(CC) $(LDFLAGS) -o foo foo.o $(LIBS)
 foo.o: foo.c
     $(CC) $(CFLAGS) -c foo.c
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3), <i><a href="/docs/linux/man/1-uuid/">uuid</a></i>(1), <i><a href="/docs/linux/man/3-ossp--uuid/">OSSP::uuid</a></i>(3). </p>
<h2>Index</h2>
