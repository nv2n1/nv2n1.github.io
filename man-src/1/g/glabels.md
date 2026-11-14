---
title: "glabels(1)"
name: "glabels"
section: "1"
letter: "g"
url: "/docs/linux/man/1-glabels/"
description: "glabels – Label and business card creation program for GNOME"
---

<h2>NAME</h2>
<p> glabels &#8211; Label and business card creation program for GNOME</p>
<h2>SYNOPSIS</h2>
<p> <code>glabels</code> [OPTIONS] [label-filename&#8230;] </p>
<p> <code>glabels-batch</code> [OPTIONS] [label-filename&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>glabels</code> is a lightweight program for creating labels and business cards for the GNOME desktop environment. It is designed to work with various laser/ink-jet peel-off label and business card sheets that you&#8217;ll find at most office supply stores. <code>glabels</code> is pre-configured with templates for many of these products. It also provides an interactive template designer for creating new templates according to user specifications. </p>
<p> For full documentation see the <code>gLabels</code> online help. </p>
<p> <code>glabels-batch</code> is a command line utility to print labels previously prepared with <code>glabels.</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Display a summary of available command-line options.</p>
<dt><code>&#8211;usage</code></p>
<dd> Display a short usage summary.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print program version information.</dl>
<p> <code>Options specific to glabels-batch</code></p>
<dl>
<dt><code>-o</code> <i>filename</i>, <code>&#8211;output</code>=<i>filename</i></p>
<dd> Set output filename to <i>filename</i>. (default=&quot;output.ps&quot;)</p>
<dt><code>-s</code> <i>n</i>, <code>&#8211;sheets</code>=<i>n</i></p>
<dd> Set number of sheets to <i>n</i>. (default=1)</p>
<dt><code>-c</code> <i>n</i>, <code>&#8211;copies</code>=<i>n</i></p>
<dd> Set number of copies to <i>n</i>. (default=1)</p>
<dt><code>-f</code> <i>n</i>, <code>&#8211;first</code>=<i>n</i></p>
<dd> Set label on first sheet to start printing from to <i>n</i>. (default=1)</p>
<dt><code>-l</code>, <code>&#8211;outline</code></p>
<dd> Print outlines around labels. This is useful for testing printer alignment or printing proof sheets.</p>
<dt><code>-r</code>, <code>&#8211;reverse</code></p>
<dd> Print mirror image of labels. This is useful for clear labels intended to be seen from the back through glass. </p>
</dl>
<h2>FILES</h2>
<p> The $HOME/.glabels directory contains all user-defined templates.</p>
<h2>SEE ALSO</h2>
<p> The gLabels homepage at &lt;<a rel="nofollow" href="http://glabels.sourceforge.net/">http://glabels.sourceforge.net/</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Jim Evins &lt;evins [at] snaught.com&gt; </p>
<h2>Index</h2>
