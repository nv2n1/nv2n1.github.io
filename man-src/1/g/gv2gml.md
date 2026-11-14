---
title: "gv2gml(1)"
name: "gv2gml"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gv2gml/"
description: "gml2gv,gv2gml – GML-DOT converters"
---

<h2 class="name">NAME</h2>
<p> gml2gv,gv2gml &#8211; GML-DOT converters </p>
<h2>SYNOPSIS</h2>
<p> <code>gml2gv</code> [ <code>-?v</code> ] [ <code>-g</code><i>gname</i> ] [ <code>-o</code><i>outfile</i> ] [ <i>files</i> ]<br />
 <code>gv2gml</code> [ <code>-?</code> ] [ <code>-o</code><i>outfile</i> ] [ <i>files</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>gml2gv</code> converts a graph specified in the GML format to a graph in the GV (formerly DOT) format. <code>gv2gml</code> converts a graph specified in the GV format to a graph in the GML format.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><code>-v</code></p>
<dd> Turns on verbose mode</p>
<dt><code>-?</code></p>
<dd> Prints usage information and exits.</p>
<dt><code>-g</code><i>gname</i></p>
<dd> The string <i>gname</i> is used as the name of the generated graph. If multiple graphs are generated, subsequent graphs use the name <i>gname</i> appended with an integer.</p>
<dt><code>-o</code><i>outfile</i></p>
<dd> Prints output to the file <i>outfile</i>. If not given, <code>gml2gv</code> uses stdout.</p>
<dt></dl>
<h2>OPERANDS</h2>
<dd> The following operand is supported:</p>
<dl>
<dt><i>files</i></p>
<dd> Names of files containing 1 or more graphs in GML. If no <i>files</i> operand is specified, the standard input will be used.</dl>
<h2>RETURN CODES</h2>
<p> Return <code>0</code> if there were no problems during conversion; and non-zero if any error occurred.</p>
<h2>LIMITATIONS</h2>
<p> As both the graph and graphics models of GV and GML differ significantly, the conversion is at best approximate. In particular, it is not clear how multiedges are differentiated in GML, so multiedges are created in GV with no user-available key. Also, no attribute information is lost, in that any GML attributes that aren&#8217;t converted to GV equivalents are retained as attributes in the output graph. </p>
<p> At present, <code>gv2gml</code> does not support subgraphs and clusters. In addition, there does not appear to be a standard mechanism for specifying default node and edge attributes in GML, so any attributes are repeated for every node and edge.</p>
<h2>AUTHORS</h2>
<p> Emden R. Gansner &lt;erg [at] research.att.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dot/">dot</a>(1), <a href="/docs/linux/man/3-libcgraph/">libcgraph</a>(3) </p>
<h2>Index</h2>
