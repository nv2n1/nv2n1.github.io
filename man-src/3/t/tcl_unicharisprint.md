---
title: "tcl_unicharisprint(3)"
name: "tcl_unicharisprint"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_unicharisprint/"
description: "Tcl_UniCharIsAlnum, Tcl_UniCharIsAlpha, Tcl_UniCharIsControl, Tcl_UniCharIsDigit, Tcl_UniCharIsGraph, Tcl_UniCharIsLower, Tcl_UniCharIsPrint, Tcl_UniCharIsPunct, Tcl_UniCharIsSpace, Tcl_UniCharIsUp..."
---

<p>Tcl_UniCharIsAlnum, Tcl_UniCharIsAlpha, Tcl_UniCharIsControl, Tcl_UniCharIsDigit, Tcl_UniCharIsGraph, Tcl_UniCharIsLower, Tcl_UniCharIsPrint, Tcl_UniCharIsPunct, Tcl_UniCharIsSpace, Tcl_UniCharIsUpper, Tcl_UniCharIsWordChar &#8211; routines for classification of Tcl_UniChar characters </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_UniCharIsAlnum</code>(<i>ch</i>)
int
<code>Tcl_UniCharIsAlpha</code>(<i>ch</i>)
int
<code>Tcl_UniCharIsControl</code>(<i>ch</i>)
int
<code>Tcl_UniCharIsDigit</code>(<i>ch</i>)
int
<code>Tcl_UniCharIsGraph</code>(<i>ch</i>)
int
<code>Tcl_UniCharIsLower</code>(<i>ch</i>)
int
<code>Tcl_UniCharIsPrint</code>(<i>ch</i>)
int
<code>Tcl_UniCharIsPunct</code>(<i>ch</i>)
int
<code>Tcl_UniCharIsSpace</code>(<i>ch</i>)
int
<code>Tcl_UniCharIsUpper</code>(<i>ch</i>)
int
<code>Tcl_UniCharIsWordChar</code>(<i>ch</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>ch</i> (in) The Tcl_UniChar to be examined. </p>
</dl>
<h2>Description</h2>
<p>All of the routines described examine Tcl_UniChars and return a boolean value. A non-zero return value means that the character does belong to the character class associated with the called routine. The rest of this document just describes the character classes associated with the various routines. </p>
<p> Note: A Tcl_UniChar is a Unicode character represented as an unsigned, fixed-size quantity. </p>
<h2>Character Classes</h2>
<p><code>Tcl_UniCharIsAlnum</code> tests if the character is an alphanumeric Unicode character. </p>
<p> <code>Tcl_UniCharIsAlpha</code> tests if the character is an alphabetic Unicode character. </p>
<p> <code>Tcl_UniCharIsControl</code> tests if the character is a Unicode control character. </p>
<p> <code>Tcl_UniCharIsDigit</code> tests if the character is a numeric Unicode character. </p>
<p> <code>Tcl_UniCharIsGraph</code> tests if the character is any Unicode print character except space. </p>
<p> <code>Tcl_UniCharIsLower</code> tests if the character is a lowercase Unicode character. </p>
<p> <code>Tcl_UniCharIsPrint</code> tests if the character is a Unicode print character. </p>
<p> <code>Tcl_UniCharIsPunct</code> tests if the character is a Unicode punctuation character. </p>
<p> <code>Tcl_UniCharIsSpace</code> tests if the character is a whitespace Unicode character. </p>
<p> <code>Tcl_UniCharIsUpper</code> tests if the character is an uppercase Unicode character. </p>
<p> <code>Tcl_UniCharIsWordChar</code> tests if the character is alphanumeric or a connector punctuation mark. </p>
<h2>Keywords</h2>
<p>unicode, classification</p>
