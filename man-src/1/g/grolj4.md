---
title: "grolj4(1)"
name: "grolj4"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grolj4/"
description: "grolj4 – groff driver for HP LaserJet 4 family"
---

<h2 class="name">NAME</h2>
<p> grolj4 &#8211; groff driver for HP LaserJet 4 family </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-l</code> ] [ <code>-c </code><i>num-copies</i> ] [<code>-d</code> [<i>n</i>]] [ <code>-F </code><i>font-directory</i> ] [ <code>-p </code><i>paper-size</i> ] [ <code>-w </code><i>line-width</i> ] [<i>file</i> &#8230;] <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>grolj4</code> is a driver for <code>groff</code> that produces output in PCL5 format suitable for an HP LaserJet 4 printer. </p>
<p> There is an additional drawing command available:</p>
<dl>
<dt><code>\D&#8217;R&nbsp;</code><i>dh dv</i><code>&#8216;</code></p>
<dd> Draw a rule (solid black rectangle), with one corner at the current position, and the diagonally opposite corner at the current position +(<i>dh</i>,<i>dv</i>). Afterwards the current position will be at the opposite corner. This generates a PCL fill rectangle command, and so will work on printers that do not support HPGL/2 unlike the other <code>\D</code> commands.</dl>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-c</code><i> num-copies</i></p>
<dd> Print <i>num-copies</i> copies of each page.</p>
<dt><code>-l</code></p>
<dd> Print the document with a landscape orientation.</p>
<dt><code>-d</code></p>
<dd> [<i>n</i>] Use duplex mode <i>n</i>: 1 is long-side binding; 2 is short-side binding; default is 1.</p>
<dt><code>-p</code><i> paper-size</i></p>
<dd> Set the paper size to <i>paper-size</i>, which must be one of letter, legal, executive, a4, com10, monarch, c5, b5, dl.</p>
<dt><code>-v</code></p>
<dd> <code>&#8211;version</code> Print the version number.</p>
<dt><code>-w</code><i> line-width</i></p>
<dd> Set the default line thickness to <i>line-width</i> thousandths of an em. If this option isn&#8217;t specified, the line thickness defaults to 0.04~em.</p>
<dt><code>-F</code><i> font-directory</i></p>
<dd> Prepend directory <i>font-directory</i>/dev<i>name</i> to the search path for font and device description files; <i>name</i> is the name of the device, usually <code>lj4</code>.</dl>
<p> The following four commands are available additionally in the font description files:</p>
<dl>
<dt><code>pclweight</code><i>&nbsp;N</i></p>
<dd> The integer value <i>N</i> must be in the range -7 to +7; default is~0.</p>
<dt><code>pclstyle</code><i>&nbsp;N</i></p>
<dd> The integer value <i>N</i> must be in the range 0 to 32767; default is~0.</p>
<dt><code>pclproportional</code><i>&nbsp;N</i></p>
<dd> A boolean flag which can be either 0 or~1; default is~0.</p>
<dt><code>pcltypeface</code><i>&nbsp;N</i></p>
<dd> The integer value <i>N</i> must be in the range 0 to 65535; default is~0.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><i>GROFF_FONT_PATH</i></p>
<dd> A list of directories in which to search for the <i>dev</i>name directory in addition to the default ones. See <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) and <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) for more details.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devlj4/DESC</i></p>
<dd> Device description file.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devlj4/</i>F</p>
<dd> Font description file for font <i>F</i>.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:tmac/lj4.tmac</i></p>
<dd> Macros for use with <code>grolj4</code>.</dl>
<h2>BUGS</h2>
<p> Small dots.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-lj4_font/">lj4_font</a></code>(5), <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/5-groff_out/">groff_out</a></code>(5), <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5), <code><a href="/docs/linux/man/7-groff_char/">groff_char</a></code>(7) </p>
<h2>Index</h2>
