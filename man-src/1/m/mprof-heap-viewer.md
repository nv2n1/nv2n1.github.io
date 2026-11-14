---
title: "mprof-heap-viewer(1)"
name: "mprof-heap-viewer"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mprof-heap-viewer/"
description: "mprof-heap-viewer – GUI viewer for the logging profiler heap snapshots"
---

<h2>NAME</h2>
<p> mprof-heap-viewer &#8211; GUI viewer for the logging profiler heap snapshots</p>
<h2>SYNOPSIS</h2>
<p> <code>mprof-heap-viewer</code> file</p>
<h2>DESCRIPTION</h2>
<p> <code>mprof-heap-viewer</code> GUI viewer for the logging profiler heap snapshots </p>
<p> WARNING: this application is unfinished and experimental. Nevertheless it should work, and bug reports are encouraged. </p>
<p> This program decodes the contents of a logging profiler output file and locates all the heap snapshots inside it. The user can then select each individual snapshot and decide to load it in memory and explore its contents. </p>
<p> The GUI is organized to work on &quot;object sets&quot; (listed in a tree view on the left). All operations are performed with a popup menu on the choosen set. </p>
<p> Initially the sets are the heap snapshots (of course a heap snapshot can be considered a set of objects!). For each set the GUI shows on the right a list that breaks it down by class (one row for each class). </p>
<p> The user can then refine each set using a &quot;filter&quot;, to select a subset. Examples of filters are &quot;all objects of class X&quot;, or &quot;all objects that reference an object of class X&quot;. This way the user explores the sets breaking them down to subsets (each subset in the GUI is a child of its owner set on the tree view). </p>
<p> Moreover the user can issue a &quot;compare&quot; operation between two arbitrary sets A and B, which will compute two subsets: &quot;A &#8211; B&quot; (the objects of A which are not in B, a subsect of A) and &quot;B &#8211; A&quot; (the reverse). This can help in understanding what changed on the heap between garbage collections.</p>
<h2>Options</h2>
<p> None</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> None</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mono/">mono</a>(1) <code>.SH</code>COPYRIGHT Copyright (C) 2008 Novell, Inc (<a rel="nofollow" href="http://www.novell.com)">http://www.novell.com)</a> </p>
<h2>Index</h2>
