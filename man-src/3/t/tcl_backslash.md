---
title: "tcl_backslash(3)"
name: "tcl_backslash"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_backslash/"
description: "Tcl_Backslash – parse a backslash sequence"
---

<p>Tcl_Backslash &#8211; parse a backslash sequence </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
char
<code>Tcl_Backslash</code>(<i>src, countPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>char <i>*src</i> (in) Pointer to a string starting with a backslash.</p>
<dd>int <i>*countPtr</i> (out) If <i>countPtr</i> is not NULL, <i>*countPtr</i> gets filled in with number of characters in the backslash sequence, including the backslash character. </p>
</dl>
<h2>Description</h2>
<p>The use of <code>Tcl_Backslash</code> is deprecated in favor of <code>Tcl_UtfBackslash</code>. </p>
<p> This is a utility procedure provided for backwards compatibility with non-internationalized Tcl extensions. It parses a backslash sequence and returns the low byte of the Unicode character corresponding to the sequence. <code>Tcl_Backslash</code> modifies <i>*countPtr</i> to contain the number of characters in the backslash sequence. </p>
<p> See the Tcl manual entry for information on the valid backslash sequences. All of the sequences described in the Tcl manual entry are supported by <code>Tcl_Backslash</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/n-tcl/">Tcl</a>(n), <a href="/docs/linux/man/3-tcl_utfbackslash/">Tcl_UtfBackslash</a>(3) </p>
<h2>Keywords</h2>
<p>backslash, parse</p>
