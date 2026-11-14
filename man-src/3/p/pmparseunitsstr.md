---
title: "pmparseunitsstr(3)"
name: "pmparseunitsstr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmparseunitsstr/"
description: "pmParseUnitsStr – parse time point specification"
---

<p><code>pmParseUnitsStr</code> &#8211; parse time point specification</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmParseUnitsStr(const char *</code><i>string</i>, struct pmUnits&nbsp;<wbr>*<i>out</i>, double&nbsp;<wbr>*<i>outMult</i>, char&nbsp;<wbr>**<i>errMsg</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p><code>pmParseUnitsStr</code> is designed to encapsulate the interpretation of a unit/scale specification in command line switches for use by the PCP client tools. This function expects to be called with the unit/scale specification as <code>string</code>. This specification takes the general form produced by <code>pmUnitsStr</code>. Briefly, the format allows <code>/</code>-separated divisor and dividend, each listing space-separated dimensions/scales along the space, time, and count axes. There are also a few extra possibilities: First, multiple equivalent sets of keywords are accepted for the time &amp; space dimensions, insensitive to case. For example, &quot;microseconds&quot;, &quot;microsecond&quot;, &quot;microsec&quot;, &quot;us&quot; are considered synonymous, as are &quot;kilobytes&quot;, &quot;KB&quot;, &quot;kiloByte&quot;, and so on. Second, units may be offered in any order, e.g., <code>ms kb count x 10^3</code> or <code>count x 10^3 kb ms</code>. They may not be repeated within the denominator or within the numerator. Each scale/unit keyword may be immediately followed by positive or negative exponents, e.g., <code>^-4</code>. Third, numerical scaling factors may be supplied. These are factored together with implicit scale conversions into the final <code>outMult</code> result. The <code>out</code> and <code>outMult</code> values must both be allocated before calling <code>pmParseUnitsStr</code>. If the conversion is successful, <code>pmParseUnitsStr</code> returns 0, and fills in <code>out</code> and <code>outMult</code> with the unit/scales defined by the input parameter. If the argument strings could not be parsed, it returns a negative status code. </p>
<h2>Examples</h2>
<p><center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center>string</td>
<td ALIGN=center>out</td>
<td ALIGN=center>outMult
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>2 count</td>
<td>{0,1,0,0,0,0}</td>
<td>0.5
</td>
</tr>
<tr VALIGN=top>
<td>count / 7.5 nanosecond</td>
<td>{0,1,-1,0,0,0}</td>
<td>7.5
</td>
</tr>
<tr VALIGN=top>
<td>10 kilobytes / 2.5e2 count x 10^3</td>
<td>{1,-1,0,1,3,0}</td>
<td>25
</td>
</tr>
<tr VALIGN=top>
<td>millisecond / second^2</td>
<td>{0,0,-1,0,0,3}</td>
<td>1000
</td>
</tr>
<tr VALIGN=top>
<td>mb/s</td>
<td>{1,0,-1,2,0,3}</td>
<td>1
</td>
</tr>
</table>
</table>
<p></center> </p>
<h2>Return Value</h2>
<p>A zero status indicates success. A negative status indicates an error, in which case the errMsg pointer will receive a textual error message, which the caller should later <i>free()</i>. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmunitsstr/">pmUnitsStr</a></code>(3), <code><a href="/docs/linux/man/3-pmconvscale/">pmConvScale</a></code>(3), and <code><a href="/docs/linux/man/3-pmlookupdesc/">pmLookupDesc</a></code>(3). </p>
