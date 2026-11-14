---
title: "pmnumberstr(3)"
name: "pmnumberstr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmnumberstr/"
description: "pmNumberStr, pmNumberStr_r – fixed width output format for numbers"
---

<p><code>pmNumberStr</code>, <code>pmNumberStr_r</code> &#8211; fixed width output format for numbers</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> const char *pmNumberStr(double </code><i>value</i>);<br />
 char *pmNumberStr_r(double <i>value</i>, char *<i>buf</i>, int <i>buflen</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p><code>pmNumberStr</code> returns the address of a 8-byte buffer that holds a null-byte terminated representation of <i>value</i> suitable for output with fixed width fields. The <code>pmNumberStr_r</code> function does the same, but stores the result in a user-supplied buffer <i>buf</i> of length <i>buflen</i>, which should have room for at least 8 bytes. </p>
<p> The value is scaled using multipliers in powers of &#8220;one thousand&#8221; (the decimal &#8220;kilo&#8221;) and has a bias that provides greater precision for positive numbers as opposed to negative numbers. </p>
<p> The format depends on the sign and magnitude of <i>value</i> as follows (d represents a decimal digit): <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><i>value</i> range</td>
<td ALIGN=center>format
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&gt;&nbsp;<wbr>999995000000000</td>
<td> inf?
</td>
</tr>
<tr VALIGN=top>
<td>999995000000000 &#8211; 999995000000</td>
<td>ddd.ddT
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>999995000000 &#8211; 999995000</td>
<td>ddd.ddG
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>999995000 &#8211; 999995</td>
<td>ddd.ddM
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>999995 &#8211; 999.995</td>
<td>ddd.ddK
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>999.995 &#8211; 0.005</td>
<td>ddd.dd
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0.005 &#8211; -0.005</td>
<td> 0.00
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-0.005 &#8211; -99.95</td>
<td>-dd.dd
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-99.995 &#8211; -99995</td>
<td>-dd.ddK
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-99995 &#8211; -99995000</td>
<td>-dd.ddM
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-99995000 &#8211; -99995000000</td>
<td>-dd.ddG
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-99995000000 &#8211; -99995000000000</td>
<td>-dd.ddT
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;&nbsp;<wbr>-99995000000000</td>
<td>-inf?
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> At the boundary points of the ranges, the chosen format will retain the maximum number of significant digits.</p>
<h2>Notes</h2>
<p><code>pmNumberStr</code> returns a pointer to a static buffer and hence is not thread-safe. Multi-threaded applications should use <code>pmNumberStr_r</code> instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) </p>
