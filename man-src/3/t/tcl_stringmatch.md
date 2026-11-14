---
title: "tcl_stringmatch(3)"
name: "tcl_stringmatch"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_stringmatch/"
description: "Tcl_StringMatch, Tcl_StringCaseMatch – test whether a string matches a pattern"
---

<p>Tcl_StringMatch, Tcl_StringCaseMatch &#8211; test whether a string matches a pattern </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_StringMatch</code>(<i>str</i>, <i>pattern</i>)
int
<code>Tcl_StringCaseMatch</code>(<i>str</i>, <i>pattern</i>, <i>flags</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>const char <i>*str</i> (in) String to test.</p>
<dd>const char <i>*pattern</i> (in) Pattern to match against string. May contain special characters from the set *?\[].</p>
<dd>int <i>flags</i> (in) OR-ed combination of match flags, currently only <code>TCL_MATCH_NOCASE</code>. 0 specifies a case-sensitive search. </p>
</dl>
<h2>Description</h2>
<p>This utility procedure determines whether a string matches a given pattern. If it does, then <code>Tcl_StringMatch</code> returns 1. Otherwise <code>Tcl_StringMatch</code> returns 0. The algorithm used for matching is the same algorithm used in the <code>string match</code> Tcl command and is similar to the algorithm used by the C-shell for file name matching; see the Tcl manual entry for details. </p>
<p> In <code>Tcl_StringCaseMatch</code>, the algorithm is the same, but you have the option to make the matching case-insensitive. If you choose this (by passing <code>TCL_MATCH_NOCASE</code>), then the string and pattern are essentially matched in the lower case. </p>
<h2>Keywords</h2>
<p>match, pattern, string</p>
