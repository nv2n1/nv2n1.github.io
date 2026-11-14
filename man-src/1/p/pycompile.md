---
title: "pycompile(1)"
name: "pycompile"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pycompile/"
description: "pycompile – byte compile Python source files"
---

<h2 class="name">NAME</h2>
<p> pycompile &#8211; byte compile Python source files </p>
<h2>SYNOPSIS</h2>
<p> pycompile [-V [X.Y][-][A.B]] DIR_OR_FILE [-X REGEXPR] </p>
<p> pycompile -p PACKAGE</p>
<h2>DESCRIPTION</h2>
<p> Wrapper around Python standard library&#8217;s py_compile module to byte-compile Python files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd> show program&#8217;s version number and exit</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-f</code>,<code> &#8211;force</code></p>
<dd> force rebuild of byte-code files even if timestamps are up-to-date</p>
<dt><code>-O</code></p>
<dd> byte-compile to .pyo files</p>
<dt><code>-q</code>,<code> &#8211;quiet</code></p>
<dd> be quiet</p>
<dt><code>-v</code>,<code> &#8211;verbose</code></p>
<dd> turn verbose mode on</p>
<dt><code>-p</code><i>&nbsp;PACKAGE</i>,<code>&nbsp;&#8211;package=</code><i>PACKAGE</i></p>
<dd> specify Debian package name whose files should be bytecompiled (combining with DIR_OR_FILE will additionally limit list of files)</p>
<dt><code>-V</code><i>&nbsp;VRANGE</i></p>
<dd> force private modules to be bytecompiled with Python version from given range, regardless of the default Python version in the system. If there are no other options, bytecompile all public modules for installed Python versions that match given range. VERSION_RANGE examples:</p>
<dt>&bull;</p>
<dd> <code>2.5</code> version 2.5 only</p>
<dt>&bull;</p>
<dd> <code>2.5-</code> version 2.5 or newer</p>
<dt>&bull;</p>
<dd> <code>2.5-2.7</code> version 2.5 or 2.6</p>
<dt>&bull;</p>
<dd> <code>-3.0</code> all supported 2.X versions</p>
<dt><code>-X</code><i>&nbsp;REGEXPR</i>,<code>&nbsp;&#8211;exclude=</code><i>REGEXPR</i></p>
<dd> exclude items that match given REGEXPR. You may use this option multiple times to build up a list of things to exclude</dl>
<h2>AUTHOR</h2>
<p> Piotr Ożarowski, 2012-2013 </p>
<h2>Index</h2>
