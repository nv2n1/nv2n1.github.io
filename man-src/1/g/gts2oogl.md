---
title: "gts2oogl(1)"
name: "gts2oogl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gts2oogl/"
description: "gts2oogl – converts a GTS file to OOGL file format (Geomview)."
---

<h2 class="name">NAME</h2>
<p> gts2oogl &#8211; converts a GTS file to OOGL file format (Geomview).</p>
<h2>SYNOPSIS</h2>
<p> <code>gts2oogl</code> [<i>OPTIONS</i>]&nbsp;&lt;&nbsp;<i>input.srf&nbsp;</i>&gt;&nbsp;<i>output.oogl</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gts2oogl</code> command. </p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-G</code>,&nbsp;<code>&#8211;gnuplot</code></p>
<dd> Writes isolines in gnuplot format.</p>
<dt><code>&#8211;component</code></p>
<dd> Color faces according to the component they belong too.</p>
<dt><code>&#8211;quality</code></p>
<dd> Color faces according to their quality.</p>
<dt><code>&#8211;area</code></p>
<dd> Color faces according to their area.</p>
<dt><code>&#8211;incomp</code></p>
<dd> Color incompatible faces.</p>
<dt><code>-f&nbsp;</code><i>VAL</i>,&nbsp;<code>&#8211;fold=</code><i>VAL</i></p>
<dd> Color faces which make an angle smaller than <i>VAL</i> degrees with any of their neighbors.</p>
<dt><code>-t</code>,&nbsp;<code>&#8211;faces</code></p>
<dd> Output individual faces.</p>
<dt><code>&#8211;epv</code></p>
<dd> Color vertices according to number of edges per vertex.</p>
<dt><code>-H&nbsp;</code><i>C</i>,&nbsp;<code>&#8211;height=</code><i>C</i></p>
<dd> Color vertices according to their <i>C</i> coordinate.</p>
<dt><code>-g</code>,&nbsp;<code>&#8211;gaussian</code></p>
<dd> Color vertices according to Gaussian curvature.</p>
<dt><code>-C</code>,&nbsp;<code>&#8211;curvature</code></p>
<dd> Color vertices according to mean curvature.</p>
<dt><code>&#8211;boundary</code></p>
<dd> Output boundary edges.</p>
<dt><code>-e&nbsp;</code><i>A</i>,&nbsp;<code>&#8211;feature=</code><i>A</i></p>
<dd> Output `feature&#8217; edges defined by angle <i>A</i>.</p>
<dt><code>&#8211;non-manifold</code></p>
<dd> Output non-manifold edges.</p>
<dt><code>&#8211;duplicate</code></p>
<dd> Output duplicate edges.</p>
<dt><code>-i&nbsp;</code><i>N</i>,&nbsp;<code>&#8211;isolines=</code><i>N</i></p>
<dd> Draw <i>N</i> isolines (levels of constant altitude).</p>
<dt><code>-I&nbsp;</code><i>L</i>,&nbsp;<code>&#8211;isolines=</code><i>L</i></p>
<dd> Draw isoline at level <i>L</i>.</p>
<dt><code>&#8211;cmap=</code><i>FILE</i></p>
<dd> Load <i>FILE</i> as colormap.</p>
<dt><code>-m&nbsp;</code><i>VAL</i>,&nbsp;<code>&#8211;min=</code><i>VAL</i></p>
<dd> Use <i>VAL</i> as minimum scaling value.</p>
<dt><code>-M&nbsp;</code><i>VAL</i>,&nbsp;<code>&#8211;max=</code><i>VAL</i></p>
<dd> Use <i>VAL</i> as maximum scaling value.</p>
<dt><code>-r</code>,&nbsp;<code>&#8211;reverse</code></p>
<dd> Reverse colormap.</p>
<dt><code>-n</code>,&nbsp;<code>&#8211;nosurface</code></p>
<dd> Do not output surface.</p>
<dt><code>-F&nbsp;</code><i>C</i>,&nbsp;<code>&#8211;flatten=</code><i>C</i></p>
<dd> Set <i>C</i> coordinate to average value.</p>
<dt><code>-v</code>,&nbsp;<code>&#8211;verbose</code></p>
<dd> Display surface statistics.</p>
<dt><code>-h</code>,&nbsp;<code>&#8211;help</code></p>
<dd> Display the help and exit. </p>
</dl>
<h2>AUTHOR</h2>
<p> gts2oogl was written by Stephane Pipinet &lt;popinet [at] users.sourceforge.net&gt;. </p>
<p> This manual page was written by Ruben Molina &lt;rmolina [at] udea.edu.co&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
