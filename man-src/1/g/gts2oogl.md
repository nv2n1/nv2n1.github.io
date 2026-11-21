---
title: "gts2oogl(1)"
name: "gts2oogl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gts2oogl/"
description: "gts2oogl – converts a GTS file to OOGL file format (Geomview)."
---

<h2>SYNOPSIS</h2>
<p> <code>gts2oogl</code> [<i>OPTIONS</i>]&nbsp;&lt;&nbsp;<i>input.srf&nbsp;</i>&gt;&nbsp;<i>output.oogl</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gts2oogl</code> command. </p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-G</code>,&nbsp;<code>&#8211;gnuplot</code></dt>
<dd> Writes isolines in gnuplot format.</dd>
<dt><code>&#8211;component</code></dt>
<dd> Color faces according to the component they belong too.</dd>
<dt><code>&#8211;quality</code></dt>
<dd> Color faces according to their quality.</dd>
<dt><code>&#8211;area</code></dt>
<dd> Color faces according to their area.</dd>
<dt><code>&#8211;incomp</code></dt>
<dd> Color incompatible faces.</dd>
<dt><code>-f&nbsp;</code><i>VAL</i>,&nbsp;<code>&#8211;fold=</code><i>VAL</i></dt>
<dd> Color faces which make an angle smaller than <i>VAL</i> degrees with any of their neighbors.</dd>
<dt><code>-t</code>,&nbsp;<code>&#8211;faces</code></dt>
<dd> Output individual faces.</dd>
<dt><code>&#8211;epv</code></dt>
<dd> Color vertices according to number of edges per vertex.</dd>
<dt><code>-H&nbsp;</code><i>C</i>,&nbsp;<code>&#8211;height=</code><i>C</i></dt>
<dd> Color vertices according to their <i>C</i> coordinate.</dd>
<dt><code>-g</code>,&nbsp;<code>&#8211;gaussian</code></dt>
<dd> Color vertices according to Gaussian curvature.</dd>
<dt><code>-C</code>,&nbsp;<code>&#8211;curvature</code></dt>
<dd> Color vertices according to mean curvature.</dd>
<dt><code>&#8211;boundary</code></dt>
<dd> Output boundary edges.</dd>
<dt><code>-e&nbsp;</code><i>A</i>,&nbsp;<code>&#8211;feature=</code><i>A</i></dt>
<dd> Output `feature&#8217; edges defined by angle <i>A</i>.</dd>
<dt><code>&#8211;non-manifold</code></dt>
<dd> Output non-manifold edges.</dd>
<dt><code>&#8211;duplicate</code></dt>
<dd> Output duplicate edges.</dd>
<dt><code>-i&nbsp;</code><i>N</i>,&nbsp;<code>&#8211;isolines=</code><i>N</i></dt>
<dd> Draw <i>N</i> isolines (levels of constant altitude).</dd>
<dt><code>-I&nbsp;</code><i>L</i>,&nbsp;<code>&#8211;isolines=</code><i>L</i></dt>
<dd> Draw isoline at level <i>L</i>.</dd>
<dt><code>&#8211;cmap=</code><i>FILE</i></dt>
<dd> Load <i>FILE</i> as colormap.</dd>
<dt><code>-m&nbsp;</code><i>VAL</i>,&nbsp;<code>&#8211;min=</code><i>VAL</i></dt>
<dd> Use <i>VAL</i> as minimum scaling value.</dd>
<dt><code>-M&nbsp;</code><i>VAL</i>,&nbsp;<code>&#8211;max=</code><i>VAL</i></dt>
<dd> Use <i>VAL</i> as maximum scaling value.</dd>
<dt><code>-r</code>,&nbsp;<code>&#8211;reverse</code></dt>
<dd> Reverse colormap.</dd>
<dt><code>-n</code>,&nbsp;<code>&#8211;nosurface</code></dt>
<dd> Do not output surface.</dd>
<dt><code>-F&nbsp;</code><i>C</i>,&nbsp;<code>&#8211;flatten=</code><i>C</i></dt>
<dd> Set <i>C</i> coordinate to average value.</dd>
<dt><code>-v</code>,&nbsp;<code>&#8211;verbose</code></dt>
<dd> Display surface statistics.</dd>
<dt><code>-h</code>,&nbsp;<code>&#8211;help</code></dt>
<dd> Display the help and exit. </dd>
</dl>
<h2>AUTHOR</h2>
<p> gts2oogl was written by Stephane Pipinet &lt;popinet [at] users.sourceforge.net&gt;. </p>
<p> This manual page was written by Ruben Molina &lt;rmolina [at] udea.edu.co&gt;, for the Debian project (but may be used by others). </p>
