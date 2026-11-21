---

title: "m2gmetis(1)"
name: "m2gmetis"
section: "1"
letter: "m"
url: "/docs/linux/man/1-m2gmetis/"
description: "m2gmetis – Converts a mesh into a graph that is compatible with METIS."
---

<p> m2gmetis &#8211; Converts a mesh into a graph that is compatible with METIS.</p>
<h2>SYNOPSIS</h2>
<p> <code>m2gmetis</code> [<i>options</i>] <i>&lt;meshfile&gt; &lt;graphfile&gt;</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt>
</dt><dd> Required parameters</dd>
<dt>meshfile</dt>
<dd> Stores the input mesh.</dd>
<dt>graphfile</dt>
<dd> The filename of the output graph.</dd>
<dt>
</dt><dd> Optional parameters</dd>
<dt> <code>-gtype</code>=<i>string</i></dt>
<dd>Specifies the graph that will be generated. The possible values are:</dd>
<dt>dual</dt>
<dd> &#8211; Generate dual graph of the mesh [default]</dd>
<dt>nodal</dt>
<dd> &#8211; Generate the nodal graph of the mesh</dd>
<dt> <code>-ncommon</code>=<i>int</i> [applies when gtype=dual]</dt>
<dd>Specifies the common number of nodes that two elements must have in order to put an edge between them in the dual graph. Default is 1.</dd>
<dt> <code>-dbglvl</code>=<i>int</i></dt>
<dd>Selects the dbglvl.</dd>
<dt> <code>-help</code></dt>
<dd>Prints this message. </dd>
</dl>
