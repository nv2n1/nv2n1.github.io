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
<dt><code>&#8211;help</code></dt>
<dd> Prints the short usage information.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Prints the version number and date of the installed <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3) library.</dd>
<dt><code>&#8211;all</code></dt>
<dd> Forces the output of all flags, that is, including extra flags which are not <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> specific.</dd>
<dt><code>&#8211;prefix</code></dt>
<dd> Prints the installation prefix of architecture independent files</dd>
<dt><code>&#8211;exec-prefix</code></dt>
<dd> Prints the installation prefix of architecture dependent files.</dd>
<dt><code>&#8211;bindir</code></dt>
<dd> Prints the installation directory of binaries.</dd>
<dt><code>&#8211;libdir</code></dt>
<dd> Prints the installation directory of libraries.</dd>
<dt><code>&#8211;includedir</code></dt>
<dd> Prints the installation directory of include headers.</dd>
<dt><code>&#8211;mandir</code></dt>
<dd> Prints the installation directory of manual pages.</dd>
<dt><code>&#8211;datadir</code></dt>
<dd> Prints the installation directory of shared data.</dd>
<dt><code>&#8211;acdir</code></dt>
<dd> Prints the installation directory of <code>autoconf</code> data.</dd>
<dt><code>&#8211;cflags</code></dt>
<dd> Prints the C compiler flags which are needed to compile the <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3)-based application. The output is usually added to the <tt> CFLAGS<br />
 </tt> uuidiable of the applications <tt> Makefile<br />
 </tt>.</dd>
<dt><code>&#8211;ldflags</code></dt>
<dd> Prints the linker flags (<tt> -L<br />
 </tt>) which are needed to link the application with the <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3) library. The output is usually added to the <tt> LDFLAGS<br />
 </tt> uuidiable of the applications <tt> Makefile<br />
 </tt>.</dd>
<dt><code>&#8211;libs</code></dt>
<dd> Prints the library flags (<tt> -l<br />
 </tt>) which are needed to link the application with the C <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3) library. The output is usually added to the <tt> LIBS<br />
 </tt> uuidiable of the applications <tt> Makefile<br />
 </tt>.</dd></dl>
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
<p> <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3), <i><a href="/docs/linux/man/1-uuid/">uuid</a></i>(1), <i>OSSP::uuid</i>(3). </p>
<h2>Index</h2>
