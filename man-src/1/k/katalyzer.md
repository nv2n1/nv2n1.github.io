---
title: "katalyzer(1)"
name: "katalyzer"
section: "1"
letter: "k"
url: "/docs/linux/man/1-katalyzer/"
description: "katalyzer – analyzes Kate streams and displays various information about them."
---

<h2 class="name">NAME</h2>
<p> katalyzer &#8211; analyzes Kate streams and displays various information about them.</p>
<h2>SYNOPSIS</h2>
<p> <code>katalyzer</code> <code>[-hV]</code> <code>[-l </code><i>types</i><code>]</code> <code>[-l!]</code> [ infile ] </p>
<h2>DESCRIPTION</h2>
<p> <code>katalyzer</code> analyzes Kate streams and displays information about them. The type of information to select is selectable on the command line. Several multiplexed Kate streams may be analyzed at the same time. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Show command line help.</p>
<dt><code>-V</code></p>
<dd> Show version information.</p>
<dt><code>-l</code> types</p>
<dd> Select the types of information to log, from the list below. These characters may be concatenated in a single -l option, as, eg, <code>ls</code> does (eg, <code>katalyzer</code> -l Ttv). Refer to the <code>katalyzer</code> command line help for a fully up to date list of types.<br />
&nbsp;<wbr>e: errors<br />
&nbsp;<wbr>p: packet<br />
&nbsp;<wbr>c: container specific information<br />
&nbsp;<wbr>T: Timing<br />
&nbsp;<wbr>t: text<br />
&nbsp;<wbr>v: event<br />
&nbsp;<wbr>d: dump page and packets<br />
&nbsp;<wbr>S: statistics<br />
&nbsp;<wbr>-: miscellaneous information that doesn&#8217;t belong in any other type </p>
<dt><code>-l!</code></p>
<dd> Shorthand to select all information to log. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Analyzes any Kate stream in an Ogg file: </p>
<p>&nbsp;<wbr>katalyzer input.ogg </p>
<p> Analyzes any Kate stream in an Ogg file, displaying only errors: </p>
<p>&nbsp;<wbr>katalyzer -l e input.ogg </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-katedec/">katedec</a></code>(1), <code><a href="/docs/linux/man/1-kateenc/">kateenc</a></code>(1) </p>
<h2>Index</h2>
