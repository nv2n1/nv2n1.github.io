---
title: "x86_64-linux-gnu-python3-6m-config(1)"
name: "x86_64-linux-gnu-python3-6m-config"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x86_64-linux-gnu-python3-6m-config/"
description: "python-config – output build options for python C/C++ extensions or embedding"
---

<p>python-config &#8211; output build options for python C/C++ extensions or embedding </p>
<h2>Synopsis</h2>
<p><code>python-config</code> [ <code>&#8211;prefix</code> ] [ <code>&#8211;exec-prefix</code> ] [ <code>&#8211;includes</code> ] [ <code>&#8211;libs</code> ] [ <code>&#8211;cflags</code> ] [ <code>&#8211;ldflags</code> ] [ <code>&#8211;extension-suffix</code> ] [ <code>&#8211;abiflags</code> ] [ <code>&#8211;help</code> ]</p>
<h2>Description</h2>
<p><code>python-config</code> helps compiling and linking programs, which embed the Python interpreter, or extension modules that can be loaded dynamically (at run time) into the interpreter.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>&#8211;abiflags</code></p>
<dd>print the the ABI flags as specified by PEP 3149.</p>
<dt><code>&#8211;cflags</code></p>
<dd>print the C compiler flags.</p>
<dt><code>&#8211;ldflags</code></p>
<dd>print the flags that should be passed to the linker.</p>
<dt><code>&#8211;includes</code></p>
<dd>similar to <i>&#8211;cflags</i> but only with -I options (path to python header files).</p>
<dt><code>&#8211;libs</code></p>
<dd>similar to <i>&#8211;ldflags</i> but only with -l options (used libraries).</p>
<dt><code>&#8211;prefix</code></p>
<dd>prints the prefix (base directory) under which python can be found.</p>
<dt><code>&#8211;exec-prefix</code></p>
<dd>print the prefix used for executable program directories (such as bin, sbin, etc).</p>
<dt><code>&#8211;extension-suffix</code></p>
<dd>print the extension suffix used for binary extensions.</p>
<dt><code>&#8211;help</code></p>
<dd>print the usage message.</dl>
<h2>Examples</h2>
<p>To build the singe-file c program <i>prog</i> against the python library, use </p>
<dl COMPACT>
<dd>gcc $(python-config &#8211;cflags &#8211;ldflags) progr.cpp -o progr.cpp</dl>
<p> The same in a makefile: </p>
<dl COMPACT>
<dd>CFLAGS+=$(shell python-config &#8211;cflags)</dl>
<dl COMPACT>
<dd>LDFLAGS+=$(shell python-config &#8211;ldflags)</dl>
<dl COMPACT>
<dd>all: progr</dl>
<p> To build a dynamically loadable python module, use </p>
<dl COMPACT>
<dd>gcc $(python-config &#8211;cflags &#8211;ldflags) -shared -fPIC progr.cpp -o progr.so</dl>
<h2>See Also</h2>
<p>python (1)<br />
 <a rel="nofollow" href="http://docs.python.org/extending/extending.html">http://docs.python.org/extending/extending.html</a><br />
 /usr/share/doc/python/faq/extending.html </p>
<h2>Authors</h2>
<p>This manual page was written by Johann Felix Soden &lt;johfel [at] gmx.de&gt; for the Debian project (and may be used by others).</p>
