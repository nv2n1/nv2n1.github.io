---
title: "m2gmetis(1)"
name: "m2gmetis"
section: "1"
letter: "m"
url: "/docs/linux/man/1-m2gmetis/"
description: "m2gmetis – Converts a mesh into a graph that is compatible with METIS."
---

<h2>NAME</h2>
<p> m2gmetis &#8211; Converts a mesh into a graph that is compatible with METIS.</p>
<h2>SYNOPSIS</h2>
<p> <code>m2gmetis</code> [<i>options</i>] <i>&lt;meshfile&gt; &lt;graphfile&gt;</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd> Required parameters</p>
<dt>meshfile</p>
<dd> Stores the input mesh.</p>
<dt>graphfile</p>
<dd> The filename of the output graph.</p>
<dt>
<dd> Optional parameters</p>
<dt> <code>-gtype</code>=<i>string</i></p>
<dt>
<dd>
<dd>Specifies the graph that will be generated. The possible values are:</p>
<dt>dual</p>
<dd> &#8211; Generate dual graph of the mesh [default]</p>
<dt>nodal</p>
<dd> &#8211; Generate the nodal graph of the mesh</p>
<dt> <code>-ncommon</code>=<i>int</i> [applies when gtype=dual]</p>
<dt>
<dd>
<dd>Specifies the common number of nodes that two elements must have in order to put an edge between them in the dual graph. Default is 1.</p>
<dt> <code>-dbglvl</code>=<i>int</i></p>
<dt>
<dd>
<dd>Selects the dbglvl.</p>
<dt> <code>-help</code></p>
<dt>
<dd>
<dd>Prints this message. </p>
</dl>
<h2>Index</h2>
