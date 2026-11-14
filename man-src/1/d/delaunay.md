---
title: "delaunay(1)"
name: "delaunay"
section: "1"
letter: "d"
url: "/docs/linux/man/1-delaunay/"
description: "delaunay – constructs the constrained Delaunay triangulation of the input"
---

<h2 class="name">NAME</h2>
<p> delaunay &#8211; constructs the constrained Delaunay triangulation of the input</p>
<h2>SYNOPSIS</h2>
<p> <code>delaunay</code> [<i>OPTIONS</i>]&nbsp;&lt;&nbsp;<i>file.gts</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>delaunay</code> command. This command constructs the constrained Delaunay triangulation of the input </p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-b</code>,&nbsp;<code>&#8211;hull</code></p>
<dd> Do not keep convex hull.</p>
<dt><code>-e</code>,&nbsp;<code>&#8211;noconst</code></p>
<dd> Do not add constrained edges.</p>
<dt><code>-S</code>,&nbsp;<code>&#8211;split</code></p>
<dd> Split constraints (experimental).</p>
<dt><code>-H</code>,&nbsp;<code>&#8211;holes</code></p>
<dd> Remove holes from the triangulation.</p>
<dt><code>-d</code>,&nbsp;<code>&#8211;duplicates</code></p>
<dd> Remove duplicate vertices.</p>
<dt><code>-r</code>,&nbsp;<code>&#8211;randomize</code></p>
<dd> Shuffle input vertex list.</p>
<dt><code>-c</code>,&nbsp;<code>&#8211;check</code></p>
<dd> Check Delaunay property.</p>
<dt><code>-f&nbsp;</code><i>FNAME</i>,&nbsp;<code>&#8211;files=</code><i>FNAME</i></p>
<dd> Generate evolution files.</p>
<dt><code>-o</code>,&nbsp;<code>&#8211;conform</code></p>
<dd> Generate conforming triangulation.</p>
<dt><code>-s&nbsp;</code><i>N</i>,&nbsp;<code>&#8211;steiner=</code><i>N</i></p>
<dd> Maximum number of Steiner points for conforming triangulation (default is no limit).</p>
<dt><code>-q&nbsp;</code><i>Q</i>,&nbsp;<code>&#8211;quality=</code><i>Q</i></p>
<dd> Set the minimum acceptable face quality.</p>
<dt><code>-a&nbsp;</code><i>A</i>,&nbsp;<code>&#8211;area=</code><i>A</i></p>
<dd> Set the maximum acceptable face area.</p>
<dt><code>-v</code>,&nbsp;<code>&#8211;verbose</code></p>
<dd> Print statistics about the triangulation.</p>
<dt><code>-h</code>,&nbsp;<code>&#8211;help</code></p>
<dd> Display the help and exit. </p>
</dl>
<h2>AUTHOR</h2>
<p> delaunay was written by Stephane Popinet &lt;popinet [at] users.sourceforge.net&gt;. </p>
<p> This manual page was written by Ruben Molina &lt;rmolina [at] udea.edu.co&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
