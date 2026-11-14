---
title: "tcl_printdouble(3)"
name: "tcl_printdouble"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_printdouble/"
description: "Tcl_PrintDouble – Convert floating value to string"
---

<p>Tcl_PrintDouble &#8211; Convert floating value to string </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_PrintDouble</code>(<i>interp, value, dst</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Before Tcl 8.0, the <code>tcl_precision</code> variable in this interpreter controlled the conversion. As of Tcl 8.0, this argument is ignored and the conversion is controlled by the <code>tcl_precision</code> variable that is now shared by all interpreters.</p>
<dd>double <i>value</i> (in) Floating-point value to be converted.</p>
<dd>char <i>*dst</i> (out) Where to store the string representing <i>value</i>. Must have at least <code>TCL_DOUBLE_SPACE</code> characters of storage. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_PrintDouble</code> generates a string that represents the value of <i>value</i> and stores it in memory at the location given by <i>dst</i>. It uses <code>%g</code> format to generate the string, with one special twist: the string is guaranteed to contain either a &#8220;.&#8221; or an &#8220;e&#8221; so that it does not look like an integer. Where <code>%g</code> would generate an integer with no decimal point, <code>Tcl_PrintDouble</code> adds &#8220;.0&#8221;. </p>
<p> If the <code>tcl_precision</code> value is non-zero, the result will have precisely that many digits of significance. If the value is zero (the default), the result will have the fewest digits needed to represent the number in such a way that <code>Tcl_NewDoubleObj</code> will generate the same number when presented with the given string. IEEE semantics of rounding to even apply to the conversion. </p>
<h2>Keywords</h2>
<p>conversion, double-precision, floating-point, string</p>
