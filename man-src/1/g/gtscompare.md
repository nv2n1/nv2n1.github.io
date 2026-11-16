---
title: "gtscompare(1)"
name: "gtscompare"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtscompare/"
description: "gtscompare – compare two GTS files."
---

<h2 class="name">NAME</h2>
<p> gtscompare &#8211; compare two GTS files.</p>
<h2>SYNOPSIS</h2>
<p> <code>gtscompare</code> [<i>OPTIONS</i>] <i>FILE1 FILE2 DELTA</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>gtscompare</code> command. </p>
<p> <i>DELTA</i> is the sampling length expressed as a fraction of the bounding box diagonal of the second surface. </p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-s</code>,&nbsp;<code>&#8211;symmetric</code></dt>
<dd> Symmetric statistics.</dd>
<dt><code>-i</code>,&nbsp;<code>&#8211;image</code></dt>
<dd> Output visualisation mesh.</dd>
<dt><code>-c&nbsp;</code><i>FILE</i>,&nbsp;<code>&#8211;cmap=</code><i>FILE</i></dt>
<dd> Load <i>FILE</i> as colormap.</dd>
<dt><code>-m&nbsp;</code><i>VAL</i>,&nbsp;<code>&#8211;min=</code><i>VAL</i></dt>
<dd> Use <i>VAL</i> as minimum scaling value.</dd>
<dt><code>-M&nbsp;</code><i>VAL</i>,&nbsp;<code>&#8211;max=</code><i>VAL</i></dt>
<dd> Use <i>VAL</i> as maximum scaling value.</dd>
<dt><code>-r</code>,&nbsp;<code>&#8211;reverse</code></dt>
<dd> Reverse colormap.</dd>
<dt><code>-l</code>,&nbsp;<code>&#8211;log</code></dt>
<dd> Use log scale.</dd>
<dt><code>-h</code>,&nbsp;<code>&#8211;help</code></dt>
<dd> Display the help and exit. </dd>
</dl>
<h2>AUTHOR</h2>
<p> gtscompare was written by Stephane Popinet &lt;popinet [at] users.sourceforge.net&gt;. </p>
<p> This manual page was written by Ruben Molina &lt;rmolina [at] udea.edu.co&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
