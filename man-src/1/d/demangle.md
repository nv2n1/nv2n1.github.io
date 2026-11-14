---
title: "demangle(1)"
name: "demangle"
section: "1"
letter: "d"
url: "/docs/linux/man/1-demangle/"
description: "demangle – Undo C++ name mangling for symbols"
---

<h2 class="name">NAME</h2>
<p> demangle &#8211; Undo C++ name mangling for symbols </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>demangle</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>demangle</code></p>
<dd>reads a list of C++ mangled symbol names from standard input and converts these names to human-readable form on standard output. </p>
<p> This utility is part of the KDE Software Development Kit.</p>
<h2>EXAMPLE</h2>
<p> Create a file called names containing the following mangled symbol names: </p>
<dl>
<dt>
<dd>
<pre>
_ZNK6Object10metaObjectEv 
_ZN8QPtrListI5ArrowE5clearEv 
_ZTC4Kolf0_11KMainWindow
</pre>
</dl>
<p> These names can then be demangled as follows: </p>
<dl>
<dt>
<dd>
<pre>
example$ <code>demangle</code><code> &lt; </code><code>names</code>
Object::metaObject() const 
QPtrList&lt;Arrow&gt;::clear() 
construction vtable for KMainWindow-in-Kolf
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kminspector/">kminspector</a>(1) <a href="/docs/linux/man/1-kmtrace/">kmtrace</a>(1) <a href="/docs/linux/man/1-match/">match</a>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Ben Burton</code> &lt;bab [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
