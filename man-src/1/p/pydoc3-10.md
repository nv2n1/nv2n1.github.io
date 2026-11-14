---
title: "pydoc3-10(1)"
name: "pydoc3-10"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pydoc3-10/"
description: "pydoc3.10 – the Python documentation tool"
---

<p>pydoc3.10 &#8211; the Python documentation tool </p>
<h2>Synopsis</h2>
<p><code>pydoc3.10</code> <i>name</i> </p>
<p> <code>pydoc3.10 -k</code> <i>keyword</i> </p>
<p> <code>pydoc3.10 -p</code> <i>port</i> </p>
<p> <code>pydoc3.10 -g</code> </p>
<p> <code>pydoc3.10 -w</code> <i>module [&#8230;]</i></p>
<h2>Description</h2>
<p><code>pydoc3.10</code> <i>name</i> Show text documentation on something. <i>name</i> may be the name of a Python keyword, topic, function, module, or package, or a dotted reference to a class or function within a module or module in a package. If <i>name</i> contains a &#8216;/&#8217;, it is used as the path to a Python source file to document. If name is &#8216;keywords&#8217;, &#8216;topics&#8217;, or &#8216;modules&#8217;, a listing of these things is displayed. </p>
<p> <code>pydoc3.10 -k</code> <i>keyword</i> Search for a keyword in the synopsis lines of all available modules. </p>
<p> <code>pydoc3.10 -p</code> <i>port</i> Start an HTTP server on the given port on the local machine. </p>
<p> <code>pydoc3.10 -g</code> Pop up a graphical interface for finding and serving documentation. </p>
<p> <code>pydoc3.10 -w</code> <i>name [&#8230;]</i> Write out the HTML documentation for a module to a file in the current directory. If <i>name</i> contains a &#8216;/&#8217;, it is treated as a filename; if it names a directory, documentation is written for all the contents.</p>
<h2>Author</h2>
<p>Moshe Zadka, based on &quot;pydoc &#8211;help&quot;</p>
