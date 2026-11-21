---

title: "xkbprint(1)"
name: "xkbprint"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xkbprint/"
description: "xkbprint – print an XKB keyboard description"
---

<p> <code>xkbprint</code> [options] source [ output_file ]</p>
<p> The <i>xkbprint</i> command generates a printable or encapsulated PostScript description of the XKB keyboard description specified by <i>source</i>. The <i>source</i> can be any compiled keymap (.xkm) file that includes a geometry description or an X display specification. If an <i>output_file</i> is specified, xkbprint writes to it. If no output file is specified, xkbprint creates replaces the extension of the source file with <i>.ps</i> or <i>.eps</i> depending on the requested format. If the source is a non-local X display (e.g.:0), xkbprint appends the appropriate prefix to the display specification, replacing the colon with a dash. For a local display, xkprint uses server-<i>n</i> where <i>n</i> is the number of the display.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, -help</code></dt>
<dd> Prints a usage message.</dd>
<dt><code>-color</code></dt>
<dd> Print using the colors specified in the geometry file; by default, xkbprint prints a black-and-white image of the keyboard.</dd>
<dt><code>-dflts</code></dt>
<dd> Attempt to compute default names for any missing components, such as keys.</dd>
<dt><code>-diffs</code></dt>
<dd> Show symbols only where they are explicitly bound.</dd>
<dt><code>-eps</code></dt>
<dd> Generate an encapsulated PostScript file.</dd>
<dt><code>-fit</code></dt>
<dd> Fit the keyboard image on the page (default).</dd>
<dt><code>-full</code></dt>
<dd> Print the keyboard at full size.</dd>
<dt><code>-grid&nbsp;</code><i>res</i></dt>
<dd> Print a grid with <i>res</i>&nbsp;mm resolution over the keyboard.</dd>
<dt><code>-if&nbsp;</code><i>fontName</i></dt>
<dd> Specifies an internal PostScript type 1 font to dump to the specified output file or to <i>fontName</i>.pfa, if no output file is specified. No keyboard description is printed if an internal font is dumped.</dd>
<dt><code>-label&nbsp;</code><i>type</i></dt>
<dd> Specifies the labels to be printed on keys; valid types are: <i>none</i>, <i>name</i>, <i>code</i>, and <i>symbols</i>.</dd>
<dt><code>-lc&nbsp;</code><i>&lt;locale&gt;</i></dt>
<dd> Specifies a locale in which KeySyms should be resolved.</dd>
<dt><code>-level1</code></dt>
<dd> Generate level 1 PostScript.</dd>
<dt><code>-level2</code></dt>
<dd> Generate level 2 PostScript.</dd>
<dt><code>-lg&nbsp;</code><i>group</i></dt>
<dd> Print symbols in keyboard groups starting from <i>group</i>.</dd>
<dt><code>-ll&nbsp;</code><i>level</i></dt>
<dd> Print symbols starting from shift level <i>level</i>.</dd>
<dt><code>-mono</code></dt>
<dd> Generate black-and-white image of keyboard (default).</dd>
<dt><code>-n&nbsp;</code><i>num</i></dt>
<dd> Print <i>num</i> copies.</dd>
<dt><code>-nkg&nbsp;</code><i>num</i></dt>
<dd> Print the symbols in <i>num</i> keyboard groups.</dd>
<dt><code>-npk&nbsp;</code><i>num</i></dt>
<dd> Number of keyboard images to print on each page; for EPS files, this specifies the total number of keyboard images to print.</dd>
<dt><code>-o&nbsp;</code><i>file</i></dt>
<dd> Write output to <i>file</i>.</dd>
<dt><code>-R</code><i>directory</i></dt>
<dd> Use <i>directory</i> as the root directory; all path names are interpreted relative to <i>directory</i>.</dd>
<dt><code>-pict </code><i>which</i></dt>
<dd> Controls use of pictographs instead of keysym names where available. <i>which</i> can be any of <i>all</i>, <i>none</i>, or <i>common</i> (default).</dd>
<dt><code>-synch</code></dt>
<dd> Forces synchronization for X requests.</dd>
<dt><code>-version</code></dt>
<dd> Print out the program version and exit.</dd>
<dt><code>-w&nbsp;</code><i>level</i></dt>
<dd> Sets warning level (0 for no warning, 10 for all warnings).</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-x/">X</a></code>(7), <code><a href="/docs/linux/man/1-xkbcomp/">xkbcomp</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1995, Silicon Graphics Computer Systems Copyright 1995, 1998 The Open Group<br />
 See <code><a href="/docs/linux/man/7-x/">X</a></code>(7) for a full statement of rights and permissions.</p>
<h2>AUTHOR</h2>
<p> Erik Fortune, Silicon Graphics </p>
