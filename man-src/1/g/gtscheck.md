---
title: "gtscheck(1)"
name: "gtscheck"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtscheck/"
description: "gtscheck – checks that a surface defines a closed, orientable non self-intersecting manifold."
---

<h2 class="name">NAME</h2>
<p> gtscheck &#8211; checks that a surface defines a closed, orientable non self-intersecting manifold.</p>
<h2>SYNOPSIS</h2>
<p> <code>gtscheck</code> [<i>OPTION</i>]&nbsp;&lt;&nbsp;<i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gtscheck</code> command. </p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-v</code>,&nbsp;<code>&#8211;verbose</code></p>
<dd> Print statistics about the surface.</p>
<dt><code>-h</code>,&nbsp;<code>&#8211;help</code></p>
<dd> Display the help and exit. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The return status reflects the error encountered: <code>0</code> none <code>1</code> the input file is not a valid GTS file <code>2</code> the surface is not an orientable manifold <code>3</code> the surface is an orientable manifold but is self-intersecting </p>
<h2>AUTHOR</h2>
<p> gtscheck was written by Stephane Popinet &lt;popinet [at] users.sourceforge.net&gt;. </p>
<p> This manual page was written by Ruben Molina &lt;rmolina [at] udea.edu.co&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
