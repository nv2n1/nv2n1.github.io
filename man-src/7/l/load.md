---
title: "load(7)"
name: "load"
section: "7"
letter: "l"
url: "/docs/linux/man/7-load/"
description: "LOAD – load a shared library file"
---

<p>LOAD &#8211; load a shared library file </p>
<h2>Synopsis</h2>
<pre>LOAD '<i>filename</i>'</pre>
<h2>Description</h2>
<p>This command loads a shared library file into the PostgreSQL server&#8217;s address space. If the file has been loaded already, the command does nothing. Shared library files that contain C functions are automatically loaded whenever one of their functions is called. Therefore, an explicit <code>LOAD</code> is usually only needed to load a library that modifies the server&#8217;s behavior through &#8220;hooks&#8221; rather than providing a set of functions. </p>
<p> The file name is specified in the same way as for shared library names in CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)]; in particular, one can rely on a search path and automatic addition of the system&#8217;s standard shared library file name extension. See in the documentation for more information on this topic. </p>
<p> Non-superusers can only apply <code>LOAD</code> to library files located in <i>$libdir/plugins/</i> &#8212; the specified <i>filename</i> must begin with exactly that string. (It is the database administrator&#8217;s responsibility to ensure that only &#8220;safe&#8221; libraries are installed there.)</p>
<h2>Compatibility</h2>
<p><code>LOAD</code> is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)] </p>
