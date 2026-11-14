---
title: "tcl_utftotitle(3)"
name: "tcl_utftotitle"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_utftotitle/"
description: "Tcl_UniCharToUpper, Tcl_UniCharToLower, Tcl_UniCharToTitle, Tcl_UtfToUpper, Tcl_UtfToLower, Tcl_UtfToTitle – routines for manipulating the case of Unicode characters and UTF-8 strings"
---

<p>Tcl_UniCharToUpper, Tcl_UniCharToLower, Tcl_UniCharToTitle, Tcl_UtfToUpper, Tcl_UtfToLower, Tcl_UtfToTitle &#8211; routines for manipulating the case of Unicode characters and UTF-8 strings </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_UniChar
<code>Tcl_UniCharToUpper</code>(<i>ch</i>)
Tcl_UniChar
<code>Tcl_UniCharToLower</code>(<i>ch</i>)
Tcl_UniChar
<code>Tcl_UniCharToTitle</code>(<i>ch</i>)
int
<code>Tcl_UtfToUpper</code>(<i>str</i>)
int
<code>Tcl_UtfToLower</code>(<i>str</i>)
int
<code>Tcl_UtfToTitle</code>(<i>str</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>ch</i> (in) The Tcl_UniChar to be converted.</p>
<dd>char <i>*str</i> (in/out) Pointer to UTF-8 string to be converted in place. </p>
</dl>
<h2>Description</h2>
<p>The first three routines convert the case of individual Unicode characters: </p>
<p> If <i>ch</i> represents a lower-case character, <code>Tcl_UniCharToUpper</code> returns the corresponding upper-case character. If no upper-case character is defined, it returns the character unchanged. </p>
<p> If <i>ch</i> represents an upper-case character, <code>Tcl_UniCharToLower</code> returns the corresponding lower-case character. If no lower-case character is defined, it returns the character unchanged. </p>
<p> If <i>ch</i> represents a lower-case character, <code>Tcl_UniCharToTitle</code> returns the corresponding title-case character. If no title-case character is defined, it returns the corresponding upper-case character. If no upper-case character is defined, it returns the character unchanged. Title-case is defined for a small number of characters that have a different appearance when they are at the beginning of a capitalized word. </p>
<p> The next three routines convert the case of UTF-8 strings in place in memory: </p>
<p> <code>Tcl_UtfToUpper</code> changes every UTF-8 character in <i>str</i> to upper-case. Because changing the case of a character may change its size, the byte offset of each character in the resulting string may differ from its original location. <code>Tcl_UtfToUpper</code> writes a null byte at the end of the converted string. <code>Tcl_UtfToUpper</code> returns the new length of the string in bytes. This new length is guaranteed to be no longer than the original string length. </p>
<p> <code>Tcl_UtfToLower</code> is the same as <code>Tcl_UtfToUpper</code> except it turns each character in the string into its lower-case equivalent. </p>
<p> <code>Tcl_UtfToTitle</code> is the same as <code>Tcl_UtfToUpper</code> except it turns the first character in the string into its title-case equivalent and all following characters into their lower-case equivalents. </p>
<h2>Bugs</h2>
<p>At this time, the case conversions are only defined for the ISO8859-1 characters. Unicode characters above 0x00ff are not modified by these routines. </p>
<h2>Keywords</h2>
<p>utf, unicode, toupper, tolower, totitle, case</p>
