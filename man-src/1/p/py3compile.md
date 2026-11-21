---

title: "py3compile(1)"
name: "py3compile"
section: "1"
letter: "p"
url: "/docs/linux/man/1-py3compile/"
description: "py3compile – byte compile Python 3 source files"
---

<p> py3compile [-V [X.Y][-][A.B]] DIR_OR_FILE [-X REGEXPR] </p>
<p> pycompile -p PACKAGE</p>
<p> Wrapper around Python standard library&#8217;s py_compile module to byte-compile Python 3 files.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> show program&#8217;s version number and exit</dd>
<dt><code>-h</code>,<code> &#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-f</code>,<code> &#8211;force</code></dt>
<dd> force rebuild of byte-code files even if timestamps are up-to-date</dd>
<dt><code>-O</code></dt>
<dd> byte-compile to .pyo files</dd>
<dt><code>-q</code>,<code> &#8211;quiet</code></dt>
<dd> be quiet</dd>
<dt><code>-v</code>,<code> &#8211;verbose</code></dt>
<dd> turn verbose mode on</dd>
<dt><code>-p</code><i>&nbsp;PACKAGE</i>,<code>&nbsp;&#8211;package=</code><i>PACKAGE</i></dt>
<dd> specify Debian package name whose files should be bytecompiled</dd>
<dt><code>-V</code><i>&nbsp;VRANGE</i></dt>
<dd> force private modules to be bytecompiled with Python 3 version from given range, regardless of the default Python 3 version in the system. If there are no other options, bytecompile all public modules for installed Python 3 versions that match given range. VERSION_RANGE examples:</dd>
<dt>&bull;</dt>
<dd> <code>3.1</code> version 3.1 only,</dd>
<dt>&bull;</dt>
<dd> <code>3.1-</code> version 3.1 or newer,</dd>
<dt>&bull;</dt>
<dd> <code>3.1-3.3</code> version 3.1 or 3.2,</dd>
<dt>&bull;</dt>
<dd> <code>-4.0</code> all supported 3.X versions</dd>
<dt><code>-X</code><i>&nbsp;REGEXPR</i>,<code>&nbsp;&#8211;exclude=</code><i>REGEXPR</i></dt>
<dd> exclude items that match given REGEXPR. You may use this option multiple times to build up a list of things to exclude</dd></dl>
<h2>AUTHOR</h2>
<p> Piotr Ożarowski, 2012-2013 </p>
