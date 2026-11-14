---
title: "cscppc(1)"
name: "cscppc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cscppc/"
description: "cscppc – a compiler wrapper that runs cppcheck in background"
---

<h2 class="name">NAME</h2>
<p> cscppc &#8211; a compiler wrapper that runs cppcheck in background </p>
<h2>SYNOPSIS</h2>
<p> <code>cscppc</code> [<i>&#8211;help</i> | <i>&#8211;print-path-to-wrap</i>]</p>
<h2>DESCRIPTION</h2>
<p> cscppc is a compiler wrapper that runs cppcheck in background. Create a symbolic link to cscppc named as your compiler (gcc, g++, &#8230;) and put it to your $PATH. </p>
<p> The following parameters are given to cppcheck by default: </p>
<dl>
<dt>
<dd> &bull; -D__GNUC__</dl>
<dl>
<dt>
<dd> &bull; -D__STDC__</dl>
<dl>
<dt>
<dd> &bull; -D__i386__ &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [32bit architecture only]</dl>
<dl>
<dt>
<dd> &bull; -D__WORDSIZE=32&nbsp;<wbr> [32bit architecture only]</dl>
<dl>
<dt>
<dd> &bull; -D__x86_64__ &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> [64bit architecture only]</dl>
<dl>
<dt>
<dd> &bull; -D__WORDSIZE=64&nbsp;<wbr> [64bit architecture only]</dl>
<dl>
<dt>
<dd> &bull; &#8211;inline-suppr</dl>
<dl>
<dt>
<dd> &bull; &#8211;quiet</dl>
<dl>
<dt>
<dd> &bull; &#8211;template=&quot;{file}:{line}: {severity}: {id}: {message}&quot;</dl>
<dl>
<dt>
<dd> &bull; &#8211;suppressions-list=/usr/share/cscppc/default.supp</dl>
<p> The following parameters are passed to cppcheck from compiler&#8217;s command line: </p>
<dl>
<dt>
<dd> &bull; -D&#8230;</dl>
<dl>
<dt>
<dd> &bull; -I&#8230;</dl>
<p> The following file extensions are recognized as C/C++ source files: </p>
<dl>
<dt>
<dd> &bull; c</dl>
<dl>
<dt>
<dd> &bull; C</dl>
<dl>
<dt>
<dd> &bull; cc</dl>
<dl>
<dt>
<dd> &bull; cpp</dl>
<dl>
<dt>
<dd> &bull; cxx</dl>
<p> The following path substrings are black-listed from being scanned by cppcheck: </p>
<dl>
<dt>
<dd> &bull; conftest.c</dl>
<dl>
<dt>
<dd> &bull; _configtest.c</dl>
<dl>
<dt>
<dd> &bull; /CMakeTmp/</dl>
<dl>
<dt>
<dd> &bull; ../test.c</dl>
<p> If cscppc is installed on system, the following command activates the wrapper: </p>
<dl>
<dt>
<dd>
<pre>
export PATH=&quot;`cscppc --print-path-to-wrap`:$PATH&quot;
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Prints basic usage information.</dl>
<p> <code>&#8211;print-path-to-wrap</code></p>
<dl>
<dt>
<dd> Prints path to the directory with symlinks to the cscppc executable.</dl>
<h2>EXIT STATUS</h2>
<p> cscppc propagates the exit status returned by the compiler (in case cscppc succeeds to run the compiler). The exit status returned by cppcheck does not affect the resulting exit status.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>DEBUG_CSCPPC</code></p>
<dl>
<dt>
<dd> If set to a non-empty string, cscppc outputs the list of parameters given to cppcheck to the standard output.</dl>
<p> <code>CSCPPC_ADD_OPTS</code></p>
<dl>
<dt>
<dd> cscppc expects a colon-separated list of Cppcheck options that should be appended to command line prior to invoking Cppcheck. The options are appended even if they already appear in the command line and they are always appended at the end of the command line.</dl>
<h2>BUGS</h2>
<p> Please report bugs and feature requests to the following mailing-list: </p>
<dl>
<dt>
<dd>
<pre>
<a rel="nofollow" href="https://fedorahosted.org/mailman/listinfo/cscppc-devel">https://fedorahosted.org/mailman/listinfo/cscppc-devel</a>
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Written by Kamil Dudka.</p>
<h2>COPYING</h2>
<p> Copyright (C) 2013-2014 Red Hat, Inc. Free use of this software is granted under the terms of the GNU General Public License (GPL). See the COPYING file for details. </p>
<h2>Index</h2>
