---
title: "neon-config(1)"
name: "neon-config"
section: "1"
letter: "n"
url: "/docs/linux/man/1-neon-config/"
description: "neon-config – script providing information about installed copy of neon library"
---

<h2 class="name">NAME</h2>
<p> neon-config &#8211; script providing information about installed copy of neon library </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>neon-config</code> [<code>&#8211;prefix</code>] [[<code>&#8211;cflags</code>] | [<code>&#8211;libs</code>] | [<code>&#8211;la-file</code>] | [<code>&#8211;support</code>&nbsp;<wbr><i>feature</i>] | [<code>&#8211;help</code>] | [<code>&#8211;version</code>]]</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>neon-config</code> script provides information about an installed copy of the neon library. The <code>&#8211;cflags</code> and <code>&#8211;libs</code> options instruct how to compile and link an application against the library; the <code>&#8211;version</code> and <code>&#8211;support</code> options can help determine whether the library meets the applications requirements.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;cflags</code></p>
<dl>
<dt>
<dd> Print the flags which should be passed to the C compiler when compiling object files, when the object files use neon header files.</dl>
<p> <code>&#8211;libs</code></p>
<dl>
<dt>
<dd> Print the flags which should be passed to the linker when linking an application which uses the neon library</dl>
<p> <code>&#8211;la-file</code></p>
<dl>
<dt>
<dd> Print the location of the libtool library script, libneon.la, which can be used to link against neon by applications using libtool.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the version of the library</dl>
<p> <code>&#8211;prefix</code> <i>dir</i></p>
<dl>
<dt>
<dd> If <i>dir</i> is given; relocate output of <code>&#8211;cflags</code> and <code>&#8211;libs</code> as if neon was installed in given prefix directory. Otherwise, print the installation prefix of the library.</dl>
<p> <code>&#8211;support</code> <i>feature</i></p>
<dl>
<dt>
<dd> The script exits with success if <i>feature</i> is supported by the library.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help message; includes list of known features and whether they are supported or not.</dl>
<h2>EXAMPLE</h2>
<p> Below is a Makefile fragment which could be used to build an application against an installed neon library, when the <code>neon-config</code> script can be found in <code>$PATH</code>. </p>
<dl>
<dt>
<dd>
<pre>
CFLAGS = `neon-config --cflags`
LIBS = `neon-config --libs`
OBJECTS = myapp.o
TARGET = myapp
$(TARGET): $(OBJECTS)
        $(CC) $(LDFLAGS) -o $(TARGET) $(OBJECTS) $(LIBS)
myapp.o: myapp.c
        $(CC) $(CFLAGS) -c myapp.c -o myapp.o
</pre>
</dl>
<h2>AUTHOR</h2>
<p> <code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<h2>Index</h2>
