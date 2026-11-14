---
title: "xkbprint(1)"
name: "xkbprint"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xkbprint/"
description: "xkbprint – print an XKB keyboard description"
---

<h2 class="name">NAME</h2>
<p> xkbprint &#8211; print an XKB keyboard description </p>
<h2>SYNOPSIS</h2>
<p> <code>xkbprint</code> [options] source [ output_file ]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xkbprint</i> command generates a printable or encapsulated PostScript description of the XKB keyboard description specified by <i>source</i>. The <i>source</i> can be any compiled keymap (.xkm) file that includes a geometry description or an X display specification. If an <i>output_file</i> is specified, xkbprint writes to it. If no output file is specified, xkbprint creates replaces the extension of the source file with <i>.ps</i> or <i>.eps</i> depending on the requested format. If the source is a non-local X display (e.g.:0), xkbprint appends the appropriate prefix to the display specification, replacing the colon with a dash. For a local display, xkprint uses server-<i>n</i> where <i>n</i> is the number of the display.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, -help</code></p>
<dd> Prints a usage message.</p>
<dt><code>-color</code></p>
<dd> Print using the colors specified in the geometry file; by default, xkbprint prints a black-and-white image of the keyboard.</p>
<dt><code>-dflts</code></p>
<dd> Attempt to compute default names for any missing components, such as keys.</p>
<dt><code>-diffs</code></p>
<dd> Show symbols only where they are explicitly bound.</p>
<dt><code>-eps</code></p>
<dd> Generate an encapsulated PostScript file.</p>
<dt><code>-fit</code></p>
<dd> Fit the keyboard image on the page (default).</p>
<dt><code>-full</code></p>
<dd> Print the keyboard at full size.</p>
<dt><code>-grid&nbsp;</code><i>res</i></p>
<dd> Print a grid with <i>res</i>&nbsp;mm resolution over the keyboard.</p>
<dt><code>-if&nbsp;</code><i>fontName</i></p>
<dd> Specifies an internal PostScript type 1 font to dump to the specified output file or to <i>fontName</i>.pfa, if no output file is specified. No keyboard description is printed if an internal font is dumped.</p>
<dt><code>-label&nbsp;</code><i>type</i></p>
<dd> Specifies the labels to be printed on keys; valid types are: <i>none</i>, <i>name</i>, <i>code</i>, and <i>symbols</i>.</p>
<dt><code>-lc&nbsp;</code><i>&lt;locale&gt;</i></p>
<dd> Specifies a locale in which KeySyms should be resolved.</p>
<dt><code>-level1</code></p>
<dd> Generate level 1 PostScript.</p>
<dt><code>-level2</code></p>
<dd> Generate level 2 PostScript.</p>
<dt><code>-lg&nbsp;</code><i>group</i></p>
<dd> Print symbols in keyboard groups starting from <i>group</i>.</p>
<dt><code>-ll&nbsp;</code><i>level</i></p>
<dd> Print symbols starting from shift level <i>level</i>.</p>
<dt><code>-mono</code></p>
<dd> Generate black-and-white image of keyboard (default).</p>
<dt><code>-n&nbsp;</code><i>num</i></p>
<dd> Print <i>num</i> copies.</p>
<dt><code>-nkg&nbsp;</code><i>num</i></p>
<dd> Print the symbols in <i>num</i> keyboard groups.</p>
<dt><code>-npk&nbsp;</code><i>num</i></p>
<dd> Number of keyboard images to print on each page; for EPS files, this specifies the total number of keyboard images to print.</p>
<dt><code>-o&nbsp;</code><i>file</i></p>
<dd> Write output to <i>file</i>.</p>
<dt><code>-R</code><i>directory</i></p>
<dd> Use <i>directory</i> as the root directory; all path names are interpreted relative to <i>directory</i>.</p>
<dt><code>-pict </code><i>which</i></p>
<dd> Controls use of pictographs instead of keysym names where available. <i>which</i> can be any of <i>all</i>, <i>none</i>, or <i>common</i> (default).</p>
<dt><code>-synch</code></p>
<dd> Forces synchronization for X requests.</p>
<dt><code>-version</code></p>
<dd> Print out the program version and exit.</p>
<dt><code>-w&nbsp;</code><i>level</i></p>
<dd> Sets warning level (0 for no warning, 10 for all warnings).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-x/">X</a></code>(7), <code><a href="/docs/linux/man/1-xkbcomp/">xkbcomp</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1995, Silicon Graphics Computer Systems Copyright 1995, 1998 The Open Group<br />
 See <code><a href="/docs/linux/man/7-x/">X</a></code>(7) for a full statement of rights and permissions.</p>
<h2>AUTHOR</h2>
<p> Erik Fortune, Silicon Graphics </p>
<h2>Index</h2>
